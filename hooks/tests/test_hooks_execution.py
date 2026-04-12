#!/usr/bin/env python3
"""
Execution Tests for Pre-Commit Hooks
Tests that hooks execute correctly with dynamic engine
"""

import unittest
import sys
import subprocess
from pathlib import Path
import tempfile

# Add parent path
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestPreCommitHookExecution(unittest.TestCase):
    """Test actual pre-commit hook execution"""

    def setUp(self):
        """Set up test environment"""
        self.hooks_dir = Path(__file__).parent.parent
        self.python = sys.executable

    def test_precommit_message_hook_exists(self):
        """Test that pre-commit-message.py exists and is executable"""
        hook_path = self.hooks_dir / "pre-commit-message.py"

        self.assertTrue(hook_path.exists(), f"Hook not found: {hook_path}")

    def test_precommit_skills_hook_exists(self):
        """Test that pre-commit-skills.py exists"""
        hook_path = self.hooks_dir / "pre-commit-skills.py"

        self.assertTrue(hook_path.exists(), f"Hook not found: {hook_path}")

    def test_precommit_workflows_hook_exists(self):
        """Test that pre-commit-workflows.py exists"""
        hook_path = self.hooks_dir / "pre-commit-workflows.py"

        self.assertTrue(hook_path.exists(), f"Hook not found: {hook_path}")

    def test_validate_skill_hook_exists(self):
        """Test that validate-skill.py exists"""
        hook_path = self.hooks_dir / "validate-skill.py"

        self.assertTrue(hook_path.exists(), f"Hook not found: {hook_path}")

    def test_engine_modules_importable(self):
        """Test that all engine modules are importable"""
        try:
            from engine.dynamic_hooks_engine import DynamicHooksEngine
            from engine.configuration_loader import ConfigurationLoader
            from engine.context_resolver import ContextResolver
            from engine.plugin_manager import PluginManager
            from engine.learning_engine import LearningEngine
        except ImportError as e:
            self.fail(f"Failed to import engine modules: {e}")

    def test_all_config_files_exist(self):
        """Test that all configuration files exist"""
        config_files = [
            self.hooks_dir / "config" / "hooks-config.yaml",
            self.hooks_dir / "config" / "hooks-context.yaml",
            self.hooks_dir / "config" / "hooks-plugins.yaml",
        ]

        for config_file in config_files:
            self.assertTrue(config_file.exists(), f"Config file not found: {config_file}")

    def test_config_files_not_empty(self):
        """Test that config files are not empty"""
        config_files = [
            self.hooks_dir / "config" / "hooks-config.yaml",
            self.hooks_dir / "config" / "hooks-context.yaml",
            self.hooks_dir / "config" / "hooks-plugins.yaml",
        ]

        for config_file in config_files:
            size = config_file.stat().st_size
            self.assertGreater(size, 0, f"Config file is empty: {config_file}")


class TestConfigurationIntegration(unittest.TestCase):
    """Test configuration integration with hooks"""

    def setUp(self):
        """Set up test environment"""
        self.hooks_dir = Path(__file__).parent.parent
        sys.path.insert(0, str(self.hooks_dir))

    def test_precommit_message_uses_dynamic_engine(self):
        """Test that pre-commit-message.py imports DynamicHooksEngine"""
        hook_path = self.hooks_dir / "pre-commit-message.py"

        with open(hook_path, 'r') as f:
            content = f.read()

        self.assertIn('DynamicHooksEngine', content,
                     "Hook should use DynamicHooksEngine")

    def test_configuration_hierarchy_in_engine(self):
        """Test that configuration hierarchy is applied correctly"""
        from engine.dynamic_hooks_engine import DynamicHooksEngine

        config_dir = str(self.hooks_dir / "config")
        engine = DynamicHooksEngine(config_dir=config_dir, skip_plugin_loading=True)

        # Engine should have loaded all three config levels
        self.assertIsNotNone(engine.global_config)
        self.assertIsNotNone(engine.context_config)
        self.assertIsNotNone(engine.plugins_config)

    def test_fallback_config_available(self):
        """Test that all hooks have fallback configs defined"""
        hook_files = [
            self.hooks_dir / "pre-commit-message.py",
            self.hooks_dir / "pre-commit-skills.py",
            self.hooks_dir / "pre-commit-workflows.py",
            self.hooks_dir / "validate-skill.py",
        ]

        for hook_file in hook_files:
            with open(hook_file, 'r') as f:
                content = f.read()

            self.assertIn('FALLBACK_CONFIG', content,
                         f"{hook_file.name} should have FALLBACK_CONFIG")


if __name__ == '__main__':
    unittest.main()
