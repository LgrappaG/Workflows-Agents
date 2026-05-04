"""
Event Type Definitions
======================

Pydantic models for all event types in the orchestration system.
BaseEvent defines common attributes: timestamp, source_agent, correlation_id.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class BaseEvent(BaseModel):
    """Base event model with common attributes"""

    model_config = ConfigDict(use_enum_values=True)

    source_agent: str = Field(..., description="Agent that generated the event")
    correlation_id: str = Field(
        ..., description="Unique correlation ID for tracking event chains"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Event creation timestamp"
    )


class SkillValidatedEvent(BaseEvent):
    """Event emitted when a skill is validated"""

    skill_id: str = Field(..., description="ID of the validated skill")
    validation_passed: bool = Field(..., description="Whether validation passed")
    validation_message: Optional[str] = Field(
        None, description="Optional validation details"
    )


class SkillReadyEvent(BaseEvent):
    """Event emitted when a skill is ready for execution"""

    skill_id: str = Field(..., description="ID of the ready skill")
    ready_for: str = Field(..., description="What the skill is ready for")


class GoalStartedEvent(BaseEvent):
    """Event emitted when a goal execution starts"""

    goal_id: str = Field(..., description="ID of the goal")
    goal_description: str = Field(..., description="Description of the goal")


class GoalAchievedEvent(BaseEvent):
    """Event emitted when a goal is successfully achieved"""

    goal_id: str = Field(..., description="ID of the achieved goal")
    result: dict = Field(..., description="Result data from goal achievement")


class AgentStartedEvent(BaseEvent):
    """Event emitted when an agent starts"""

    agent_name: str = Field(..., description="Name of the agent")
    task_id: str = Field(..., description="ID of the task being started")


class AgentCompletedEvent(BaseEvent):
    """Event emitted when an agent completes a task"""

    agent_name: str = Field(..., description="Name of the agent")
    task_id: str = Field(..., description="ID of the completed task")
    result: dict = Field(..., description="Result data from task completion")


class AgentFailedEvent(BaseEvent):
    """Event emitted when an agent fails a task"""

    agent_name: str = Field(..., description="Name of the agent")
    task_id: str = Field(..., description="ID of the failed task")
    error: str = Field(..., description="Error message")
    error_details: Optional[dict] = Field(
        None, description="Additional error context"
    )
