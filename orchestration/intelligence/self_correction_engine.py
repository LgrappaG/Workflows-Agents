"""
Self-Correction Engine
======================

Learns from recovery successes and improves strategies.

Responsibilities:
- Track successful recovery patterns
- Learn optimal strategies for each error type
- Suggest strategy improvements based on success rates
- Adapt thresholds based on historical data
- Build confidence scores for strategies
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict


class RecoveryPattern:
    """Represents a successful recovery pattern"""

    def __init__(self, error_type: str, strategy: str):
        self.error_type = error_type
        self.strategy = strategy
        self.success_count = 0
        self.failure_count = 0
        self.average_recovery_time_ms = 0
        self.recovery_times = []
        self.context_conditions = defaultdict(int)

    def record_success(self, recovery_time_ms: int, context: Dict[str, Any]):
        """Record successful recovery"""
        self.success_count += 1
        self.recovery_times.append(recovery_time_ms)
        self.average_recovery_time_ms = sum(self.recovery_times) / len(self.recovery_times)

        # Track context conditions that led to success
        for key, value in context.items():
            context_key = f"{key}={value}"
            self.context_conditions[context_key] += 1

    def record_failure(self):
        """Record failed recovery"""
        self.failure_count += 1

    def get_success_rate(self) -> float:
        """Get success rate for this strategy"""
        total = self.success_count + self.failure_count
        if total == 0:
            return 0.0
        return self.success_count / total

    def get_confidence_score(self) -> float:
        """
        Calculate confidence score for this strategy (0.0 - 1.0)
        Based on number of trials and success rate
        """
        total_trials = self.success_count + self.failure_count

        if total_trials < 5:
            # Not enough data
            return min(total_trials / 5, 1.0) * self.get_success_rate()

        # With sufficient trials, success rate becomes the score
        return self.get_success_rate()

    def get_optimal_conditions(self) -> Dict[str, str]:
        """Get context conditions that most frequently led to success"""
        if not self.context_conditions:
            return {}

        # Return top 3 conditions
        sorted_conditions = sorted(
            self.context_conditions.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return {
            condition.split("=")[0]: condition.split("=")[1]
            for condition, _ in sorted_conditions[:3]
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "error_type": self.error_type,
            "strategy": self.strategy,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "success_rate": f"{self.get_success_rate()*100:.1f}%",
            "confidence_score": f"{self.get_confidence_score():.2f}",
            "average_recovery_time_ms": f"{self.average_recovery_time_ms:.0f}",
            "optimal_conditions": self.get_optimal_conditions()
        }


class StrategyLearner:
    """Learns optimal recovery strategies"""

    def __init__(self):
        self.patterns = {}  # key=f"{error_type}_{strategy}" -> RecoveryPattern
        self.strategy_improvements = []

    def record_recovery_attempt(
        self,
        error_type: str,
        strategy: str,
        success: bool,
        recovery_time_ms: int,
        context: Dict[str, Any]
    ):
        """Record a recovery attempt"""
        pattern_key = f"{error_type}_{strategy}"

        if pattern_key not in self.patterns:
            self.patterns[pattern_key] = RecoveryPattern(error_type, strategy)

        pattern = self.patterns[pattern_key]

        if success:
            pattern.record_success(recovery_time_ms, context)
        else:
            pattern.record_failure()

    def get_best_strategy_for_error(self, error_type: str) -> Optional[Tuple[str, float]]:
        """
        Get the best strategy for a given error type.
        Returns (strategy_name, confidence_score)
        """
        candidates = [
            p for key, p in self.patterns.items()
            if p.error_type == error_type
        ]

        if not candidates:
            return None

        # Sort by confidence score
        sorted_by_confidence = sorted(
            candidates,
            key=lambda p: p.get_confidence_score(),
            reverse=True
        )

        best = sorted_by_confidence[0]
        return (best.strategy, best.get_confidence_score())

    def get_all_strategies_for_error(self, error_type: str) -> List[Dict[str, Any]]:
        """Get all strategies for an error type, ranked by effectiveness"""
        candidates = [
            p for key, p in self.patterns.items()
            if p.error_type == error_type
        ]

        sorted_by_confidence = sorted(
            candidates,
            key=lambda p: p.get_confidence_score(),
            reverse=True
        )

        return [p.to_dict() for p in sorted_by_confidence]

    def suggest_strategy_improvements(self) -> List[Dict[str, Any]]:
        """Suggest improvements to recovery strategies"""
        improvements = []

        # Find patterns with low success rates but enough trials
        for pattern_key, pattern in self.patterns.items():
            total_trials = pattern.success_count + pattern.failure_count

            if total_trials < 10:
                continue  # Not enough data

            if pattern.get_success_rate() < 0.5:
                improvements.append({
                    "error_type": pattern.error_type,
                    "current_strategy": pattern.strategy,
                    "success_rate": f"{pattern.get_success_rate()*100:.1f}%",
                    "total_trials": total_trials,
                    "recommendation": f"Consider alternative strategy for {pattern.error_type}",
                    "priority": "high" if total_trials > 20 else "medium"
                })

        return improvements

    def generate_learning_report(self) -> Dict[str, Any]:
        """Generate comprehensive learning report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "patterns_learned": len(self.patterns),
            "total_recovery_attempts": sum(
                p.success_count + p.failure_count
                for p in self.patterns.values()
            ),
            "total_successes": sum(
                p.success_count for p in self.patterns.values()
            ),
            "overall_success_rate": self._calculate_overall_success_rate(),
            "best_performing_strategies": self._get_best_strategies(5),
            "struggling_strategies": self._get_struggling_strategies(5),
            "improvement_suggestions": self.suggest_strategy_improvements()
        }

        return report

    def _calculate_overall_success_rate(self) -> str:
        """Calculate overall success rate across all patterns"""
        total_successes = sum(p.success_count for p in self.patterns.values())
        total_attempts = sum(
            p.success_count + p.failure_count
            for p in self.patterns.values()
        )

        if total_attempts == 0:
            return "N/A"

        rate = total_successes / total_attempts
        return f"{rate*100:.1f}%"

    def _get_best_strategies(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get best performing strategies"""
        sorted_patterns = sorted(
            self.patterns.values(),
            key=lambda p: p.get_confidence_score(),
            reverse=True
        )

        return [p.to_dict() for p in sorted_patterns[:limit]]

    def _get_struggling_strategies(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get struggling strategies that need improvement"""
        # Patterns with multiple trials but low success rate
        struggling = [
            p for p in self.patterns.values()
            if (p.success_count + p.failure_count) >= 10
            and p.get_success_rate() < 0.5
        ]

        sorted_patterns = sorted(
            struggling,
            key=lambda p: p.get_success_rate()
        )

        return [p.to_dict() for p in sorted_patterns[:limit]]


class SelfCorrectionEngine:
    """Main self-correction engine"""

    def __init__(self):
        self.learner = StrategyLearner()
        self.threshold_adjustments = {}
        self.learning_history = []

    def record_recovery_attempt(
        self,
        error_type: str,
        strategy: str,
        success: bool,
        recovery_time_ms: int,
        context: Dict[str, Any]
    ):
        """Record a recovery attempt and learn from it"""
        self.learner.record_recovery_attempt(
            error_type,
            strategy,
            success,
            recovery_time_ms,
            context
        )

        # Track learning event
        self.learning_history.append({
            "timestamp": datetime.now().isoformat(),
            "error_type": error_type,
            "strategy": strategy,
            "success": success,
            "recovery_time_ms": recovery_time_ms,
            "environment": context.get("environment", context.get("phase", "unknown"))
        })

    def get_recommended_strategy(self, error_type: str) -> Optional[Dict[str, Any]]:
        """Get recommended recovery strategy for an error type"""
        best = self.learner.get_best_strategy_for_error(error_type)

        if not best:
            return None

        strategy_name, confidence = best
        all_strategies = self.learner.get_all_strategies_for_error(error_type)

        return {
            "recommended_strategy": strategy_name,
            "confidence": f"{confidence:.2f}",
            "all_strategies": all_strategies[:3]  # Top 3 options
        }

    def suggest_threshold_adjustments(self, environment: str) -> List[Dict[str, Any]]:
        """
        Suggest threshold adjustments for a specific environment based on learning.
        """
        suggestions = []

        # Analyze recovery patterns by environment
        environment_attempts = [
            entry for entry in self.learning_history
            if entry["environment"] == environment
        ]

        if len(environment_attempts) < 10:
            return suggestions  # Not enough data

        # Calculate environment-specific success rate
        successes = sum(1 for e in environment_attempts if e["success"])
        success_rate = successes / len(environment_attempts)

        if success_rate < 0.7:
            suggestions.append({
                "type": "relaxed_thresholds",
                "environment": environment,
                "current_success_rate": f"{success_rate*100:.1f}%",
                "recommendation": f"Consider relaxing validation thresholds for {environment}",
                "rationale": "Recovery success rate below 70% suggests thresholds may be too strict"
            })

        # Analyze recovery times
        recovery_times = [
            e["recovery_time_ms"] for e in environment_attempts
            if e["success"]
        ]

        if recovery_times:
            avg_recovery_time = sum(recovery_times) / len(recovery_times)
            if avg_recovery_time > 5000:  # 5 seconds
                suggestions.append({
                    "type": "optimize_recovery_speed",
                    "environment": environment,
                    "average_recovery_ms": f"{avg_recovery_time:.0f}",
                    "recommendation": "Review recovery strategies for performance optimization",
                    "rationale": "Average recovery time exceeds 5 seconds"
                })

        return suggestions

    def generate_adaptation_plan(self) -> Dict[str, Any]:
        """Generate comprehensive adaptation plan based on learning"""
        return {
            "timestamp": datetime.now().isoformat(),
            "learning_report": self.learner.generate_learning_report(),
            "threshold_adjustments": {
                "phase_4": self.suggest_threshold_adjustments("phase_4"),
                "phase_5_enrichment": self.suggest_threshold_adjustments("phase_5_enrichment"),
                "phase_6_bootstrap": self.suggest_threshold_adjustments("phase_6_bootstrap")
            },
            "strategy_recommendations": self._generate_strategy_recommendations(),
            "next_actions": self._generate_next_actions()
        }

    def _generate_strategy_recommendations(self) -> List[Dict[str, Any]]:
        """Generate strategy recommendations"""
        improvements = self.learner.suggest_strategy_improvements()

        recommendations = []
        for improvement in improvements[:5]:  # Top 5
            recommendations.append({
                "error_type": improvement["error_type"],
                "action": f"Replace {improvement['current_strategy']} (success rate: {improvement['success_rate']})",
                "priority": improvement["priority"]
            })

        return recommendations

    def _generate_next_actions(self) -> List[str]:
        """Generate next actions based on learning"""
        actions = []

        # Check if we have enough data for adaptation
        if self.learner.patterns:
            actions.append("Continue collecting recovery data")

        # Check for struggling strategies
        improvements = self.learner.suggest_strategy_improvements()
        if improvements:
            actions.append(f"Review and replace {len(improvements)} underperforming strategies")

        # Overall guidance
        overall_rate = self.learner._calculate_overall_success_rate()
        if overall_rate != "N/A":
            rate_float = float(overall_rate.rstrip("%"))
            if rate_float > 0.85:
                actions.append("System is performing excellently - maintain current strategies")
            elif rate_float > 0.7:
                actions.append("Good performance - continue monitoring and refining")
            else:
                actions.append("Review overall strategy selection and environment-specific adaptations")

        return actions

    def save_adaptation_plan(self, output_path: str = ".agents/orchestration/metrics/adaptation_plan.json"):
        """Save adaptation plan to file"""
        plan = self.generate_adaptation_plan()
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, 'w') as f:
            json.dump(plan, f, indent=2)

        return output_path

    def export_learned_strategies(self, output_path: str = ".agents/orchestration/metrics/learned_strategies.json"):
        """Export learned strategies for production use"""
        strategies = {}

        for pattern_key, pattern in self.learner.patterns.items():
            error_type = pattern.error_type

            if error_type not in strategies:
                strategies[error_type] = {
                    "best_strategy": None,
                    "confidence": 0.0,
                    "all_strategies": []
                }

            strategies[error_type]["all_strategies"].append(pattern.to_dict())

        # Set best strategy
        for error_type in strategies:
            best = self.learner.get_best_strategy_for_error(error_type)
            if best:
                strategies[error_type]["best_strategy"] = best[0]
                strategies[error_type]["confidence"] = best[1]

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, 'w') as f:
            json.dump(strategies, f, indent=2)

        return output_path
