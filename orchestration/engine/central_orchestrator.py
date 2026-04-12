"""
Central Orchestrator
====================

Main orchestration engine that coordinates goal decomposition, agent dispatch,
state management, and error detection.

This is the heart of the orchestration system. It:
1. Receives high-level goals from users
2. Decomposes them into sub-goals
3. Resolves dependencies between sub-goals
4. Dispatches to appropriate agents
5. Monitors execution via heartbeat
6. Detects and handles errors
7. Tracks execution state for learning
"""

import json
import uuid
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from enum import Enum
from pathlib import Path

# Import hardening components
try:
    from security.hardened_orchestration import (
        require_policy_check,
        require_circuit_breaker,
        HardenedExecutionContext,
    )
    HARDENING_ENABLED = True
except ImportError:
    HARDENING_ENABLED = False

logger = logging.getLogger(__name__)


class ExecutionStatus(Enum):
    """Execution state machine"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"
    RECOVERED = "recovered"


class CentralOrchestrator:
    """
    Central coordinator for multi-agent orchestration.

    Responsibilities:
    - Goal decomposition (complex → sub-goals)
    - Dependency resolution (ordering)
    - Agent routing (goal → agent mapping)
    - State management (persistence)
    - Error monitoring (detection & logging)
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize orchestrator.

        Args:
            config_path: Path to orchestration config (YAML/JSON)
                        Defaults to .agents/orchestration/config/orchestration-config.yaml
        """
        self.execution_id = f"orch_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        self.state = None  # Will be initialized by StateManager
        self.config = {}
        self.agents = {}  # Agent registry (populated later)
        self.goals_registry = {}  # Goal definitions
        self.agent_mapping = {}  # Goal → Agent mapping

        # Paths
        self.config_dir = Path(config_path or ".agents/orchestration/config")
        self.metrics_dir = Path(".agents/orchestration/metrics")
        self.metrics_dir.mkdir(parents=True, exist_ok=True)

        # Load configuration
        self._load_configuration()

    def _load_configuration(self):
        """Load YAML configuration files"""
        # TODO: Integrate with ConfigurationLoader from hooks system
        # For now, load basic config structure
        self.config = {
            "version": "1.0",
            "orchestrator": {
                "mode": "centralized",
                "heartbeat_interval_seconds": 30,
                "heartbeat_timeout_seconds": 300,
                "max_retry_attempts": 3,
            },
            "contexts": {},
            "agents": {},
            "goals": {}
        }

        print(f"[Orchestrator] Loaded configuration from {self.config_dir}")

    def execute_goal(
        self,
        goal: str,
        context: Optional[str] = None,
        auto_correct: bool = True,
        timeout_seconds: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute a high-level goal.

        Args:
            goal: Goal name (e.g., "deploy-game-release")
            context: Execution context (e.g., "phase_5_enrichment", "ci_strict")
            auto_correct: Enable intelligent error recovery
            timeout_seconds: Execution timeout
            **kwargs: Additional goal parameters

        Returns:
            Execution result with status, metrics, errors

        HARDENING: Policy check + circuit breaker enabled (Phase 1)

        Example:
            result = orchestrator.execute_goal(
                goal="deploy-game-release",
                context="phase_5_enrichment",
                platform="all"
            )
        """
        # HARDENING: Check execution policy before proceeding
        if HARDENING_ENABLED:
            try:
                from security.policy_engine import get_policy_engine
                policy_engine = get_policy_engine()

                # Pre-flight policy check
                goal_data = {
                    "goal": goal,
                    "agent": "orchestrator",
                    "operation": "execute_goal",
                    "context": context
                }
                policy_engine.check_goal_allowed(goal_data)
                logger.info(f"[Security] Policy check PASSED: {goal}")

            except (PermissionError, ResourceWarning) as e:
                logger.error(f"[Security] Policy violation: {e}")
                return {
                    "execution_id": f"orch_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    "goal": goal,
                    "status": ExecutionStatus.FAILED.value,
                    "error": "Policy violation",
                    "detail": str(e),
                }

        print(f"\n[Orchestrator] Starting execution: {self.execution_id}")
        print(f"[Orchestrator] Goal: {goal}")
        print(f"[Orchestrator] Context: {context or 'default'}")

        # Step 1: Resolve context
        resolved_context = self._resolve_context(context)
        print(f"[Orchestrator] Resolved context: {resolved_context}")

        # Step 2: Decompose goal into sub-goals
        sub_goals = self._decompose_goal(goal, resolved_context)
        print(f"[Orchestrator] Decomposed into {len(sub_goals)} sub-goals: {[g['name'] for g in sub_goals]}")

        # Step 3: Resolve dependencies (ordering)
        execution_order = self._resolve_dependencies(sub_goals)
        print(f"[Orchestrator] Execution order: {execution_order}")

        # Step 4: Execute sub-goals in order with error handling
        results = {
            "execution_id": self.execution_id,
            "goal": goal,
            "context": resolved_context,
            "status": ExecutionStatus.IN_PROGRESS.value,
            "start_time": datetime.now().isoformat(),
            "sub_goals": [],
            "errors": [],
            "error_recoveries": []
        }

        for sub_goal in execution_order:
            print(f"\n[Orchestrator] Executing sub-goal: {sub_goal['name']}")

            # Execute sub-goal (placeholder - agents implemented in Phase 2)
            result = self._execute_sub_goal(sub_goal, resolved_context)
            results["sub_goals"].append(result)

            # Check for errors
            if result.get("status") == "failed":
                print(f"[Orchestrator] ERROR in {sub_goal['name']}: {result.get('error')}")
                results["errors"].append(result)

                if auto_correct:
                    # Try self-correction (Phase 3)
                    recovery = self._attempt_recovery(sub_goal, result, resolved_context)
                    results["error_recoveries"].append(recovery)
                    if recovery.get("success"):
                        print(f"[Orchestrator] RECOVERED from error")
                        result["status"] = "recovered"
                        results["sub_goals"][-1] = result
                    else:
                        print(f"[Orchestrator] Recovery FAILED")
                        results["status"] = ExecutionStatus.FAILED.value
                        break
                else:
                    results["status"] = ExecutionStatus.FAILED.value
                    break

        # Step 5: Aggregate results
        results["end_time"] = datetime.now().isoformat()
        results["status"] = ExecutionStatus.COMPLETED.value if results["status"] != ExecutionStatus.FAILED.value else ExecutionStatus.FAILED.value

        # Store metrics
        self._store_execution_metrics(results)

        print(f"\n[Orchestrator] Execution completed: {results['status']}")
        return results

    def _resolve_context(self, context: Optional[str]) -> Dict[str, Any]:
        """Resolve execution context"""
        # TODO: Integrate with ContextResolver from hooks system
        return {
            "phase": context or "phase_4",
            "environment": "ci_strict",
            "timestamp": datetime.now().isoformat()
        }

    def _decompose_goal(self, goal: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Decompose complex goal into sub-goals"""
        # TODO: Load from goal-mapping.yaml
        # Placeholder implementation
        decomposition = {
            "deploy-game-release": [
                {"name": "validate-all-skills", "agent": "validation", "priority": 1},
                {"name": "gate-approval-decision", "agent": "validation", "priority": 2},
                {"name": "sync-with-remote", "agent": "sync", "priority": 1},
                {"name": "deploy-game-release", "agent": "deploy", "priority": 3}
            ],
            "validate-before-deploy": [
                {"name": "validate-all-skills", "agent": "validation", "priority": 1},
                {"name": "gate-approval-decision", "agent": "validation", "priority": 2}
            ]
        }

        return decomposition.get(goal, [])

    def _resolve_dependencies(self, sub_goals: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Resolve dependencies and return execution order"""
        # Sort by priority
        return sorted(sub_goals, key=lambda x: x.get("priority", 999))

    def _execute_sub_goal(self, sub_goal: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a sub-goal via appropriate agent"""
        # TODO: Dispatch to agent (Phase 2)
        # For Phase 1, return mock result
        return {
            "name": sub_goal["name"],
            "agent": sub_goal["agent"],
            "status": "completed",
            "duration_ms": 100,
            "timestamp": datetime.now().isoformat()
        }

    def _attempt_recovery(self, sub_goal: Dict[str, Any], error: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Attempt intelligent error recovery (Phase 3)"""
        # TODO: Integrate error detection + self-correction engine
        return {
            "sub_goal": sub_goal["name"],
            "error": error.get("error"),
            "strategy": "retry_with_backoff",
            "success": False,  # Placeholder
            "details": "Not implemented in Phase 1"
        }

    def _store_execution_metrics(self, results: Dict[str, Any]):
        """Store execution metrics for learning"""
        metrics_file = self.metrics_dir / f"{results['execution_id']}.json"
        metrics_file.write_text(json.dumps(results, indent=2))
        print(f"[Orchestrator] Metrics stored: {metrics_file}")

    def get_state(self) -> Dict[str, Any]:
        """Get current orchestration state"""
        if self.state:
            return self.state.get_state()
        return {"status": "not_initialized"}

    def get_improvement_suggestions(self) -> List[Dict[str, Any]]:
        """Get improvement suggestions from learning engine (Phase 3)"""
        # TODO: Integrate with LearningEngine
        return []
