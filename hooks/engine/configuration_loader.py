"""
Configuration Loader for Dynamic Hooks System
Loads and validates YAML configuration files with JSON Schema
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, List
from jsonschema import validate, ValidationError, Draft7Validator
from copy import deepcopy

class ConfigurationLoader:
    """
    Loads and merges YAML configuration files with validation
    Supports three-level hierarchy: Global > Context > Plugin
    """

    def __init__(self, config_dir: str = None):
        """
        Initialize configuration loader

        Args:
            config_dir: Directory containing YAML configs
                       Defaults to .agents/hooks/config/
        """
        if config_dir is None:
            config_dir = os.path.join(
                os.path.dirname(__file__),
                "..", "config"
            )

        self.config_dir = Path(config_dir)
        self.schema_dir = Path(config_dir).parent / "schemas"
        self.configs_cache = {}
        self.schemas_cache = {}

    def load_global_config(self) -> Dict[str, Any]:
        """Load global hooks-config.yaml"""
        return self._load_yaml_file("hooks-config.yaml", "config-schema.json")

    def load_context_config(self) -> Dict[str, Any]:
        """Load context-specific hooks-context.yaml"""
        return self._load_yaml_file("hooks-context.yaml", "config-schema.json")

    def load_plugins_config(self) -> Dict[str, Any]:
        """Load plugin registry hooks-plugins.yaml"""
        return self._load_yaml_file("hooks-plugins.yaml", "plugin-schema.json")

    def _load_yaml_file(self, yaml_filename: str, schema_filename: str) -> Dict[str, Any]:
        """
        Load YAML file and validate against JSON schema

        Args:
            yaml_filename: Name of YAML file to load
            schema_filename: Name of JSON schema for validation

        Returns:
            Parsed and validated configuration dictionary

        Raises:
            FileNotFoundError: If file not found
            ValidationError: If validation fails
            yaml.YAMLError: If YAML parsing fails
        """
        # Check cache first
        if yaml_filename in self.configs_cache:
            return self.configs_cache[yaml_filename]

        yaml_path = self.config_dir / yaml_filename
        schema_path = self.schema_dir / schema_filename

        # Load YAML
        if not yaml_path.exists():
            raise FileNotFoundError(f"Config file not found: {yaml_path}")

        with open(yaml_path, 'r') as f:
            try:
                config = yaml.safe_load(f) or {}
            except yaml.YAMLError as e:
                raise yaml.YAMLError(f"Invalid YAML in {yaml_filename}: {e}")

        # Load and validate schema
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_path}")

        with open(schema_path, 'r') as f:
            schema = json.load(f)

        # Validate config against schema
        try:
            validate(instance=config, schema=schema)
        except ValidationError as e:
            raise ValidationError(
                f"Configuration validation failed in {yaml_filename}: {e.message}",
                instance=e.instance
            )

        # Cache result
        self.configs_cache[yaml_filename] = config
        return config

    def merge_configurations(
        self,
        global_config: Dict[str, Any],
        context_config: Dict[str, Any],
        context_name: str,
        plugin_config: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Merge three-level configuration hierarchy

        Order of precedence (highest to lowest):
        1. Plugin-specific config
        2. Context-specific config
        3. Global config

        Args:
            global_config: Global defaults
            context_config: Context-specific overrides
            context_name: Name of context to apply
            plugin_config: Plugin-specific overrides (optional)

        Returns:
            Merged effective configuration
        """
        # Start with global config (deep copy to avoid mutations)
        effective = deepcopy(global_config)

        # Apply context-specific overrides
        if context_name in context_config.get("contexts", {}):
            context = context_config["contexts"][context_name]
            effective = self._deep_merge(effective, context)

        # Apply environment-specific overrides if applicable
        env = os.getenv("HOOKS_ENVIRONMENT")
        if env and env in context_config.get("environments", {}):
            env_config = context_config["environments"][env]
            effective = self._deep_merge(effective, env_config)

        # Apply plugin-specific overrides if provided
        if plugin_config:
            effective = self._deep_merge(effective, plugin_config)

        return effective

    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep merge two dictionaries
        override takes precedence over base

        Args:
            base: Base dictionary
            override: Dictionary with overrides

        Returns:
            Merged dictionary
        """
        result = deepcopy(base)

        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge dicts
                result[key] = self._deep_merge(result[key], value)
            else:
                # Override with new value
                result[key] = deepcopy(value)

        return result

    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate that configuration is internally consistent

        Args:
            config: Configuration to validate

        Returns:
            True if valid, raises exception if not
        """
        errors = []

        # Check gate thresholds are in logical order
        gates = config.get("gates", {})

        for gate_name, gate_config in gates.items():
            if "min_length" in gate_config and "max_length" in gate_config:
                if gate_config["min_length"] > gate_config["max_length"]:
                    errors.append(
                        f"Gate {gate_name}: min_length > max_length is invalid"
                    )

            if "min_bytes" in gate_config and "max_bytes" in gate_config:
                if gate_config["min_bytes"] > gate_config["max_bytes"]:
                    errors.append(
                        f"Gate {gate_name}: min_bytes > max_bytes is invalid"
                    )

        if errors:
            raise ValueError("Configuration validation failed:\n" + "\n".join(errors))

        return True

    def get_gate_threshold(
        self,
        config: Dict[str, Any],
        gate_name: str,
        threshold_key: str,
        default: Any = None
    ) -> Any:
        """
        Get threshold value for a specific gate, with fallback to default

        Args:
            config: Configuration dictionary
            gate_name: Name of gate (e.g., 'description')
            threshold_key: Key within gate config (e.g., 'min_length')
            default: Default value if not found

        Returns:
            Threshold value or default
        """
        gates = config.get("gates", {})
        gate = gates.get(gate_name, {})
        return gate.get(threshold_key, default)

    def get_validation_mode(self, config: Dict[str, Any], mode_name: str) -> Dict[str, Any]:
        """
        Get validation mode configuration

        Args:
            config: Configuration dictionary
            mode_name: Name of validation mode (strict, lenient, experimental)

        Returns:
            Validation mode configuration
        """
        modes = config.get("validation_modes", {})
        return modes.get(mode_name, {})

    def clear_cache(self):
        """Clear configuration cache (useful for testing)"""
        self.configs_cache.clear()
        self.schemas_cache.clear()


class ConfigurationValidator:
    """
    Static helper class for configuration validation
    """

    @staticmethod
    def validate_gate_number(gate_num: int) -> bool:
        """Validate gate number is 1-8"""
        return 1 <= gate_num <= 8

    @staticmethod
    def validate_mode(mode: str) -> bool:
        """Validate validation mode"""
        return mode in ["strict", "lenient", "experimental"]

    @staticmethod
    def validate_phase(phase: int) -> bool:
        """Validate phase number"""
        return 1 <= phase <= 7

    @staticmethod
    def validate_domain(domain: str, approved_domains: List[str]) -> bool:
        """Validate domain is in approved list"""
        return domain in approved_domains
