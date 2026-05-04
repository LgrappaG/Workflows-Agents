"""
WorldState - State representation for GOAP
Encapsulates game/system state as dict with utilities for planning
"""
from typing import Dict, Any, Optional


class WorldState:
    """
    Represents the world state in GOAP planning.
    Immutable wrapper around a state dictionary.
    """

    def __init__(self, state: Dict[str, Any]):
        """
        Initialize world state from dictionary.

        Args:
            state: Dictionary of state key-value pairs
        """
        self._state = dict(state)  # Copy to avoid external mutations

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a state value by key.

        Args:
            key: State key
            default: Default value if key not found

        Returns:
            State value or default
        """
        return self._state.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a state value (mutates this state).

        Args:
            key: State key
            value: State value
        """
        self._state[key] = value

    def clone(self) -> "WorldState":
        """
        Create an independent copy of this state.

        Returns:
            New WorldState with same values
        """
        return WorldState(self._state)

    def distance_to(self, other: "WorldState") -> int:
        """
        Calculate manhattan distance to another state.
        Distance = number of keys with different values.

        Args:
            other: Target state

        Returns:
            Number of differing state values
        """
        distance = 0
        all_keys = set(self._state.keys()) | set(other._state.keys())

        for key in all_keys:
            self_val = self._state.get(key)
            other_val = other._state.get(key)
            if self_val != other_val:
                distance += 1

        return distance

    def __eq__(self, other: Any) -> bool:
        """Check equality with another state."""
        if not isinstance(other, WorldState):
            return False
        return self._state == other._state

    def __hash__(self) -> int:
        """Make state hashable for use in sets/dicts."""
        return hash(frozenset(self._state.items()))

    def __repr__(self) -> str:
        """String representation."""
        return f"WorldState({self._state})"

    def __str__(self) -> str:
        """Friendly string representation."""
        items = [f"{k}={v}" for k, v in sorted(self._state.items())]
        return "{" + ", ".join(items) + "}"
