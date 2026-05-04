# Phase 7A — Event-Driven Orchestration Architecture

## Overview

Phase 7A replaces the sequential orchestration pipeline with an **event-driven, GOAP-based** system achieving **150x latency improvement** (30s → 200ms target).

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                 OrchestratorAgent                    │
│                                                     │
│  ┌──────────┐   ┌──────────┐   ┌─────────────────┐ │
│  │   GOAP   │   │  Skill   │   │    EventBus     │ │
│  │ Planner  │──▶│  Graph   │──▶│  (async pub/sub)│ │
│  │ (A*)     │   │(conflict │   │                 │ │
│  │          │   │ detect)  │   │  ┌───────────┐  │ │
│  └──────────┘   └──────────┘   │  │Subscribers│  │ │
│                                │  └───────────┘  │ │
│                                └─────────────────┘ │
└─────────────────────────────────────────────────────┘
```

## Data Flow

```
Goal Request
    │
    ▼
┌─────────────────┐
│ Graph Validation │ ← detect_conflicts(), detect_cycles()
│ (SkillGraph)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  GOAP Planning  │ ← A* search with manhattan heuristic
│  (GOAPPlanner)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GoalStartedEvent│ ← EventBus.publish()
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Execute Actions │ ← Sequential action application
│ (per-step       │
│  SkillReady     │ ← EventBus.publish() per step
│  events)        │
└────────┬────────┘
         │
         ▼
┌──────────────────┐
│GoalAchievedEvent │ ← EventBus.publish()
└──────────────────┘
```

## Component Reference

### EventBus (`orchestration/event_bus.py`)

| Feature | Detail |
|---------|--------|
| Pattern | Async pub/sub with `asyncio.Queue` |
| Subscriptions | UUID-based, type-safe |
| Handler Support | Both async and sync handlers |
| Error Handling | Exceptions caught per-handler, logged |
| Shutdown | Graceful 5s timeout |

### Event Types (`orchestration/events.py`)

| Event | Fields | Trigger |
|-------|--------|---------|
| `SkillValidatedEvent` | skill_id, status, gates, metadata | Skill passes validation |
| `SkillReadyEvent` | skill_id, domain, priority | Skill ready for execution |
| `GoalStartedEvent` | goal_id, goal_name | Orchestrator starts goal |
| `GoalAchievedEvent` | goal_id, result, execution_time_ms | Goal completed |
| `AgentStartedEvent` | agent_id, agent_type | Agent begins execution |
| `AgentCompletedEvent` | agent_id, result, execution_time_ms | Agent completes |
| `AgentFailedEvent` | agent_id, error, error_code | Agent fails |
| `WorkflowStartedEvent` | workflow_id, workflow_name | Workflow begins |
| `WorkflowCompletedEvent` | workflow_id, result, execution_time_ms | Workflow completes |

### GOAP Planner (`orchestration/goap/`)

| Component | Purpose |
|-----------|---------|
| `WorldState` | Immutable state dict with manhattan distance heuristic |
| `Action` | Preconditions + effects (PDDL-style) |
| `GOAPPlanner` | A* search over state space, max 1000 iterations |

### Skill Graph (`orchestration/graph/`)

| Component | Purpose |
|-----------|---------|
| `Skill` | Dataclass with pre/postconditions, cost, domain |
| `SkillGraph` | Directed dependency graph with cache |
| `detect_conflicts()` | Finds contradictory postconditions |
| `detect_cycles()` | DFS-based cycle detection |

### Agents (`orchestration/agents/`)

| Agent | Purpose |
|-------|---------|
| `BaseAgent` | ABC with lifecycle events (started/completed/failed) |
| `OrchestratorAgent` | Main coordinator: GOAP + SkillGraph + EventBus |

## Performance Targets

| Metric | Baseline (v9.1) | Phase 7A Target | Achieved |
|--------|-----------------|-----------------|----------|
| Orchestration Latency | 30,000 ms | 200 ms | TBD |
| Event Throughput | N/A | 500+ events/sec | TBD |
| GOAP Planning Time | Manual | <100 ms | TBD |
| Improvement Factor | — | **150x** | TBD |

## File Structure

```
orchestration/
├── __init__.py              # Module exports
├── event_bus.py             # Async pub/sub event bus
├── events.py                # 9 Pydantic event models
├── agents/
│   ├── base_agent.py        # Abstract agent with lifecycle
│   └── orchestrator_agent.py # Main GOAP+Graph coordinator
├── goap/
│   ├── world_state.py       # State representation
│   ├── action.py            # Action with preconditions/effects
│   └── planner.py           # A* search planner
└── graph/
    ├── skill_graph.py       # Dependency graph
    └── conflict_detector.py # Conflict & cycle detection
```
