"""
Enterprise Hardening System for .agents
========================================

Phase 1: Core Security Layer
- SafeFileOperations: Protected file I/O with audit logging
- SafeProcessExecution: Shell injection prevention
- AgentSandbox: Resource limits (CPU, memory, timeout)
- CircuitBreaker: Prevents cascading failures
- PolicyEngine: Access control enforcement

Phase 2: Monitoring & Self-Healing (extending existing components)
- PerformanceMonitor: Security metrics tracking
- AnomalyDetector: Suspicious pattern detection
- SelfHealingOrchestrator: Auto-remediation

Phase 3: Compliance & Intelligence (extending existing components)
- DistributedTracer: Operation tracing
- ComplianceReporter: Audit trail generation
- PerformancePredictor: ML-based failure prediction
"""

from .safe_operations import (
    SafeFileOperations,
    SafeProcessExecution,
    get_safe_file_operations,
    get_safe_process_execution,
)

from .agent_sandbox import (
    AgentSandbox,
    ResourceTier,
    SandboxConfig,
    get_sandbox_manager,
)

from .circuit_breaker import (
    CircuitBreaker,
    CircuitBreakerOpenException,
    get_circuit_breaker_manager,
)

from .policy_engine import (
    PolicyEngine,
    AgentPolicy,
    get_policy_engine,
)

__all__ = [
    # Safe Operations
    "SafeFileOperations",
    "SafeProcessExecution",
    "get_safe_file_operations",
    "get_safe_process_execution",
    # Sandbox
    "AgentSandbox",
    "ResourceTier",
    "SandboxConfig",
    "get_sandbox_manager",
    # Circuit Breaker
    "CircuitBreaker",
    "CircuitBreakerOpenException",
    "get_circuit_breaker_manager",
    # Policy Engine
    "PolicyEngine",
    "AgentPolicy",
    "get_policy_engine",
]

__version__ = "1.0.0"
__author__ = "Agent Security Team"
