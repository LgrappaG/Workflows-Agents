"""
End-to-End Orchestration System
================================

Multi-agent orchestration framework for autonomous goal execution with intelligent error recovery.

Features:
- 4 specialized agents (Deploy, Sync, Validation, Knowledge)
- Central orchestrator for goal decomposition and coordination
- OrchestratorAgent with GOAP planning and event-driven lifecycle
- State management with heartbeat monitoring
- Intelligent error detection and self-correction
- Event-driven pub/sub system with async event bus
- Skill dependency graph with conflict/cycle detection

Version: 1.1 (Phase 7A — Event-Driven Orchestration)
Status: Development
"""

from orchestration.engine.central_orchestrator import CentralOrchestrator
from orchestration.engine.state_manager import StateManager
from orchestration.engine.heartbeat_engine import HeartbeatEngine
from orchestration.event_bus import EventBus, Subscription
from orchestration.events import (
    BaseEvent,
    SkillValidatedEvent,
    SkillReadyEvent,
    GoalStartedEvent,
    GoalAchievedEvent,
    AgentStartedEvent,
    AgentCompletedEvent,
    AgentFailedEvent,
    WorkflowStartedEvent,
    WorkflowCompletedEvent,
    EventType,
)
from orchestration.agents.base_agent import BaseAgent
from orchestration.agents.orchestrator_agent import OrchestratorAgent
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action
from orchestration.goap.planner import GOAPPlanner
from orchestration.graph.skill_graph import SkillGraph, Skill
from orchestration.graph.conflict_detector import detect_conflicts, detect_cycles

__version__ = "1.1.0"
__all__ = [
    # Engine
    "CentralOrchestrator",
    "StateManager",
    "HeartbeatEngine",
    # Event Bus
    "EventBus",
    "Subscription",
    # Events
    "BaseEvent",
    "SkillValidatedEvent",
    "SkillReadyEvent",
    "GoalStartedEvent",
    "GoalAchievedEvent",
    "AgentStartedEvent",
    "AgentCompletedEvent",
    "AgentFailedEvent",
    "WorkflowStartedEvent",
    "WorkflowCompletedEvent",
    "EventType",
    # Agents
    "BaseAgent",
    "OrchestratorAgent",
    # GOAP
    "WorldState",
    "Action",
    "GOAPPlanner",
    # Skill Graph
    "SkillGraph",
    "Skill",
    "detect_conflicts",
    "detect_cycles",
]
