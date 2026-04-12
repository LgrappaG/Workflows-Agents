"""
Error Handlers Framework
=========================

Shared error handling utilities for all orchestration agents.

Provides:
- Error classification
- Recovery pattern templates
- Error context tracking
- Recovery strategy selection
"""

from typing import Dict, List, Any, Callable, Optional
from datetime import datetime


class ErrorType:
    """Error type constants"""
    # Deployment errors
    BUILD_FAILURE = "build_failure"
    DEPLOYMENT_TIMEOUT = "deployment_timeout"
    VERIFICATION_FAILED = "verification_failed"
    ROLLBACK_FAILED = "rollback_failed"

    # Sync errors
    MERGE_CONFLICT = "merge_conflict"
    REMOTE_DIVERGENCE = "remote_divergence"
    NETWORK_FAILURE = "network_failure"
    PUSH_REJECTED = "push_rejected"

    # Validation errors
    GATE_FAILURE = "gate_failure"
    TEST_FAILURE = "test_failure"
    PLUGIN_DISAGREEMENT = "plugin_disagreement"
    QUALITY_CHECK_FAILED = "quality_check_failed"

    # Learning errors
    INSUFFICIENT_DATA = "insufficient_data"
    PATTERN_NOT_FOUND = "pattern_not_found"
    METRICS_CORRUPTION = "metrics_corruption"

    # Orchestration errors
    GOAL_NOT_DECOMPOSABLE = "goal_not_decomposable"
    DEPENDENCY_FAILURE = "dependency_failure"
    STATE_CORRUPTION = "state_corruption"


class RecoveryStrategy:
    """Recovery strategy templates"""

    @staticmethod
    def retry_with_backoff() -> Dict[str, Any]:
        """Exponential backoff retry strategy"""
        return {
            "name": "retry_with_backoff",
            "max_attempts": 3,
            "backoff_seconds": [1, 2, 4],
            "description": "Retry operation with exponential backoff"
        }

    @staticmethod
    def rollback() -> Dict[str, Any]:
        """Rollback to previous state"""
        return {
            "name": "rollback",
            "preserve_state": True,
            "description": "Roll back to previous known-good state"
        }

    @staticmethod
    def analyze_and_suggest() -> Dict[str, Any]:
        """Analyze error and suggest fix"""
        return {
            "name": "analyze_and_suggest",
            "suggest_fix": True,
            "description": "Analyze error details and suggest resolution"
        }

    @staticmethod
    def consensus_voting() -> Dict[str, Any]:
        """Use plugin consensus voting"""
        return {
            "name": "consensus_voting",
            "voting_strategy": "majority",
            "min_votes": 2,
            "description": "Wait for plugin consensus vote"
        }

    @staticmethod
    def accumulate_samples() -> Dict[str, Any]:
        """Accumulate more data before analysis"""
        return {
            "name": "accumulate_samples",
            "min_samples": 10,
            "description": "Collect more samples before analysis"
        }

    @staticmethod
    def skip_and_continue() -> Dict[str, Any]:
        """Skip current sub-goal and continue"""
        return {
            "name": "skip_and_continue",
            "description": "Skip current operation and continue with next"
        }


class ErrorContext:
    """Error context with full execution information"""

    def __init__(self, error_type: str, message: str, agent_name: str):
        self.error_type = error_type
        self.message = message
        self.agent_name = agent_name
        self.timestamp = datetime.now().isoformat()
        self.metadata = {}
        self.recovery_attempts = []

    def add_metadata(self, key: str, value: Any):
        """Add contextual metadata"""
        self.metadata[key] = value
        return self

    def record_recovery_attempt(self, strategy: str, success: bool, details: str):
        """
        Record a recovery attempt.
        """
        self.recovery_attempts.append({
            "timestamp": datetime.now().isoformat(),
            "strategy": strategy,
            "success": success,
            "details": details
        })
        return self

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "error_type": self.error_type,
            "message": self.message,
            "agent": self.agent_name,
            "timestamp": self.timestamp,
            "metadata": self.metadata,
            "recovery_attempts": self.recovery_attempts,
            "total_attempts": len(self.recovery_attempts),
            "recovery_succeeded": any(a["success"] for a in self.recovery_attempts)
        }

    def is_recoverable(self) -> bool:
        """Check if error has successful recovery"""
        return any(a["success"] for a in self.recovery_attempts)


