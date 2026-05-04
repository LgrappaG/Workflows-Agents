"""
Event Bus
=========

Async event bus with pub/sub pattern using asyncio.Queue.
Allows agents to publish and subscribe to events asynchronously.
"""

import asyncio
import logging
from typing import Callable, Dict, List, Type, Optional, Union, Any, Coroutine
from uuid import uuid4
from orchestration.events import BaseEvent

logger = logging.getLogger(__name__)

PROCESSOR_SHUTDOWN_TIMEOUT = 5.0  # Graceful shutdown timeout in seconds


class Subscription:
    def __init__(
        self,
        event_type: Type[BaseEvent],
        handler: Union[Callable[[BaseEvent], Any], Callable[[BaseEvent], Coroutine[Any, Any, Any]]],
        subscription_id: str
    ):
        self.event_type = event_type
        self.handler = handler
        self.subscription_id = subscription_id


class EventBus:
    def __init__(self):
        self._subscriptions: Dict[Type[BaseEvent], List[Subscription]] = {}
        self._queue: Optional[asyncio.Queue] = None
        self._processor_task: Optional[asyncio.Task] = None
        self._lock: Optional[asyncio.Lock] = None
        self._running = False

    async def start(self):
        async with self._lock if self._lock else asyncio.Lock():
            if self._running:
                return

            self._loop = asyncio.get_event_loop()
            self._queue = asyncio.Queue()
            if self._lock is None:
                self._lock = asyncio.Lock()
            self._processor_task = asyncio.create_task(self._process_queue())
            self._running = True
            logger.debug("EventBus started")

    async def stop(self):
        if self._lock is None:
            self._lock = asyncio.Lock()

        async with self._lock:
            if not self._running:
                return

            self._running = False
            await self._queue.put(None)  # Stop signal

            try:
                await asyncio.wait_for(self._processor_task, timeout=PROCESSOR_SHUTDOWN_TIMEOUT)
            except asyncio.TimeoutError:
                logger.error("EventBus processor shutdown timeout, cancelling task")
                self._processor_task.cancel()
            except Exception as e:
                logger.error(f"Error stopping EventBus: {e}")

            logger.debug("EventBus stopped")

    def subscribe(self, event_type: Type[BaseEvent], handler: Callable) -> Subscription:
        if event_type not in self._subscriptions:
            self._subscriptions[event_type] = []

        subscription = Subscription(event_type, handler, str(uuid4()))
        self._subscriptions[event_type].append(subscription)
        logger.debug(f"Subscription added for {event_type.__name__}")
        return subscription

    def unsubscribe(self, subscription: Subscription) -> None:
        if subscription.event_type in self._subscriptions:
            self._subscriptions[subscription.event_type] = [
                s for s in self._subscriptions[subscription.event_type]
                if s.subscription_id != subscription.subscription_id
            ]
            logger.debug(f"Subscription removed for {subscription.event_type.__name__}")

    async def publish(self, event: BaseEvent) -> None:
        if self._queue is None:
            raise RuntimeError("EventBus not started. Call start() before publishing events.")

        await self._queue.put(event)
        logger.debug(f"Event published: {type(event).__name__}")

    async def _process_queue(self) -> None:
        while True:
            event = await self._queue.get()
            if event is None:
                self._queue.task_done()
                break

            try:
                event_type = type(event)
                if event_type in self._subscriptions:
                    for subscription in self._subscriptions[event_type]:
                        try:
                            if asyncio.iscoroutinefunction(subscription.handler):
                                await subscription.handler(event)
                            else:
                                subscription.handler(event)
                        except Exception as e:
                            logger.error(f"Error in handler for {event_type.__name__}: {e}", exc_info=True)
            finally:
                self._queue.task_done()
