"""
Error Detection Engine
======================

Analyzes error patterns and detects anomalies.

Responsibilities:
- Pattern recognition from error logs
- Anomaly detection in execution metrics
- Error clustering by root cause
- Trend analysis over time
- Risk assessment for future operations
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, Counter


class ErrorPattern:
    """Represents a detected error pattern"""

    def __init__(self, pattern_id: str, error_type: str, frequency: int):
        self.pattern_id = pattern_id
        self.error_type = error_type
        self.frequency = frequency
        self.first_occurrence = datetime.now()
        self.last_occurrence = datetime.now()
        self.context_flags = {}
        self.recovery_successes = 0
        self.recovery_failures = 0
        self.correlation_matrix = {}

    def mark_recovered(self, success: bool):
        """Track recovery outcome"""
        if success:
            self.recovery_successes += 1
        else:
            self.recovery_failures += 1

    def get_recovery_rate(self) -> float:
        """Calculate recovery success rate"""
        total = self.recovery_successes + self.recovery_failures
        if total == 0:
            return 0.0
        return self.recovery_successes / total

    def add_context_flag(self, key: str, value: Any):
        """Add contextual information"""
        self.context_flags[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "pattern_id": self.pattern_id,
            "error_type": self.error_type,
            "frequency": self.frequency,
            "first_occurrence": self.first_occurrence.isoformat(),
            "last_occurrence": self.last_occurrence.isoformat(),
            "recovery_rate": f"{self.get_recovery_rate()*100:.1f}%",
            "recovery_successes": self.recovery_successes,
            "recovery_failures": self.recovery_failures,
            "context_flags": self.context_flags
        }


class AnomalyDetector:
    """Detects anomalies in error patterns"""

    # Statistical thresholds
    ANOMALY_THRESHOLD_STDDEV = 2.0  # 2 standard deviations
    SPIKE_THRESHOLD = 5  # 5x normal frequency
    CLUSTER_SIMILARITY = 0.75

    @staticmethod
    def detect_frequency_spike(historical: List[int], current: int) -> bool:
        """Detect if current frequency is anomalously high"""
        if not historical or len(historical) < 2:
            return False

        mean = sum(historical) / len(historical)
        variance = sum((x - mean) ** 2 for x in historical) / len(historical)
        stddev = variance ** 0.5

        if stddev == 0:
            return current > mean * AnomalyDetector.SPIKE_THRESHOLD

        # Z-score calculation
        z_score = (current - mean) / stddev
        return z_score > AnomalyDetector.ANOMALY_THRESHOLD_STDDEV

    @staticmethod
    def detect_new_error_type(known_types: set, new_type: str) -> bool:
        """Detect previously unseen error type"""
        return new_type not in known_types

    @staticmethod
    def detect_cascading_errors(error_chain: List[str]) -> bool:
        """Detect if errors are cascading from single root cause"""
        return len(error_chain) > 2  # Chain of 3+ errors = cascade

    @staticmethod
    def detect_recovery_failure_pattern(pattern: ErrorPattern) -> bool:
        """Detect if recovery strategies are consistently failing"""
        if pattern.recovery_successes + pattern.recovery_failures < 3:
            return False

        recovery_rate = pattern.get_recovery_rate()
        return recovery_rate < 0.3  # Less than 30% recovery = problem


class ErrorDetectionEngine:
    """Main error detection engine"""

    def __init__(self, window_hours: int = 24):
        self.window_hours = window_hours
        self.patterns = {}  # pattern_id -> ErrorPattern
        self.error_log = []  # [{timestamp, type, agent, context}]
        self.anomalies = []  # Detected anomalies
        self.anomaly_detector = AnomalyDetector()
        self.correlation_matrix = defaultdict(int)

    def analyze_error(self, error_type: str, agent_name: str, context: Dict[str, Any], recovery_context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Analyze a single error and detect patterns.
        """
        timestamp = datetime.now()
        self.error_log.append({
            "timestamp": timestamp.isoformat(),
            "error_type": error_type,
            "agent": agent_name,
            "context": context,
            "recovery_context": recovery_context or {}
        })

        # Get or create pattern
        pattern_id = f"{agent_name}_{error_type}"
        if pattern_id not in self.patterns:
            self.patterns[pattern_id] = ErrorPattern(pattern_id, error_type, 0)

        pattern = self.patterns[pattern_id]
        pattern.frequency += 1
        pattern.last_occurrence = timestamp
        pattern.add_context_flag("agent", agent_name)
        pattern.add_context_flag("environment", context.get("environment", context.get("phase", "unknown")))

        # Track recovery outcome
        if recovery_context:
            recovery_context_success = recovery_context.get("success", False)
            pattern.mark_recovered(recovery_context_success)

        # Detect anomalies
        anomalies = self._detect_anomalies(pattern_id, pattern)

        analysis = {
            "pattern_id": pattern_id,
            "error_type": error_type,
            "agent": agent_name,
            "frequency": pattern.frequency,
            "recovery_rate": f"{pattern.get_recovery_rate()*100:.1f}%",
            "anomalies_detected": len(anomalies),
            "anomalies": anomalies
        }

        return analysis

    def _detect_anomalies(self, pattern_id: str, pattern: ErrorPattern) -> List[Dict[str, Any]]:
        """Detect anomalies for this pattern"""
        anomalies = []

        # Check for recovery failure pattern
        if self.anomaly_detector.detect_recovery_failure_pattern(pattern):
            anomalies.append({
                "type": "recovery_failure_pattern",
                "severity": "high",
                "description": f"Recovery strategies for {pattern.error_type} failing {(1-pattern.get_recovery_rate())*100:.0f}% of time",
                "recommendation": "Review and updated recovery strategies"
            })

        return anomalies

    def get_pattern_summary(self, pattern_id: Optional[str] = None) -> Dict[str, Any]:
        """Get summary of patterns"""
        if pattern_id:
            if pattern_id not in self.patterns:
                return {}
            pattern = self.patterns[pattern_id]
            return pattern.to_dict()

        # Return all patterns
        return {
            pattern_id: pattern.to_dict()
            for pattern_id, pattern in self.patterns.items()
        }

    def get_top_errors(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most frequent error types"""
        sorted_patterns = sorted(
            self.patterns.values(),
            key=lambda p: p.frequency,
            reverse=True
        )

        return [p.to_dict() for p in sorted_patterns[:limit]]

    def get_errors_by_agent(self, agent_name: str) -> List[Dict[str, Any]]:
        """Get all error patterns for a specific agent"""
        agent_patterns = [
            p for p in self.patterns.values()
            if p.context_flags.get("agent") == agent_name
        ]

        return [p.to_dict() for p in agent_patterns]

    def get_errors_by_environment(self, environment: str) -> List[Dict[str, Any]]:
        """Get error patterns for a specific environment"""
        environment_patterns = [
            p for p in self.patterns.values()
            if p.context_flags.get("environment") == environment
        ]

        return [p.to_dict() for p in environment_patterns]

    def detect_error_chains(self) -> List[Dict[str, Any]]:
        """
        Detect cascading error chains.
        Returns list of error sequences that likely have root cause relationship.
        """
        # Look for errors happening in close temporal proximity
        chains = []

        if len(self.error_log) < 3:
            return chains

        # Group errors by time window (5 minute buckets)
        time_buckets = defaultdict(list)
        for error_entry in self.error_log[-100:]:  # Look at recent 100 errors
            timestamp = datetime.fromisoformat(error_entry["timestamp"])
            bucket = timestamp.replace(minute=(timestamp.minute // 5) * 5, second=0, microsecond=0)
            time_buckets[bucket].append(error_entry)

        # Find buckets with multiple error types
        for bucket, errors in time_buckets.items():
            if len(errors) > 2:
                error_types = [e["error_type"] for e in errors]
                agents = [e["agent"] for e in errors]

                if len(set(error_types)) > 1:
                    chains.append({
                        "timestamp": bucket.isoformat(),
                        "error_sequence": error_types,
                        "agents_involved": agents,
                        "likely_chain": True
                    })

        return chains

    def get_error_recovery_correlation(self) -> Dict[str, Dict[str, float]]:
        """
        Get correlation between error types and successful recovery strategies.
        """
        correlation = defaultdict(lambda: defaultdict(int))

        for pattern_id, pattern in self.patterns.items():
            error_type = pattern.error_type
            recovery_rate = pattern.get_recovery_rate()

            correlation[error_type]["total_occurrences"] = pattern.frequency
            correlation[error_type]["recovery_rate"] = recovery_rate

        return dict(correlation)

    def predict_next_error(self) -> Optional[Dict[str, Any]]:
        """
        Predict likely next error based on patterns.
        """
        if not self.patterns:
            return None

        # Get most frequent recent error
        sorted_by_freq = sorted(
            self.patterns.values(),
            key=lambda p: p.frequency,
            reverse=True
        )

        top_pattern = sorted_by_freq[0]

        # Check if pattern is accelerating
        recent_errors = [
            e for e in self.error_log[-50:]
            if e["error_type"] == top_pattern.error_type
        ]

        if len(recent_errors) > 3:
            return {
                "predicted_error_type": top_pattern.error_type,
                "probability": min(top_pattern.frequency / len(self.error_log), 1.0),
                "affected_agents": list(set(
                    e["agent"] for e in recent_errors
                )),
                "typical_recovery_rate": f"{top_pattern.get_recovery_rate()*100:.1f}%"
            }

        return None

    def get_high_risk_operations(self) -> List[Dict[str, Any]]:
        """
        Identify high-risk combinations of agents and environments.
        """
        risk_matrix = defaultdict(lambda: {"errors": 0, "total": 0})

        for error_entry in self.error_log:
            agent = error_entry["agent"]
            environment = error_entry["context"].get("environment", error_entry["context"].get("phase", "unknown"))
            key = f"{agent}@{environment}"

            risk_matrix[key]["errors"] += 1

        # Calculate historical total for comparison
        for error_entry in self.error_log:
            agent = error_entry["agent"]
            environment = error_entry["context"].get("environment", error_entry["context"].get("phase", "unknown"))
            key = f"{agent}@{environment}"
            risk_matrix[key]["total"] += 1

        # Find high-risk combinations (>30% error rate)
        high_risk = []
        for combo, stats in risk_matrix.items():
            if stats["total"] > 0:
                error_rate = stats["errors"] / stats["total"]
                if error_rate > 0.3:
                    agent, environment = combo.split("@")
                    high_risk.append({
                        "agent": agent,
                        "environment": environment,
                        "error_rate": f"{error_rate*100:.1f}%",
                        "total_operations": stats["total"],
                        "error_count": stats["errors"]
                    })

        return sorted(high_risk, key=lambda x: float(x["error_rate"].rstrip("%")), reverse=True)

    def generate_diagnostics_report(self) -> Dict[str, Any]:
        """Generate comprehensive diagnostics report"""
        return {
            "timestamp": datetime.now().isoformat(),
            "error_log_size": len(self.error_log),
            "unique_patterns": len(self.patterns),
            "top_errors": self.get_top_errors(5),
            "error_chains": self.detect_error_chains(),
            "error_recovery_correlation": self.get_error_recovery_correlation(),
            "predicted_next_error": self.predict_next_error(),
            "high_risk_operations": self.get_high_risk_operations(),
            "average_recovery_rate": f"{sum(p.get_recovery_rate() for p in self.patterns.values()) / len(self.patterns)*100:.1f}%" if self.patterns else "N/A"
        }

    def save_report(self, output_path: str = ".agents/orchestration/metrics/error_diagnostics.json"):
        """Save diagnostics report to file"""
        report = self.generate_diagnostics_report()
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, 'w') as f:
            json.dump(report, f, indent=2)

        return output_path
