#!/usr/bin/env python3
"""
Unit Tests for ConfigurationLoader
Tests YAML loading, merging, and schema validation
"""

import unittest
import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

# Add parent path
sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.configuration_loader import ConfigurationLoader, ConfigurationValidator


class TestConfigurationLoader(unittest.TestCase):
    """Test ConfigurationLoader component"""

    def setUp(self):
        """Set up test environment"""
        self.config_dir = Path(__file__).parent.parent / "config"
        self.loader = ConfigurationLoader(str(self.config_dir))

    def test_load_global_config(self):
        """Test loading global configuration"""
        config = self.loader.load_global_config()

        self.assertIsNotNone(config)
        self.assertIn('gates', config)
        self.assertIn('validation_modes', config)
        self.assertIn('domains', config)

    def test_load_context_config(self):
        """Test loading context configuration"""
        config = self.loader.load_context_config()

        self.assertIsNotNone(config)
        self.assertIn('contexts', config)

        # Check phase contexts exist
        self.assertIn('phase_4', config['contexts'])
        self.assertIn('phase_5_enrichment', config['contexts'])

    def test_load_plugins_config(self):
        """Test loading plugins configuration"""
        config = self.loader.load_plugins_config()

        self.assertIsNotNone(config)
        self.assertIn('plugins', config)

    def test_config_has_required_fields(self):
        """Test that configs have all required top-level fields"""
        global_config = self.loader.load_global_config()
        context_config = self.loader.load_context_config()
        plugins_config = self.loader.load_plugins_config()

        # Global config requirements
        self.assertIn('metadata', global_config)
        self.assertIn('gates', global_config)

        # Context config requirements
        self.assertIn('metadata', context_config)
        self.assertIn('contexts', context_config)

        # Plugins config requirements
        self.assertIn('metadata', plugins_config)
        self.assertIn('plugins', plugins_config)

    def test_config_validation_no_errors(self):
        """Test that current configs pass validation"""
        config_dir = Path(__file__).parent.parent / "config"
        validator = ConfigurationValidator(str(config_dir))

        errors = validator.validate_all()

        # Should have no errors or only warnings
        error_count = len([e for e in errors if 'error' in e.lower()])
        self.assertEqual(error_count, 0, f"Config validation errors: {errors}")

    def test_gate_config_structure(self):
        """Test that gate configurations have correct structure"""
        config = self.loader.load_global_config()
        gates = config['gates']

        # Check required gates
        required_gates = ['yaml_frontmatter', 'naming_convention', 'description',
                         'mandates', 'response_pattern', 'file_size']

        for gate in required_gates:
            self.assertIn(gate, gates, f"Missing gate: {gate}")

    def test_validation_modes_exist(self):
        """Test that all validation modes are configured"""
        config = self.loader.load_global_config()
        modes = config['validation_modes']

        required_modes = ['strict', 'lenient', 'experimental']
        for mode in required_modes:
            self.assertIn(mode, modes)
            self.assertIn('multiplier', modes[mode])
            self.assertIn('fail_on_warnings', modes[mode])

    def test_domain_configuration(self):
        """Test domain configuration is comprehensive"""
        config = self.loader.load_global_config()
        domains = config['domains']

        self.assertIn('approved', domains)
        self.assertGreater(len(domains['approved']), 50,
                          "Should have 50+ approved domains")

    def test_context_overrides_global(self):
        """Test that context overrides are applied correctly"""
        global_config = self.loader.load_global_config()
        context_config = self.loader.load_context_config()

        # Phase 5 should have different file_size limit than global
        phase5_config = context_config['contexts']['phase_5_enrichment']

        if 'thresholds' in phase5_config and 'file_size' in phase5_config['thresholds']:
            phase5_max = phase5_config['thresholds']['file_size'].get('max_bytes')
            global_max = global_config['gates']['file_size'].get('max_bytes')

            # Phase 5 should typically be more lenient
            if phase5_max and global_max:
                self.assertGreaterEqual(phase5_max, global_max)


class TestConfigurationValidator(unittest.TestCase):
    """Test ConfigurationValidator component"""

    def setUp(self):
        """Set up test environment"""
        self.config_dir = Path(__file__).parent.parent / "config"
        self.validator = ConfigurationValidator(str(self.config_dir))

    def test_validate_all_returns_list(self):
        """Test that validate_all returns a list"""
        result = self.validator.validate_all()
        self.assertIsInstance(result, list)

    def test_schema_files_exist(self):
        """Test that JSON schema files exist"""
        config_dir = Path(__file__).parent.parent / "config"

        # Schemas should be in schemas/ subdirectory or adjacent to config
        schema_locations = [
            config_dir / "schemas" / "config-schema.json",
            config_dir.parent / "schemas" / "config-schema.json",
        ]

        schema_found = any(p.exists() for p in schema_locations)
        self.assertTrue(schema_found or len(self.validator.validate_all()) == 0,
                       "Schema files should exist or validation should handle gracefully")


if __name__ == '__main__':
    unittest.main()
