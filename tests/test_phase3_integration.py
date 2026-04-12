"""
Phase 3 Integration Tests
==========================

Tests for:
- Error Detection Engine (pattern recognition, anomaly detection)
- Self-Correction Engine (learning from recovery)
- Recovery Manager (circuit breakers, retry strategies, rollbacks)
- Intelligence Router (multi-agent consensus voting)
"""

import sys
from pathlib import Path

# Add .agents to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestration.intelligence import (
    ErrorDetectionEngine,
    SelfCorrectionEngine,
    RecoveryManager,
    IntelligenceRouter,
    VotingStrategy,
    Vote,
    ExponentialBackoffStrategy
)


def test_error_detection_basic():
    """Test basic error detection"""
    print("\n[TEST] Error Detection - Basic Pattern Detection")

    engine = ErrorDetectionEngine()

    # Simulate errors
    for i in range(5):
        analysis = engine.analyze_error(
            error_type="gate_failure",
            agent_name="validation",
            context={"phase": "phase_4"}
        )

    patterns = engine.get_top_errors(limit=1)
    assert len(patterns) == 1, "Should have 1 pattern"
    assert patterns[0]["error_type"] == "gate_failure", "Should detect gate_failure"
    assert patterns[0]["frequency"] == 5, "Should have frequency of 5"

    print(f"  [OK] Detected pattern: {patterns[0]['error_type']} (frequency: {patterns[0]['frequency']})")

    return True


def test_error_detection_chain():
    """Test error chain detection"""
    print("\n[TEST] Error Detection - Error Chain Detection")

    engine = ErrorDetectionEngine()

    # Simulate cascading errors
    errors = [
        ("build_failure", "deploy"),
        ("deployment_timeout", "deploy"),
        ("verification_failed", "deploy")
    ]

    for error_type, agent in errors:
        engine.analyze_error(error_type, agent, {"phase": "phase_4"})

    chains = engine.detect_error_chains()
    assert len(chains) > 0, "Should detect error chain"
    assert len(chains[0]["error_sequence"]) >= 2, "Chain should have multiple errors"

    print(f"  [OK] Detected error chain with {len(chains[0]['error_sequence'])} errors")

    return True


def test_error_detection_high_risk():
    """Test high-risk operation detection"""
    print("\n[TEST] Error Detection - High-Risk Operations")

    engine = ErrorDetectionEngine()

    # Simulate high error rate for deploy agent in phase_5
    for i in range(10):
        engine.analyze_error(
            error_type="build_failure",
            agent_name="deploy",
            context={"phase": "phase_5_enrichment"}
        )

    high_risk = engine.get_high_risk_operations()
    assert len(high_risk) > 0, "Should identify high-risk operations"

    print(f"  [OK] Identified {len(high_risk)} high-risk operation(s)")

    return True


def test_self_correction_learning():
    """Test self-correction engine learning"""
    print("\n[TEST] Self-Correction Engine - Strategy Learning")

    engine = SelfCorrectionEngine()

    # Record successful recoveries
    for i in range(8):
        engine.record_recovery_attempt(
            error_type="build_failure",
            strategy="retry_with_verbose",
            success=True,
            recovery_time_ms=1000 + (i * 100),
            context={"phase": "phase_4"}
        )

    # Record some failures
    for i in range(2):
        engine.record_recovery_attempt(
            error_type="build_failure",
            strategy="retry_with_verbose",
            success=False,
            recovery_time_ms=5000,
            context={"phase": "phase_4"}
        )

    recommendation = engine.get_recommended_strategy("build_failure")
    assert recommendation is not None, "Should have recommendation"
    assert float(recommendation["confidence"]) > 0.7, "Should have high confidence"

    print(f"  [OK] Learned strategy: {recommendation['recommended_strategy']} (confidence: {recommendation['confidence']})")

    return True


def test_self_correction_adaptation():
    """Test adaptation plan generation"""
    print("\n[TEST] Self-Correction Engine - Adaptation Planning")

    engine = SelfCorrectionEngine()

    # Record phase-specific recoveries
    for phase in ["phase_4", "phase_5_enrichment"]:
        for i in range(15):
            engine.record_recovery_attempt(
                error_type="gate_failure",
                strategy="analyze_and_suggest",
                success=(i % 3 != 0),  # 66% success rate
                recovery_time_ms=2000 + (i * 50),
                context={"phase": phase}
            )

    adaptation_plan = engine.generate_adaptation_plan()
    assert "threshold_adjustments" in adaptation_plan, "Should include threshold adjustments"

    print(f"  [OK] Generated adaptation plan with {len(adaptation_plan['threshold_adjustments'])} phase contexts")

    return True


def test_recovery_manager_circuit_breaker():
    """Test circuit breaker pattern"""
    print("\n[TEST] Recovery Manager - Circuit Breaker")

    manager = RecoveryManager()

    # Get circuit breaker
    cb = manager.get_circuit_breaker("deploy_operation")
    assert cb.state.value == "closed", "Initial state should be closed"

    # Simulate failures
    for i in range(5):
        cb.record_failure()

    assert cb.state.value == "open", "State should become open after failures"

    # Try operation - should be blocked
    can_attempt = cb.can_attempt_operation()
    assert not can_attempt, "Should not allow operation when open"

    print(f"  [OK] Circuit breaker transitioned from closed to {cb.state.value}")

    return True


