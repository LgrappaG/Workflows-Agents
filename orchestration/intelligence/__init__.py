"""
Orchestration Intelligence
===========================

Intelligence & Self-Correction components

Modules:
- error_detection_engine: Pattern recognition and anomaly detection
- self_correction_engine: Learning from recovery successes
- recovery_manager: Advanced retry strategies and circuit breakers
- intelligence_router: Multi-agent consensus voting and decision making
"""

from orchestration.intelligence.error_detection_engine import (
    ErrorDetectionEngine,
    ErrorPattern,
    AnomalyDetector
)

from orchestration.intelligence.self_correction_engine import (
    SelfCorrectionEngine,
    StrategyLearner,
    RecoveryPattern
)

from orchestration.intelligence.recovery_manager import (
    RecoveryManager,
    CircuitBreaker,
    RollbackSequence,
    RetryBudget,
    ExponentialBackoffStrategy,
    LinearBackoffStrategy
)

from orchestration.intelligence.intelligence_router import (
    IntelligenceRouter,
    VotingRound,
    AgentConsensus,
    ConflictResolver,
    DecisionAuditTrail,
    VotingStrategy,
    Vote
)

__all__ = [
    # Error Detection
    "ErrorDetectionEngine",
    "ErrorPattern",
    "AnomalyDetector",
    # Self-Correction
    "SelfCorrectionEngine",
    "StrategyLearner",
    "RecoveryPattern",
    # Recovery Management
    "RecoveryManager",
    "CircuitBreaker",
    "RollbackSequence",
    "RetryBudget",
    "ExponentialBackoffStrategy",
    "LinearBackoffStrategy",
    # Intelligence Routing
    "IntelligenceRouter",
    "VotingRound",
    "AgentConsensus",
    "ConflictResolver",
    "DecisionAuditTrail",
    "VotingStrategy",
    "Vote"
]
