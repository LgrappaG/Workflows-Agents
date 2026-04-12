"""
Learning Engine - Tracks validation metrics and suggests rule optimizations
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from collections import defaultdict, Counter

logger = logging.getLogger(__name__)


class LearningEngine:
    """
    Tracks validation metrics and provides adaptive suggestions

    Features:
    - Historical validation tracking
    - Per-gate failure analysis
    - Threshold optimization suggestions
    - Trend analysis
    - Report-only mode (no auto-modifications)
    """

    def __init__(self, metrics_file: str = None):
        """
        Initialize learning engine

        Args:
            metrics_file: Path to validation metrics JSON file
                         Defaults to .agents/hooks/metrics/validation_metrics.json
        """
        if metrics_file is None:
            metrics_file = Path(__file__).parent.parent / "metrics" / "validation_metrics.json"

        self.metrics_file = Path(metrics_file)
        self.metrics_file.parent.mkdir(parents=True, exist_ok=True)

        self.metrics = self._load_metrics()
        self.suggestions_cache = {}

    def track_validation(self, skill_path: str, validation_result: Dict[str, Any]):
        """
        Track a validation result for learning

        Args:
            skill_path: Path to skill being validated
            validation_result: Complete validation result dictionary
        """
        record = {
            "timestamp": datetime.now().isoformat(),
            "skill": skill_path,
            "passed": validation_result.get("pass", False),
            "context": validation_result.get("context"),
            "mode": validation_result.get("mode"),
            "gates": {},
            "plugins": validation_result.get("plugins", {}),
        }

        # Extract gate results
        for gate_num, gate_result in validation_result.get("gates", {}).items():
            record["gates"][str(gate_num)] = {
                "pass": gate_result.get("pass", False),
                "name": gate_result.get("name"),
                "message": gate_result.get("message"),
            }

        # Add to metrics
        if "validations" not in self.metrics:
            self.metrics["validations"] = []

        self.metrics["validations"].append(record)

        # Save metrics
        self._save_metrics()

        logger.info(f"Tracked validation for: {skill_path}")

    def suggest_optimizations(self) -> Dict[str, Any]:
        """
        Analyze validation history and suggest rule optimizations

        Returns:
            {
                "suggested_changes": [
                    {
                        "gate": "response",
                        "threshold": "max_steps",
                        "current_value": 4,
                        "suggested_value": 5,
                        "reason": "95% of skills exceed current limit",
                        "confidence": 0.92
                    }
                ],
                "gate_statistics": {...},
                "trends": {...},
                "report_timestamp": "2026-04-12T..."
            }
        """
        if not self.metrics.get("validations"):
            return {
                "suggested_changes": [],
                "gate_statistics": {},
                "reason": "Insufficient data for suggestions"
            }

        suggestions = {
            "suggested_changes": [],
            "gate_statistics": self._analyze_gate_failures(),
            "trends": self._analyze_trends(),
            "report_timestamp": datetime.now().isoformat(),
            "total_validations": len(self.metrics.get("validations", [])),
        }

        # Analyze each gate for potential optimizations
        gate_stats = suggestions["gate_statistics"]

        for gate_name, stats in gate_stats.items():
            if stats["fail_rate"] > 0.5:  # Gate failing >50%
                suggestion = self._suggest_gate_optimization(gate_name, stats)
                if suggestion:
                    suggestions["suggested_changes"].append(suggestion)

        return suggestions

    def _analyze_gate_failures(self) -> Dict[str, Dict[str, Any]]:
        """Analyze failure rates per gate"""
        gate_stats = defaultdict(lambda: {
            "passed": 0,
            "failed": 0,
            "fail_rate": 0.0,
            "trends": []
        })

        for validation in self.metrics.get("validations", []):
            for gate_num_str, gate_result in validation.get("gates", {}).items():
                gate_name = self._get_gate_name(int(gate_num_str))

                if gate_result.get("pass"):
                    gate_stats[gate_name]["passed"] += 1
                else:
                    gate_stats[gate_name]["failed"] += 1

        # Calculate fail rates
        for gate_name, stats in gate_stats.items():
            total = stats["passed"] + stats["failed"]
            if total > 0:
                stats["fail_rate"] = stats["failed"] / total
            else:
                stats["fail_rate"] = 0.0

        return dict(gate_stats)

    def _analyze_trends(self) -> Dict[str, Any]:
        """Analyze validation trends over time"""
        if not self.metrics.get("validations"):
            return {}

        # Group by day
        daily_stats = defaultdict(lambda: {"passed": 0, "failed": 0})

        for validation in self.metrics["validations"]:
            timestamp_str = validation.get("timestamp", "")
            if not timestamp_str:
                continue

            date = timestamp_str.split("T")[0]
            if validation.get("passed"):
                daily_stats[date]["passed"] += 1
            else:
                daily_stats[date]["failed"] += 1

        # Calculate pass rate trend
        trends = {
            "by_day": dict(daily_stats),
            "overall_pass_rate": self._calculate_overall_pass_rate(),
            "improvement_over_time": self._calculate_improvement_trend(),
        }

        return trends

    def _suggest_gate_optimization(
        self,
        gate_name: str,
        stats: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Suggest optimization for a specific gate"""
        fail_rate = stats.get("fail_rate", 0)

        # Only suggest if fail rate is significant
        if fail_rate < 0.2:
            return None

        return {
            "gate": gate_name,
            "current_fail_rate": fail_rate,
            "suggestion": f"Gate {gate_name} is failing {fail_rate*100:.1f}% of validations",
            "action": "review_threshold",
            "confidence": min(fail_rate, 1.0),
            "recommendation": self._get_gate_recommendation(gate_name, fail_rate)
        }

    def _get_gate_recommendation(self, gate_name: str, fail_rate: float) -> str:
        """Get human-readable recommendation for a gate"""
        recommendations = {
            "yaml_frontmatter": "Ensure all 9 required YAML fields are present and properly formatted.",
            "naming_convention": "Skill names must follow {domain}-{specialty} pattern with valid domains.",
            "description": "Description should be 50-100 characters and action-oriented. Consider relaxing limits.",
            "risk_level": "Review risk level assignments. Consider complexity of actual skills.",
            "mandates": "Mandates must be specific and actionable. Current limit may be too strict.",
            "response": "Response steps should be concrete and sequenced. Consider increasing max steps.",
            "file_size": "File size limit may be too restrictive. Phase 5+ may need 1500+ bytes.",
            "cross_skill_consistency": "Ensure consistency patterns are appropriate for current phase.",
        }

        return recommendations.get(
            gate_name,
            f"Review {gate_name} validation threshold based on {fail_rate*100:.1f}% fail rate"
        )

    def _get_gate_name(self, gate_num: int) -> str:
        """Map gate number to gate name"""
        gate_names = {
            1: "yaml_frontmatter",
            2: "naming_convention",
            3: "description",
            4: "risk_level",
            5: "mandates",
            6: "response",
            7: "file_size",
            8: "cross_skill_consistency",
        }
        return gate_names.get(gate_num, f"gate_{gate_num}")

    def _calculate_overall_pass_rate(self) -> float:
        """Calculate overall validation pass rate"""
        validations = self.metrics.get("validations", [])
        if not validations:
            return 0.0

        passed = sum(1 for v in validations if v.get("passed"))
        return passed / len(validations)

    def _calculate_improvement_trend(self) -> str:
        """Calculate if pass rate is improving over time"""
        validations = self.metrics.get("validations", [])
        if len(validations) < 10:
            return "insufficient_data"

        # Compare first half vs second half
        midpoint = len(validations) // 2
        first_half = sum(1 for v in validations[:midpoint] if v.get("passed")) / midpoint
        second_half = sum(1 for v in validations[midpoint:] if v.get("passed")) / (len(validations) - midpoint)

        if second_half > first_half:
            return "improving"
        elif second_half < first_half:
            return "degrading"
        else:
            return "stable"

    def _load_metrics(self) -> Dict[str, Any]:
        """Load metrics from JSON file"""
        if not self.metrics_file.exists():
            return {"validations": []}

        try:
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load metrics: {e}")
            return {"validations": []}

    def _save_metrics(self):
        """Save metrics to JSON file"""
        try:
            with open(self.metrics_file, 'w') as f:
                json.dump(self.metrics, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save metrics: {e}")

    def export_report(self, output_path: str = None) -> str:
        """
        Export learning analysis as human-readable report

        Args:
            output_path: Optional path to save report

        Returns:
            Report text
        """
        suggestions = self.suggest_optimizations()

        report = f"""
╔══════════════════════════════════════════════════════════════════╗
║            VALIDATION LEARNING & OPTIMIZATION REPORT             ║
╚══════════════════════════════════════════════════════════════════╝

Generated: {suggestions['report_timestamp']}
Total Validations Analyzed: {suggestions['total_validations']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GATE STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
        for gate_name, stats in suggestions.get("gate_statistics", {}).items():
            report += f"\n{gate_name}:\n"
            report += f"  Pass Rate: {(1-stats['fail_rate'])*100:.1f}%\n"
            report += f"  Passed: {stats['passed']}, Failed: {stats['failed']}\n"

        report += f"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        report += "SUGGESTED OPTIMIZATIONS\n"
        report += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        if suggestions.get("suggested_changes"):
            for i, change in enumerate(suggestions["suggested_changes"], 1):
                report += f"\n{i}. {change.get('gate')}\n"
                report += f"   {change.get('recommendation')}\n"
                report += f"   Confidence: {change.get('confidence', 0)*100:.0f}%\n"
        else:
            report += "\nNo suggested optimizations at this time.\n"

        if output_path:
            Path(output_path).write_text(report)
            logger.info(f"Report saved to: {output_path}")

        return report

    def clear_old_metrics(self, days_to_keep: int = 30):
        """
        Clear metrics older than specified days

        Args:
            days_to_keep: Number of days to retain
        """
        cutoff_date = datetime.now() - timedelta(days=days_to_keep)

        validations = self.metrics.get("validations", [])
        kept = [
            v for v in validations
            if datetime.fromisoformat(v.get("timestamp", "")) > cutoff_date
        ]

        logger.info(f"Clearing old metrics: kept {len(kept)}/{len(validations)} records")
        self.metrics["validations"] = kept
        self._save_metrics()
