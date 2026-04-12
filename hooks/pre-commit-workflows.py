#!/usr/bin/env python3
"""
Pre-Commit Workflows Validator for .agents Framework
Validates workflow definitions and skills integration

Uses DynamicHooksEngine for configuration.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import re
import yaml

# Configuration
BASE_DIR = Path(__file__).parent.parent  # .agents directory
SKILLS_DIR = BASE_DIR / "skills"
WORKFLOWS_DIR = BASE_DIR / "workflows"

# Add hooks engine to path
hooks_path = Path(__file__).parent
sys.path.insert(0, str(hooks_path))

try:
    from engine.dynamic_hooks_engine import DynamicHooksEngine
    USE_DYNAMIC_ENGINE = True
except ImportError:
    USE_DYNAMIC_ENGINE = False

# Fallback configuration
FALLBACK_CONFIG = {
    'gates': {
        'workflow': {
            'min_steps': 4,
            'max_steps': 7
        }
    }
}


class WorkflowValidator:
    """Validates workflow definitions."""

    def __init__(self, use_dynamic=USE_DYNAMIC_ENGINE):
        self.errors = []
        self.warnings = []
        self.workflow_count = 0
        self.passed = 0
        self.failed = 0
        self.use_dynamic = use_dynamic

        # Initialize dynamic engine if available
        self.engine = None
        self.config = None
        if self.use_dynamic:
            try:
                self.engine = DynamicHooksEngine(skip_plugin_loading=True)
                self.config = self.engine.get_effective_config()
            except Exception as e:
                print(f"[WARNING] Could not load dynamic engine: {e}. Using hardcoded defaults.")
                self.use_dynamic = False

        # Set default config values
        if not self.use_dynamic or not self.config:
            self.config = FALLBACK_CONFIG

    def get_workflow_config(self):
        """Get workflow validation config from config."""
        return self.config.get('gates', {}).get('workflow', FALLBACK_CONFIG['gates']['workflow'])

    def validate_file(self, workflow_path: Path) -> bool:
        """Validate a single workflow file."""
        try:
            with open(workflow_path, 'r', encoding='utf-8') as f:
                content = f.read()

            try:
                workflow_data = yaml.safe_load(content)
            except yaml.YAMLError as e:
                self.errors.append(f"{workflow_path}: YAML parse error: {e}")
                return False

            if not workflow_data:
                self.errors.append(f"{workflow_path}: Empty workflow definition")
                return False

            # Validate workflow structure
            if 'name' not in workflow_data:
                self.errors.append(f"{workflow_path}: Missing 'name' field")
                return False

            if 'steps' not in workflow_data:
                self.errors.append(f"{workflow_path}: Missing 'steps' field")
                return False

            steps = workflow_data.get('steps', [])
            if not isinstance(steps, list):
                self.errors.append(f"{workflow_path}: 'steps' must be a list")
                return False

            # Get dynamic config values
            workflow_config = self.get_workflow_config()
            min_steps = workflow_config.get('min_steps', 4)
            max_steps = workflow_config.get('max_steps', 7)

            # Validate step count
            if len(steps) < min_steps:
                self.warnings.append(f"{workflow_path}: Workflow has too few steps ({len(steps)}, min {min_steps})")
            elif len(steps) > max_steps:
                self.warnings.append(f"{workflow_path}: Workflow has too many steps ({len(steps)}, max {max_steps})")

            # Validate each step
            for i, step in enumerate(steps):
                if not isinstance(step, dict):
                    self.errors.append(f"{workflow_path}: Step {i+1} is not a dictionary")
                    return False

                if 'name' not in step:
                    self.errors.append(f"{workflow_path}: Step {i+1} missing 'name' field")
                    return False

                # Validate skills reference
                if 'skills' in step:
                    skills = step['skills']
                    if isinstance(skills, str):
                        skills = [s.strip() for s in skills.split(',')]
                    elif not isinstance(skills, list):
                        self.errors.append(f"{workflow_path}: Step {i+1} 'skills' must be string or list")
                        return False

                    for skill in skills:
                        if not self._skill_exists(skill):
                            self.warnings.append(f"{workflow_path}: Step {i+1} references unknown skill: '{skill}'")

                # Validate bash commands use Unix semantics
                if 'bash' in step:
                    cmd = step['bash']
                    if isinstance(cmd, str) and self._has_windows_syntax(cmd):
                        self.errors.append(f"{workflow_path}: Step {i+1} uses Windows syntax, must use Unix semantics")
                        return False

                # Validate MCP server references
                if 'mcp' in step:
                    mcp = step['mcp']
                    if not self._validate_mcp_server(mcp):
                        self.warnings.append(f"{workflow_path}: Step {i+1} references potentially invalid MCP server: '{mcp}'")

            self.workflow_count += 1
            self.passed += 1
            return True

        except Exception as e:
            self.errors.append(f"{workflow_path}: Unexpected error: {e}")
            self.failed += 1
            return False

    def _skill_exists(self, skill_name: str) -> bool:
        """Check if a skill exists in the skills directory."""
        skill_dir = SKILLS_DIR / skill_name
        skill_file = skill_dir / "SKILL.md"
        return skill_file.exists()

    def _has_windows_syntax(self, cmd: str) -> bool:
        """Detect Windows-specific syntax in bash command."""
        windows_patterns = [
            r'\\[^\\]',  # Windows path separators
            r'[A-Z]:\\',  # Drive letters
            r'cmd\.exe',
            r'powershell',
            r'\.bat',
            r'\.cmd',
            r'NUL',
            r'CON',
            r'PRN',
            r'AUX',
        ]

        for pattern in windows_patterns:
            if re.search(pattern, cmd, re.IGNORECASE):
                return True

        return False

    def _validate_mcp_server(self, mcp_name: str) -> bool:
        """Validate MCP server name format."""
        # MCP servers follow pattern: {provider}-{service}
        return bool(re.match(r'^[a-z]+-[a-z]+(-[a-z]+)*$', mcp_name))

    def validate_workflows_dir(self) -> int:
        """Validate all workflows in the workflows directory."""
        print("=" * 70)
        print("PRE-COMMIT WORKFLOWS VALIDATOR")
        print("=" * 70)
        print()

        if not WORKFLOWS_DIR.exists():
            print(f"NOTE: Workflows directory not found: {WORKFLOWS_DIR}")
            print("This may be normal if workflows are not yet defined.")
            return 0

        # Find all workflow files
        workflow_files = list(WORKFLOWS_DIR.glob('*.yaml')) + list(WORKFLOWS_DIR.glob('*.yml'))

        if not workflow_files:
            print("No workflow files found to validate.\n")
            return 0

        print(f"Found {len(workflow_files)} workflows to validate\n")

        # Validate each workflow
        for workflow_file in sorted(workflow_files):
            if self.validate_file(workflow_file):
                print(f"  [OK] {workflow_file.name}")
            else:
                print(f"  [FAIL] {workflow_file.name}")
                self.failed += 1

        # Print summary
        print("\n" + "=" * 70)
        print("VALIDATION SUMMARY")
        print("=" * 70)
        print(f"Total Workflows Checked: {self.workflow_count}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")

        if self.workflow_count > 0:
            pass_rate = (self.passed / self.workflow_count) * 100
            print(f"Pass Rate: {pass_rate:.1f}%")

        if self.errors:
            print(f"\nErrors ({len(self.errors)}):")
            print("-" * 70)
            for error in self.errors[:10]:
                print(f"  • {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more errors")

        if self.warnings:
            print(f"\nWarnings ({len(self.warnings)}):")
            print("-" * 70)
            for warning in self.warnings[:10]:
                print(f"  • {warning}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more warnings")

        print()
        if self.failed == 0:
            print("SUCCESS: All workflows passed pre-commit validation!")
            return 0
        else:
            print(f"FAILURE: {self.failed} workflows failed validation")
            return 1


def main() -> int:
    """Main function."""
    validator = WorkflowValidator()
    return validator.validate_workflows_dir()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
