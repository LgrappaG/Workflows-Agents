"""
Agent Lifecycle Tests
=====================

Tests for base agent lifecycle with event emission.
Verifies that agents emit AgentStartedEvent, AgentCompletedEvent, and AgentFailedEvent.
"""

import asyncio
import pytest
from orchestration.event_bus import EventBus
from orchestration.events import AgentStartedEvent, AgentCompletedEvent, AgentFailedEvent
from orchestration.agents import BaseAgent


class SimpleAgent(BaseAgent):
    """Test agent that succeeds"""

    async def execute(self):
        """Execute a simple task"""
        await asyncio.sleep(0.01)  # Simulate work
        return {"status": "success", "data": "task completed"}


class FailingAgent(BaseAgent):
    """Test agent that fails"""

    async def execute(self):
        """Execute a task that fails"""
        await asyncio.sleep(0.01)  # Simulate work
        raise Exception("Intentional test failure")


@pytest.mark.asyncio
async def test_agent_lifecycle():
    """
    Test agent lifecycle: AgentStartedEvent → execute → AgentCompletedEvent

    Verifies:
    1. Agent emits AgentStartedEvent with agent_id and agent_type
    2. Agent calls execute() method
    3. Agent emits AgentCompletedEvent with result and execution_time_ms
    """
    event_bus = EventBus()
    received_events = []

    async def handler(event):
        received_events.append(event)

    # Start event bus
    await event_bus.start()

    try:
        # Subscribe to all three event types
        event_bus.subscribe(AgentStartedEvent, handler)
        event_bus.subscribe(AgentCompletedEvent, handler)
        event_bus.subscribe(AgentFailedEvent, handler)

        # Create and run agent
        agent = SimpleAgent(agent_id="test-agent-001", event_bus=event_bus, agent_type="TestAgent")
        await agent.run()

        # Allow async processing
        await asyncio.sleep(0.1)

        # Verify events
        assert len(received_events) == 2, f"Expected 2 events, got {len(received_events)}"

        # First event should be AgentStartedEvent
        started_event = received_events[0]
        assert isinstance(started_event, AgentStartedEvent)
        assert started_event.source_agent == "test-agent-001"
        assert started_event.agent_id == "test-agent-001"
        assert started_event.agent_type == "TestAgent"

        # Second event should be AgentCompletedEvent
        completed_event = received_events[1]
        assert isinstance(completed_event, AgentCompletedEvent)
        assert completed_event.source_agent == "test-agent-001"
        assert completed_event.agent_id == "test-agent-001"
        assert completed_event.result is not None
        assert completed_event.execution_time_ms >= 0
        assert completed_event.result.get("status") == "success"

    finally:
        # Stop event bus
        await event_bus.stop()


@pytest.mark.asyncio
async def test_agent_error_handling():
    """
    Test agent error handling: FailingAgent → AgentFailedEvent

    Verifies:
    1. Agent emits AgentStartedEvent
    2. Agent calls execute() which raises exception
    3. Agent emits AgentFailedEvent with error message
    """
    event_bus = EventBus()
    received_events = []

    async def handler(event):
        received_events.append(event)

    # Start event bus
    await event_bus.start()

    try:
        # Subscribe to all event types
        event_bus.subscribe(AgentStartedEvent, handler)
        event_bus.subscribe(AgentCompletedEvent, handler)
        event_bus.subscribe(AgentFailedEvent, handler)

        # Create and run agent that will fail
        agent = FailingAgent(agent_id="test-agent-002", event_bus=event_bus, agent_type="FailingAgent")
        await agent.run()

        # Allow async processing
        await asyncio.sleep(0.1)

        # Verify events
        assert len(received_events) == 2, f"Expected 2 events, got {len(received_events)}"

        # First event should be AgentStartedEvent
        started_event = received_events[0]
        assert isinstance(started_event, AgentStartedEvent)
        assert started_event.source_agent == "test-agent-002"
        assert started_event.agent_id == "test-agent-002"

        # Second event should be AgentFailedEvent
        failed_event = received_events[1]
        assert isinstance(failed_event, AgentFailedEvent)
        assert failed_event.source_agent == "test-agent-002"
        assert failed_event.agent_id == "test-agent-002"
        assert "Intentional test failure" in failed_event.error

    finally:
        # Stop event bus
        await event_bus.stop()