class ErrorClassifier:
    """Classify and categorize errors"""

    # Error severity levels
    SEVERITY_CRITICAL = "critical"
    SEVERITY_HIGH = "high"
    SEVERITY_MEDIUM = "medium"
    SEVERITY_LOW = "low"

    # Error categories
    CATEGORY_BUILD = "build"
    CATEGORY_DEPLOYMENT = "deployment"
    CATEGORY_SYNC = "sync"
    CATEGORY_VALIDATION = "validation"
    CATEGORY_DATA = "data"
    CATEGORY_INFRASTRUCTURE = "infrastructure"

    @staticmethod
    def classify(error_type: str) -> Dict[str, str]:
        """
        Classify error by type and return metadata.
        """
        classification = {
            ErrorType.BUILD_FAILURE: {
                "category": ErrorClassifier.CATEGORY_BUILD,
                "severity": ErrorClassifier.SEVERITY_HIGH,
                "retryable": True
            },
            ErrorType.DEPLOYMENT_TIMEOUT: {
                "category": ErrorClassifier.CATEGORY_DEPLOYMENT,
                "severity": ErrorClassifier.SEVERITY_HIGH,
                "retryable": True
            },
            ErrorType.VERIFICATION_FAILED: {
                "category": ErrorClassifier.CATEGORY_DEPLOYMENT,
                "severity": ErrorClassifier.SEVERITY_CRITICAL,
                "retryable": False
            },
            ErrorType.MERGE_CONFLICT: {
                "category": ErrorClassifier.CATEGORY_SYNC,
                "severity": ErrorClassifier.SEVERITY_HIGH,
                "retryable": True
            },
            ErrorType.NETWORK_FAILURE: {
                "category": ErrorClassifier.CATEGORY_INFRASTRUCTURE,
                "severity": ErrorClassifier.SEVERITY_MEDIUM,
                "retryable": True
            },
            ErrorType.GATE_FAILURE: {
                "category": ErrorClassifier.CATEGORY_VALIDATION,
                "severity": ErrorClassifier.SEVERITY_MEDIUM,
                "retryable": False
            },
            ErrorType.INSUFFICIENT_DATA: {
                "category": ErrorClassifier.CATEGORY_DATA,
                "severity": ErrorClassifier.SEVERITY_LOW,
                "retryable": False
            }
        }

        return classification.get(error_type, {
            "category": "unknown",
            "severity": ErrorClassifier.SEVERITY_MEDIUM,
            "retryable": False
        })


