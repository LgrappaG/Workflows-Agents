#!/usr/bin/env python3
"""
Comprehensive Skill Validator for .agents Framework
Validates all 8 quality gates for skills
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import re
import yaml
from datetime import datetime

# Configuration
BASE_DIR = Path(__file__).parent.parent.parent
SKILLS_DIR = BASE_DIR / ".agents" / "skills"

# Valid domains (same as pre-commit-skills.py)
VALID_DOMAINS = {
    'advanced', 'animation', 'audio', 'ai', 'analytics', 'anomaly', 'api',
    'asset', 'automated', 'behavior', 'blueprint', 'build', 'ci-cd', 'clustering',
    'collision', 'component', 'compute', 'computer-vision', 'console', 'constraint',
    'cross-engine', 'custom', 'data', 'debug', 'decision', 'deployment', 'dialogue',
    'distribution', 'dynamic', 'edge', 'ensemble', 'engine', 'feature', 'federated',
    'fine-tuning', 'garbage-collection', 'godot', 'graphics', 'gpu', 'hierarchy',
    'hyperparameter', 'il', 'inference', 'input', 'inspector', 'interpolation',
    'ik', 'joint', 'language', 'layer', 'level', 'lighting', 'localization',
    'machine-learning', 'math', 'memory', 'mesh', 'ml', 'mobile', 'model',
    'motion', 'motor', 'movement', 'multiplayer', 'navigation', 'neural-network',
    'nlp', 'node', 'networking', 'normalization', 'object', 'optimization',
    'particle', 'performance', 'physics', 'pipeline', 'plugin', 'pooling',
    'prediction', 'procedural', 'profiler', 'profiling', 'projection', 'property',
    'rag', 'ray', 'reflection', 'reinforcement', 'rendering', 'resource',
    'response', 'rigging', 'runtime', 'scripting', 'security', 'sensor',
    'serialization', 'shader', 'socket', 'sound', 'spatial', 'specialized',
    'state', 'streaming', 'string', 'structure', 'synchronization', 'system',
    'task', 'telemetry', 'temporal', 'terrain', 'testing', 'texture', 'thread',
    'tile', 'time', 'tool', 'trace', 'transfer', 'transform', 'transition',
    'ui', 'unreal', 'validation', 'vfx', 'vr', 'world', 'xr',
}

REQUIRED_FIELDS = ['name', 'description', 'risk', 'source', 'date_added',
                   'usage', 'avoid', 'mandates', 'response']
VALID_RISK_LEVELS = ['low', 'medium', 'high']
DESCRIPTION_MIN = 50
DESCRIPTION_MAX = 100
FILE_SIZE_MIN = 600
FILE_SIZE_MAX = 1200


class Gate1Validator:
    """Gate 1: YAML Frontmatter Validation"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate YAML frontmatter completeness."""
        missing_fields = [f for f in REQUIRED_FIELDS if f not in skill_data]
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"

        for field in REQUIRED_FIELDS:
            value = skill_data.get(field, '')
            if not value or (isinstance(value, str) and not value.strip()):
                return False, f"Field '{field}' is empty or whitespace-only"

        return True, "All required fields present and populated"


class Gate2Validator:
    """Gate 2: Skill Naming Convention"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate skill name follows {domain}-{specialty} pattern."""
        name = skill_data.get('name', '')

        if not re.match(r'^[a-z]+-[a-z\-]+$', name):
            return False, f"Name doesn't match pattern: must be lowercase with hyphens"

        parts = name.split('-', 1)
        if len(parts) != 2:
            return False, f"Name must have format: {{domain}}-{{specialty}}"

        domain, specialty = parts

        if domain not in VALID_DOMAINS:
            return False, f"Invalid domain: '{domain}'. Must be from approved list"

        if len(specialty) < 2:
            return False, f"Specialty too short: '{specialty}' (min 2 chars)"

        # Check for redundancy (e.g., "animation-animator")
        if specialty.startswith(domain[:3]):
            return False, f"Redundant naming: specialty shouldn't start with domain"

        return True, f"Valid naming pattern for domain '{domain}'"


class Gate3Validator:
    """Gate 3: Description Quality & Optimization"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate description is concise, clear, and action-oriented."""
        desc = skill_data.get('description', '')

        if len(desc) < DESCRIPTION_MIN:
            return False, f"Description too short: {len(desc)} chars (min {DESCRIPTION_MIN})"

        if len(desc) > DESCRIPTION_MAX:
            return False, f"Description too long: {len(desc)} chars (max {DESCRIPTION_MAX})"

        # Check for action-oriented start
        first_word = desc.split()[0].lower() if desc.split() else ''
        filler_words = {'the', 'this', 'that', 'a', 'an', 'is', 'are'}
        if first_word in filler_words:
            return False, f"Description should start with action verb, not '{first_word}'"

        # Check for common filler patterns
        if ' and ' in desc and desc.count(' and ') > 2:
            return False, f"Description has excessive 'and' conjunctions (reduce redundancy)"

        return True, f"Description quality optimal ({len(desc)} chars)"


