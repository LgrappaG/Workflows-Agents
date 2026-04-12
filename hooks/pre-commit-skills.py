#!/usr/bin/env python3
"""
Pre-Commit Skills Validator for .agents Framework
Validates YAML frontmatter and naming conventions before commit

Uses DynamicHooksEngine for configuration.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import re
import yaml
from datetime import date

# Configuration
BASE_DIR = Path(__file__).parent.parent  # .agents directory
SKILLS_DIR = BASE_DIR / "skills"

# Add hooks engine to path
hooks_path = Path(__file__).parent
sys.path.insert(0, str(hooks_path))

try:
    from engine.dynamic_hooks_engine import DynamicHooksEngine
    USE_DYNAMIC_ENGINE = True
except ImportError:
    USE_DYNAMIC_ENGINE = False

# Fallback hardcoded values
FALLBACK_DOMAINS = {
    'advanced', 'animation', 'audio', 'ai', 'analytics', 'anomaly', 'api',
    'architecture', 'asset', 'automated', 'behavior', 'blueprint', 'build', 'ci', 'ci-cd', 'cinemachine',
    'clustering', 'collision', 'compatibility', 'component', 'compute', 'computer', 'computer-vision', 'console', 'constraint',
    'configuration', 'controller', 'cross', 'cross-engine', 'cross-validation', 'csharp', 'custom',
    'data', 'debug', 'decision', 'deployment', 'development', 'dialogue', 'distribution',
    'dynamic', 'edge', 'editor', 'ensemble', 'engine', 'feature', 'federated', 'fine', 'fine-tuning',
    'garbage-collection', 'gesture', 'godot', 'graphics', 'gpu', 'hierarchy', 'hyperparameter',
    'il', 'inference', 'injection', 'input', 'inspector', 'interpolation', 'ik', 'joint',
    'language', 'layer', 'level', 'lighting', 'localization', 'machine', 'machine-learning', 'material',
    'math', 'memory', 'mesh', 'metrics', 'ml', 'mobile', 'model', 'module', 'motion', 'motor',
    'movement', 'multiplayer', 'navmesh', 'navigation', 'neural', 'neural-network', 'nlp', 'node',
    'networking', 'normalization', 'object', 'optimization', 'particle', 'pathfinding',
    'performance', 'persistence', 'physics', 'pipeline', 'platform', 'plugin', 'pooling',
    'prediction', 'privacy', 'procedural', 'profiler', 'profiling', 'projection', 'property',
    'quality', 'rag', 'ray', 'reflection', 'reinforcement', 'rendering', 'resource', 'response',
    'rigging', 'runtime', 'savedata', 'scripting', 'security', 'sensor', 'serialization',
    'shader', 'socket', 'sound', 'spatial', 'specialized', 'state', 'streaming', 'string',
    'structure', 'synchronization', 'system', 'task', 'telemetry', 'temporal', 'terrain',
    'testing', 'texture', 'thread', 'tile', 'time', 'timeline', 'tool', 'trace', 'training',
    'transfer', 'transform', 'transition', 'ui', 'unreal', 'validation', 'version', 'vfx',
    'vr', 'world', 'xr', 'community', 'compliance', 'benchmark'
}

FALLBACK_REQUIRED_FIELDS = ['name', 'description', 'risk', 'source', 'date_added',
                            'usage', 'avoid', 'mandates', 'response']

FALLBACK_RISK_LEVELS = ['low', 'medium', 'high']

# Consolidated fallback configuration
FALLBACK_CONFIG = {
    'gates': {
        'yaml_frontmatter': {
            'required_fields': FALLBACK_REQUIRED_FIELDS
        },
        'naming_convention': {
            'approved_domains': list(FALLBACK_DOMAINS)
        },
        'risk_level': {
            'valid_levels': FALLBACK_RISK_LEVELS
        },
        'description': {
            'min_length': 50,
            'max_length': 100
        }
    }
}


class SkillValidator:
    """Validates skills against pre-commit requirements."""

    def __init__(self, use_dynamic=USE_DYNAMIC_ENGINE):
        self.errors = []
        self.warnings = []
        self.skill_count = 0
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

    def get_required_fields(self):
        """Get required YAML fields from config."""
        return self.config.get('gates', {}).get('yaml_frontmatter', {}).get('required_fields', FALLBACK_REQUIRED_FIELDS)

    def get_approved_domains(self):
        """Get approved domains from config."""
        domains = self.config.get('gates', {}).get('naming_convention', {}).get('approved_domains')
        if isinstance(domains, list):
            return set(domains)
        return FALLBACK_DOMAINS

    def get_valid_risk_levels(self):
        """Get valid risk levels from config."""
        return self.config.get('gates', {}).get('risk_level', {}).get('valid_levels', FALLBACK_RISK_LEVELS)

    def get_description_min(self):
        """Get min description length from config."""
        return self.config.get('gates', {}).get('description', {}).get('min_length', 50)

    def get_description_max(self):
        """Get max description length from config."""
        return self.config.get('gates', {}).get('description', {}).get('max_length', 100)

    def validate_file(self, skill_path: Path) -> bool:
        """Validate a single skill file."""
        try:
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract YAML frontmatter
            if not content.startswith('---'):
                self.errors.append(f"{skill_path}: Missing YAML frontmatter start")
                return False

            # Find closing ---
            end_marker = content.find('\n---\n', 4)
            if end_marker == -1:
                self.errors.append(f"{skill_path}: Malformed YAML frontmatter")
                return False

            frontmatter_str = content[4:end_marker]

            try:
                skill_data = yaml.safe_load(frontmatter_str)
            except yaml.YAMLError as e:
                self.errors.append(f"{skill_path}: YAML parse error: {e}")
                return False

            if not skill_data:
                self.errors.append(f"{skill_path}: Empty YAML frontmatter")
                return False

            # Get dynamic config values
            required_fields = self.get_required_fields()
            valid_risk_levels = self.get_valid_risk_levels()
            desc_min = self.get_description_min()
            desc_max = self.get_description_max()

            # Validate required fields
            missing_fields = [f for f in required_fields if f not in skill_data]
            if missing_fields:
                self.errors.append(
                    f"{skill_path}: Missing required fields: {', '.join(missing_fields)}"
                )
                return False

            # Validate field values
            for field in required_fields:
                value = skill_data.get(field, '')
                if not value or (isinstance(value, str) and not value.strip()):
                    self.errors.append(f"{skill_path}: Field '{field}' is empty")
                    return False

            # Validate skill name format
            skill_name = skill_data['name']
            if not self._validate_skill_name(skill_name):
                self.errors.append(f"{skill_path}: Invalid skill name format: '{skill_name}'")
                return False

            # Validate risk level
            risk = skill_data.get('risk', '').lower()
            if risk not in valid_risk_levels:
                self.errors.append(
                    f"{skill_path}: Invalid risk level '{risk}'. Must be one of: {', '.join(valid_risk_levels)}"
                )
                return False

            # Validate description length
            desc = skill_data.get('description', '')
            if len(desc) < desc_min:
                self.warnings.append(
                    f"{skill_path}: Description too short ({len(desc)} chars, min {desc_min})"
                )
            elif len(desc) > desc_max:
                self.warnings.append(
                    f"{skill_path}: Description too long ({len(desc)} chars, max {desc_max})"
                )

            # Validate date format (YYYY-MM-DD)
            date_added = skill_data.get('date_added', '')
            # Convert datetime.date to string if needed
            if isinstance(date_added, date):
                date_added = date_added.isoformat()
            if not isinstance(date_added, str) or not re.match(r'^\d{4}-\d{2}-\d{2}$', date_added):
                self.errors.append(
                    f"{skill_path}: Invalid date format '{date_added}'. Expected YYYY-MM-DD"
                )
                return False

            self.skill_count += 1
            self.passed += 1
            return True

        except Exception as e:
            self.errors.append(f"{skill_path}: Unexpected error: {e}")
            self.failed += 1
            return False

    def _validate_skill_name(self, name: str) -> bool:
        """Validate skill name follows {domain}-{specialty} pattern."""
        if not re.match(r'^[a-z0-9]+-[a-zA-Z0-9\-]+$', name):
            return False

        parts = name.split('-', 1)
        if len(parts) != 2:
            return False

        domain, specialty = parts

        # Check if domain is valid using dynamic config
        approved_domains = self.get_approved_domains()
        if domain not in approved_domains:
            return False

        # Specialty should have substance
        if len(specialty) < 2:
            return False

        return True

    def validate_skills_dir(self, max_issues: int = 10) -> int:
        """Validate all skills in the skills directory."""
        print("=" * 70)
        print("PRE-COMMIT SKILLS VALIDATOR")
        print("=" * 70)
        print()

        if not SKILLS_DIR.exists():
            print(f"ERROR: Skills directory not found: {SKILLS_DIR}")
            return 1

        # Find all SKILL.md files
        skill_files = list(SKILLS_DIR.glob('*/SKILL.md'))
        print(f"Found {len(skill_files)} skills to validate\n")

        # Validate each skill
        for skill_file in sorted(skill_files):
            if self.validate_file(skill_file):
                print(f"  [OK] {skill_file.parent.name}")
            else:
                print(f"  [FAIL] {skill_file.parent.name}")
                self.failed += 1

        # Print summary
        print("\n" + "=" * 70)
        print("VALIDATION SUMMARY")
        print("=" * 70)
        print(f"Total Skills Checked: {self.skill_count}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")

        if self.skill_count > 0:
            pass_rate = (self.passed / self.skill_count) * 100
            print(f"Pass Rate: {pass_rate:.1f}%")

        if self.errors:
            print(f"\nErrors ({len(self.errors)} total):")
            print("-" * 70)
            for i, error in enumerate(self.errors[:max_issues], 1):
                print(f"{i}. {error}")
            if len(self.errors) > max_issues:
                print(f"... and {len(self.errors) - max_issues} more errors")

        if self.warnings:
            print(f"\nWarnings ({len(self.warnings)} total):")
            print("-" * 70)
            for i, warning in enumerate(self.warnings[:max_issues], 1):
                print(f"{i}. {warning}")
            if len(self.warnings) > max_issues:
                print(f"... and {len(self.warnings) - max_issues} more warnings")

        print()
        if self.failed == 0:
            print("SUCCESS: All skills passed pre-commit validation!")
            return 0
        else:
            print(f"FAILURE: {self.failed} skills failed validation")
            return 1


def main() -> int:
    """Main function."""
    validator = SkillValidator()
    return validator.validate_skills_dir()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
