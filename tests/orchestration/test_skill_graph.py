"""
Skill Dependency Graph Tests
Test suite for Skill Graph with dependency resolution and conflict detection
"""
import pytest
from orchestration.graph.skill_graph import Skill, SkillGraph
from orchestration.graph.conflict_detector import detect_conflicts, detect_cycles


class TestSkillGraphCreation:
    """Tests for basic Skill Graph creation and management"""

    def test_skill_graph_creation(self):
        """Test adding skills to graph and retrieving them"""
        graph = SkillGraph()

        # Create two skills
        skill1 = Skill(
            id="skill_1",
            name="Validate Config",
            preconditions={"config_loaded": True},
            postconditions={"config_validated": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Deploy Service",
            preconditions={"config_validated": True},
            postconditions={"service_deployed": True}
        )

        # Add to graph
        graph.add_skill(skill1)
        graph.add_skill(skill2)

        # Retrieve and verify
        retrieved_1 = graph.get_skill("skill_1")
        retrieved_2 = graph.get_skill("skill_2")

        assert retrieved_1.name == "Validate Config"
        assert retrieved_2.name == "Deploy Service"

        # Get all skills
        all_skills = graph.get_all_skills()
        assert len(all_skills) == 2
        assert skill1 in all_skills
        assert skill2 in all_skills

    def test_skill_graph_get_nonexistent_skill(self):
        """Test retrieving nonexistent skill returns None"""
        graph = SkillGraph()
        assert graph.get_skill("nonexistent") is None

    def test_skill_graph_domain_filtering(self):
        """Test filtering skills by domain"""
        graph = SkillGraph()

        skill1 = Skill(
            id="deploy_1",
            name="Deploy",
            preconditions={},
            postconditions={"deployed": True},
            domain="deployment"
        )

        skill2 = Skill(
            id="validate_1",
            name="Validate",
            preconditions={},
            postconditions={"validated": True},
            domain="validation"
        )

        skill3 = Skill(
            id="deploy_2",
            name="Deploy Backup",
            preconditions={},
            postconditions={"backup_deployed": True},
            domain="deployment"
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)
        graph.add_skill(skill3)

        # Get skills by domain
        deployment_skills = graph.get_skills_by_domain("deployment")
        assert len(deployment_skills) == 2
        assert skill1 in deployment_skills
        assert skill3 in deployment_skills
        assert skill2 not in deployment_skills

        validation_skills = graph.get_skills_by_domain("validation")
        assert len(validation_skills) == 1
        assert skill2 in validation_skills


class TestSkillGraphDependencies:
    """Tests for dependency resolution"""

    def test_skill_graph_dependencies(self):
        """Test that skill2 depends on skill1 (postcondition satisfies precondition)"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Setup",
            preconditions={},
            postconditions={"ready": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Execute",
            preconditions={"ready": True},
            postconditions={"done": True}
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)

        # skill2 depends on skill1
        deps = graph.get_dependencies("skill_2")
        assert deps == {"skill_1"}

    def test_skill_graph_no_dependencies(self):
        """Test skill with no dependencies"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Root",
            preconditions={},
            postconditions={"initialized": True}
        )

        graph.add_skill(skill1)

        deps = graph.get_dependencies("skill_1")
        assert deps == set()

    def test_skill_graph_multiple_dependencies(self):
        """Test skill with multiple dependencies"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Load Config",
            preconditions={},
            postconditions={"config_loaded": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Load Credentials",
            preconditions={},
            postconditions={"credentials_loaded": True}
        )

        skill3 = Skill(
            id="skill_3",
            name="Initialize",
            preconditions={"config_loaded": True, "credentials_loaded": True},
            postconditions={"initialized": True}
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)
        graph.add_skill(skill3)

        # skill3 depends on both skill1 and skill2
        deps = graph.get_dependencies("skill_3")
        assert deps == {"skill_1", "skill_2"}

    def test_skill_graph_get_dependents(self):
        """Test reverse dependency lookup - which skills depend on this one"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Setup",
            preconditions={},
            postconditions={"ready": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Process A",
            preconditions={"ready": True},
            postconditions={"result_a": True}
        )

        skill3 = Skill(
            id="skill_3",
            name="Process B",
            preconditions={"ready": True},
            postconditions={"result_b": True}
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)
        graph.add_skill(skill3)

        # Both skill2 and skill3 depend on skill1
        dependents = graph.get_dependents("skill_1")
        assert dependents == {"skill_2", "skill_3"}

        # Nothing depends on skill2
        dependents_2 = graph.get_dependents("skill_2")
        assert dependents_2 == set()


class TestConflictDetection:
    """Tests for conflict detection"""

    def test_skill_graph_conflict_detection(self):
        """Test detecting conflicting postconditions"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Set Mode A",
            preconditions={},
            postconditions={"mode": "A"}
        )

        skill2 = Skill(
            id="skill_2",
            name="Set Mode B",
            preconditions={},
            postconditions={"mode": "B"}  # Conflicts with skill1
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)

        conflicts = detect_conflicts(graph)

        # Should detect conflict on 'mode' key
        assert len(conflicts) > 0
        conflict_found = any(
            (pair[0] == "skill_1" and pair[1] == "skill_2") or
            (pair[0] == "skill_2" and pair[1] == "skill_1")
            for pair in [c[:2] for c in conflicts]
        )
        assert conflict_found

    def test_skill_graph_no_conflict_on_different_keys(self):
        """Test no conflict when postconditions affect different keys"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Setup A",
            preconditions={},
            postconditions={"ready_a": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Setup B",
            preconditions={},
            postconditions={"ready_b": True}
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)

        conflicts = detect_conflicts(graph)
        assert len(conflicts) == 0

    def test_skill_graph_no_conflict_on_same_value(self):
        """Test no conflict when postconditions set same key to same value"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Set Flag 1",
            preconditions={},
            postconditions={"flag": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Set Flag 2",
            preconditions={},
            postconditions={"flag": True}  # Same key, same value - no conflict
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)

        conflicts = detect_conflicts(graph)
        assert len(conflicts) == 0


class TestCycleDetection:
    """Tests for circular dependency detection"""

    def test_skill_graph_cycle_detection(self):
        """Test detecting circular dependencies"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Action A",
            preconditions={"state_c": True},
            postconditions={"state_a": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Action B",
            preconditions={"state_a": True},
            postconditions={"state_b": True}
        )

        skill3 = Skill(
            id="skill_3",
            name="Action C",
            preconditions={"state_b": True},
            postconditions={"state_c": True}
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)
        graph.add_skill(skill3)

        cycles = detect_cycles(graph)

        # Should detect cycle: skill1 -> skill2 -> skill3 -> skill1
        assert len(cycles) > 0

    def test_skill_graph_no_cycles(self):
        """Test acyclic dependency graph"""
        graph = SkillGraph()

        skill1 = Skill(
            id="skill_1",
            name="Setup",
            preconditions={},
            postconditions={"ready": True}
        )

        skill2 = Skill(
            id="skill_2",
            name="Process",
            preconditions={"ready": True},
            postconditions={"done": True}
        )

        skill3 = Skill(
            id="skill_3",
            name="Cleanup",
            preconditions={"done": True},
            postconditions={"cleaned": True}
        )

        graph.add_skill(skill1)
        graph.add_skill(skill2)
        graph.add_skill(skill3)

        cycles = detect_cycles(graph)
        assert len(cycles) == 0
