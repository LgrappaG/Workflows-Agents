"""
Recovery Manager
================

Manages advanced recovery strategies and retry logic.

Responsibilities:
- Exponential backoff with jitter
- Circuit breaker pattern
- Rollback sequencing
- Retry budget management
- Recovery state tracking
"""

import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable, Tuple
from enum import Enum


class CircuitState(Enum):
    """Circuit breaker states"""
    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Failing, denying requests
    HALF_OPEN = "half_open"  # Testing recovery


class RetryStrategy:
    """Base retry strategy"""

    def __init__(self, max_attempts: int = 3):
        self.max_attempts = max_attempts
        self.attempt_count = 0
        self.last_attempt_time = None

    def should_retry(self) -> bool:
        """Check if should retry"""
        return self.attempt_count < self.max_attempts

    def get_wait_time(self) -> float:
        """Get time to wait before next attempt (seconds)"""
        return 1.0

    def mark_attempt(self):
        """Mark an attempt"""
        self.attempt_count += 1
        self.last_attempt_time = datetime.now()

    def reset(self):
        """Reset retry state"""
        self.attempt_count = 0
        self.last_attempt_time = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "attempt_count": self.attempt_count,
            "max_attempts": self.max_attempts,
            "can_retry": self.should_retry()
        }


class ExponentialBackoffStrategy(RetryStrategy):
    """Exponential backoff with jitter"""

    def __init__(self, max_attempts: int = 3, base_delay: float = 1.0, max_delay: float = 60.0):
        super().__init__(max_attempts)
        self.base_delay = base_delay
        self.max_delay = max_delay

    def get_wait_time(self) -> float:
        """
        Calculate wait time using exponential backoff with jitter.
        wait_time = min(base_delay * 2^attempt + jitter, max_delay)
        """
        exponential = self.base_delay * (2 ** self.attempt_count)
        jitter = random.uniform(0, exponential * 0.1)  # 10% jitter
        wait_time = min(exponential + jitter, self.max_delay)
        return wait_time


class LinearBackoffStrategy(RetryStrategy):
    """Linear backoff strategy"""

    def __init__(self, max_attempts: int = 3, increment_seconds: float = 1.0):
        super().__init__(max_attempts)
        self.increment_seconds = increment_seconds

    def get_wait_time(self) -> float:
        """wait_time = attempt_count * increment_seconds"""
        return self.attempt_count * self.increment_seconds


