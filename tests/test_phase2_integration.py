"""
Phase 2 Integration Tests
==========================

Tests for:
- All 4 agents initialization and basic execution
- Error handling in each agent
- Metric tracking and logging
- Agent status reporting
"""

import sys
from pathlib import Path

# Add .agents to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestration.agents import BaseAgent, DeployAgent, SyncAgent, ValidationAgent, KnowledgeAgent
from orchestration.error_handlers import ErrorHandler, ErrorType, ErrorContext


def test_agent_initialization():
    """Test all agents initialize correctly"""
    print("\n[TEST] Agent Initialization")

    agents = [
        DeployAgent(),
        SyncAgent(),
        ValidationAgent(),
        KnowledgeAgent()
    ]

    for agent in agents:
        assert agent.name is not None, f"Agent {agent} has no name"
        assert agent.specialization is not None, f"Agent {agent} has no specialization"
        assert len(agent.supported_goals) > 0, f"Agent {agent} has no supported goals"
        print(f"  [OK] {agent.name}: {agent.specialization}")

    return True


def test_deploy_agent_execution():
    """Test Deploy Agent executes deploy-game-release goal"""
    print("\n[TEST] Deploy Agent Execution")

    agent = DeployAgent()
    result = agent.execute(
        goal="deploy-game-release",
        context={"phase": "phase_4"},
        platform="linux",
        version="1.0.0",
        environment="staging"
    )

    assert result["status"] == "completed", f"Expected completed, got {result['status']}"
    assert "stages" in result, "Missing stages in result"
    assert len(result["stages"]) == 4, f"Expected 4 stages, got {len(result['stages'])}"
    assert "duration_ms" in result, "Missing duration_ms"
    print(f"  [OK] Deploy completed in {result['duration_ms']:.0f}ms with {len(result['stages'])} stages")

    return True


def test_sync_agent_execution():
    """Test Sync Agent executes sync-with-remote goal"""
    print("\n[TEST] Sync Agent Execution")

    agent = SyncAgent()
    result = agent.execute(
        goal="sync-with-remote",
        context={"phase": "phase_4"}
    )

    assert result["status"] == "completed", f"Expected completed, got {result['status']}"
    assert "operations" in result, "Missing operations in result"
    print(f"  [OK] Sync completed with {len(result['operations'])} operations")

    return True


def test_validation_agent_execution():
    """Test Validation Agent executes validate-all-skills goal"""
    print("\n[TEST] Validation Agent Execution")

    agent = ValidationAgent()

    # Test Phase 4 (strict mode)
    result_phase4 = agent.execute(
        goal="validate-all-skills",
        context={"phase": "phase_4"}
    )

    assert result_phase4["status"] == "pass", f"Phase 4 validation should pass"
    assert "gates" in result_phase4, "Missing gates in result"
    assert len(result_phase4["gates"]) == 8, f"Expected 8 gates, got {len(result_phase4['gates'])}"
    print(f"  [OK] Phase 4 validation: {result_phase4['summary']['pass_rate']}")

    # Test Phase 5 (lenient mode - gate 7 fails but should be handled)
    result_phase5 = agent.execute(
        goal="validate-all-skills",
        context={"phase": "phase_5_enrichment"}
    )

    assert result_phase5["status"] == "fail", f"Phase 5 should have gate 7 failure for testing"
    assert result_phase5["gates"][7]["status"] == "fail", "Gate 7 should fail in phase 5"
    print(f"  [OK] Phase 5 validation: {result_phase5['summary']['pass_rate']} (gate 7 allowed to fail)")

    return True


def test_knowledge_agent_execution():
    """Test Knowledge Agent executes learn-and-optimize goal"""
    print("\n[TEST] Knowledge Agent Execution")

    agent = KnowledgeAgent()
    result = agent.execute(
        goal="learn-and-optimize",
        context={"phase": "phase_4"}
    )

    assert result["status"] == "completed", f"Expected completed, got {result['status']}"
    assert "analysis" in result, "Missing analysis in result"
    print(f"  [OK] Learning completed: {result['learning_summary']['recommendations']} recommendations")

    # Test suggest-improvements
    result_improve = agent.execute(
        goal="suggest-improvements",
        context={"phase": "phase_5_enrichment"}
    )

    assert result_improve["status"] == "completed", f"Expected completed, got {result_improve['status']}"
    assert "suggestions" in result_improve, "Missing suggestions"
    print(f"  [OK] Suggestions generated: {len(result_improve['suggestions'])} items")

    return True


