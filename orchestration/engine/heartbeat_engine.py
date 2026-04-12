"""
Heartbeat Engine
================

Monitors orchestration health with periodic heartbeat checks
and timeout detection.

Features:
- 30-second heartbeat intervals
- Timeout detection (300s default)
- Health state tracking
- Alert/escalation on missed beats
"""

import threading
import time
from datetime import datetime, timedelta
from typing import Callable, Optional, Dict, Any


class HeartbeatEngine:
    """
    Monitors orchestration health via periodic heartbeat.

    Detects timeouts, stuck executions, and enables recovery.
    """

    def __init__(
        self,
        interval_seconds: int = 30,
        timeout_seconds: int = 300,
        on_timeout: Optional[Callable] = None
    ):
        """
        Initialize heartbeat engine.

        Args:
            interval_seconds: Heartbeat interval (default 30s)
            timeout_seconds: Timeout threshold (default 300s)
            on_timeout: Callback function when timeout detected
        """
        self.interval_seconds = interval_seconds
        self.timeout_seconds = timeout_seconds
        self.on_timeout = on_timeout
        self.last_heartbeat = datetime.now()
        self.is_running = False
        self.thread = None
        self.execution_id = None

    def start(self, execution_id: str):
        """Start heartbeat monitoring"""
        self.execution_id = execution_id
        self.last_heartbeat = datetime.now()
        self.is_running = True

        self.thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
        self.thread.start()

        print(f"[Heartbeat] Started monitoring {execution_id}")

    def stop(self):
        """Stop heartbeat monitoring"""
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=5)
        print(f"[Heartbeat] Stopped monitoring {self.execution_id}")

    def ping(self):
        """Update heartbeat (called by orchestrator)"""
        self.last_heartbeat = datetime.now()

    def _heartbeat_loop(self):
        """Main heartbeat monitoring loop"""
        while self.is_running:
            time.sleep(self.interval_seconds)

            time_since_beat = (datetime.now() - self.last_heartbeat).total_seconds()

            if time_since_beat > self.timeout_seconds:
                print(f"[Heartbeat] TIMEOUT: No heartbeat for {time_since_beat:.0f}s")

                if self.on_timeout:
                    self.on_timeout({
                        "execution_id": self.execution_id,
                        "last_heartbeat": self.last_heartbeat.isoformat(),
                        "timeout_seconds": self.timeout_seconds,
                        "time_since_beat": time_since_beat
                    })
            else:
                print(f"[Heartbeat] Beat OK ({time_since_beat:.0f}s / {self.timeout_seconds}s)")

    def get_health(self) -> Dict[str, Any]:
        """Get health status"""
        time_since_beat = (datetime.now() - self.last_heartbeat).total_seconds()
        is_healthy = time_since_beat <= self.timeout_seconds

        return {
            "execution_id": self.execution_id,
            "is_running": self.is_running,
            "is_healthy": is_healthy,
            "last_heartbeat": self.last_heartbeat.isoformat(),
            "time_since_beat_seconds": time_since_beat,
            "timeout_threshold": self.timeout_seconds
        }
