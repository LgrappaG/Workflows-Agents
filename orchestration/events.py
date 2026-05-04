"""
Event Type Definitions
======================

Pydantic-based event types for the orchestration system.
All events inherit from BaseEvent and include timestamp, source_agent, and correlation_id.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

DEFAULT_SKILL_PRIORITY = 5  # Default priority for ready skills


class EventType(str, Enum):
    """Enumeration of all event types in the system"""
    SKILL_VALIDATED = "skill_validated"
    SKILL_READY = "skill_ready"
    GOAL_STARTED = "goal_started"
    GOAL_ACHIEVED = "goal_achieved"
    AGENT_STARTED = "agent_started"
    AGENT_COMPLETED = "agent_completed"
    AGENT_FAILED = "agent_failed"
    WORKFLOW_STARTED = "workflow_started"
    WORKFLOW_COMPLETED = "workflow_completed"


class BaseEvent(BaseModel):
    """Base class for all events"""
    model_config = ConfigDict(use_enum_values=False)

    event_type: EventType
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source_agent: Optional[str] = None
    correlation_id: Optional[str] = None


class SkillValidatedEvent(BaseEvent):
    """Emitted when a skill passes validation gates"""
    event_type: EventType = EventType.SKILL_VALIDATED
    skill_id: str
    status: str  # "passed", "failed", "partial"
    gates: List[int] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SkillReadyEvent(BaseEvent):
    """Emitted when a skill is ready for execution"""
    event_type: EventType = EventType.SKILL_READY
    skill_id: str
    domain: str
    priority: int = DEFAULT_SKILL_PRIORITY


class GoalStartedEvent(BaseEvent):
    """Emitted when orchestration starts a goal"""
    event_type: EventType = EventType.GOAL_STARTED
    goal_id: str
    goal_name: str


class GoalAchievedEvent(BaseEvent):
    """Emitted when a goal is achieved"""
    event_type: EventType = EventType.GOAL_ACHIEVED
    goal_id: str
    result: Dict[str, Any]
    execution_time_ms: float


class AgentStartedEvent(BaseEvent):
    """Emitted when an agent starts processing"""
    event_type: EventType = EventType.AGENT_STARTED
    agent_id: str
    agent_type: str


class AgentCompletedEvent(BaseEvent):
    """Emitted when an agent completes successfully"""
    event_type: EventType = EventType.AGENT_COMPLETED
    agent_id: str
    result: Dict[str, Any]
    execution_time_ms: float


class AgentFailedEvent(BaseEvent):
    """Emitted when an agent fails"""
    event_type: EventType = EventType.AGENT_FAILED
    agent_id: str
    error: str
    error_code: Optional[int] = None


class WorkflowStartedEvent(BaseEvent):
    """Emitted when orchestration starts a workflow"""
    event_type: EventType = EventType.WORKFLOW_STARTED
    workflow_id: str
    workflow_name: str


class WorkflowCompletedEvent(BaseEvent):
    """Emitted when orchestration completes a workflow"""
    event_type: EventType = EventType.WORKFLOW_COMPLETED
    workflow_id: str
    result: Dict[str, Any]
    execution_time_ms: float
