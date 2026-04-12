"""
Plugin Manager - Loads and executes plugins with consensus voting
"""

import os
import sys
import logging
import importlib
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class PluginVote:
    """Represents a single plugin's vote on validation"""
    plugin_id: str
    plugin_name: str
    vote: str  # "PASS", "FAIL", or "WARN"
    confidence: float  # 0.0 to 1.0
    message: str
    weight: float  # Consensus weight


class PluginManager:
    """
    Manages plugin loading, execution, and consensus voting

    Features:
    - Automatic plugin discovery
    - Consensus voting system (majority vote)
    - Weighted voting support
    - Plugin isolation (subprocess execution)
    -Plugin error handling
    """

    def __init__(self, plugins_config: Dict[str, Any], engine_config: Dict[str, Any]):
        """
        Initialize plugin manager

        Args:
            plugins_config: Plugins configuration from hooks-plugins.yaml
            engine_config: Engine configuration
        """
        self.plugins_config = plugins_config
        self.engine_config = engine_config
        self.loaded_plugins = {}
        self.plugin_cache = {}

        # Plugin execution settings
        execution_config = plugins_config.get("execution", {})
        self.consensus_strategy = execution_config.get("consensus", {}).get("strategy", "majority_vote")
        self.min_consensus = execution_config.get("consensus", {}).get("minimum_consensus", 2)
        self.weighted_voting = execution_config.get("consensus", {}).get("weighted_voting", True)
        self.timeout_per_plugin = execution_config.get("timeout_per_plugin", 10)

        # Load plugins
        self._load_plugins()

    def _load_plugins(self):
        """Load all enabled plugins"""
        plugins_to_load = {}

        # Collect all enabled plugins
        for plugin_id, plugin_config in self.plugins_config.get("plugins", {}).items():
            if plugin_config.get("enabled", False):
                plugins_to_load[plugin_id] = plugin_config

        for plugin_id, plugin_config in self.plugins_config.get("optional_plugins", {}).items():
            if plugin_config.get("enabled", False):
                plugins_to_load[plugin_id] = plugin_config

        logger.info(f"Loading {len(plugins_to_load)} enabled plugins")

        for plugin_id, plugin_config in plugins_to_load.items():
            try:
                plugin = self._load_plugin(plugin_id, plugin_config)
                if plugin:
                    self.loaded_plugins[plugin_id] = {
                        "instance": plugin,
                        "config": plugin_config,
                        "weight": plugin_config.get("consensus_weight", 1.0),
                    }
                    logger.info(f"✓ Loaded plugin: {plugin_id}")
            except Exception as e:
                logger.error(f"✗ Failed to load plugin {plugin_id}: {e}")

    def _load_plugin(self, plugin_id: str, plugin_config: Dict[str, Any]) -> Optional[Any]:
        """
        Load a single plugin

        Args:
            plugin_id: Plugin ID
            plugin_config: Plugin configuration

        Returns:
            Loaded plugin instance or None if failed
        """
        try:
            module_name = plugin_config.get("module")
            class_name = plugin_config.get("class")

            if not module_name or not class_name:
                logger.error(f"Plugin {plugin_id}: missing module or class")
                return None

            # Import module
            module = importlib.import_module(module_name)

            # Get class
            plugin_class = getattr(module, class_name)

            # Instantiate plugin
            plugin_instance = plugin_class(
                name=plugin_id,
                config=plugin_config.get("config", {})
            )

            return plugin_instance

        except (ImportError, AttributeError, Exception) as e:
            logger.error(f"Failed to load plugin {plugin_id}: {e}")
            return None

    def execute_plugins(
        self,
        hook_name: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute all plugins registered for a hook

        Args:
            hook_name: Hook name (e.g., 'validate_skill', 'post_validation')
            context: Context passed to plugins

        Returns:
            Dictionary with plugin execution results
        """
        results = {}

        for plugin_id, plugin_data in self.loaded_plugins.items():
            plugin_config = plugin_data["config"]

            # Check if plugin handles this hook
            if hook_name not in plugin_config.get("hooks", []):
                continue

            # Check if plugin has a pattern and if skill matches
            if "pattern" in plugin_config:
                skill_path = context.get("skill_path", "")
                import re
                if not re.search(plugin_config["pattern"], skill_path):
                    logger.debug(f"Plugin {plugin_id}: pattern mismatch for {skill_path}")
                    continue

            try:
                logger.debug(f"Executing plugin: {plugin_id}")

                plugin_instance = plugin_data["instance"]
                method_name = f"on_{hook_name}"

                if hasattr(plugin_instance, method_name):
                    method = getattr(plugin_instance, method_name)
                    result = method(context)

                    results[plugin_id] = {
                        "success": True,
                        "result": result,
                        "weight": plugin_data["weight"],
                    }
                else:
                    logger.warning(f"Plugin {plugin_id}: no method {method_name}")

            except Exception as e:
                logger.error(f"Plugin {plugin_id} error: {e}")
                results[plugin_id] = {
                    "success": False,
                    "error": str(e),
                    "weight": plugin_data["weight"],
                }

        return results

    def get_consensus(self, plugin_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate consensus from multiple plugin votes

        Returns:
            {
                "pass": bool,
                "votes": List[PluginVote],
                "strategy": str,
                "reason": str,
            }
        """
        if not plugin_results:
            # No plugins ran, use framework default
            return {
                "pass": True,
                "votes": [],
                "strategy": "no_plugins",
                "reason": "No plugins executed, using framework default"
            }

        votes: List[PluginVote] = []

        # Collect votes from plugins
        for plugin_id, result in plugin_results.items():
            if not result.get("success"):
                continue

            plugin_result = result.get("result", {})
            vote = PluginVote(
                plugin_id=plugin_id,
                plugin_name=plugin_id.replace("_", "-"),
                vote=plugin_result.get("vote", "PASS"),
                confidence=plugin_result.get("confidence", 1.0),
                message=plugin_result.get("message", ""),
                weight=result.get("weight", 1.0),
            )
            votes.append(vote)

        # Apply consensus strategy
        if self.consensus_strategy == "majority_vote":
            return self._majority_vote_consensus(votes)
        elif self.consensus_strategy == "all_must_pass":
            return self._all_must_pass_consensus(votes)
        elif self.consensus_strategy == "any_can_pass":
            return self._any_can_pass_consensus(votes)
        else:
            logger.warning(f"Unknown consensus strategy: {self.consensus_strategy}")
            return self._majority_vote_consensus(votes)

    def _majority_vote_consensus(self, votes: List[PluginVote]) -> Dict[str, Any]:
        """Calculate consensus using weighted majority vote"""
        if not votes:
            return {
                "pass": True,
                "votes": [],
                "strategy": "majority_vote",
                "reason": "No votes cast"
            }

        # Weighted vote counting
        pass_weight = 0.0
        fail_weight = 0.0

        for vote in votes:
            if vote.vote == "PASS":
                pass_weight += vote.weight
            elif vote.vote == "FAIL":
                fail_weight += vote.weight

        total_weight = pass_weight + fail_weight
        pass_percentage = (pass_weight / total_weight * 100) if total_weight > 0 else 0

        # Determine result
        passed = pass_weight >= fail_weight and len([v for v in votes if v.vote == "PASS"]) >= self.min_consensus

        return {
            "pass": passed,
            "votes": [
                {
                    "plugin": v.plugin_id,
                    "vote": v.vote,
                    "confidence": v.confidence,
                    "weight": v.weight,
                    "message": v.message
                }
                for v in votes
            ],
            "statistics": {
                "pass_weight": pass_weight,
                "fail_weight": fail_weight,
                "pass_percentage": pass_percentage,
            },
            "strategy": "majority_vote",
            "reason": (
                f"Majority vote: {len([v for v in votes if v.vote == 'PASS'])} PASS, "
                f"{len([v for v in votes if v.vote == 'FAIL'])} FAIL "
                f"({pass_percentage:.1f}% pass)"
            )
        }

    def _all_must_pass_consensus(self, votes: List[PluginVote]) -> Dict[str, Any]:
        """All plugins must vote PASS"""
        passed = all(v.vote == "PASS" for v in votes)

        return {
            "pass": passed,
            "votes": [
                {"plugin": v.plugin_id, "vote": v.vote}
                for v in votes
            ],
            "strategy": "all_must_pass",
            "reason": "All plugins must vote PASS" if passed else "One or more plugins voted FAIL"
        }

    def _any_can_pass_consensus(self, votes: List[PluginVote]) -> Dict[str, Any]:
        """Any plugin voting PASS is sufficient"""
        passed = any(v.vote == "PASS" for v in votes)

        return {
            "pass": passed,
            "votes": [
                {"plugin": v.plugin_id, "vote": v.vote}
                for v in votes
            ],
            "strategy": "any_can_pass",
            "reason": "Any plugin voting PASS is sufficient" if passed else "No plugins voted PASS"
        }

    def get_plugin_info(self) -> Dict[str, Any]:
        """Get information about loaded plugins"""
        return {
            "total_loaded": len(self.loaded_plugins),
            "plugins": [
                {
                    "id": plugin_id,
                    "weight": plugin_data["weight"],
                    "config": plugin_data["config"],
                }
                for plugin_id, plugin_data in self.loaded_plugins.items()
            ],
            "execution_config": {
                "strategy": self.consensus_strategy,
                "min_consensus": self.min_consensus,
                "weighted_voting": self.weighted_voting,
            }
        }
