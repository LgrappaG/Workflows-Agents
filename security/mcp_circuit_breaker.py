"""
MCP Circuit Breaker for 48-Agent Hierarchy
Prevents infinite loops in agent-to-agent communication

Hard Boundary: If two agents exchange the same error message 3+ times
within 5 seconds, their communication channel is forcibly closed for 60s.
Human-in-the-loop alert is triggered.
"""

import time
import logging
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class ErrorExchange:
    """Single error message exchange between two agents"""
    error_message: str
    timestamp: float
    sender: str
    receiver: str


@dataclass
class AgentPairState:
    """State for a pair of agents communicating with each other"""
    sender: str
    receiver: str
    error_exchanges: List[ErrorExchange] = field(default_factory=list)
    circuit_state: str = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    circuit_open_time: Optional[float] = None
    failure_count: int = 0


class InterAgentCircuitBreaker:
    """
    Hard Boundary: Prevents agent-to-agent communication loops

    Monitors all MCP message routing between agents.
    Detects when same error repeats 3+ times in 5 second window.
    Opens circuit forcibly, requires human intervention to recover.
    """

    def __init__(self,
                 message_threshold: int = 3,
                 time_window: float = 5.0,
                 cooldown_seconds: float = 60.0):
        """
        Args:
            message_threshold: Same error message N times = breach
            time_window: Check within M seconds
            cooldown_seconds: How long circuit stays OPEN
        """
        self.message_threshold = message_threshold
        self.time_window = time_window
        self.cooldown_seconds = cooldown_seconds

        # Track all agent pairs: (sender, receiver) -> AgentPairState
        self.agent_pairs: Dict[Tuple[str, str], AgentPairState] = {}

        # Track which pairs have human alerts pending
        self.alerting_pairs: Dict[Tuple[str, str], Dict] = {}

        logger.info(f"[SECURITY] Circuit Breaker initialized: "
                   f"threshold={message_threshold}, "
                   f"window={time_window}s, "
                   f"cooldown={cooldown_seconds}s")

    def can_send_message(self, sender_agent: str, receiver_agent: str) -> bool:
        """
        Hard Boundary Check: Can this message be routed?

        Returns False if circuit is OPEN for this pair.
        """
        pair = (sender_agent, receiver_agent)

        if pair not in self.agent_pairs:
            self.agent_pairs[pair] = AgentPairState(sender=sender_agent, receiver=receiver_agent)

        state = self.agent_pairs[pair]

        # Check if circuit is OPEN
        if state.circuit_state == "OPEN":
            elapsed = time.time() - state.circuit_open_time

            if elapsed < self.cooldown_seconds:
                # Still in cooldown - block message
                logger.critical(
                    f"[SECURITY] Hard boundary: Agent {sender_agent}→{receiver_agent} "
                    f"circuit OPEN (cooldown for {self.cooldown_seconds - elapsed:.1f}s)"
                )
                return False
            else:
                # Cooldown expired - attempt recovery
                logger.warning(
                    f"[SECURITY] Circuit breaker recovery attempt: "
                    f"{sender_agent}→{receiver_agent}"
                )
                state.circuit_state = "HALF_OPEN"
                state.error_exchanges = []
                state.failure_count = 0

        return True

    def record_error_exchange(self, sender_agent: str, receiver_agent: str,
                             error_message: str) -> bool:
        """
        Record when receiver sends error back to sender.

        Returns False if circuit breaker should open.
        """
        pair = (sender_agent, receiver_agent)

        if pair not in self.agent_pairs:
            self.agent_pairs[pair] = AgentPairState(sender=sender_agent, receiver=receiver_agent)

        state = self.agent_pairs[pair]
        now = time.time()

        # Add exchange
        exchange = ErrorExchange(
            error_message=error_message,
            timestamp=now,
            sender=sender_agent,
            receiver=receiver_agent
        )
        state.error_exchanges.append(exchange)

        # Clean old exchanges outside time window
        state.error_exchanges = [
            ex for ex in state.error_exchanges
            if now - ex.timestamp < self.time_window
        ]

        # Count errors by type
        error_counts = defaultdict(int)
        for ex in state.error_exchanges:
            # Normalize error message (remove timestamps, etc)
            normalized = self._normalize_error(ex.error_message)
            error_counts[normalized] += 1

        # Hard Boundary: Check if same error repeated N times
        for error_type, count in error_counts.items():
            if count >= self.message_threshold:
                # BREACH - Open circuit
                logger.critical(
                    f"[SECURITY] Hard boundary violation: "
                    f"Agent {sender_agent}→{receiver_agent} "
                    f"exchanged error '{error_type}' {count} times in {self.time_window}s. "
                    f"Circuit OPEN. Human intervention required."
                )

                state.circuit_state = "OPEN"
                state.circuit_open_time = now
                state.failure_count += 1

                # Alert human
                self._trigger_human_alert(sender_agent, receiver_agent, error_type, count)

                return False

        logger.debug(
            f"[AUDIT] Error exchange recorded: "
            f"{sender_agent}→{receiver_agent}: {error_message}"
        )

        return True

    def _normalize_error(self, error_message: str) -> str:
        """Remove variable parts from error message for comparison"""
        # Remove file paths, timestamps, iteration counts
        import re
        normalized = re.sub(r'/[^\s]+', '<PATH>', error_message)
        normalized = re.sub(r'\d{10,}', '<TIMESTAMP>', normalized)
        normalized = re.sub(r'iteration \d+', '<ITERATION>', normalized)
        return normalized.strip()[:100]  # First 100 chars

    def _trigger_human_alert(self, sender: str, receiver: str, error_type: str, count: int):
        """Alert human operator of circuit breaker breach"""
        pair = (sender, receiver)
        alert_msg = (
            f"🚨 CIRCUIT BREAKER OPEN: Agent {sender} ↔ {receiver}\n"
            f"Error '{error_type}' repeated {count} times\n"
            f"Status: Circuit OPEN for {self.cooldown_seconds}s\n"
            f"Action: Check agent logs, fix issue, then reset circuit\n"
            f"Time: {datetime.now().isoformat()}"
        )

        self.alerting_pairs[pair] = {
            "message": alert_msg,
            "time": time.time(),
            "sender": sender,
            "receiver": receiver
        }

        logger.error(f"[HUMAN ALERT] {alert_msg}")
        # TODO: Send to Slack/email/dashboard

    def get_status(self) -> Dict:
        """Get operational dashboard data"""
        now = time.time()

        open_circuits = []
        at_risk_pairs = []

        for pair, state in self.agent_pairs.items():
            if state.circuit_state == "OPEN":
                elapsed = now - state.circuit_open_time
                if elapsed < self.cooldown_seconds:
                    open_circuits.append({
                        "pair": f"{state.sender}→{state.receiver}",
                        "state": "OPEN",
                        "cooldown_remaining": self.cooldown_seconds - elapsed,
                        "failure_count": state.failure_count
                    })

            # At-risk pairs (approaching threshold)
            if len(state.error_exchanges) >= self.message_threshold - 1:
                error_counts = defaultdict(int)
                for ex in state.error_exchanges:
                    normalized = self._normalize_error(ex.error_message)
                    error_counts[normalized] += 1

                at_risk_pairs.append({
                    "pair": f"{state.sender}→{state.receiver}",
                    "errors": dict(error_counts),
                    "total_exchanges": len(state.error_exchanges)
                })

        return {
            "timestamp": datetime.now().isoformat(),
            "total_agent_pairs": len(self.agent_pairs),
            "open_circuits": open_circuits,
            "at_risk_pairs": at_risk_pairs,
            "pending_human_alerts": len(self.alerting_pairs),
            "alerting_pairs": list(self.alerting_pairs.keys())
        }

    def reset_circuit(self, sender: str, receiver: str) -> bool:
        """
        Manually reset a circuit breaker (human action)

        Requires confirmation that issue was fixed.
        """
        pair = (sender, receiver)

        if pair not in self.agent_pairs:
            logger.warning(f"No circuit for pair {sender}→{receiver}")
            return False

        state = self.agent_pairs[pair]
        logger.warning(f"[ADMIN] Resetting circuit for {sender}→{receiver}")

        state.circuit_state = "CLOSED"
        state.error_exchanges = []
        state.circuit_open_time = None
        state.failure_count = 0

        # Remove from alerts
        if pair in self.alerting_pairs:
            del self.alerting_pairs[pair]

        return True


