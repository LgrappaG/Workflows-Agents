"""
Event Bus
=========

Async event bus with pub/sub pattern using asyncio.Queue.
Allows agents to publish and subscribe to events asynchronously.
"""

import asyncio
import uuid
from typing import Type, Callable, Dict, List, Optional
from orchestration.events import BaseEvent


class EventBus:
    """Async event bus with pub/sub pattern"""

    def __init__(self):
        """Initialize the event bus with empty subscriber registry"""
        self._subscribers: Dict[Type[BaseEvent], Dict[str, Callable]] = {}
        self._event_queue: Optional[asyncio.Queue] = None
        self._running = False
        self._processor_task: Optional[asyncio.Task] = None

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
        Publish an event to the queue for processing.

        Args:
            event: The event to publish
        """
        if self._event_queue is not None:
            await self._event_queue.put(event)

    async def _process_queue(self) -> None:
        """
        Process events from queue continuously.

        Pulls events from the queue and dispatches them to all subscribed handlers.
        Runs until a None sentinel value is received.
        """
        while True:
            try:
                event = await self._event_queue.get()

                # None is stop signal
                if event is None:
                    break

                # Dispatch event to all subscribers
                event_type = type(event)
                if event_type in self._subscribers:
                    handlers = list(self._subscribers[event_type].values())
                    for handler in handlers:
                        try:
                            # Handle both sync and async handlers
                            if asyncio.iscoroutinefunction(handler):
                                await handler(event)
                            else:
                                handler(event)
                        except Exception as e:
                            print(f"Error in event handler: {e}")

                self._event_queue.task_done()
            except Exception as e:
                print(f"Error processing event queue: {e}")

    async def start(self) -> None:
        """Start the event bus processing loop"""
        if self._running:
            return

        self._running = True
        self._event_queue = asyncio.Queue()
        self._processor_task = asyncio.create_task(self._process_queue())

    async def stop(self) -> None:
        """Stop the event bus processing loop"""
        if not self._running:
            return

        self._running = False

        # Send stop signal to queue
        if self._event_queue is not None:
            await self._event_queue.put(None)

        # Wait for processor to finish
        if self._processor_task is not None:
            await self._processor_task
