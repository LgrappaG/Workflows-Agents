"""
Event Bus
=========

Async event bus with pub/sub pattern using asyncio.Queue.
Allows agents to publish and subscribe to events asynchronously.
"""

import asyncio
import uuid
from typing import Type, Callable, Dict, List
from orchestration.events import BaseEvent


class EventBus:
    """Async event bus with pub/sub pattern"""

    def __init__(self):
        """Initialize the event bus with empty subscriber registry"""
        self._subscribers: Dict[Type[BaseEvent], Dict[str, Callable]] = {}
        self._event_queue: asyncio.Queue = asyncio.Queue()
        self._running = False

    def subscribe(
        self, event_type: Type[BaseEvent], handler: Callable[[BaseEvent], None]
    ) -> str:
        """
        Subscribe a handler to an event type.

        Args:
            event_type: The event type to subscribe to
            handler: Async function to call when event is published

        Returns:
            subscription_id: Unique ID for this subscription (for unsubscribing)
        """
        if event_type not in self._subscribers:
            self._subscribers[event_type] = {}

        subscription_id = str(uuid.uuid4())
        self._subscribers[event_type][subscription_id] = handler
        return subscription_id

    def unsubscribe(self, event_type: Type[BaseEvent], subscription_id: str) -> None:
        """
        Unsubscribe a handler from an event type.

        Args:
            event_type: The event type to unsubscribe from
            subscription_id: The subscription ID returned from subscribe()
        """
        if event_type in self._subscribers:
            self._subscribers[event_type].pop(subscription_id, None)

    async def publish(self, event: BaseEvent) -> None:
        """
        Publish an event to all subscribers.

        Args:
            event: The event to publish
        """
        event_type = type(event)

        # Call all handlers for this event type
        if event_type in self._subscribers:
            handlers = list(self._subscribers[event_type].values())
            for handler in handlers:
                # Execute handler asynchronously
                asyncio.create_task(self._execute_handler(handler, event))

    async def _execute_handler(self, handler: Callable, event: BaseEvent) -> None:
        """
        Execute an event handler safely.

        Args:
            handler: The handler function to execute
            event: The event to pass to the handler
        """
        try:
            await handler(event)
        except Exception as e:
            # Log error but don't stop other handlers
            print(f"Error in event handler: {e}")

    async def start(self) -> None:
        """Start the event bus processing loop"""
        self._running = True

    async def stop(self) -> None:
        """Stop the event bus processing loop"""
        self._running = False
