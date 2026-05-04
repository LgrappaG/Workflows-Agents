"""
Base Agent
==========

Abstract base class defining the agent interface and lifecycle with event emission.

All agents must:
1. Implement execute() method
2. Have a run() method that emits lifecycle events
3. Handle errors gracefully
"""

import asyncio
import time
from abc import ABC, abstractmethod
from typing import Any, Optional
from uuid import uuid4
from enum import Enum
from orchestration.event_bus import EventBus
from orchestration.events import (
    AgentStartedEvent,
    AgentCompletedEvent,
    AgentFailedEvent,
)


class AgentStatus(Enum):
    """Agent execution states"""
    IDLE = "idle"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    RECOVERED = "recovered"


class BaseAgent(ABC):
    """
    Abstract base class for all orchestration agents.

    Defines the lifecycle contract that all agents must follow:
    - Initialize with agent_id, event_bus, and agent_type
    - Implement execute() method
    - run() method handles event emission and error handling
    """

    def __init__(self, agent_id: str, event_bus: EventBus, agent_type: str):
        """
        Initialize agent.

        Args:
            agent_id: Unique identifier for this agent
            event_bus: EventBus instance for publishing events
            agent_type: Type/classification of agent (e.g., "ValidationAgent")
        """
        self.agent_id = agent_id
        self.event_bus = event_bus
        self.agent_type = agent_type
        self.correlation_id = str(uuid4())

    @abstractmethod
    async def execute(self) -> Any:
        """
        Execute the agent's task.

        Subclasses must implement this method to define agent-specific behavior.

        Returns:
            Result data from task execution

        Raises:
            Any exception should be caught by run() method
        """
        pass

    async def run(self) -> None:
        """
        Run the agent with full lifecycle event emission.

        Lifecycle:
        1. Emit AgentStartedEvent
        2. Call execute()
        3. On success: emit AgentCompletedEvent with result and execution_time_ms
        4. On error: emit AgentFailedEvent with error message

        This method handles timing, error catching, and all event emissions.
        """
        # Emit start event
        start_event = AgentStartedEvent(
            source_agent=self.agent_id,
            correlation_id=self.correlation_id,
            agent_id=self.agent_id,
            agent_type=self.agent_type,
        )
        await self.event_bus.publish(start_event)

        # Measure execution time
        start_time = time.time()

        try:
            # Execute the agent's task
            result = await self.execute()

            # Calculate execution time in milliseconds
            execution_time_ms = (time.time() - start_time) * 1000

            # Emit completion event with result and timing
            completion_event = AgentCompletedEvent(
                source_agent=self.agent_id,
                correlation_id=self.correlation_id,
                agent_id=self.agent_id,
                result={
                    "status": "success",
                    "data": result,
                    "execution_time_ms": execution_time_ms,
                },
                execution_time_ms=execution_time_ms,
            )
            await self.event_bus.publish(completion_event)

        except Exception as e:
            # Calculate execution time even on failure
            execution_time_ms = (time.time() - start_time) * 1000

            # Emit failure event with error details
            failure_event = AgentFailedEvent(
                source_agent=self.agent_id,
                correlation_id=self.correlation_id,
                agent_id=self.agent_id,
                error=str(e),
                error_code=None,
            )
            await self.event_bus.publish(failure_event)
