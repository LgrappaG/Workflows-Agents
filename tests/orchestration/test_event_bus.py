"""
Event Bus Tests
===============

Tests for async event bus with pub/sub pattern.
Tests subscription, multiple subscribers, and unsubscription.
"""

import asyncio
import pytest
from datetime import datetime
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
from orchestration.event_bus import EventBus


@pytest.mark.asyncio
async def test_event_bus_subscription():
    """Test that EventBus correctly subscribes to events"""
    event_bus = EventBus()
    received_events = []

    async def handler(event: BaseEvent) -> None:
        received_events.append(event)

    # Start the event bus
    await event_bus.start()

    try:
        # Subscribe to SkillValidatedEvent
        event_bus.subscribe(SkillValidatedEvent, handler)

        # Publish an event
        event = SkillValidatedEvent(
            source_agent="validator",
            correlation_id="test-123",
            skill_id="skill-001",
            validation_passed=True,
        )
        await event_bus.publish(event)

        # Allow async processing
        await asyncio.sleep(0.1)

        # Verify event was received
        assert len(received_events) == 1
        assert received_events[0].skill_id == "skill-001"
        assert received_events[0].validation_passed is True
    finally:
        # Stop the event bus
        await event_bus.stop()


@pytest.mark.asyncio
async def test_event_bus_multiple_subscribers():
    """Test that EventBus handles multiple subscribers to same event type"""
    event_bus = EventBus()
    received_events_1 = []
    received_events_2 = []

    async def handler1(event: BaseEvent) -> None:
        received_events_1.append(event)

    async def handler2(event: BaseEvent) -> None:
        received_events_2.append(event)

    # Start the event bus
    await event_bus.start()

    try:
        # Subscribe both handlers to SkillValidatedEvent
        event_bus.subscribe(SkillValidatedEvent, handler1)
        event_bus.subscribe(SkillValidatedEvent, handler2)

        # Publish an event
        event = SkillValidatedEvent(
            source_agent="validator",
            correlation_id="test-456",
            skill_id="skill-002",
            validation_passed=True,
        )
        await event_bus.publish(event)

        # Allow async processing
        await asyncio.sleep(0.1)

        # Verify both handlers received the event
        assert len(received_events_1) == 1
        assert len(received_events_2) == 1
        assert received_events_1[0].skill_id == "skill-002"
        assert received_events_2[0].skill_id == "skill-002"
    finally:
        # Stop the event bus
        await event_bus.stop()


@pytest.mark.asyncio
async def test_event_bus_unsubscribe():
    """Test that EventBus correctly unsubscribes from events"""
    event_bus = EventBus()
    received_events = []

    async def handler(event: BaseEvent) -> None:
        received_events.append(event)

    # Start the event bus
    await event_bus.start()

    try:
        # Subscribe
        subscription_id = event_bus.subscribe(SkillValidatedEvent, handler)

        # Publish first event (should be received)
        event1 = SkillValidatedEvent(
            source_agent="validator",
            correlation_id="test-789",
            skill_id="skill-003",
            validation_passed=True,
        )
        await event_bus.publish(event1)
        await asyncio.sleep(0.1)

        # Unsubscribe
        event_bus.unsubscribe(SkillValidatedEvent, subscription_id)

        # Publish second event (should NOT be received)
        event2 = SkillValidatedEvent(
            source_agent="validator",
            correlation_id="test-790",
            skill_id="skill-004",
            validation_passed=True,
        )
        await event_bus.publish(event2)
        await asyncio.sleep(0.1)

        # Verify only first event was received
        assert len(received_events) == 1
        assert received_events[0].skill_id == "skill-003"
    finally:
        # Stop the event bus
        await event_bus.stop()
