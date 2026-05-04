"""
Performance Tests
=================

Benchmarks for orchestration system components:
1. Event bus throughput (target: 500+ events/sec)
2. GOAP planning time (target: <100ms for 10-action chains)
3. Full orchestration pipeline latency
"""

import asyncio
import time
import pytest
from orchestration.event_bus import EventBus
from orchestration.events import SkillReadyEvent, GoalStartedEvent, GoalAchievedEvent
from orchestration.goap.planner import GOAPPlanner
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action
from orchestration.graph.skill_graph import SkillGraph, Skill
from orchestration.agents.orchestrator_agent import OrchestratorAgent


@pytest.mark.asyncio
async def test_event_bus_throughput():
    """
    Benchmark: EventBus must handle 500+ events/sec.

    Publishes 1000 events and measures throughput.
    """
    event_bus = EventBus()
    received_count = 0

    async def handler(event):
        nonlocal received_count
        received_count += 1

    await event_bus.start()

    try:
        event_bus.subscribe(SkillReadyEvent, handler)

        # Publish 1000 events
        num_events = 1000
        start_time = time.time()

        for i in range(num_events):
            event = SkillReadyEvent(
                skill_id=f"skill-{i}",
                domain="benchmark",
                source_agent="benchmark-agent",
            )
            await event_bus.publish(event)

        # Wait for all events to be processed
        await asyncio.sleep(0.5)

        elapsed = time.time() - start_time
        throughput = num_events / elapsed if elapsed > 0 else float("inf")

        # Verify throughput target
        assert throughput >= 500, (
            f"EventBus throughput {throughput:.0f} events/sec "
            f"below target of 500 events/sec"
        )
        assert received_count == num_events, (
            f"Expected {num_events} events, received {received_count}"
        )

        print(f"\n[PERF] EventBus Throughput: {throughput:.0f} events/sec ({num_events} events in {elapsed:.3f}s)")

    finally:
        await event_bus.stop()


@pytest.mark.asyncio
async def test_goap_planning_performance():
    """
    Benchmark: GOAP planner must find 10-action chain in <100ms.

    Creates a linear 10-step chain and measures planning time.
    """
    planner = GOAPPlanner()

    # Build a 10-step linear chain: step_0 → step_1 → ... → step_9
    num_steps = 10
    for i in range(num_steps):
        preconditions = {f"step_{i}": True} if i > 0 else {"start": True}
        effects = {f"step_{i + 1}" if i < num_steps - 1 else "done": True}

        planner.add_action(Action(
            name=f"action_{i}",
            cost=1.0,
            preconditions=preconditions,
            effects=effects,
        ))

    # Plan from start → done
    start_state = WorldState({"start": True})
    goal_state = WorldState({"done": True})

    # Measure planning time (average over 10 runs)
    times = []
    for _ in range(10):
        start_time = time.time()
        plan = planner.plan(start_state, goal_state)
        elapsed_ms = (time.time() - start_time) * 1000
        times.append(elapsed_ms)

    avg_time_ms = sum(times) / len(times)
    max_time_ms = max(times)

    # Verify plan correctness
    assert plan is not None, "GOAP planner should find a valid plan"
    assert len(plan) == num_steps, f"Expected {num_steps}-step plan, got {len(plan)}"

    # Verify performance target
    assert avg_time_ms < 100, (
        f"GOAP planning avg {avg_time_ms:.1f}ms exceeds 100ms target"
    )

    print(f"\n[PERF] GOAP Planning: avg={avg_time_ms:.2f}ms, max={max_time_ms:.2f}ms (10-action chain, 10 runs)")


@pytest.mark.asyncio
async def test_full_pipeline_latency():
    """
    Benchmark: Full orchestration pipeline (goal → plan → execute → events) latency.

    Target: <200ms for a 3-step plan.
    """
    event_bus = EventBus()
    planner = GOAPPlanner()
    skill_graph = SkillGraph()

    # Setup 3-step pipeline
    planner.add_action(Action("validate", 1.0, {"validated": False}, {"validated": True}))
    planner.add_action(Action("build", 2.0, {"validated": True, "built": False}, {"built": True}))
    planner.add_action(Action("deploy", 3.0, {"built": True, "deployed": False}, {"deployed": True}))

    skill_graph.add_skill(Skill("validate", "Validate", {}, {"validated": True}, 1.0, "test"))
    skill_graph.add_skill(Skill("build", "Build", {"validated": True}, {"built": True}, 2.0, "test"))
    skill_graph.add_skill(Skill("deploy", "Deploy", {"built": True}, {"deployed": True}, 3.0, "test"))

    await event_bus.start()

    try:
        orchestrator = OrchestratorAgent(
            agent_id="bench-orch-001",
            event_bus=event_bus,
            skill_graph=skill_graph,
            goap_planner=planner,
        )

        start_state = WorldState({"validated": False, "built": False, "deployed": False})
        goal_state = WorldState({"deployed": True})

        # Measure end-to-end latency (average over 5 runs)
        times = []
        for i in range(5):
            start_time = time.time()
            result = await orchestrator.plan_and_execute(
                goal_id=f"bench-goal-{i}",
                start_state=start_state,
                goal_state=goal_state,
            )
            elapsed_ms = (time.time() - start_time) * 1000
            times.append(elapsed_ms)

        avg_time_ms = sum(times) / len(times)
        max_time_ms = max(times)

        # Verify correctness
        assert result["status"] == "achieved"
        assert result["plan_length"] == 3

        # Verify performance target
        assert avg_time_ms < 200, (
            f"Pipeline latency avg {avg_time_ms:.1f}ms exceeds 200ms target"
        )

        print(f"\n[PERF] Full Pipeline: avg={avg_time_ms:.2f}ms, max={max_time_ms:.2f}ms (3-step plan, 5 runs)")

    finally:
        await event_bus.stop()
