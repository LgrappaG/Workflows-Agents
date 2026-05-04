"""
End-to-End Orchestration System
================================

Multi-agent orchestration framework for autonomous goal execution with intelligent error recovery.

Features:
- 4 specialized agents (Deploy, Sync, Validation, Knowledge)
- Central orchestrator for goal decomposition and coordination
- State management with heartbeat monitoring
- Intelligent error detection and self-correction
- Learning integration for continuous improvement
- Async event bus with pub/sub pattern for agent communication

Version: 1.0
Status: Development
"""

from orchestration.engine.central_orchestrator import CentralOrchestrator
from orchestration.engine.state_manager import StateManager
from orchestration.engine.heartbeat_engine import HeartbeatEngine
from orchestration.event_bus import EventBus
from orchestration.events import (
    BaseEvent,
    SkillValidatedEvent,
    SkillReadyEvent,
    GoalStartedEvent,
    GoalAchievedEvent,
    AgentStartedEvent,
    AgentCompletedEvent,
    AgentFailedEvent,
)

__version__ = "1.0.0"
__all__ = [
    "CentralOrchestrator",
    "StateManager",
    "HeartbeatEngine",
    "EventBus",
    "BaseEvent",
    "SkillValidatedEvent",
    "SkillReadyEvent",
    "GoalStartedEvent",
    "GoalAchievedEvent",
    "AgentStartedEvent",
    "AgentCompletedEvent",
    "AgentFailedEvent",
]