def test_agent_error_handling():
    """Test agent error handling with proper recovery"""
    print("\n[TEST] Agent Error Handling")

    agent = DeployAgent()

    # Test handling of deployment error
    error_ctx = agent.handle_error(
        error={"type": "build_failure", "message": "Compilation failed"},
        context={"phase": "phase_4"}
    )

    assert error_ctx["strategy"] == "retry_with_verbose", f"Expected retry_with_verbose, got {error_ctx['strategy']}"
    assert error_ctx["success"] == True, "Error recovery should succeed"
    print(f"  [OK] Build failure recovered with: {error_ctx['strategy']}")

    # Test sync agent conflict resolution
    sync_agent = SyncAgent()
    merge_error = sync_agent.handle_error(
        error={"type": "merge_conflict", "message": "Merge conflict detected"},
        context={"phase": "phase_4"}
    )

    assert merge_error["strategy"] == "analyze_and_suggest", f"Expected analyze_and_suggest, got {merge_error['strategy']}"
    print(f"  [OK] Merge conflict handled with: {merge_error['strategy']}")

    return True


def test_agent_metrics_tracking():
    """Test agent metrics collection and reporting"""
    print("\n[TEST] Agent Metrics Tracking")

    agent = ValidationAgent()

    # Execute multiple times to build history
    for _ in range(3):
        agent.execute(
            goal="validate-all-skills",
            context={"phase": "phase_4"}
        )

    # Get metrics
    metrics = agent.get_metrics()

    assert metrics["total_executions"] == 3, f"Expected 3 executions, got {metrics['total_executions']}"
    assert "success_rate" in metrics, "Missing success_rate in metrics"
    assert "avg_duration_ms" in metrics, "Missing avg_duration_ms in metrics"
    print(f"  [OK] Metrics: {metrics['success_rate']*100:.0f}% success rate, {metrics['total_executions']} executions")

    return True


def test_error_handler_framework():
    """Test error handler framework functionality"""
    print("\n[TEST] Error Handler Framework")

    handler = ErrorHandler("test_agent")

    # Create error context
    error_ctx = handler.create_context(ErrorType.BUILD_FAILURE, "Build compilation failed")
    assert error_ctx.error_type == ErrorType.BUILD_FAILURE
    assert error_ctx.agent_name == "test_agent"
    print(f"  [OK] Error context created: {error_ctx.error_type}")

    # Handle error with recovery
    error_handled = handler.handle(
        ErrorType.DEPLOYMENT_TIMEOUT,
        "Deployment took longer than 5 minutes",
        context_data={"phase": "phase_4"}
    )

    recovery_strategies = error_handled.metadata.get("suggested_strategies", [])
    assert len(recovery_strategies) > 0, "Should suggest recovery strategies"
    print(f"  [OK] Recovery strategies suggested: {recovery_strategies[0]['name']}")

    # Check error statistics
    stats = handler.get_error_stats()
    assert stats["total_errors"] == 1, f"Expected 1 error, got {stats['total_errors']}"
    print(f"  [OK] Error stats: {stats['total_errors']} errors tracked")

    return True


def test_agent_status_reporting():
    """Test agent status reporting"""
    print("\n[TEST] Agent Status Reporting")

    agents = [
        DeployAgent(),
        SyncAgent(),
        ValidationAgent(),
        KnowledgeAgent()
    ]

    for agent in agents:
        status = agent.get_status()

        assert "name" in status, f"{agent.name}: Missing name in status"
        assert "specialization" in status, f"{agent.name}: Missing specialization in status"
        assert "status" in status, f"{agent.name}: Missing status in status"
        assert status["status"] == "idle", f"{agent.name}: Should be idle initially"

        print(f"  [OK] {agent.name}: {status['status']}")

    return True


def run_all_tests():
    """Run all Phase 2 tests"""
    print("\n" + "="*60)
    print("PHASE 2: CORE AGENTS INTEGRATION TESTS")
    print("="*60)

    tests = [
        test_agent_initialization,
        test_deploy_agent_execution,
        test_sync_agent_execution,
        test_validation_agent_execution,
        test_knowledge_agent_execution,
        test_agent_error_handling,
        test_agent_metrics_tracking,
        test_error_handler_framework,
        test_agent_status_reporting
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"  [FAILED] {e}")
            failed += 1
        except Exception as e:
            print(f"  [ERROR] {e}")
            failed += 1

    print("\n" + "="*60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("="*60)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
