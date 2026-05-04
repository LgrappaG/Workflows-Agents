"""
Action - Represents a GOAP action with preconditions and effects
"""
from typing import Dict, Any
from orchestration.goap.world_state import WorldState


class Action:
    """
    Represents an action in GOAP planning.
    An action has preconditions (must be true to execute),
    effects (changes when executed), and a cost.
    """

    def __init__(
        self,
        name: str,
        cost: float,
        preconditions: Dict[str, Any],
        effects: Dict[str, Any]
    ):
        """
        Initialize an action.

        Args:
            name: Action name (e.g., "validate", "deploy")
            cost: Cost to execute this action
            preconditions: Dict of required state values {key: required_value}
            effects: Dict of state changes {key: new_value}
        """
        self.name = name
        self.cost = float(cost)
        self.preconditions = dict(preconditions)
        self.effects = dict(effects)

    def preconditions_met(self, state: WorldState) -> bool:
        """
        Check if all preconditions are satisfied in the given state.

        Args:
            state: Current world state

        Returns:
            True if all preconditions match the state
        """
        for key, required_value in self.preconditions.items():
            if state.get(key) != required_value:
                return False
        return True

    def apply(self, state: WorldState) -> WorldState:
        """
        Apply this action to a state, creating a new state with effects applied.
        Does NOT modify the input state.

        Args:
            state: Current world state

        Returns:
            New state with effects applied
        """
        new_state = state.clone()
        for key, value in self.effects.items():
            new_state.set(key, value)
        return new_state

    def can_execute(self, state: WorldState) -> bool:
        """
        Check if this action can be executed in the given state.
        Alias for preconditions_met().

        Args:
            state: Current world state

        Returns:
            True if action can be executed
        """
        return self.preconditions_met(state)

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"Action({self.name}, cost={self.cost}, "
            f"pre={self.preconditions}, eff={self.effects})"
        )

    def __str__(self) -> str:
        """Friendly string representation."""
        return self.name
