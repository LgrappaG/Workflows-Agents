"""
Benchmark Script for Orchestration System
==========================================

Runs performance benchmarks and generates a summary report.

Usage:
    python scripts/benchmark_orchestration.py
"""

import asyncio
import time
import statistics
from orchestration.event_bus import EventBus
from orchestration.events import SkillReadyEvent
from orchestration.goap.planner import GOAPPlanner
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action
from orchestration.graph.skill_graph import SkillGraph, Skill
from orchestration.agents.orchestrator_agent import OrchestratorAgent


async def benchmark_event_bus(num_events: int = 5000) -> dict:
    """Benchmark EventBus throughput."""
    event_bus = EventBus()
    received = 0

    async def handler(event):
        nonlocal received
        received += 1

    await event_bus.start()
    event_bus.subscribe(SkillReadyEvent, handler)

    start = time.time()
    for i in range(num_events):
        await event_bus.publish(SkillReadyEvent(
            skill_id=f"s-{i}", domain="bench", source_agent="bench"
        ))
    await asyncio.sleep(1.0)  # Allow processing
    elapsed = time.time() - start

    await event_bus.stop()

    return {
        "name": "EventBus Throughput",
        "events": num_events,
        "received": received,
        "elapsed_s": elapsed,
        "throughput": num_events / elapsed,
        "target": 500,
        "passed": (num_events / elapsed) >= 500,
    }


async def benchmark_goap_planning(chain_length: int = 10, runs: int = 100) -> dict:
    """Benchmark GOAP planning for N-action chains."""
    planner = GOAPPlanner()

    for i in range(chain_length):
        pre = {f"step_{i}": True} if i > 0 else {"start": True}
        eff = {f"step_{i + 1}" if i < chain_length - 1 else "done": True}
        planner.add_action(Action(f"a_{i}", 1.0, pre, eff))

    start_state = WorldState({"start": True})
    goal_state = WorldState({"done": True})

    times = []
    for _ in range(runs):
        t0 = time.time()
        plan = planner.plan(start_state, goal_state)
        times.append((time.time() - t0) * 1000)

    return {
        "name": f"GOAP Planning ({chain_length}-step)",
        "runs": runs,
        "plan_length": len(plan) if plan else 0,
        "avg_ms": statistics.mean(times),
        "median_ms": statistics.median(times),
        "p95_ms": sorted(times)[int(runs * 0.95)],
        "max_ms": max(times),
        "target_ms": 100,
        "passed": statistics.mean(times) < 100,
    }


async def benchmark_full_pipeline(runs: int = 20) -> dict:
    """Benchmark full orchestration pipeline."""
    event_bus = EventBus()
    planner = GOAPPlanner()
    graph = SkillGraph()

    planner.add_action(Action("validate", 1.0, {"validated": False}, {"validated": True}))
    planner.add_action(Action("build", 2.0, {"validated": True, "built": False}, {"built": True}))
    planner.add_action(Action("deploy", 3.0, {"built": True, "deployed": False}, {"deployed": True}))

    graph.add_skill(Skill("validate", "Validate", {}, {"validated": True}, 1.0, "bench"))
    graph.add_skill(Skill("build", "Build", {"validated": True}, {"built": True}, 2.0, "bench"))
    graph.add_skill(Skill("deploy", "Deploy", {"built": True}, {"deployed": True}, 3.0, "bench"))

    await event_bus.start()

    orchestrator = OrchestratorAgent("bench-orch", event_bus, graph, planner)
    start_state = WorldState({"validated": False, "built": False, "deployed": False})
    goal_state = WorldState({"deployed": True})

    times = []
    for i in range(runs):
        t0 = time.time()
        await orchestrator.plan_and_execute(f"bench-{i}", start_state, goal_state)
        times.append((time.time() - t0) * 1000)

    await event_bus.stop()

    return {
        "name": "Full Pipeline (3-step)",
        "runs": runs,
        "avg_ms": statistics.mean(times),
        "median_ms": statistics.median(times),
        "p95_ms": sorted(times)[int(runs * 0.95)],
        "max_ms": max(times),
        "target_ms": 200,
        "passed": statistics.mean(times) < 200,
        "improvement_factor": 30000 / statistics.mean(times),
    }


async def main():
    """Run all benchmarks and print summary."""
    print("=" * 60)
    print("  Phase 7A Orchestration — Performance Benchmarks")
    print("=" * 60)

    results = []

    # Event Bus
    print("\n▶ Running EventBus throughput benchmark...")
    r = await benchmark_event_bus()
    results.append(r)
    status = "✅ PASS" if r["passed"] else "❌ FAIL"
    print(f"  {status} | {r['throughput']:.0f} events/sec (target: {r['target']})")

    # GOAP Planning
    print("\n▶ Running GOAP planning benchmark...")
    r = await benchmark_goap_planning()
    results.append(r)
    status = "✅ PASS" if r["passed"] else "❌ FAIL"
    print(f"  {status} | avg={r['avg_ms']:.2f}ms, p95={r['p95_ms']:.2f}ms (target: <{r['target_ms']}ms)")

    # Full Pipeline
    print("\n▶ Running full pipeline benchmark...")
    r = await benchmark_full_pipeline()
    results.append(r)
    status = "✅ PASS" if r["passed"] else "❌ FAIL"
    print(f"  {status} | avg={r['avg_ms']:.2f}ms, p95={r['p95_ms']:.2f}ms (target: <{r['target_ms']}ms)")
    print(f"  Improvement factor: {r['improvement_factor']:.0f}x (baseline: 30,000ms)")

    # Summary
    print("\n" + "=" * 60)
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    print(f"  Summary: {passed}/{total} benchmarks passed")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
