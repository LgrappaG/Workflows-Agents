"""
Skill Dependency Graph
Manages skills, their dependencies, and detects conflicts
"""
from dataclasses import dataclass, field
from typing import Dict, Set, List, Optional, Any


@dataclass
class Skill:
    """
    Represents a skill in the dependency graph.

    A skill has preconditions (what must be true before execution)
    and postconditions (what will be true after execution).
    """
    id: str
    name: str
    preconditions: Dict[str, Any] = field(default_factory=dict)
    postconditions: Dict[str, Any] = field(default_factory=dict)
    cost: float = 1.0
    domain: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    def __hash__(self):
        """Make skill hashable so it can be used in sets"""
        return hash(self.id)

    def __eq__(self, other):
        """Compare skills by ID"""
        if not isinstance(other, Skill):
            return False
        return self.id == other.id

    def satisfies_preconditions(self, requirements: Dict[str, Any]) -> bool:
        """
        Check if this skill's postconditions satisfy at least one requirement.

        Args:
            requirements: Dict of preconditions to check

        Returns:
            True if at least one requirement is satisfied by this skill's postconditions
        """
        # Check if any key-value pair in postconditions matches requirements
        for key, value in self.postconditions.items():
            if key in requirements and requirements[key] == value:
                return True
        return False


class SkillGraph:
    """
    Manages a directed graph of skills with their dependencies.

    Dependencies are derived from preconditions and postconditions:
    - If Skill A's postcondition satisfies Skill B's precondition,
      then Skill B depends on Skill A.
    """

    def __init__(self):
        """Initialize empty skill graph"""
        self._skills: Dict[str, Skill] = {}
        self._dependencies_cache: Dict[str, Set[str]] = {}
        self._cache_dirty = True

    def add_skill(self, skill: Skill) -> None:
        """
        Add a skill to the graph.

        Args:
            skill: Skill object to add
        """
        self._skills[skill.id] = skill
        self._cache_dirty = True

    def get_skill(self, skill_id: str) -> Optional[Skill]:
        """
        Retrieve a skill by ID.

        Args:
            skill_id: ID of the skill to retrieve

        Returns:
            Skill object or None if not found
        """
        return self._skills.get(skill_id)

    def get_all_skills(self) -> List[Skill]:
        """
        Get all skills in the graph.

        Returns:
            List of all skills
        """
        return list(self._skills.values())

    def get_skills_by_domain(self, domain: str) -> List[Skill]:
        """
        Get all skills in a specific domain.

        Args:
            domain: Domain name to filter by

        Returns:
            List of skills matching the domain
        """
        return [skill for skill in self._skills.values() if skill.domain == domain]

    def get_dependencies(self, skill_id: str) -> Set[str]:
        """
        Get skills that this skill depends on.

        A skill depends on another if the other's postconditions satisfy
        this skill's preconditions.

        Args:
            skill_id: ID of the skill

        Returns:
            Set of skill IDs this skill depends on
        """
        skill = self.get_skill(skill_id)
        if skill is None:
            return set()

        dependencies = set()

        # Check each skill in graph
        for other_skill in self._skills.values():
            if other_skill.id == skill.id:
                continue

            # Check if other_skill's postconditions satisfy this skill's preconditions
            if other_skill.satisfies_preconditions(skill.preconditions):
                dependencies.add(other_skill.id)

        return dependencies

    def get_dependents(self, skill_id: str) -> Set[str]:
        """
        Get skills that depend on this skill (reverse dependency lookup).

        Args:
            skill_id: ID of the skill

        Returns:
            Set of skill IDs that depend on this skill
        """
        dependents = set()

        # Find all skills that have skill_id in their dependencies
        for other_id in self._skills.keys():
            if other_id == skill_id:
                continue

            if skill_id in self.get_dependencies(other_id):
                dependents.add(other_id)

        return dependents

    def _rebuild_dependency_cache(self) -> None:
        """Rebuild the dependency cache"""
        self._dependencies_cache.clear()
        for skill_id in self._skills.keys():
            self._dependencies_cache[skill_id] = self.get_dependencies(skill_id)
        self._cache_dirty = False
