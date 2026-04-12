#!/usr/bin/env python3
"""
Integration Tests for DynamicHooksEngine
Tests complete validation workflows and context handling
"""

import unittest
import sys
from pathlib import Path
import os

# Add parent path
sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.dynamic_hooks_engine import DynamicHooksEngine
from engine.context_resolver import ContextResolver


class TestDynamicHooksEngine(unittest.TestCase):
    """Test DynamicHooksEngine integration"""

    def setUp(self):
        """Set up test environment"""
        self.config_dir = str(Path(__file__).parent.parent / "config")
        self.engine = DynamicHooksEngine(config_dir=self.config_dir, skip_plugin_loading=True)

    def test_engine_initialization(self):
        """Test that engine initializes without errors"""
        self.assertIsNotNone(self.engine)
        self.assertIsNotNone(self.engine.global_config)
        self.assertIsNotNone(self.engine.context_config)
        self.assertIsNotNone(self.engine.plugins_config)

    def test_get_effective_config_strict(self):
        """Test getting effective config for strict mode"""
        os.environ['HOOKS_CONTEXT'] = 'phase_4'

        engine = DynamicHooksEngine(config_dir=self.config_dir, skip_plugin_loading=True)
        effective_config = engine.get_effective_config()

        self.assertIn('gates', effective_config)
        self.assertEqual(effective_config.get('validation_mode', 'strict'), 'strict')

    def test_get_effective_config_lenient(self):
        """Test getting effective config for lenient mode"""
        os.environ['HOOKS_CONTEXT'] = 'phase_5_enrichment'

        engine = DynamicHooksEngine(config_dir=self.config_dir, skip_plugin_loading=True)
        effective_config = engine.get_effective_config()

        self.assertIn('gates', effective_config)

    def test_context_detection_works(self):
        """Test that context detection resolves correctly"""
        context = self.engine.current_context

        self.assertIsNotNone(context)
        self.assertIn('phase', context)
        self.assertIn('environment', context)

    def test_engine_has_required_components(self):
        """Test that engine has all required components"""
        self.assertIsNotNone(self.engine.config_loader)
        self.assertIsNotNone(self.engine.context_resolver)
        self.assertIsNotNone(self.engine.learning_engine)

    def test_get_version(self):
        """Test getting engine version"""
        version = self.engine.get_version()

        self.assertIsNotNone(version)
        self.assertTrue(version.startswith('1.'), f"Version should be 1.x.x format, got {version}")

    def test_get_status(self):
        """Test getting engine status"""
        status = self.engine.get_status()

        self.assertIsInstance(status, dict)
        self.assertIn('version', status)
        self.assertIn('components_status', status)
        self.assertIn('current_context', status)

    def test_validation_modes_accessible(self):
        """Test that validation modes are accessible through engine"""
        modes = self.engine.get_validation_modes()

        self.assertIsNotNone(modes)
        self.assertIn('strict', modes)
        self.assertIn('lenient', modes)
        self.assertIn('experimental', modes)


class TestContextDetection(unittest.TestCase):
    """Test context detection logic"""

    def test_context_resolver_initialization(self):
        """Test ContextResolver initializes correctly"""
        resolver = ContextResolver()

        self.assertIsNotNone(resolver)

    def test_detect_phase_from_env(self):
        """Test detecting phase from environment variable"""
        os.environ['HOOKS_CONTEXT'] = 'phase_5_enrichment'
        resolver = ContextResolver()

        context = resolver.resolve()

        self.assertEqual(context['phase'], 'phase_5_enrichment')

    def test_detect_default_context(self):
        """Test that default context is used when not specified"""
        # Clear environment
        if 'HOOKS_CONTEXT' in os.environ:
            del os.environ['HOOKS_CONTEXT']

        resolver = ContextResolver()
        context = resolver.resolve()

        self.assertIsNotNone(context)
        self.assertIn('phase', context)


class TestBackwardCompatibility(unittest.TestCase):
    """Test backward compatibility with hardcoded values"""

    def setUp(self):
        """Set up test environment"""
        self.config_dir = str(Path(__file__).parent.parent / "config")
        self.engine = DynamicHooksEngine(config_dir=self.config_dir, skip_plugin_loading=True)

    def test_commit_message_config_has_conventional_types(self):
        """Test that commit message config has all conventional commit types"""
        config = self.engine.global_config

        required_types = ['feat', 'fix', 'docs', 'refactor', 'perf', 'test', 'chore']

        # Check if config has commit_message section
        if 'commit_message' in config:
            if 'valid_types' in config['commit_message']:
                types = config['commit_message']['valid_types']
                for req_type in required_types:
                    self.assertIn(req_type, types)

    def test_gate_descriptions_config_has_thresholds(self):
        """Test that gate configurations have expected thresholds"""
        config = self.engine.global_config
        gates = config['gates']

        # Description gate should have min/max length
        if 'description' in gates:
            self.assertIn('min_length', gates['description'])
            self.assertIn('max_length', gates['description'])


if __name__ == '__main__':
    unittest.main()
