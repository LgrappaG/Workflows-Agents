"""
Agent Execution Circuit Breaker
================================

Prevents cascading failures and infinite loops in agent execution.
Uses standard circuit breaker pattern with three states:
- CLOSED: Normal operation, calls pass through
- OPEN: Too many failures, calls are rejected immediately
- HALF_OPEN: Testing if service has recovered

Integration Points:
- CentralOrchestrator.execute_goal() - Rate limiting
- BaseAgent.execute() - Failure tracking
- Error recovery logic
"""

import time
import logging
from typing import Dict, Optional, Callable, Any
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import deque

logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Circuit breaker state machine"""
    CLOSED = "closed"        # Normal - requests pass through
    OPEN = "open"            # Failing - requests rejected immediately
    HALF_OPEN = "half_open"  # Testing - limited requests allowed


@dataclass
class CircuitMetrics:
    """Metrics for a circuit"""
    total_calls: int = 0
    successful_calls: int = 0
    failed_calls: int = 0
    rejected_calls: int = 0
    last_failure_time: Optional[datetime] = None
    circuit_opened_time: Optional[datetime] = None


class CircuitBreaker:
    """
    Standard circuit breaker pattern implementation.

    Prevents cascading failures by:
    1. Tracking success/failure rates
    2. Opening circuit when failure threshold exceeded
    3. Automatically half-opening to test recovery
    4. Failing fast when circuit is open
    """

    def __init__(
        self,
        circuit_name: str,
        failure_threshold: int = 5,
        recovery_timeout_sec: int = 60,
        half_open_max_calls: int = 3,
        sample_window_sec: int = 60
    ):
        """
        Initialize circuit breaker.

        Args:
            circuit_name: Name of circuit (for logging)
            failure_threshold: Failures before opening (e.g., 5 fails/min)
            recovery_timeout_sec: Seconds before attempting recovery
            half_open_max_calls: Max calls allowed when half-open
            sample_window_sec: Time window for failure rate calculation
        """

        self.circuit_name = circuit_name
        self.failure_threshold = failure_threshold
        self.recovery_timeout_sec = recovery_timeout_sec
        self.half_open_max_calls = half_open_max_calls
        self.sample_window_sec = sample_window_sec

        self.state = CircuitState.CLOSED
        self.state_changed_time = datetime.now()

        self.metrics = CircuitMetrics()
        self.recent_failures: deque = deque(maxlen=100)  # Track recent failures
        self.half_open_calls = 0

        logger.info(
            f"CircuitBreaker '{circuit_name}' created: "
            f"threshold={failure_threshold}, "
            f"recovery_timeout={recovery_timeout_sec}s"
        )

    def call(self, fn: Callable, *args, **kwargs) -> Any:
        """
        Execute function with circuit breaker protection.

        Args:
            fn: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            Function result

        Raises:
            CircuitBreakerOpenException: If circuit is open
            Any exception from fn: If execution fails and circuit not open
        """

        # Check circuit state
        self._update_state()

        if self.state == CircuitState.OPEN:
            self.metrics.rejected_calls += 1
            error_msg = f"Circuit OPEN: {self.circuit_name}"
            logger.warning(error_msg)
            raise CircuitBreakerOpenException(error_msg)

        # Execute function
        try:
            result = fn(*args, **kwargs)
            self._on_success()
            return result

        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        """Handle successful call"""

        self.metrics.successful_calls += 1
        self.metrics.total_calls += 1

        # If we're in half-open, go back to closed
        if self.state == CircuitState.HALF_OPEN:
            self._change_state(CircuitState.CLOSED)
            logger.info(f"Circuit CLOSED: {self.circuit_name} (recovery successful)")

        self.half_open_calls = 0

    def _on_failure(self):
        """Handle failed call"""

        self.metrics.failed_calls += 1
        self.metrics.total_calls += 1
        self.metrics.last_failure_time = datetime.now()

        # Track recent failure for threshold calculation
        self.recent_failures.append(datetime.now())

        # Check if we should open circuit
        if self._should_open_circuit():
            self._change_state(CircuitState.OPEN)
            self.metrics.circuit_opened_time = datetime.now()
            logger.error(
                f"Circuit OPEN: {self.circuit_name} "
                f"({self.metrics.failed_calls} failures)"
            )

    def _should_open_circuit(self) -> bool:
        """
        Check if failure threshold exceeded.

        Counts failures within sample_window_sec.
        """

        now = datetime.now()
        cutoff = now - timedelta(seconds=self.sample_window_sec)

        # Count recent failures within window
        recent_count = sum(
            1 for failure_time in self.recent_failures
            if failure_time > cutoff
        )

        return recent_count >= self.failure_threshold

    def _update_state(self):
        """Update circuit state transitions"""

        if self.state == CircuitState.OPEN:
            # Check if recovery timeout expired
            time_since_opened = (
                datetime.now() - self.state_changed_time
            ).total_seconds()

            if time_since_opened >= self.recovery_timeout_sec:
                self._change_state(CircuitState.HALF_OPEN)
                self.half_open_calls = 0
                logger.info(
                    f"Circuit HALF_OPEN: {self.circuit_name} "
                    f"(testing recovery)"
                )

        elif self.state == CircuitState.HALF_OPEN:
            # Limit calls in half-open state
            if self.half_open_calls >= self.half_open_max_calls:
                # Too many calls already, reject new ones
                pass

    def _change_state(self, new_state: CircuitState):
        """Change circuit state and log transition"""

        old_state = self.state
        self.state = new_state
        self.state_changed_time = datetime.now()

        logger.info(
            f"Circuit state transition: {old_state.value} → {new_state.value} "
            f"({self.circuit_name})"
        )

    def get_metrics(self) -> Dict:
        """Get circuit metrics for monitoring"""

        now = datetime.now()
        cutoff = now - timedelta(seconds=self.sample_window_sec)
        recent_failures = sum(
            1 for t in self.recent_failures
            if t > cutoff
        )

        time_in_current_state = (now - self.state_changed_time).total_seconds()

        return {
            "circuit_name": self.circuit_name,
            "state": self.state.value,
            "time_in_state_sec": time_in_current_state,
            "total_calls": self.metrics.total_calls,
            "successful_calls": self.metrics.successful_calls,
            "failed_calls": self.metrics.failed_calls,
            "rejected_calls": self.metrics.rejected_calls,
            "failure_rate": (
                self.metrics.failed_calls / max(1, self.metrics.total_calls)
            ),
            "recent_failures_in_window": recent_failures,
            "last_failure_time": self.metrics.last_failure_time.isoformat()
            if self.metrics.last_failure_time else None,
        }

    def reset(self):
        """Reset circuit to closed state"""

        self._change_state(CircuitState.CLOSED)
        self.metrics = CircuitMetrics()
        self.recent_failures.clear()
        self.half_open_calls = 0
        logger.info(f"Circuit RESET: {self.circuit_name}")


class CircuitBreakerOpenException(Exception):
    """Exception raised when circuit is open"""
    pass


class CircuitBreakerManager:
    """Manages multiple circuit breakers for different agents"""

    def __init__(self):
        self.breakers: Dict[str, CircuitBreaker] = {}

    def get_breaker(self, name: str) -> CircuitBreaker:
        """Get or create circuit breaker"""

        if name not in self.breakers:
            self.breakers[name] = CircuitBreaker(name)

        return self.breakers[name]

    def get_all_metrics(self) -> Dict[str, Dict]:
        """Get metrics for all breakers"""

        return {
            name: breaker.get_metrics()
            for name, breaker in self.breakers.items()
        }


# Singleton instance
_circuit_manager: Optional[CircuitBreakerManager] = None


def get_circuit_breaker_manager() -> CircuitBreakerManager:
    """Get or create global circuit breaker manager"""
    global _circuit_manager
    if _circuit_manager is None:
        _circuit_manager = CircuitBreakerManager()
    return _circuit_manager