class Gate4Validator:
    """Gate 4: Risk Level Appropriateness"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate risk level is appropriate for complexity."""
        risk = skill_data.get('risk', '').lower()

        if risk not in VALID_RISK_LEVELS:
            return False, f"Invalid risk level: '{risk}'. Must be one of: {', '.join(VALID_RISK_LEVELS)}"

        name = skill_data.get('name', '')

        # Heuristic risk assessment
        high_complexity_keywords = [
            'advanced', 'complex', 'reinforcement', 'learning', 'neural',
            'optimization', 'synchronization', 'networking', 'distributed',
            'architecture', 'engine', 'serialization', 'cross-platform'
        ]

        medium_complexity_keywords = [
            'setup', 'configuration', 'integration', 'system', 'management',
            'implementation', 'design', 'specialized', 'custom', 'framework'
        ]

        contains_high = any(kw in name for kw in high_complexity_keywords)
        contains_medium = any(kw in name for kw in medium_complexity_keywords)

        if contains_high and risk == 'low':
            return False, f"Risk level 'low' inappropriate for complex skill '{name}'"

        if risk == 'high' and not contains_high and not contains_medium:
            return False, f"Risk level 'high' may be inappropriate for simple skill '{name}'"

        return True, f"Risk level '{risk}' is appropriate for this skill"


class Gate5Validator:
    """Gate 5: Mandates Clarity & Specificity"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate mandates are clear, specific, and actionable."""
        mandates_str = skill_data.get('mandates', '')

        if not mandates_str:
            return False, "Mandates field is empty"

        mandates = [m.strip() for m in mandates_str.split(',')]

        if len(mandates) < 3:
            return False, f"Too few mandates: {len(mandates)} (minimum 3)"

        vague_words = {'good', 'bad', 'well', 'properly', 'correct', 'proper', 'appropriate'}
        action_verbs = {'validate', 'test', 'check', 'verify', 'implement', 'ensure', 'maintain',
                        'configure', 'optimize', 'profile', 'document', 'review'}

        for mandate in mandates:
            if not mandate or len(mandate) < 5:
                return False, f"Mandate too short or empty: '{mandate}'"

            first_word = mandate.split()[0].lower() if mandate.split() else ''

            if first_word not in action_verbs and not first_word[0].isupper():
                return False, f"Mandate should start with action verb: '{mandate}'"

            if any(vague_word in mandate.lower() for vague_word in vague_words):
                if not any(detail in mandate.lower() for detail in ['specific', 'measure', 'metric']):
                    return False, f"Mandate is too vague: '{mandate}' (add specifics)"

        return True, f"Mandates are clear and specific ({len(mandates)} mandates)"


class Gate6Validator:
    """Gate 6: Response Patterns Actionability"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate response patterns are specific and achievable."""
        response_str = skill_data.get('response', '')

        if not response_str:
            return False, "Response field is empty"

        steps = [s.strip() for s in response_str.split(',')]

        if len(steps) < 3 or len(steps) > 4:
            return False, f"Response should have 3-4 steps, found {len(steps)}"

        for step in steps:
            if not step or len(step) < 3:
                return False, f"Response step too short: '{step}'"

            # Check for concrete action
            if ' and ' in step:
                return False, f"Response step too complex (multiple actions): '{step}'"

        return True, f"Response pattern is clear and actionable ({len(steps)} steps)"


class Gate7Validator:
    """Gate 7: Token Efficiency & File Size"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate token efficiency and file size."""
        try:
            file_size = skill_path.stat().st_size
        except:
            return False, "Unable to determine file size"

        if file_size > FILE_SIZE_MAX:
            return False, f"File size too large: {file_size} bytes (max {FILE_SIZE_MAX})"

        if file_size < FILE_SIZE_MIN:
            return False, f"File size too small: {file_size} bytes (min {FILE_SIZE_MIN})"

        # Estimate token count (rough: ~4 chars per token)
        estimated_tokens = file_size // 4
        max_tokens = FILE_SIZE_MAX // 4

        return True, f"Token efficiency optimal ({file_size} bytes, ~{estimated_tokens} tokens)"


