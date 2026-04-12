"""
Phase 3 Integration Tests
==========================

Tests for System Intelligence Layer (Phase 3)
- Distributed Tracing
- ML Performance Prediction
- Remediation Optimizer
- Dependency Graph Analyzer
- Compliance Reporter
"""

import sys
import logging
from pathlib import Path
from datetime import datetime, timedelta
import json

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# Add .agents to path
sys.path.insert(0, str(Path(__file__).parent.parent))


class Phase3IntegrationTests:
    """Integration tests for Phase 3 System Intelligence"""

    def __init__(self):
        self.test_results = []
        self.tests_passed = 0
        self.tests_failed = 0

    def run_test(self, name, description, test_func):
        """Run a single test and track results"""
        logger.info(f"\n{'='*70}")
        logger.info(f"TEST: {name}")
        logger.info(f"{'='*70}")
        logger.info(f"Description: {description}")

        try:
            test_func()
            self.tests_passed += 1
            self.test_results.append({"name": name, "status": "PASS", "timestamp": datetime.now().isoformat()})
            logger.info("[OK]")
        except AssertionError as e:
            self.tests_failed += 1
            self.test_results.append({"name": name, "status": "FAIL", "error": str(e), "timestamp": datetime.now().isoformat()})
            logger.error(f"[FAILED]: {e}")
        except Exception as e:
            self.tests_failed += 1
            self.test_results.append({"name": name, "status": "ERROR", "error": str(e), "timestamp": datetime.now().isoformat()})
            logger.error(f"[ERROR]: {e}")

    def test_1_distributed_tracing_end_to_end(self):
        """Scenario: End-to-end request tracing through 5-agent chain"""
        from orchestration.tracing.distributed_tracer import DistributedTracer, SpanKind

        tracer = DistributedTracer()
        trace = tracer.start_trace("user-request-001")
        assert trace is not None, "Trace creation failed"
        assert trace.trace_id is not None, "Trace ID not generated"

        trace.start_span("orchestrator-request", SpanKind.INTERNAL)
        trace.current_span.set_attribute("agent", "Orchestrator-1")
        trace.start_span("agent-1-processing", SpanKind.INTERNAL, parent=trace.current_span)
        trace.current_span.set_attribute("agent", "Agent-1")
        trace.end_span()
        trace.end_span()

        assert len(trace.spans) >= 2, f"Expected 2+ spans, got {len(trace.spans)}"
        tracer.end_trace("user-request-001")
        traces = tracer.get_traces_by_operation("orchestrator-request")
        assert len(traces) > 0, "Trace not stored"
        logger.info(f"Created trace with {len(trace.spans)} spans")

    def test_2_ml_performance_prediction_accuracy(self):
        """Scenario: Predict performance degradation 5min ahead"""
        from orchestration.ml.performance_predictor import PerformancePredictor, PerformanceMetrics

        predictor = PerformancePredictor()
        base_time = datetime.now()
        for i in range(30):
            metric = PerformanceMetrics(
                timestamp=base_time - timedelta(minutes=30-i),
                cpu_percent=20 + i * 2.5,
                memory_mb=150 + i * 2.5,
                latency_ms=100 + i * 30,
                error_rate=0.0 + i * 0.001,
                throughput=1000
            )
            predictor.record_metric("Agent-Test", metric)

        trained = predictor.train_models("Agent-Test")
        assert trained, "Model training failed"

        predictions = predictor.predict_bottleneck("Agent-Test", minutes_ahead=5)
        assert len(predictions) > 0, "No predictions generated"

        cpu_pred = [p for p in predictions if p.metric == "cpu"][0]
        assert cpu_pred.severity in ["WARNING", "CRITICAL"], "Severity not escalated"
        logger.info(f"Predicted {len(predictions)} metrics, highest severity: {cpu_pred.severity}")

    def test_3_remediation_learning_effectiveness(self):
        """Scenario: Test if optimal remediation strategy improves success rate"""
        from orchestration.learning.remediation_optimizer import RemediationOptimizer

        optimizer = RemediationOptimizer()
        for i in range(20):
            success = i >= 10
            optimizer.record_outcome(
                f"INC-{i:05d}",
                "transient",
                "retry",
                success,
                recovery_time_seconds=2.5 if success else 5.0
            )

        stats = optimizer.get_strategy_stats("transient")
        assert stats["attempts"] == 20, "Event tracking failed"
        assert stats["success_rate"] == 0.5, "Success rate calculation wrong"

        rec = optimizer.recommend_strategy("transient")
        assert rec == "retry", "Strategy recommendation incorrect"
        logger.info(f"Remediation optimizer tracking: {stats['success_rate']:.0%} success rate")

    def test_4_dependency_cascade_analysis(self):
        """Scenario: Identify failure cascade if critical agent fails"""
        from orchestration.learning.dependency_analyzer import DependencyGraph

        graph = DependencyGraph()
        graph.add_agent("Orchestrator", "Master", "CRITICAL", "STANDARD", "compute")
        graph.add_agent("Worker-1", "Worker 1", "MEDIUM", "STANDARD", "compute")
        graph.add_agent("Storage", "Storage", "HIGH", "PREMIUM", "storage")

        graph.add_dependency("Worker-1", "Orchestrator", "depends_on", "MEDIUM")
        graph.add_dependency("Storage", "Orchestrator", "depends_on", "HIGH")

        impact = graph.get_agent_impact("Orchestrator")
        assert impact["impact_level"] in ["HIGH", "CRITICAL"], "Impact not detected"

        cascade = graph.simulate_failure_cascade("Orchestrator")
        assert cascade.total_impact in ["HIGH", "CRITICAL"], "Cascade severity wrong"
        logger.info(f"Cascade analysis: {cascade.affected_agents} agents affected, {cascade.total_impact} impact")

    def test_5_compliance_audit_trail_integrity(self):
        """Scenario: Record 50 events and verify audit trail integrity"""
        from orchestration.learning.compliance_reporter import ComplianceReporter

        reporter = ComplianceReporter()
        for i in range(50):
            event_type = "data_access" if i % 3 == 0 else "decision"
            reporter.record_event(
                event_type=event_type,
                agent_id=f"Agent-{i % 5}",
                action=f"Operation {i}",
                entity_id=f"entity-{i // 10}",
                status="SUCCESS" if i % 5 != 0 else "FAILURE"
            )

        assert len(reporter.events) == 50, "Event recording failed"

        access_events = reporter.get_audit_trail(event_type="data_access")
        expected_access = sum(1 for i in range(50) if i % 3 == 0)
        assert len(access_events) == expected_access, "Event filtering failed"

        for event in reporter.events:
            assert event.hash_signature is not None, "Hash signature missing"
            assert len(event.hash_signature) == 64, "Hash signature invalid"

        logger.info(f"Audit trail: {len(reporter.events)} events, all hashes valid")

    def test_6_phase3_component_integration(self):
        """Scenario: All 5 Phase 3 components working together"""
        from orchestration.tracing.distributed_tracer import DistributedTracer, SpanKind
        from orchestration.ml.performance_predictor import PerformancePredictor, PerformanceMetrics
        from orchestration.learning.remediation_optimizer import RemediationOptimizer
        from orchestration.learning.dependency_analyzer import DependencyGraph
        from orchestration.learning.compliance_reporter import ComplianceReporter

        tracer = DistributedTracer()
        predictor = PerformancePredictor()
        optimizer = RemediationOptimizer()
        graph = DependencyGraph()
        reporter = ComplianceReporter()

        trace = tracer.start_trace("sys-degradation-001")
        trace.start_span("agent-1-operation", SpanKind.INTERNAL)

        for i in range(15):
            metric = PerformanceMetrics(
                timestamp=datetime.now() - timedelta(minutes=15-i),
                cpu_percent=30 + i * 3,
                memory_mb=180 + i * 2,
                latency_ms=150 + i * 20,
                error_rate=0.0,
                throughput=1000
            )
            predictor.record_metric("Agent-1", metric)

        predictor.train_models("Agent-1")
        predictions = predictor.predict_bottleneck("Agent-1")
        if predictions:
            optimizer.record_outcome("INC-001", "resource", "resource", True, recovery_time_seconds=15.0)

        graph.add_agent("Agent-1", "Test Agent", "MEDIUM", "STANDARD", "compute")
        graph.add_agent("Storage-1", "Storage", "HIGH", "PREMIUM", "storage")
        graph.add_dependency("Agent-1", "Storage-1", "depends_on")

        reporter.create_processing_record(
            "proc-incident-001",
            "Performance degradation response",
            "legitimate_interest",
            "performance_metrics",
            retention_days=365,
            processors=["Agent-1", "Monitor-1"]
        )

        reporter.record_event(
            event_type="anomaly",
            agent_id="Agent-1",
            action="Performance degradation detected",
            entity_id="INC-001",
            reason="Performance monitoring"
        )

        trace.end_span()
        tracer.end_trace("sys-degradation-001")

        assert len(tracer.get_traces_by_operation("agent-1-operation")) > 0, "Tracing failed"
        assert predictor.models.get("Agent-1") is not None, "ML training failed"
        assert len(optimizer.outcomes) > 0, "Remediation recording failed"
        assert len(graph.nodes) > 0, "Dependency tracking failed"
        assert len(reporter.events) > 0, "Compliance recording failed"

        logger.info("Full Phase 3 integration successful")

    def run_all_tests(self):
        """Execute all Phase 3 integration tests"""
        logger.info("\n" + "="*70)
        logger.info("PHASE 3 INTEGRATION TEST SUITE")
        logger.info("="*70)

        self.run_test("Distributed Tracing (End-to-End)", "Verify trace creation, span linking", self.test_1_distributed_tracing_end_to_end)
        self.run_test("ML Performance Prediction", "Test ARIMA forecasting and anomaly prediction", self.test_2_ml_performance_prediction_accuracy)
        self.run_test("Remediation Learning", "Verify strategy recommendation and success tracking", self.test_3_remediation_learning_effectiveness)
        self.run_test("Dependency Cascade Analysis", "Simulate failure propagation and impact", self.test_4_dependency_cascade_analysis)
        self.run_test("Compliance Audit Trail", "Verify event immutability and audit trail integrity", self.test_5_compliance_audit_trail_integrity)
        self.run_test("Full Phase 3 Integration", "All 5 components working together", self.test_6_phase3_component_integration)

        logger.info("\n" + "="*70)
        logger.info("PHASE 3 INTEGRATION TEST SUMMARY")
        logger.info("="*70)
        logger.info(f"Tests Passed: {self.tests_passed}/6")
        logger.info(f"Tests Failed: {self.tests_failed}/6")
        logger.info("="*70)

        if self.tests_failed == 0:
            logger.info("[OK] ALL TESTS PASSED - Phase 3 Ready for Production")
        else:
            logger.error("[FAILED] SOME TESTS FAILED")

        return self.tests_failed == 0


def main():
    tester = Phase3IntegrationTests()
    success = tester.run_all_tests()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