# Singleton instance
_circuit_breaker_instance: Optional[InterAgentCircuitBreaker] = None


def get_circuit_breaker() -> InterAgentCircuitBreaker:
    """Get or create singleton circuit breaker"""
    global _circuit_breaker_instance
    if _circuit_breaker_instance is None:
        _circuit_breaker_instance = InterAgentCircuitBreaker()
    return _circuit_breaker_instance


def route_mcp_message(sender_agent: str, receiver_agent: str,
                      message: Dict, execute_fn) -> Dict:
    """
    Wrapper for MCP message routing with circuit breaker.

    Args:
        sender_agent: Sending agent name
        receiver_agent: Receiving agent name
        message: Message payload
        execute_fn: Actual function to execute (e.g., agent dispatch)

    Returns:
        Response from execute_fn, or error if circuit open
    """
    cb = get_circuit_breaker()

    # Hard boundary: Check if can send
    if not cb.can_send_message(sender_agent, receiver_agent):
        logger.error(f"Circuit breaker blocked: {sender_agent}→{receiver_agent}")
        return {
            "error": "Circuit breaker open",
            "sender": sender_agent,
            "receiver": receiver_agent,
            "message": f"Communication channel closed. Check alerting_pairs for status."
        }

    try:
        # Execute the actual message routing
        response = execute_fn(sender_agent, receiver_agent, message)
        return response
    except Exception as e:
        # Record error exchange
        error_str = str(e)
        cb.record_error_exchange(sender_agent, receiver_agent, error_str)

        raise


# Example usage in orchestration engine:
if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(name)s - %(message)s"
    )

    # Create circuit breaker
    cb = get_circuit_breaker()

    # Simulate agent pair exchanging errors
    print("Simulating Agent12 ↔ Agent15 communication loop...")

    for i in range(5):
        # Simulate messages
        error = "CompilationError: Unexpected token at line 42"

        can_send = cb.can_send_message("Agent12", "Agent15")
        print(f"  Exchange {i+1}: can_send={can_send}")

        if can_send:
            cb.record_error_exchange("Agent12", "Agent15", error)

    # Check status
    print("\nCircuit Breaker Status:")
    import json
    print(json.dumps(cb.get_status(), indent=2))

    # Reset
    print("\nResetting circuit...")
    cb.reset_circuit("Agent12", "Agent15")
    print("Status after reset:")
    print(json.dumps(cb.get_status(), indent=2))
