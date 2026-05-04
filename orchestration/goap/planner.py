"""
GOAPPlanner - A* search-based Goal-Oriented Action Planning
"""
import heapq
from typing import List, Optional, Dict, Set, Tuple
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action


class GOAPPlanner:
    """
    GOAP (Goal-Oriented Action Planning) planner using A* search.
    Finds optimal action sequence to reach a goal state from start state.
    """

    def __init__(self, max_iterations: int = 1000):
        """
        Initialize the planner.

        Args:
            max_iterations: Maximum iterations to prevent infinite loops
        """
        self.actions: List[Action] = []
        self.max_iterations = max_iterations

    def add_action(self, action: Action) -> None:
        """
        Register an action available to the planner.

        Args:
            action: Action to add to the planning domain
        """
        self.actions.append(action)

    def plan(self, start: WorldState, goal: WorldState) -> Optional[List[Action]]:
        """
        Find action sequence using A* search.
        f(n) = g(n) + h(n), where:
            - g(n) = cost so far from start
            - h(n) = heuristic (manhattan distance to goal)

        Args:
            start: Initial world state
            goal: Desired goal state (partial match - only specified keys matter)

        Returns:
            List of actions to reach goal, or None if no plan exists
        """
        # Check if already at goal
        if self._is_goal(start, goal):
            return []

        # A* open set: list of (f_score, counter, state, path)
        counter = 0
        open_set: List[Tuple[float, int, WorldState, List[Action]]] = []
        heapq.heappush(open_set, (0.0, counter, start, []))
        counter += 1

        # Closed set: states we've already fully explored
        closed_set: Set[WorldState] = set()

        iterations = 0

        while open_set and iterations < self.max_iterations:
            iterations += 1

            # Pop lowest f-score state
            f_score, _, current_state, path = heapq.heappop(open_set)

            # Skip if already visited
            if current_state in closed_set:
                continue

            closed_set.add(current_state)

            # Check if goal reached
            if self._is_goal(current_state, goal):
                return path

            # Expand neighbors (try all applicable actions)
            for action in self.actions:
                if not action.can_execute(current_state):
                    continue

                # Apply action to get next state
                next_state = action.apply(current_state)

                # Skip if already visited
                if next_state in closed_set:
                    continue

                # Calculate cost
                g_score = sum(a.cost for a in path) + action.cost
                h_score = next_state.distance_to(goal)
                f_new = g_score + h_score

                new_path = path + [action]

                # Add to open set
                heapq.heappush(open_set, (f_new, counter, next_state, new_path))
                counter += 1

        # No plan found
        return None

    def _is_goal(self, state: WorldState, goal: WorldState) -> bool:
        """
        Check if state satisfies goal.
        Goal is a partial match - only keys in goal dict must match.

        Args:
            state: Current state
            goal: Goal state (partial specification)

        Returns:
            True if state satisfies all goal conditions
        """
        for key, value in goal._state.items():
            if state.get(key) != value:
                return False
        return True
