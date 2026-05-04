"""
Integration Tests
=================

End-to-end tests verifying the full orchestration pipeline:
EventBus + GOAP + SkillGraph + OrchestratorAgent

Tests cover:
1. Full goal lifecycle (plan → execute → events)
2. Error handling (no plan found, cycle detection)
3. Multi-step planning with event verification
"""

import asyncio
import pytest
from orchestration.event_bus import EventBus
from orchestration.events import (
    GoalStartedEvent,
    GoalAchievedEvent,
    SkillReadyEvent,
    AgentStartedEvent,
    AgentCompletedEvent,
)
from orchestration.goap.planner import GOAPPlanner
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action
from orchestration.graph.skill_graph import SkillGraph, Skill
from orchestration.agents.orchestrator_agent import OrchestratorAgent


def _build_test_planner() -> GOAPPlanner:
    """Build a GOAP planner with standard test actions."""
    planner = GOAPPlanner()

    planner.add_action(Action(
        name="validate",
        cost=1.0,
        preconditions={"validated": False},
        effects={"validated": True},
    ))
    planner.add_action(Action(
        name="build",
        cost=2.0,
        preconditions={"validated": True, "built": False},
        effects={"built": True},
    ))
    planner.add_action(Action(
        name="deploy",
        cost=3.0,
        preconditions={"built": True, "deployed": False},
        effects={"deployed": True},
    ))

    return planner


def _build_test_skill_graph() -> SkillGraph:
    """Build a skill graph matching the test actions."""
    graph = SkillGraph()

    graph.add_skill(Skill(
        id="validate",
        name="Validation Skill",
        preconditions={},
        postconditions={"validated": True},
        cost=1.0,
        domain="testing",
    ))
    graph.add_skill(Skill(
        id="build",
        name="Build Skill",
        preconditions={"validated": True},
        postconditions={"built": True},
        cost=2.0,
        domain="testing",
    ))
    graph.add_skill(Skill(
        id="deploy",
        name="Deploy Skill",
        preconditions={"built": True},
        postconditions={"deployed": True},
        cost=3.0,
        domain="testing",
    ))

    return graph


@pytest.mark.asyncio
async def test_full_orchestration_pipeline():
    """
    End-to-end test: OrchestratorAgent plans and executes a 3-step goal.

    Verifies:
    1. GOAP planner finds valid 3-action plan
    2. GoalStartedEvent emitted with correct goal_id
    3. SkillReadyEvent emitted for each action step
    4. GoalAchievedEvent emitted with result containing execution timing
    5. All events arrive in correct order
    """
    event_bus = EventBus()
    planner = _build_test_planner()
    skill_graph = _build_test_skill_graph()
    received_events = []

    async def handler(event):
        received_events.append(event)

    await event_bus.start()

    try:
        # Subscribe to goal and skill events
        event_bus.subscribe(GoalStartedEvent, handler)
        event_bus.subscribe(GoalAchievedEvent, handler)
        event_bus.subscribe(SkillReadyEvent, handler)

        # Create orchestrator
        orchestrator = OrchestratorAgent(
            agent_id="orchestrator-001",
            event_bus=event_bus,
            skill_graph=skill_graph,
            goap_planner=planner,
        )

        # Define goal: validated=False, built=False, deployed=False → deployed=True
        start_state = WorldState({
            "validated": False,
            "built": False,
            "deployed": False,
        })
        goal_state = WorldState({"deployed": True})

        # Execute
        result = await orchestrator.plan_and_execute(
            goal_id="goal-deploy-001",
            start_state=start_state,
            goal_state=goal_state,
        )

        # Allow event processing
        await asyncio.sleep(0.1)

        # Verify result
        assert result["status"] == "achieved"
        assert result["plan_length"] == 3
        assert result["actions_executed"] == ["validate", "build", "deploy"]
        assert result["execution_time_ms"] >= 0
        assert result["planning_time_ms"] >= 0

        # Verify events (GoalStarted + 3x SkillReady + GoalAchieved = 5 events)
        assert len(received_events) == 5, f"Expected 5 events, got {len(received_events)}: {[type(e).__name__ for e in received_events]}"

        # Event order verification
        assert isinstance(received_events[0], GoalStartedEvent)
        assert received_events[0].goal_id == "goal-deploy-001"

        assert isinstance(received_events[1], SkillReadyEvent)
        assert received_events[1].skill_id == "validate"

        assert isinstance(received_events[2], SkillReadyEvent)
        assert received_events[2].skill_id == "build"

        assert isinstance(received_events[3], SkillReadyEvent)
        assert received_events[3].skill_id == "deploy"

        assert isinstance(received_events[4], GoalAchievedEvent)
        assert received_events[4].goal_id == "goal-deploy-001"
        assert received_events[4].execution_time_ms >= 0

    finally:
        await event_bus.stop()


