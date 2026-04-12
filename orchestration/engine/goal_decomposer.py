"""
Goal Decomposer
===============

Decomposes high-level goals into sub-goals and resolves dependencies.

This component translates user intentions (goals) into executable tasks
by analyzing the goal decomposition map and resolving dependencies.
"""

from typing import List, Dict, Any, Optional


class GoalDecomposer:
    """
    Decomposes complex goals into sub-goals.

    Maps high-level goals to their constituent sub-goals and determines
    execution order based on dependencies.
    """

    # Goal decomposition map (will be loaded from YAML in integration)
    GOAL_DECOMPOSITION = {
        "deploy-game-release": [
            {"name": "validate-all-skills", "agent": "validation", "priority": 1},
            {"name": "gate-approval-decision", "agent": "validation", "priority": 2},
            {"name": "sync-with-remote", "agent": "sync", "priority": 1},
            {"name": "deploy-game-release", "agent": "deploy", "priority": 3}
        ],
        "validate-before-deploy": [
            {"name": "validate-all-skills", "agent": "validation", "priority": 1},
            {"name": "gate-approval-decision", "agent": "validation", "priority": 2}
        ],
        "sync-team-collaboration": [
            {"name": "sync-with-remote", "agent": "sync", "priority": 1}
        ],
        "learn-and-optimize": [
            {"name": "learn-from-metrics", "agent": "knowledge", "priority": 1},
            {"name": "suggest-error-fixes", "agent": "knowledge", "priority": 2}
        ]
    }

    # Dependencies between sub-goals
    DEPENDENCIES = {
        "gate-approval-decision": ["validate-all-skills"],
        "deploy-game-release": ["gate-approval-decision", "sync-with-remote"]
    }

    def __init__(self):
        """Initialize goal decomposer"""
        pass

    def decompose(self, goal: str) -> List[Dict[str, Any]]:
        """
        Decompose goal into sub-goals.

        Args:
            goal: Goal to decompose

        Returns:
            List of sub-goals
        """
        sub_goals = self.GOAL_DECOMPOSITION.get(goal, [])

        if not sub_goals:
            raise ValueError(f"Unknown goal: {goal}")

        return sub_goals

    def resolve_dependencies(self, sub_goals: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Resolve dependencies and return execution order.

        Args:
            sub_goals: List of sub-goals

        Returns:
            Ordered list of sub-goals respecting dependencies
        """
        # Build dependency graph
        graph = {}
        for sg in sub_goals:
            name = sg["name"]
            deps = self.DEPENDENCIES.get(name, [])
            graph[name] = deps

        # Topological sort
        execution_order = []
        visited = set()
        visiting = set()

        def visit(node):
            if node in visited:
                return
            if node in visiting:
                raise ValueError(f"Circular dependency: {node}")

            visiting.add(node)

            for dep in graph.get(node, []):
                if dep in [sg["name"] for sg in sub_goals]:
                    visit(dep)

            visiting.remove(node)
            visited.add(node)
            execution_order.append(node)

        for sg in sub_goals:
            visit(sg["name"])

        # Return in execution order
        name_to_sg = {sg["name"]: sg for sg in sub_goals}
        return [name_to_sg[name] for name in execution_order]

    def get_sub_goal_info(self, sub_goal_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a sub-goal"""
        for goal_name, sub_goals in self.GOAL_DECOMPOSITION.items():
            for sg in sub_goals:
                if sg["name"] == sub_goal_name:
                    return sg

        return None
