"""
Phase 1 Hardening Integration Tests
====================================

Tests for security integration with orchestration system.

Coverage:
- Safe file operations (audit trail, backups, atomic writes)
- Circuit breaker (failure threshold, state transitions)
- Policy enforcement (agent whitelist, operation whitelist, resource quotas)
- Agent sandbox (resource limits, timeouts)
- CentralOrchestrator hardening (policy checks)
- StateManager hardening (safe file writes)
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock
import sys
import os

# Add paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from security.safe_operations import SafeFileOperations, SafeProcessExecution
from security.circuit_breaker import CircuitBreaker, CircuitBreakerOpenException
from security.policy_engine import PolicyEngine, AgentPolicy
from security.agent_sandbox import AgentSandbox, SandboxConfig, ResourceTier


class TestSafeFileOperations:
    """Test SafeFileOperations wrapper"""

    def setup_method(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.safe_ops = SafeFileOperations(
            audit_log_path=f"{self.temp_dir.name}/audit.jsonl"
        )

    def teardown_method(self):
        """Clean up"""
        self.temp_dir.cleanup()

    def test_safe_write_creates_file(self):
        """Test that safe write creates file"""
        test_file = f"{self.temp_dir.name}/test.json"
        content = '{"data": "test"}'

        self.safe_ops.write_file(test_file, content)

        assert Path(test_file).exists()
        assert Path(test_file).read_text() == content

    def test_safe_write_creates_backup(self):
        """Test that safe write creates backup of existing file"""
        test_file = f"{self.temp_dir.name}/test.json"

        # Write initial file
        self.safe_ops.write_file(test_file, '{"version": 1}')

        # Write again (should create backup)
        self.safe_ops.write_file(test_file, '{"version": 2}')

        # Check backups directory
        backups = list(self.safe_ops.backup_dir.glob("*.bak"))
        assert len(backups) > 0

    def test_safe_write_denied_path_raises_error(self):
        """Test that writing to denied path raises PermissionError"""
        with pytest.raises(PermissionError):
            self.safe_ops.write_file("/etc/passwd", "test")

    def test_safe_write_creates_audit_log(self):
        """Test that safe write creates audit trail"""
        test_file = f"{self.temp_dir.name}/test.json"
        self.safe_ops.write_file(test_file, '{"test": "data"}')

        # Check audit log
        audit_log = Path(self.safe_ops.audit_log_path)
        assert audit_log.exists()

        # Parse audit entry
        with open(audit_log) as f:
            entry = json.loads(f.readline())

        assert entry["operation"] == "write"
        assert "test.json" in entry["path"]
        assert entry["success"] is True

    def test_safe_read_file(self):
        """Test safe file read"""
        test_file = f"{self.temp_dir.name}/test.json"
        original_content = '{"test": "read"}'

        # Write and read
        self.safe_ops.write_file(test_file, original_content)
        read_content = self.safe_ops.read_file(test_file)

        assert read_content == original_content


class TestCircuitBreaker:
    """Test CircuitBreaker implementation"""

    def test_circuit_closed_allows_calls(self):
        """Test that closed circuit allows calls"""
        breaker = CircuitBreaker("test_breaker")

        def success_fn():
            return "ok"

        result = breaker.call(success_fn)
        assert result == "ok"

    def test_circuit_opens_after_failures(self):
        """Test that circuit opens after max failures"""
        breaker = CircuitBreaker(
            "test_breaker",
            failure_threshold=3,
            sample_window_sec=60
        )

        def failing_fn():
            raise Exception("Failure")

        # Cause failures
        for i in range(3):
            try:
                breaker.call(failing_fn)
            except Exception:
                pass

        # Circuit should be OPEN
        assert breaker.state.value == "open"

        # New calls should be rejected
        with pytest.raises(CircuitBreakerOpenException):
            breaker.call(failing_fn)

    def test_circuit_transitions_to_half_open(self):
        """Test circuit half-open transition after timeout"""
        breaker = CircuitBreaker(
            "test_breaker",
            failure_threshold=2,
            recovery_timeout_sec=0,  # Immediate for testing
            sample_window_sec=60
        )

        def failing_fn():
            raise Exception("Fail")

        # Open the circuit
        for i in range(2):
            try:
                breaker.call(failing_fn)
            except Exception:
                pass

        assert breaker.state.value == "open"

        # Fast-forward time by checking _update_state
        breaker._update_state()

        assert breaker.state.value == "half_open"

    def test_circuit_gets_metrics(self):
        """Test circuit breaker metrics"""
        breaker = CircuitBreaker("test_breaker")

        def ok_fn():
            return "success"

        # Make some calls
        breaker.call(ok_fn)
        breaker.call(ok_fn)

        metrics = breaker.get_metrics()

        assert metrics["circuit_name"] == "test_breaker"
        assert metrics["total_calls"] == 2
        assert metrics["successful_calls"] == 2


class TestPolicyEngine:
    """Test PolicyEngine implementation"""

    def test_agent_allowed_check(self):
        """Test agent whitelist check"""
        policy_engine = PolicyEngine()

        assert policy_engine.check_agent_allowed("DeployAgent") is True
        assert policy_engine.check_agent_allowed("SyncAgent") is True
        assert policy_engine.check_agent_allowed("UnknownAgent") is False

    def test_operation_allowed_check(self):
        """Test operation whitelist check"""
        policy_engine = PolicyEngine()

        assert policy_engine.check_operation_allowed("DeployAgent", "deploy") is True
        assert policy_engine.check_operation_allowed("DeployAgent", "invalid_op") is False

    def test_path_access_check_denies_protected(self):
        """Test path access check denies protected paths"""
        policy_engine = PolicyEngine()

        assert policy_engine.check_path_access("DeployAgent", "/etc/passwd") is False
        assert policy_engine.check_path_access("DeployAgent", "/sys/kernel") is False

    def test_path_access_check_allows_managed(self):
        """Test path access allows managed paths"""
        policy_engine = PolicyEngine()

        assert policy_engine.check_path_access("DeployAgent", ".agents/skills") is True

    def test_comprehensive_goal_check(self):
        """Test comprehensive pre-flight goal check"""
        policy_engine = PolicyEngine()

        goal_data = {
            "agent": "DeployAgent",
            "operation": "deploy",
        }

        # Should succeed
        assert policy_engine.check_goal_allowed(goal_data) is True

        # Should fail with denied agent
        goal_data2 = {
            "agent": "MaliciousAgent",
            "operation": "execute",
        }

        with pytest.raises(PermissionError):
            policy_engine.check_goal_allowed(goal_data2)

    def test_quota_management(self):
        """Test operation quota tracking"""
        policy_engine = PolicyEngine()

        # Record operations
        policy_engine.record_operation("DeployAgent", "deploy")
        policy_engine.record_operation("DeployAgent", "deploy")

        # Should still allow (within quota)
        assert policy_engine.check_resource_quota("DeployAgent", "deploy") is True

        # Complete one
        policy_engine.complete_operation("DeployAgent", "deploy")


class TestAgentSandbox:
    """Test AgentSandbox resource limiting"""

    def test_sandbox_config_creation(self):
        """Test sandbox configuration creation"""
        config = SandboxConfig(
            agent_name="TestAgent",
            tier=ResourceTier.STANDARD,
            working_dir="/tmp/test"
        )

        assert config.agent_name == "TestAgent"
        assert config.tier == ResourceTier.STANDARD

    def test_sandbox_initialization(self):
        """Test sandbox initialization"""
        config = SandboxConfig(
            agent_name="TestAgent",
            tier=ResourceTier.STANDARD,
            working_dir="/tmp"
        )

        sandbox = AgentSandbox(config)

        assert sandbox.agent_name == "TestAgent"
        assert sandbox.memory_limit_mb == 256
        assert sandbox.cpu_limit_percent == 25


class TestIntegration:
    """Integration tests for hardening with orchestration"""

    def test_policy_prevents_unauthorized_goal(self):
        """Test that policy blocks unauthorized goals"""
        from security.policy_engine import get_policy_engine

        policy_engine = get_policy_engine()

        # Valid goal
        valid_goal = {
            "agent": "DeployAgent",
            "operation": "deploy",
        }

        # Should pass
        assert policy_engine.check_goal_allowed(valid_goal) is True

        # Invalid goal with non-approved agent
        invalid_goal = {
            "agent": "HackerAgent",
            "operation": "execute",
        }

        # Should fail
        with pytest.raises(PermissionError):
            policy_engine.check_goal_allowed(invalid_goal)

    def test_circuit_breaker_prevents_cascading_failures(self):
        """Test circuit breaker stops cascading failures"""
        from security.circuit_breaker import get_circuit_breaker_manager

        manager = get_circuit_breaker_manager()
        breaker = manager.get_breaker("DeployAgent")

        def failing_agent_call():
            raise Exception("Agent failure")

        # Simulate multiple failures
        failure_count = 0
        for i in range(10):
            try:
                breaker.call(failing_agent_call)
            except (Exception, CircuitBreakerOpenException):
                failure_count += 1

        # Should open after 5 failures
        assert breaker.state.value == "open"
        # Remaining calls rejected immediately
        assert failure_count > 5


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
