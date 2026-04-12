"""
Base Agent
==========

Abstract base class defining the agent interface contract.

All agents must:
1. Implement execute() method
2. Define supported goals
3. Handle errors with self-correction
4. Track metrics
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum


class AgentStatus(Enum):
    """Agent execution states"""
    IDLE = "idle"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    RECOVERED = "recovered"


class BaseAgent(ABC):
    """
    Abstract base class for all orchestration agents.

    Defines the contract that all agents must implement:
    - Goal execution
    - Error handling
    - Metrics tracking
    - State management
    """

    def __init__(self, name: str, specialization: str):
        """
        Initialize agent.

        Args:
            name: Agent name (deploy, sync, validation, knowledge)
            specialization: Agent specialization (Build, Version Control, QA, Learning)
        """
        self.name = name
        self.specialization = specialization
        self.status = AgentStatus.IDLE
        self.supported_goals = self._define_supported_goals()
        self.execution_history = []
        self.error_log = []

    @abstractmethod
    def _define_supported_goals(self) -> List[str]:
        """
        Define which goals this agent can handle.

        Returns:
            List of supported goal names
        """
        pass

    @abstractmethod
    def execute(self, goal: str, context: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Execute a goal.

        Args:
            goal: Goal name to execute
            context: Execution context
            **kwargs: Additional parameters

        Returns:
            Execution result with status, metrics, errors

        Example:
            result = agent.execute(
                goal="validate-all-skills",
                context={"phase": "phase_5_enrichment"},
                skills_path="path/to/skills"
            )
        """
        pass

    @abstractmethod
    def handle_error(self, error: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle error with intelligent recovery.

        Args:
            error: Error details
            context: Execution context

        Returns:
            Recovery strategy and result
        """
        pass

    def can_handle_goal(self, goal: str) -> bool:
        """Check if agent can handle this goal"""
        return goal in self.supported_goals

    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "name": self.name,
            "specialization": self.specialization,
            "status": self.status.value,
            "total_executions": len(self.execution_history),
            "total_errors": len(self.error_log)
        }

    def log_execution(self, result: Dict[str, Any]):
        """Log execution result"""
        self.execution_history.append({
            "timestamp": datetime.now().isoformat(),
            "status": result.get("status"),
            "duration_ms": result.get("duration_ms"),
            "goal": result.get("goal"),
            "errors": len(result.get("errors", []))
        })

    def log_error(self, error: Dict[str, Any]):
        """Log error for analysis"""
        self.error_log.append({
            "timestamp": datetime.now().isoformat(),
            "type": error.get("type"),
            "message": error.get("message"),
            "context": error.get("context")
        })

    def get_metrics(self) -> Dict[str, Any]:
        """Get agent metrics for learning"""
        if not self.execution_history:
            return {
                "agent": self.name,
                "total_executions": 0,
                "success_rate": 0,
                "avg_duration_ms": 0
            }

        successes = sum(1 for e in self.execution_history if e["status"] == "completed")
        avg_duration = sum(e["duration_ms"] for e in self.execution_history if e["duration_ms"]) / len(self.execution_history)

        return {
            "agent": self.name,
            "total_executions": len(self.execution_history),
            "successes": successes,
            "failures": len(self.error_log),
            "success_rate": successes / len(self.execution_history),
            "avg_duration_ms": avg_duration,
            "total_errors": len(self.error_log)
        }