class CircuitBreaker:
    """Circuit breaker pattern implementation"""

    def __init__(
        self,
        operation_name: str,
        failure_threshold: int = 5,
        state_timeout_seconds: int = 60
    ):
        self.operation_name = operation_name
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.state_timeout_seconds = state_timeout_seconds
        self.last_state_change = datetime.now()
        self.success_count_in_half_open = 0
        self.required_successes_to_close = 3

    def record_success(self):
        """Record successful operation"""
        if self.state == CircuitState.CLOSED:
            self.failure_count = 0

        elif self.state == CircuitState.HALF_OPEN:
            self.success_count_in_half_open += 1
            if self.success_count_in_half_open >= self.required_successes_to_close:
                self._close_circuit()

    def record_failure(self):
        """Record failed operation"""
        self.failure_count += 1

        if self.state == CircuitState.CLOSED:
            if self.failure_count >= self.failure_threshold:
                self._open_circuit()

        elif self.state == CircuitState.HALF_OPEN:
            self._open_circuit()

    def can_attempt_operation(self) -> bool:
        """Check if operation can be attempted"""
        if self.state == CircuitState.CLOSED:
            return True

        elif self.state == CircuitState.OPEN:
            # Check if timeout elapsed
            elapsed = (datetime.now() - self.last_state_change).total_seconds()
            if elapsed > self.state_timeout_seconds:
                self._transition_to_half_open()
                return True
            return False

        elif self.state == CircuitState.HALF_OPEN:
            return True

        return False

    def _open_circuit(self):
        """Transition to OPEN state"""
        self.state = CircuitState.OPEN
        self.last_state_change = datetime.now()

    def _transition_to_half_open(self):
        """Transition to HALF_OPEN state"""
        self.state = CircuitState.HALF_OPEN
        self.success_count_in_half_open = 0
        self.last_state_change = datetime.now()

    def _close_circuit(self):
        """Transition to CLOSED state"""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_state_change = datetime.now()

    def get_status(self) -> Dict[str, Any]:
        """Get circuit breaker status"""
        return {
            "operation": self.operation_name,
            "state": self.state.value,
            "failure_count": self.failure_count,
            "last_state_change": self.last_state_change.isoformat()
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return self.get_status()


class RollbackSequence:
    """Manages rollback of multiple operations"""

    def __init__(self, operation_id: str):
        self.operation_id = operation_id
        self.rollback_steps = []  # List of (step_name, rollback_fn)
        self.executed_steps = []  # Track successfully executed steps
        self.rollback_status = "pending"

    def add_step(self, step_name: str, operation_fn: Callable, rollback_fn: Callable):
        """
        Add an operation with associated rollback.

        Args:
            step_name: Descriptive name for the step
            operation_fn: Function to execute
            rollback_fn: Function to execute on rollback
        """
        self.rollback_steps.append({
            "step_name": step_name,
            "operation": operation_fn,
            "rollback": rollback_fn,
            "status": "pending"
        })

    def execute(self) -> Dict[str, Any]:
        """
        Execute all steps in sequence.
        If any fails, rollback executed steps in reverse order.
        """
        result = {
            "operation_id": self.operation_id,
            "total_steps": len(self.rollback_steps),
            "executed_steps": [],
            "status": "in_progress"
        }

        for i, step in enumerate(self.rollback_steps):
            try:
                # Execute step
                step_result = step["operation"]()
                step["status"] = "completed"
                self.executed_steps.append(step)

                result["executed_steps"].append({
                    "step": step["step_name"],
                    "status": "completed"
                })

            except Exception as e:
                # Execution failed - rollback
                result["failed_step"] = step["step_name"]
                result["error"] = str(e)
                result["executed_steps"].append({
                    "step": step["step_name"],
                    "status": "failed",
                    "error": str(e)
                })

                # Rollback executed steps in reverse
                self._rollback_executed_steps(result)
                self.rollback_status = "rolled_back"
                result["status"] = "rolled_back"
                return result

        self.rollback_status = "completed"
        result["status"] = "completed"
        return result

    def _rollback_executed_steps(self, result: Dict[str, Any]):
        """Rollback executed steps in reverse order"""
        result["rollback_steps"] = []

        for step in reversed(self.executed_steps):
            try:
                step["rollback"]()
                result["rollback_steps"].append({
                    "step": step["step_name"],
                    "rollback_status": "completed"
                })
            except Exception as e:
                result["rollback_steps"].append({
                    "step": step["step_name"],
                    "rollback_status": "failed",
                    "error": str(e)
                })

    def get_status(self) -> Dict[str, Any]:
        """Get rollback sequence status"""
        return {
            "operation_id": self.operation_id,
            "status": self.rollback_status,
            "total_steps": len(self.rollback_steps),
            "completed_steps": len(self.executed_steps),
            "remaining_steps": len(self.rollback_steps) - len(self.executed_steps)
        }


class RetryBudget:
    """Manages per-operation retry budget"""

    def __init__(self, total_retries_per_hour: int = 100):
        self.total_retries_per_hour = total_retries_per_hour
        self.retry_history = []  # [(timestamp, operation_name)]
        self.hour_start = datetime.now()

    def can_retry(self, operation_name: str) -> bool:
        """Check if retry budget available"""
        # Clean old entries (> 1 hour old)
        current_time = datetime.now()
        self.retry_history = [
            (ts, op) for ts, op in self.retry_history
            if (current_time - ts).total_seconds() < 3600
        ]

        # Check budget
        return len(self.retry_history) < self.total_retries_per_hour

    def record_retry(self, operation_name: str):
        """Record a retry attempt"""
        self.retry_history.append((datetime.now(), operation_name))

    def get_remaining_budget(self) -> int:
        """Get remaining retry budget"""
        current_time = datetime.now()
        self.retry_history = [
            (ts, op) for ts, op in self.retry_history
            if (current_time - ts).total_seconds() < 3600
        ]

        return max(0, self.total_retries_per_hour - len(self.retry_history))

    def get_status(self) -> Dict[str, Any]:
        """Get budget status"""
        return {
            "total_budget": self.total_retries_per_hour,
            "used": len(self.retry_history),
            "remaining": self.get_remaining_budget(),
            "reset_in_seconds": 3600 - (datetime.now() - self.hour_start).total_seconds()
        }


class RecoveryManager:
    """Main recovery manager"""

    def __init__(self):
        self.circuit_breakers = {}  # operation_name -> CircuitBreaker
        self.retry_strategies = {}  # operation_name -> RetryStrategy
        self.retry_budget = RetryBudget()
        self.recovery_attempts = []

    def get_circuit_breaker(self, operation_name: str) -> CircuitBreaker:
        """Get or create circuit breaker for operation"""
        if operation_name not in self.circuit_breakers:
            self.circuit_breakers[operation_name] = CircuitBreaker(operation_name)

        return self.circuit_breakers[operation_name]

    def get_retry_strategy(
        self,
        operation_name: str,
        strategy_type: str = "exponential",
        max_attempts: int = 3
    ) -> RetryStrategy:
        """Get or create retry strategy for operation"""
        if operation_name not in self.retry_strategies:
            if strategy_type == "exponential":
                self.retry_strategies[operation_name] = ExponentialBackoffStrategy(max_attempts)
            elif strategy_type == "linear":
                self.retry_strategies[operation_name] = LinearBackoffStrategy(max_attempts)
            else:
                self.retry_strategies[operation_name] = RetryStrategy(max_attempts)

        return self.retry_strategies[operation_name]

    def can_attempt_recovery(self, operation_name: str) -> Tuple[bool, str]:
        """
        Check if recovery can be attempted.
        Returns (can_attempt, reason)
        """
        # Check circuit breaker
        circuit_breaker = self.get_circuit_breaker(operation_name)
        if not circuit_breaker.can_attempt_operation():
            return (False, f"Circuit breaker {circuit_breaker.state.value}")

        # Check retry budget
        if not self.retry_budget.can_retry(operation_name):
            return (False, "Retry budget exhausted")

        # Check retry strategy
        strategy = self.get_retry_strategy(operation_name)
        if not strategy.should_retry():
            return (False, f"Max retries exceeded ({strategy.max_attempts})")

        return (True, "Can attempt recovery")

    def attempt_recovery(
        self,
        operation_name: str,
        operation_fn: Callable,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Attempt recovery of failed operation.
        Manages retries with backoff and circuit breaker coordination.
        """
        recovery_result = {
            "operation": operation_name,
            "attempt": 0,
            "status": "failed",
            "attempts": []
        }

        while True:
            can_attempt, reason = self.can_attempt_recovery(operation_name)

            if not can_attempt:
                recovery_result["final_reason"] = reason
                return recovery_result

            # Get strategy
            strategy = self.get_retry_strategy(operation_name)
            strategy.mark_attempt()
            recovery_result["attempt"] += 1

            # Wait if needed
            if strategy.attempt_count > 1:
                wait_time = strategy.get_wait_time()
                time.sleep(wait_time)

            # Attempt operation
            attempt_info = {
                "attempt_number": strategy.attempt_count,
                "timestamp": datetime.now().isoformat()
            }

            try:
                operation_fn()
                circuit_breaker = self.get_circuit_breaker(operation_name)
                circuit_breaker.record_success()
                self.retry_budget.record_retry(operation_name)

                attempt_info["status"] = "success"
                recovery_result["attempts"].append(attempt_info)
                recovery_result["status"] = "recovered"
                return recovery_result

            except Exception as e:
                circuit_breaker = self.get_circuit_breaker(operation_name)
                circuit_breaker.record_failure()
                self.retry_budget.record_retry(operation_name)

                attempt_info["status"] = "failed"
                attempt_info["error"] = str(e)
                recovery_result["attempts"].append(attempt_info)

                # Continue loop to retry

    def create_rollback_sequence(self, operation_id: str) -> RollbackSequence:
        """Create a new rollback sequence"""
        return RollbackSequence(operation_id)

    def get_recovery_status(self) -> Dict[str, Any]:
        """Get overall recovery status"""
        return {
            "circuit_breakers": {
                name: cb.get_status()
                for name, cb in self.circuit_breakers.items()
            },
            "retry_budget": self.retry_budget.get_status(),
            "active_strategies": len(self.retry_strategies)
        }

    def reset_operation(self, operation_name: str):
        """Reset recovery state for an operation"""
        if operation_name in self.retry_strategies:
            self.retry_strategies[operation_name].reset()

        if operation_name in self.circuit_breakers:
            cb = self.circuit_breakers[operation_name]
            cb._close_circuit()
