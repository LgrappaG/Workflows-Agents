"""
Main Dynamic Hooks Engine
Orchestrates configuration loading, context detection, and validation execution
"""

import os
import logging
from typing import Dict, Any, List, Optional
from pathlib import Path
from datetime import datetime

from .configuration_loader import ConfigurationLoader, ConfigurationValidator
from .context_resolver import ContextResolver, EnvironmentInfo
from .plugin_manager import PluginManager
from .learning_engine import LearningEngine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DynamicHooksEngine:
    """
    Main orchestrator for the dynamic hooks validation system

    Features:
    - Load and merge three-level configuration hierarchy (Global > Context > Plugin)
    - Auto-detect current phase and environment
    - Execute validation with dynamic gates and plugins
    - Track metrics for learning/adaptation
    - Generate performance reports and suggestions
    """

    def __init__(self, config_dir: str = None, skip_plugin_loading: bool = False):
        """
        Initialize Dynamic Hooks Engine

        Args:
            config_dir: Directory containing YAML configs
                       Defaults to .agents/hooks/config/
            skip_plugin_loading: If True, skip loading plugins (for testing)
        """
        self.config_dir = config_dir
        self.start_time = datetime.now()

        # Initialize components
        logger.debug("Initializing DynamicHooksEngine components...")

        self.config_loader = ConfigurationLoader(config_dir)
        self.context_resolver = ContextResolver()
        self.learning_engine = LearningEngine()
        self.plugin_manager = None

        # Load configurations
        logger.debug("Loading configuration files...")
        self.global_config = self.config_loader.load_global_config()
        self.context_config = self.config_loader.load_context_config()
        self.plugins_config = self.config_loader.load_plugins_config()

        # Resolve current context
        logger.debug("Detecting context...")
        self.current_context = self.context_resolver.resolve()
        self.current_environment = self.context_resolver.detect_environment()

        # Merge configurations
        logger.debug(f"Merging configurations for context: {self.current_context}")
        self.effective_config = self.config_loader.merge_configurations(
            self.global_config,
            self.context_config,
            self.current_context,
            plugin_config=self.plugins_config.get("execution", {})
        )

        # Validate merged config
        try:
            self.config_loader.validate_config(self.effective_config)
            logger.info("Configuration validation successful")
        except ValueError as e:
            logger.error(f"Configuration validation failed: {e}")
            raise

        # Initialize plugin manager
        if not skip_plugin_loading:
            logger.debug("Initializing plugin manager...")
            self.plugin_manager = PluginManager(
                self.plugins_config,
                self.effective_config
            )

        logger.info(
            f"DynamicHooksEngine initialized (context={self.current_context}, "
            f"mode={self._get_validation_mode()})"
        )

    def validate_skill(self, skill_path: str, gates: Optional[List[int]] = None) -> Dict[str, Any]:
        """
        Validate a skill file through all dynamic gates

        Args:
            skill_path: Path to skill SKILL.md file
            gates: Specific gate numbers to run (default: all enabled gates)

        Returns:
            Validation result dictionary containing:
            - pass: bool - Overall pass/fail
            - gates: Dict[int, Dict] - Individual gate results
            - plugins: Dict[str, Dict] - Plugin validation results
            - summary: str - Human-readable summary
        """
        logger.info(f"Validating skill: {skill_path}")

        if not Path(skill_path).exists():
            logger.error(f"Skill file not found: {skill_path}")
            return {"pass": False, "error": f"File not found: {skill_path}"}

        # Determine which gates to run
        enabled_gates = self.effective_config.get("enabling_gates", [1, 2, 3, 4, 5, 6, 7, 8])
        gates_to_run = gates or enabled_gates

        results = {
            "pass": True,
            "skill": skill_path,
            "timestamp": datetime.now().isoformat(),
            "context": self.current_context,
            "mode": self._get_validation_mode(),
            "gates": {},
            "plugins": {},
            "warnings": [],
            "errors": [],
        }

        # Run validation gates
        logger.debug(f"Running gates: {gates_to_run}")
        for gate_num in gates_to_run:
            gate_result = self._run_gate(gate_num, skill_path)
            results["gates"][gate_num] = gate_result

            if not gate_result.get("pass"):
                results["pass"] = False
                results["errors"].append(gate_result.get("message", f"Gate {gate_num} failed"))

        # Run plugins if available
        if self.plugin_manager:
            logger.debug("Running plugins...")
            plugin_results = self.plugin_manager.execute_plugins("validate_skill", {
                "skill_path": skill_path,
                "gate_results": results["gates"]
            })
            results["plugins"] = plugin_results

            # Check consensus voting
            consensus_verdict = self.plugin_manager.get_consensus(plugin_results)
            if not consensus_verdict["pass"]:
                results["pass"] = False
                results["warnings"].append(f"Plugins consensus: {consensus_verdict['reason']}")

        # Track metrics for learning
        self.learning_engine.track_validation(skill_path, results)

        # Generate summary
        results["summary"] = self._generate_summary(results)

        logger.info(f"Validation {'PASSED' if results['pass'] else 'FAILED'}: {skill_path}")
        return results

    def _run_gate(self, gate_num: int, skill_path: str) -> Dict[str, Any]:
        """
        Run a single validation gate

        Args:
            gate_num: Gate number (1-8)
            skill_path: Path to skill file

        Returns:
            Gate validation result
        """
        if not ConfigurationValidator.validate_gate_number(gate_num):
            return {
                "pass": False,
                "message": f"Invalid gate number: {gate_num}"
            }

        # Map gate numbers to gate names
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

        gate_name = gate_names.get(gate_num, f"unknown_gate_{gate_num}")
        gate_config = self.effective_config.get("gates", {}).get(gate_name, {})

        # Placeholder: In Phase 3, this will call DynamicGateValidator
        # For now, return a basic structure
        return {
            "pass": True,
            "gate": gate_num,
            "name": gate_name,
            "config": gate_config,
            "message": f"Gate {gate_num} validation placeholder"
        }

    def get_effective_config(self) -> Dict[str, Any]:
        """
        Get merged effective configuration

        Returns:
            Effective configuration used for validation
        """
        return self.effective_config

    def get_threshold(self, gate_name: str, threshold_key: str, default: Any = None) -> Any:
        """
        Get a specific threshold value with context applied

        Args:
            gate_name: Name of gate (e.g., 'description')
            threshold_key: Key within gate (e.g., 'min_length')
            default: Default value if not found

        Returns:
            Threshold value or default
        """
        return self.config_loader.get_gate_threshold(
            self.effective_config,
            gate_name,
            threshold_key,
            default
        )

    def get_context_info(self) -> Dict[str, Any]:
        """
        Get detailed context detection information

        Returns:
            Dictionary with context, environment, and detection method
        """
        return {
            "context": self.current_context,
            "environment": self.current_environment,
            "mode": self._get_validation_mode(),
            "detection_info": self.context_resolver.get_detection_info(),
            "enabled_gates": self.effective_config.get("enabled_gates", [1, 2, 3, 4, 5, 6, 7, 8]),
        }

    def get_learning_suggestions(self) -> Dict[str, Any]:
        """
        Get learning engine suggestions based on validation history

        Returns:
            Dictionary with suggested rule optimizations
        """
        return self.learning_engine.suggest_optimizations()

    def _get_validation_mode(self) -> str:
        """Get current validation mode"""
        # Extract from context configuration
        context_name = self.current_context
        contexts = self.context_config.get("contexts", {})

        if context_name in contexts:
            return contexts[context_name].get("validation_mode", "strict")

        return "strict"  # Default

    def _generate_summary(self, results: Dict[str, Any]) -> str:
        """Generate human-readable validation summary"""
        passed = sum(1 for g in results["gates"].values() if g.get("pass", False))
        total = len(results["gates"])

        return (
            f"Validation {'PASSED' if results['pass'] else 'FAILED'} "
            f"({passed}/{total} gates). "
            f"Mode: {results['mode']}, Context: {results['context']}"
        )

    def reload_config(self):
        """Reload configuration files (clears cache)"""
        logger.info("Reloading configuration...")
        self.config_loader.clear_cache()
        self.context_resolver.clear_cache()

        self.global_config = self.config_loader.load_global_config()
        self.context_config = self.config_loader.load_context_config()
        self.plugins_config = self.config_loader.load_plugins_config()

        logger.info("Configuration reloaded successfully")

    def __repr__(self) -> str:
        return (
            f"DynamicHooksEngine(context={self.current_context}, "
            f"mode={self._get_validation_mode()}, "
            f"uptime={(datetime.now() - self.start_time).total_seconds():.1f}s)"
        )


def create_engine(config_dir: str = None) -> DynamicHooksEngine:
    """
    Factory function to create and initialize a DynamicHooksEngine

    Args:
        config_dir: Optional config directory

    Returns:
        Initialized DynamicHooksEngine instance
    """
    return DynamicHooksEngine(config_dir)