def test_recovery_manager_exponential_backoff():
    """Test exponential backoff strategy"""
    print("\n[TEST] Recovery Manager - Exponential Backoff")

    strategy = ExponentialBackoffStrategy(max_attempts=3, base_delay=1.0, max_delay=60.0)

    wait_times = []
    for attempt in range(3):
        strategy.mark_attempt()
        wait_time = strategy.get_wait_time()
        wait_times.append(wait_time)

    # Verify exponential growth
    assert wait_times[0] < wait_times[1], "Wait time should increase"
    assert wait_times[1] < wait_times[2], "Wait time should continue to increase"

    print(f"  [OK] Exponential backoff: {[f'{w:.2f}s' for w in wait_times]}")

    return True


def test_recovery_manager_rollback():
    """Test rollback sequence"""
    print("\n[TEST] Recovery Manager - Rollback Sequence")

    manager = RecoveryManager()
    sequence = manager.create_rollback_sequence("deploy_1")

    # Track execution
    execution_log = []

    def op1():
        execution_log.append("op1")

    def rollback1():
        execution_log.append("rollback1")

    def op2():
        execution_log.append("op2")

    def rollback2():
        execution_log.append("rollback2")

    sequence.add_step("step1", op1, rollback1)
    sequence.add_step("step2", op2, rollback2)

    result = sequence.execute()
    assert result["status"] == "completed", "Sequence should complete successfully"
    assert execution_log == ["op1", "op2"], "Both operations should execute"

    print(f"  [OK] Rollback sequence executed: {execution_log}")

    return True


def test_intelligence_router_consensus():
    """Test multi-agent consensus voting"""
    print("\n[TEST] Intelligence Router - Consensus Voting")

    router = IntelligenceRouter(agents=["deploy", "sync", "validation", "knowledge"])

    # Agents make recommendations
    recommendations = {
        "deploy": {"decision": "approve", "confidence": 0.9, "rationale": "Build successful"},
        "sync": {"decision": "approve", "confidence": 0.85, "rationale": "Git clean"},
        "validation": {"decision": "reject", "confidence": 0.7, "rationale": "Gate 7 failed"},
        "knowledge": {"decision": "approve", "confidence": 0.75, "rationale": "No anomalies"}
    }

    # Route through consensus
    result = router.route_decision(
        decision_context={"goal": "deploy-game-release", "phase": "phase_4"},
        agent_recommendations=recommendations,
        voting_strategy=VotingStrategy.MAJORITY
    )

    assert "final_decision" in result, "Should have final decision"
    assert result["final_decision"] in ["approved", "rejected"], "Decision should be clear"

    print(f"  [OK] Multi-agent consensus: {result['final_decision']}")

    return True


def test_intelligence_router_audit_trail():
    """Test decision audit trail"""
    print("\n[TEST] Intelligence Router - Audit Trail")

    router = IntelligenceRouter(agents=["deploy", "sync"])

    # Make multiple decisions
    for i in range(3):
        router.route_decision(
            decision_context={"goal": f"goal_{i}", "phase": "phase_4"},
            agent_recommendations={
                "deploy": {"decision": "approve", "confidence": 0.8, "rationale": "OK"},
                "sync": {"decision": "approve", "confidence": 0.8, "rationale": "OK"}
            }
        )

    stats = router.get_routing_statistics()
    assert stats["total_decisions"] == 3, "Should have 3 decisions"
    assert stats["audit_trail_entries"] == 3, "Audit trail should have 3 entries"

    print(f"  [OK] Audit trail: {stats['total_decisions']} decisions recorded")

    return True


def test_phase3_integration_pipeline():
    """Test full Phase 3 integration pipeline"""
    print("\n[TEST] Phase 3 - Full Integration Pipeline")

    # Initialize all components
    error_detector = ErrorDetectionEngine()
    self_corrector = SelfCorrectionEngine()
    recovery_manager = RecoveryManager()
    intelligence_router = IntelligenceRouter()

    # Simulate error detection
    error_detector.analyze_error("build_failure", "deploy", {"phase": "phase_4"})

    # Record recovery attempt
    self_corrector.record_recovery_attempt(
        error_type="build_failure",
        strategy="retry_with_verbose",
        success=True,
        recovery_time_ms=2000,
        context={"phase": "phase_4"}
    )

    # Get recovery recommendation
    recovery_rec = self_corrector.get_recommended_strategy("build_failure")

    # Route through intelligence router
    routing_result = intelligence_router.route_decision(
        decision_context={"goal": "recover_from_build_failure"},
        agent_recommendations={
            "deploy": {"decision": "approve", "confidence": 0.9, "rationale": "Use retry strategy"},
            "knowledge": {"decision": "approve", "confidence": 0.8, "rationale": "Recovery feasible"}
        }
    )

    assert recovery_rec is not None, "Should have recovery recommendation"
    assert routing_result["final_decision"] in ["approved", "rejected"], "Should have routing decision"

    print(f"  [OK] Full pipeline: Error detected -> Recovery recommended -> Decision routed")

    return True


def run_all_tests():
    """Run all Phase 3 tests"""
    print("\n" + "="*60)
    print("PHASE 3: INTELLIGENCE & SELF-CORRECTION TESTS")
    print("="*60)

    tests = [
        test_error_detection_basic,
        test_error_detection_chain,
        test_error_detection_high_risk,
        test_self_correction_learning,
        test_self_correction_adaptation,
        test_recovery_manager_circuit_breaker,
        test_recovery_manager_exponential_backoff,
        test_recovery_manager_rollback,
        test_intelligence_router_consensus,
        test_intelligence_router_audit_trail,
        test_phase3_integration_pipeline
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