class ErrorRecoverySelector:
    """Select appropriate recovery strategy based on error context"""

    def __init__(self):
        self.strategies_by_type = self._build_strategy_map()

    def _build_strategy_map(self) -> Dict[str, Callable]:
        """Map error types to recovery strategies"""
        return {
            ErrorType.BUILD_FAILURE: RecoveryStrategy.retry_with_backoff,
            ErrorType.DEPLOYMENT_TIMEOUT: RecoveryStrategy.retry_with_backoff,
            ErrorType.VERIFICATION_FAILED: RecoveryStrategy.rollback,
            ErrorType.MERGE_CONFLICT: RecoveryStrategy.analyze_and_suggest,
            ErrorType.REMOTE_DIVERGENCE: RecoveryStrategy.retry_with_backoff,
            ErrorType.NETWORK_FAILURE: RecoveryStrategy.retry_with_backoff,
            ErrorType.GATE_FAILURE: RecoveryStrategy.analyze_and_suggest,
            ErrorType.PLUGIN_DISAGREEMENT: RecoveryStrategy.consensus_voting,
            ErrorType.INSUFFICIENT_DATA: RecoveryStrategy.accumulate_samples,
            ErrorType.PATTERN_NOT_FOUND: RecoveryStrategy.skip_and_continue,
        }

    def select_strategy(self, error_type: str) -> Dict[str, Any]:
        """
        Select recovery strategy for error type.
        """
        strategy_fn = self.strategies_by_type.get(error_type)

        if strategy_fn:
            return strategy_fn()

        # Default to skip and continue for unknown errors
        return RecoveryStrategy.skip_and_continue()

    def select_strategies(self, error_type: str, environment: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Select multiple recovery strategies in priority order.
        First strategy is primary, others are fallbacks.
        """
        primary = self.select_strategy(error_type)

        # Add environment-specific fallbacks
        fallbacks = []
        if error_type == ErrorType.GATE_FAILURE:
            if environment and "strict" in environment.lower():
                # In strict mode, suggest adjustment then skip
                fallbacks = [
                    RecoveryStrategy.rollback(),
                    RecoveryStrategy.skip_and_continue()
                ]
            else:
                # In lenient mode, just skip
                fallbacks = [RecoveryStrategy.skip_and_continue()]

        return [primary] + fallbacks


class ErrorHandler:
    """Main error handler for agents"""

    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.classifier = ErrorClassifier()
        self.strategy_selector = ErrorRecoverySelector()
        self.error_log = []

    def create_context(self, error_type: str, message: str) -> ErrorContext:
        """Create error context"""
        return ErrorContext(error_type, message, self.agent_name)

    def handle(self, error_type: str, message: str, context_data: Optional[Dict] = None) -> ErrorContext:
        """
        Handle error and return context with recovery recommendation.
        """
        error_context = self.create_context(error_type, message)

        # Classify error
        classification = self.classifier.classify(error_type)
        error_context.add_metadata("classification", classification)

        # Select recovery strategy
        environment = context_data.get("environment", context_data.get("phase")) if context_data else None
        strategies = self.strategy_selector.select_strategies(error_type, environment)
        error_context.add_metadata("suggested_strategies", strategies)

        # Log error
        self.error_log.append(error_context.to_dict())

        return error_context

    def should_retry(self, error_type: str) -> bool:
        """Check if error is retryable"""
        classification = self.classifier.classify(error_type)
        return classification.get("retryable", False)

    def get_error_stats(self) -> Dict[str, Any]:
        """Get error statistics"""
        if not self.error_log:
            return {
                "agent": self.agent_name,
                "total_errors": 0,
                "by_severity": {},
                "recovery_rate": 0
            }

        total = len(self.error_log)
        recovered = sum(1 for e in self.error_log if e.get("recovery_succeeded", False))
        by_severity = {}

        for error in self.error_log:
            severity = error.get("metadata", {}).get("classification", {}).get("severity", "unknown")
            by_severity[severity] = by_severity.get(severity, 0) + 1

        return {
            "agent": self.agent_name,
            "total_errors": total,
            "recovered": recovered,
            "recovery_rate": recovered / total if total > 0 else 0,
            "by_severity": by_severity,
            "error_types": len(set(e.get("error_type") for e in self.error_log))
        }

    def clear_log(self):
        """Clear error log"""
        self.error_log = []


class ErrorChain:
    """Chain errors for dependency failure tracking"""

    def __init__(self, root_error: ErrorContext):
        self.root_error = root_error
        self.dependent_errors = []
        self.chain_start = datetime.now()

    def add_dependent_error(self, error: ErrorContext):
        """Add error that occurred due to previous error"""
        self.dependent_errors.append(error)
        return self

    def get_chain_summary(self) -> Dict[str, Any]:
        """Get summary of error chain"""
        return {
            "root_error": self.root_error.error_type,
            "root_message": self.root_error.message,
            "chain_length": 1 + len(self.dependent_errors),
            "dependent_errors": [e.error_type for e in self.dependent_errors],
            "total_recovery_attempts": sum(len(e.recovery_attempts) for e in [self.root_error] + self.dependent_errors)
        }