class Gate8Validator:
    """Gate 8: Cross-Skill Consistency"""

    @staticmethod
    def validate(skill_data: Dict, skill_path: Path) -> Tuple[bool, str]:
        """Validate consistency with other skills."""
        name = skill_data.get('name', '')
        domain = name.split('-')[0] if '-' in name else ''

        # Find related skills (same domain)
        related_skills = []
        if domain:
            related_dir = SKILLS_DIR.parent.glob(f'*{domain}*')
            related_skills = list(SKILLS_DIR.glob(f'{domain}-*'))

        risk = skill_data.get('risk', '').lower()

        # Check risk consistency with related skills
        risk_levels = {}
        for related_path in related_skills[:5]:  # Sample up to 5 related skills
            try:
                with open(related_path / "SKILL.md", 'r') as f:
                    content = f.read()
                    if 'risk:' in content:
                        match = re.search(r'risk:\s*(\w+)', content)
                        if match:
                            r = match.group(1).lower()
                            risk_levels[r] = risk_levels.get(r, 0) + 1
            except:
                pass

        if risk_levels:
            dominant_risk = max(risk_levels, key=risk_levels.get)
            if risk not in [dominant_risk, 'low'] and len(risk_levels) > 2:
                return False, f"Risk level '{risk}' inconsistent with related skills (dominant: '{dominant_risk}')"

        # Check description style consistency (should be action-oriented)
        desc = skill_data.get('description', '')
        if not any(desc.lower().startswith(v) for v in ['implement', 'configure', 'design', 'master',
                                                          'set', 'optimize', 'create', 'develop',
                                                          'integrate', 'build', 'manage', 'handle']):
            return False, "Description should start with action verb for consistency"

        return True, "Consistent with framework standards"


class ComprehensiveValidator:
    """Runs all 8 validation gates."""

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.skill_data = {}
        self.results = {}
        self.passed_gates = 0
        self.total_gates = 8

    def load_skill(self) -> bool:
        """Load and parse skill file."""
        try:
            with open(self.skill_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if not content.startswith('---'):
                print(f"ERROR: Missing YAML frontmatter start")
                return False

            end_marker = content.find('\n---\n', 4)
            if end_marker == -1:
                print(f"ERROR: Malformed YAML frontmatter")
                return False

            frontmatter_str = content[4:end_marker]
            self.skill_data = yaml.safe_load(frontmatter_str)

            if not self.skill_data:
                print(f"ERROR: Empty YAML frontmatter")
                return False

            return True
        except Exception as e:
            print(f"ERROR: Failed to load skill: {e}")
            return False

    def validate_all(self) -> bool:
        """Run all validation gates."""
        gates = [
            (1, "YAML Frontmatter", Gate1Validator.validate),
            (2, "Naming Convention", Gate2Validator.validate),
            (3, "Description Quality", Gate3Validator.validate),
            (4, "Risk Level Appropriateness", Gate4Validator.validate),
            (5, "Mandates Clarity", Gate5Validator.validate),
            (6, "Response Patterns", Gate6Validator.validate),
            (7, "Token Efficiency", Gate7Validator.validate),
            (8, "Cross-Skill Consistency", Gate8Validator.validate),
        ]

        print(f"\nCOMPREHENSIVE SKILL VALIDATION")
        print("=" * 70)
        print(f"\nSkill: {self.skill_path.parent.name}")
        print("-" * 70)

        for gate_num, gate_name, validator_func in gates:
            passed, message = validator_func(self.skill_data, self.skill_path)

            status = "[PASS]" if passed else "[FAIL]"
            print(f"Gate {gate_num}: {gate_name:.<35} {status}")
            print(f"       {message}")

            self.results[gate_num] = (passed, message)
            if passed:
                self.passed_gates += 1

        return self.passed_gates == self.total_gates

    def print_summary(self) -> int:
        """Print validation summary."""
        print("\n" + "=" * 70)
        print("VALIDATION SUMMARY")
        print("=" * 70)

        quality_score = (self.passed_gates / self.total_gates) * 100

        status = "PASS" if self.passed_gates == self.total_gates else "FAIL"
        print(f"\nStatus: {status} ({self.passed_gates}/{self.total_gates} gates)")
        print(f"Quality Score: {quality_score:.0f}%")

        if self.passed_gates == self.total_gates:
            print("\nSUCCESS: Skill meets all quality requirements!")
            return 0
        else:
            print(f"\nFAILURE: Skill has {self.total_gates - self.passed_gates} gate(s) failing")
            return 1


def main() -> int:
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python validate-skill.py <skill-path>")
        print("\nExample: python validate-skill.py .agents/skills/animation-blend-trees/SKILL.md")
        return 1

    skill_path = Path(sys.argv[1])

    if not skill_path.exists():
        print(f"ERROR: Skill file not found: {skill_path}")
        return 1

    validator = ComprehensiveValidator(skill_path)

    if not validator.load_skill():
        return 1

    validator.validate_all()
    return validator.print_summary()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
