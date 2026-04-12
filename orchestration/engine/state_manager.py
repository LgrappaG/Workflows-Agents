"""
State Manager
=============

Manages orchestration execution state with persistence and recovery.

Responsibilities:
- Track execution progress (in-memory)
- Persist state to durable storage (JSON)
- Recover from crashes
- Provide state snapshots for debugging
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class StateManager:
    """
    Manages orchestration execution state.

    Maintains current execution state and persists to disk for:
    - Recovery from failures
    - Debugging
    - Historical analysis
    """

    def __init__(self, state_dir: Optional[str] = None):
        """
        Initialize state manager.

        Args:
            state_dir: Directory for persisting state
                      Defaults to .agents/orchestration/metrics
        """
        self.state_dir = Path(state_dir or ".agents/orchestration/metrics")
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.current_state = None
        self.checkpoint_dir = self.state_dir / "checkpoints"
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)

    def initialize_execution(self, execution_id: str, goal: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Initialize execution state.

        Args:
            execution_id: Unique execution ID
            goal: Target goal
            context: Execution context

        Returns:
            Initial state structure
        """
        self.current_state = {
            "execution_id": execution_id,
            "goal": goal,
            "context": context,
            "status": "pending",
            "start_time": datetime.now().isoformat(),
            "last_heartbeat": datetime.now().isoformat(),
            "sub_goals": {},
            "error_log": [],
            "error_recoveries": [],
            "metrics": {}
        }

        self._persist_state()
        print(f"[StateManager] State initialized: {execution_id}")
        return self.current_state

    def update_sub_goal(self, sub_goal_name: str, status: str, result: Dict[str, Any]):
        """Update sub-goal execution status"""
        if not self.current_state:
            raise RuntimeError("State not initialized")

        self.current_state["sub_goals"][sub_goal_name] = {
            "status": status,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

        self._persist_state()

    def record_error(self, sub_goal_name: str, error: Dict[str, Any]):
        """Record error for debugging and learning"""
        if not self.current_state:
            raise RuntimeError("State not initialized")

        self.current_state["error_log"].append({
            "sub_goal": sub_goal_name,
            "error": error,
            "timestamp": datetime.now().isoformat()
        })

        self._persist_state()

    def record_recovery(self, sub_goal_name: str, recovery: Dict[str, Any]):
        """Record error recovery attempt"""
        if not self.current_state:
            raise RuntimeError("State not initialized")

        self.current_state["error_recoveries"].append({
            "sub_goal": sub_goal_name,
            "recovery": recovery,
            "timestamp": datetime.now().isoformat()
        })

        self._persist_state()

    def update_heartbeat(self):
        """Update heartbeat timestamp"""
        if self.current_state:
            self.current_state["last_heartbeat"] = datetime.now().isoformat()
            self._persist_state()

    def mark_completed(self, final_status: str = "completed"):
        """Mark execution as completed"""
        if self.current_state:
            self.current_state["status"] = final_status
            self.current_state["end_time"] = datetime.now().isoformat()
            self._persist_state()
            print(f"[StateManager] Execution marked as {final_status}")

    def checkpoint(self, checkpoint_name: str):
        """Save checkpoint for recovery"""
        if not self.current_state:
            raise RuntimeError("State not initialized")

        checkpoint_file = self.checkpoint_dir / f"{self.current_state['execution_id']}_{checkpoint_name}.json"
        checkpoint_file.write_text(json.dumps(self.current_state, indent=2))
        print(f"[StateManager] Checkpoint saved: {checkpoint_file}")

    def _persist_state(self):
        """Persist state to durable storage"""
        if not self.current_state:
            return

        state_file = self.state_dir / f"{self.current_state['execution_id']}.json"
        state_file.write_text(json.dumps(self.current_state, indent=2))

    def get_state(self) -> Dict[str, Any]:
        """Get current state"""
        return self.current_state or {}

    def load_checkpoint(self, execution_id: str, checkpoint_name: str) -> Dict[str, Any]:
        """Load checkpoint for recovery"""
        checkpoint_file = self.checkpoint_dir / f"{execution_id}_{checkpoint_name}.json"
        if checkpoint_file.exists():
            self.current_state = json.loads(checkpoint_file.read_text())
            print(f"[StateManager] Checkpoint loaded: {checkpoint_file}")
            return self.current_state
        else:
            raise FileNotFoundError(f"Checkpoint not found: {checkpoint_file}")
