"""
Conflict Detection for Skill Graphs
Detects contradictory postconditions and circular dependencies
"""
from typing import List, Tuple, Set
from orchestration.graph.skill_graph import SkillGraph


def detect_conflicts(graph: SkillGraph) -> List[Tuple[str, str, str]]:
    """
    Detect skills with conflicting postconditions.

    Two skills conflict if they set the same key to different values.

    Args:
        graph: SkillGraph to analyze

    Returns:
        List of tuples (skill1_id, skill2_id, reason) for each conflict
    """
    conflicts: List[Tuple[str, str, str]] = []
    skills = graph.get_all_skills()

    # Compare each pair of skills
    for i, skill1 in enumerate(skills):
        for skill2 in skills[i + 1 :]:
            # Check for contradictory postconditions
            for key in skill1.postconditions:
                if key in skill2.postconditions:
                    if skill1.postconditions[key] != skill2.postconditions[key]:
                        reason = f"Conflicting postcondition: {key}={skill1.postconditions[key]} vs {skill2.postconditions[key]}"
                        conflicts.append((skill1.id, skill2.id, reason))
                        break

    return conflicts


def detect_cycles(graph: SkillGraph) -> List[List[str]]:
    """
    Detect circular dependencies in the skill graph using DFS.

    Args:
        graph: SkillGraph to analyze

    Returns:
        List of cycles, where each cycle is a list of skill IDs
    """
    cycles: List[List[str]] = []
    visited: Set[str] = set()
    rec_stack: Set[str] = set()
    path: List[str] = []

    def dfs(skill_id: str) -> None:
        """
        Depth-first search to detect cycles.

        Uses recursion stack to detect back edges (cycles).
        """
        visited.add(skill_id)
        rec_stack.add(skill_id)
        path.append(skill_id)

        # Get dependencies of current skill
        dependencies = graph.get_dependencies(skill_id)

        for dep_id in dependencies:
            if dep_id not in visited:
                dfs(dep_id)
            elif dep_id in rec_stack:
                # Found a cycle - extract it from path
                cycle_start = path.index(dep_id)
                cycle = path[cycle_start:] + [dep_id]
                cycles.append(cycle)

        path.pop()
        rec_stack.discard(skill_id)

    # Run DFS from each unvisited node
    for skill in graph.get_all_skills():
        if skill.id not in visited:
            dfs(skill.id)

    # Deduplicate cycles (same cycle in different orders)
    unique_cycles: List[List[str]] = []
    for cycle in cycles:
        # Normalize cycle: start from smallest element and check direction
        normalized = _normalize_cycle(cycle)
        if normalized not in unique_cycles:
            unique_cycles.append(normalized)

    return unique_cycles


def _normalize_cycle(cycle: List[str]) -> List[str]:
    """
    Normalize a cycle for comparison.

    Removes the trailing duplicate and ensures consistent ordering.

    Args:
        cycle: Cycle list with trailing duplicate

    Returns:
        Normalized cycle
    """
    if len(cycle) <= 1:
        return cycle

    # Remove trailing duplicate
    if cycle[0] == cycle[-1]:
        cycle = cycle[:-1]

    if len(cycle) == 0:
        return []

    # Find minimum element and rotate
    min_idx = cycle.index(min(cycle))
    normalized = cycle[min_idx:] + cycle[:min_idx]

    return normalized