@pytest.mark.asyncio
async def test_orchestrator_no_plan_found():
    """
    Test that orchestrator raises ValueError when no plan exists.

    Verifies:
    - Impossible goal raises clear error
    - No events emitted on planning failure
    """
    event_bus = EventBus()
    planner = GOAPPlanner()  # Empty planner — no actions available
    skill_graph = SkillGraph()
    received_events = []

    async def handler(event):
        received_events.append(event)

    await event_bus.start()

    try:
        event_bus.subscribe(GoalStartedEvent, handler)
        event_bus.subscribe(GoalAchievedEvent, handler)

        orchestrator = OrchestratorAgent(
            agent_id="orchestrator-002",
            event_bus=event_bus,
            skill_graph=skill_graph,
            goap_planner=planner,
        )

        start_state = WorldState({"deployed": False})
        goal_state = WorldState({"deployed": True})

        with pytest.raises(ValueError, match="No valid plan found"):
            await orchestrator.plan_and_execute(
                goal_id="goal-impossible",
                start_state=start_state,
                goal_state=goal_state,
            )

        # No events should be emitted since planning failed before GoalStarted
        await asyncio.sleep(0.05)
        assert len(received_events) == 0

    finally:
        await event_bus.stop()


@pytest.mark.asyncio
async def test_orchestrator_cycle_detection():
    """
    Test that orchestrator raises ValueError when skill graph has cycles.

    Verifies:
    - Circular dependency detected during graph validation
    - Clear error message with cycle details
    """
    event_bus = EventBus()
    planner = _build_test_planner()
    skill_graph = SkillGraph()

    # Create circular dependency: A needs B's output, B needs A's output
    skill_graph.add_skill(Skill(
        id="skill_a",
        name="Skill A",
        preconditions={"b_done": True},
        postconditions={"a_done": True},
    ))
    skill_graph.add_skill(Skill(
        id="skill_b",
        name="Skill B",
        preconditions={"a_done": True},
        postconditions={"b_done": True},
    ))

    await event_bus.start()

    try:
        orchestrator = OrchestratorAgent(
            agent_id="orchestrator-003",
            event_bus=event_bus,
            skill_graph=skill_graph,
            goap_planner=planner,
        )

        start_state = WorldState({"a_done": False, "b_done": False})
        goal_state = WorldState({"a_done": True, "b_done": True})

        with pytest.raises(ValueError, match="Circular dependencies"):
            await orchestrator.plan_and_execute(
                goal_id="goal-cyclic",
                start_state=start_state,
                goal_state=goal_state,
            )

    finally:
        await event_bus.stop()


@pytest.mark.asyncio
async def test_orchestrator_already_at_goal():
    """
    Test that orchestrator handles already-achieved goals gracefully.

    Verifies:
    - Empty plan returned (0 actions)
    - GoalStartedEvent and GoalAchievedEvent still emitted
    """
    event_bus = EventBus()
    planner = _build_test_planner()
    skill_graph = _build_test_skill_graph()
    received_events = []

    async def handler(event):
        received_events.append(event)

    await event_bus.start()

    try:
        event_bus.subscribe(GoalStartedEvent, handler)
        event_bus.subscribe(GoalAchievedEvent, handler)

        orchestrator = OrchestratorAgent(
            agent_id="orchestrator-004",
            event_bus=event_bus,
            skill_graph=skill_graph,
            goap_planner=planner,
        )

        # Already deployed
        start_state = WorldState({"deployed": True})
        goal_state = WorldState({"deployed": True})

        result = await orchestrator.plan_and_execute(
            goal_id="goal-noop",
            start_state=start_state,
            goal_state=goal_state,
        )

        await asyncio.sleep(0.1)

        assert result["status"] == "achieved"
        assert result["plan_length"] == 0
        assert result["actions_executed"] == []

        # GoalStarted + GoalAchieved = 2 events
        assert len(received_events) == 2
        assert isinstance(received_events[0], GoalStartedEvent)
        assert isinstance(received_events[1], GoalAchievedEvent)

    finally:
        await event_bus.stop()
