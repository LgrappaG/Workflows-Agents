"""
GOAP Planner Tests
Test suite for Goal-Oriented Action Planning with A* search
"""
import pytest
from orchestration.goap.world_state import WorldState
from orchestration.goap.action import Action
from orchestration.goap.planner import GOAPPlanner


class TestWorldState:
    """Tests for WorldState class"""

    def test_world_state_creation(self):
        """Test creating a world state with initial conditions"""
        state = WorldState({"ready": False, "deployed": False})
        assert state.get("ready") is False
        assert state.get("deployed") is False

    def test_world_state_clone(self):
        """Test cloning a world state creates independent copy"""
        state1 = WorldState({"ready": False, "deployed": False})
        state2 = state1.clone()

        # Modify the clone
        state2.set("ready", True)

        # Original should be unchanged
        assert state1.get("ready") is False
        assert state2.get("ready") is True

    def test_world_state_distance(self):
        """Test manhattan distance calculation between states"""
        state1 = WorldState({"ready": False, "deployed": False, "validated": False})
        state2 = WorldState({"ready": True, "deployed": False, "validated": True})

        # 2 keys differ (ready and validated)
        distance = state1.distance_to(state2)
        assert distance == 2

    def test_world_state_equality(self):
        """Test world state equality comparison"""
        state1 = WorldState({"ready": False, "deployed": False})
        state2 = WorldState({"ready": False, "deployed": False})
        state3 = WorldState({"ready": True, "deployed": False})

        assert state1 == state2
        assert state1 != state3

    def test_world_state_hashable(self):
        """Test world state can be used in sets/dicts"""
        state1 = WorldState({"ready": False, "deployed": False})
        state2 = WorldState({"ready": False, "deployed": False})

        # Should be hashable
        state_set = {state1, state2}
        # Equal states should result in same set size (since they hash equal)
        assert len(state_set) == 1


class TestAction:
    """Tests for Action class"""

    def test_action_creation(self):
        """Test creating an action with preconditions and effects"""
        action = Action(
            name="validate",
            cost=1.0,
            preconditions={"ready": True},
            effects={"validated": True}
        )
        assert action.name == "validate"
        assert action.cost == 1.0

    def test_action_preconditions_met(self):
        """Test checking if action preconditions are satisfied"""
        action = Action(
            name="validate",
            cost=1.0,
            preconditions={"ready": True, "config": "loaded"},
            effects={"validated": True}
        )

        state_good = WorldState({"ready": True, "config": "loaded", "other": False})
        state_bad = WorldState({"ready": False, "config": "loaded"})

        assert action.preconditions_met(state_good) is True
        assert action.preconditions_met(state_bad) is False

    def test_action_apply(self):
        """Test applying an action to a state"""
        action = Action(
            name="validate",
            cost=1.0,
            preconditions={"ready": True},
            effects={"validated": True}
        )

        state = WorldState({"ready": True, "validated": False})
        new_state = action.apply(state)

        # Original state unchanged
        assert state.get("validated") is False
        # New state has effect applied
        assert new_state.get("validated") is True


class TestGOAPPlanner:
    """Tests for GOAP Planner"""

    def test_goap_planner_simple_plan(self):
        """Test GOAP planner with 3-action chain: validate->prepare->deploy"""
        planner = GOAPPlanner()

        # Add actions
        validate_action = Action(
            name="validate",
            cost=1.0,
            preconditions={"config": "loaded"},
            effects={"validated": True}
        )

        prepare_action = Action(
            name="prepare",
            cost=2.0,
            preconditions={"validated": True},
            effects={"prepared": True}
        )

        deploy_action = Action(
            name="deploy",
            cost=1.0,
            preconditions={"prepared": True},
            effects={"deployed": True}
        )

        planner.add_action(validate_action)
        planner.add_action(prepare_action)
        planner.add_action(deploy_action)

        # Start state
        start = WorldState({"config": "loaded", "validated": False, "prepared": False, "deployed": False})

        # Goal state
        goal = WorldState({"deployed": True})

        # Plan
        plan = planner.plan(start, goal)

        # Should find a plan
        assert plan is not None
        assert len(plan) == 3

        # Check action names in sequence
        assert plan[0].name == "validate"
        assert plan[1].name == "prepare"
        assert plan[2].name == "deploy"

    def test_goap_planner_no_plan(self):
        """Test GOAP planner when no plan exists"""
        planner = GOAPPlanner()

        # Add action that can never be satisfied
        action = Action(
            name="impossible",
            cost=1.0,
            preconditions={"impossible": True},
            effects={"done": True}
        )
        planner.add_action(action)

        # Start state where precondition can't be met
        start = WorldState({"impossible": False})

        # Goal state
        goal = WorldState({"done": True})

        # Plan should fail
        plan = planner.plan(start, goal)
        assert plan is None

    def test_goap_planner_empty_plan(self):
        """Test GOAP planner when goal is already achieved"""
        planner = GOAPPlanner()

        # Start state already matches goal
        start = WorldState({"deployed": True})
        goal = WorldState({"deployed": True})

        # Plan should be empty
        plan = planner.plan(start, goal)
        assert plan is not None
        assert len(plan) == 0
