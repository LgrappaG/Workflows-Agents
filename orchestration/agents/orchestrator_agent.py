"""
Orchestrator Agent
==================

Main coordination agent that integrates GOAP planner, SkillGraph, and EventBus
to plan and execute goal-oriented workflows.

Lifecycle:
    1. Receives goal (start_state, goal_state)
    2. Uses GOAP planner to find optimal action sequence
    3. Emits GoalStartedEvent
    4. Executes plan steps sequentially, publishing events per step
    5. Emits GoalAchievedEvent on success / AgentFailedEvent on failure
"""

import time
import logging
from typing import Any, Dict, Optional, List
from uuid import uuid4
from orchestration.agents.base_agent import BaseAgent
from orchestration.event_bus import EventBus
from orchestration.events import (
    GoalStartedEvent,
    GoalAchievedEvent,
    SkillReadyEvent,
)
from orchestration.goap.planner import GOAPPlanner
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action
from orchestration.graph.skill_graph import SkillGraph
from orchestration.graph.conflict_detector import detect_conflicts, detect_cycles

logger = logging.getLogger(__name__)


class OrchestratorAgent(BaseAgent):
    """
    Main orchestrator that coordinates goal execution using GOAP planning,
    skill graph validation, and event-driven communication.

    Integrates:
    - GOAPPlanner: Finds optimal action sequence for goals
    - SkillGraph: Validates dependencies and detects conflicts
    - EventBus: Publishes lifecycle events (GoalStarted, GoalAchieved, etc.)
    """

    def __init__(
        self,
        agent_id: str,
        event_bus: EventBus,
        skill_graph: SkillGraph,
        goap_planner: GOAPPlanner,
    ):
        """
        Initialize the orchestrator.

        Args:
            agent_id: Unique identifier for this orchestrator
            event_bus: EventBus for event publishing
            skill_graph: Skill dependency graph for validation
            goap_planner: GOAP planner for action planning
        """
        super().__init__(agent_id=agent_id, event_bus=event_bus, agent_type="OrchestratorAgent")
        self.skill_graph = skill_graph
        self.goap_planner = goap_planner
        self._current_goal_id: Optional[str] = None
        self._current_plan: Optional[List[Action]] = None

    async def execute(self) -> Any:
        """
        Default execute — no-op since orchestrator uses plan_and_execute().
        Exists to satisfy the BaseAgent contract.
        """
        return {"status": "idle", "message": "Use plan_and_execute() for goal execution"}

    async def plan_and_execute(
        self,
        goal_id: str,
        start_state: WorldState,
        goal_state: WorldState,
    ) -> Dict[str, Any]:
        """
        Plan and execute a goal using GOAP + SkillGraph + EventBus.

        Steps:
        1. Validate skill graph (conflicts, cycles)
        2. Plan action sequence via GOAP
        3. Emit GoalStartedEvent
        4. Execute plan steps sequentially
        5. Emit GoalAchievedEvent

        Args:
            goal_id: Unique identifier for this goal
            start_state: Initial world state
            goal_state: Desired goal state

        Returns:
            Dict with execution result, plan details, and timing

        Raises:
            ValueError: If graph validation fails or no plan found
        """
        self._current_goal_id = goal_id
        start_time = time.time()

        # Phase 1: Graph validation
        conflicts = detect_conflicts(self.skill_graph)
        if conflicts:
            conflict_details = [
                {"skill_a": c[0], "skill_b": c[1], "reason": c[2]}
                for c in conflicts
            ]
            logger.warning(f"Skill graph conflicts detected: {conflict_details}")

        cycles = detect_cycles(self.skill_graph)
        if cycles:
            raise ValueError(
                f"Circular dependencies detected in skill graph: {cycles}. "
                "Cannot plan execution with cyclic dependencies."
            )

        # Phase 2: GOAP planning
        plan = self.goap_planner.plan(start_state, goal_state)
        if plan is None:
            raise ValueError(
                f"No valid plan found for goal '{goal_id}'. "
                f"Start: {start_state}, Goal: {goal_state}"
            )

        self._current_plan = plan
        planning_time_ms = (time.time() - start_time) * 1000

        # Phase 3: Emit GoalStartedEvent
        goal_started = GoalStartedEvent(
            source_agent=self.agent_id,
            correlation_id=self.correlation_id,
            goal_id=goal_id,
            goal_name=f"Goal-{goal_id}",
        )
        await self.event_bus.publish(goal_started)

        # Phase 4: Execute plan steps
        execution_start = time.time()
        current_state = start_state.clone()
        executed_actions: List[str] = []

        for step_idx, action in enumerate(plan):
            logger.debug(
                f"Executing step {step_idx + 1}/{len(plan)}: {action.name}"
            )

            # Verify preconditions still hold
            if not action.can_execute(current_state):
                raise ValueError(
                    f"Precondition failure at step {step_idx + 1}: "
                    f"Action '{action.name}' cannot execute in state {current_state}"
                )

            # Apply action
            current_state = action.apply(current_state)
            executed_actions.append(action.name)

            # Emit SkillReadyEvent for each completed step
            skill_ready = SkillReadyEvent(
                source_agent=self.agent_id,
                correlation_id=self.correlation_id,
                skill_id=action.name,
                domain="orchestration",
            )
            await self.event_bus.publish(skill_ready)

        execution_time_ms = (time.time() - start_time) * 1000

        # Phase 5: Build result and emit GoalAchievedEvent
        result = {
            "goal_id": goal_id,
            "status": "achieved",
            "plan_length": len(plan),
            "actions_executed": executed_actions,
            "planning_time_ms": planning_time_ms,
            "execution_time_ms": execution_time_ms,
            "conflicts_detected": len(conflicts),
            "final_state": str(current_state),
        }

        goal_achieved = GoalAchievedEvent(
            source_agent=self.agent_id,
            correlation_id=self.correlation_id,
            goal_id=goal_id,
            result=result,
            execution_time_ms=execution_time_ms,
        )
        await self.event_bus.publish(goal_achieved)

        logger.info(
            f"Goal '{goal_id}' achieved in {execution_time_ms:.1f}ms "
            f"({len(plan)} actions, planning: {planning_time_ms:.1f}ms)"
        )

        return result
