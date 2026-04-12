#!/usr/bin/env python3
"""
Pre-Commit Message Validator for .agents Framework
Validates commit messages follow conventional commits format

Uses DynamicHooksEngine for configuration.
"""

import sys
import re
from pathlib import Path

# Add hooks engine to path
hooks_path = Path(__file__).parent
sys.path.insert(0, str(hooks_path))

try:
    from engine.dynamic_hooks_engine import DynamicHooksEngine
    USE_DYNAMIC_ENGINE = True
except ImportError:
    USE_DYNAMIC_ENGINE = False

# Fallback configuration (module level for consistency)
FALLBACK_CONFIG = {
    'commit_message': {
        'valid_types': ['feat', 'fix', 'docs', 'refactor', 'perf', 'test', 'chore'],
        'valid_scopes': [
            'Phase 1', 'Phase 2', 'Phase 3', 'Phase 4',
            'Machine Learning', 'Multi-Engine', 'Custom Tools',
            'Skills', 'Validation', 'Documentation', 'Hooks',
            'CLI', 'Framework', 'Agent Hierarchy',
            'Materials System', 'UI Toolkit', 'Terrain System',
            'Animation System', 'Graphics & VFX', 'Debugging & Tools',
            'Advanced Systems', 'ML Integration', 'Tools & Extensions'
        ],
        'description_min': 5,
        'description_max': 70,
        'require_scope': False
    }
}


class CommitMessageValidator:
    """Validates commit message format."""

    def __init__(self, message_file: str, use_dynamic=USE_DYNAMIC_ENGINE):
        self.message_file = Path(message_file)
        self.message = ""
        self.errors = []
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

        # Fallback to hardcoded values
        if not self.use_dynamic:
            self.config = FALLBACK_CONFIG

    def get_valid_types(self):
        """Get valid commit types from config."""
        return self.config.get('commit_message', {}).get('valid_types', [])

    def get_valid_scopes(self):
        """Get valid scopes from config."""
        return self.config.get('commit_message', {}).get('valid_scopes', [])

    def get_description_min(self):
        """Get min description length from config."""
        return self.config.get('commit_message', {}).get('description_min', 5)

    def get_description_max(self):
        """Get max description length from config."""
        return self.config.get('commit_message', {}).get('description_max', 70)

    def load_message(self) -> bool:
        """Load commit message from file."""
        try:
            with open(self.message_file, 'r', encoding='utf-8') as f:
                self.message = f.read().strip()
            return True
        except Exception as e:
            self.errors.append(f"Failed to read message file: {e}")
            return False

    def validate(self) -> bool:
        """Validate commit message."""
        if not self.message:
            self.errors.append("Commit message is empty")
            return False

        # Get first line (subject)
        subject = self.message.split('\n')[0]

        valid_types = self.get_valid_types()
        valid_scopes = self.get_valid_scopes()
        desc_min = self.get_description_min()
        desc_max = self.get_description_max()

        # Validate format: Type: Description (SCOPE)
        types_pattern = '|'.join(re.escape(t) for t in valid_types)
        pattern = rf'^({types_pattern}):\s+(.+)\s+\((.+)\)$'
        match = re.match(pattern, subject)

        if not match:
            self.errors.append(
                f"Invalid format: '{subject}'\n"
                f"Expected: 'Type: Description (SCOPE)'\n"
                f"Valid types: {', '.join(valid_types)}"
            )
            return False

        commit_type, description, scope = match.groups()

        # Validate type (redundant with regex, but kept for clarity)
        if commit_type not in valid_types:
            self.errors.append(f"Invalid type: '{commit_type}'. Valid types: {', '.join(valid_types)}")
            return False

        # Validate description length
        if len(description) < desc_min:
            self.errors.append(f"Description too short: '{description}' (minimum {desc_min} characters)")
            return False

        if len(description) > desc_max:
            self.errors.append(f"Description too long: {len(description)} chars (maximum {desc_max})")
            return False

        # Description should start with lowercase (unless special term)
        if description[0].isupper() and description[0:2] not in ['ML', 'AI', 'UI', 'VR', 'XR', 'CI']:
            self.errors.append(f"Description should start with lowercase: '{description}'")
            return False

        # Validate scope (warning level)
        if scope not in valid_scopes:
            print(f"WARNING: Non-standard scope '{scope}' (consider using standard scopes)")
            if valid_scopes:
                print(f"Standard scopes: {', '.join(valid_scopes[:5])} ...")

        # Validate scope format
        if '(' in scope or ')' in scope or ',' in scope:
            self.errors.append(f"Invalid scope format: '{scope}' (avoid parentheses)")
            return False

        return True

    def print_result(self) -> int:
        """Print validation result."""
        valid_types = self.get_valid_types()
        valid_scopes = self.get_valid_scopes()

        if self.errors:
            print("=" * 70)
            print("COMMIT MESSAGE VALIDATION FAILED")
            print("=" * 70)
            print()
            for error in self.errors:
                print(f"[FAIL] {error}\n")

            print("=" * 70)
            print("REQUIRED FORMAT")
            print("=" * 70)
            print("Type: Description (SCOPE)")
            print()
            print("Valid Types:")
            for commit_type in valid_types:
                print(f"  • {commit_type}")
            print()
            print("Examples:")
            print("  • feat: Add phase4-ml-skills (Machine Learning)")
            print("  • fix: Correct risk level for edge-deployment (Phase 4)")
            print("  • docs: Update AGENT_HIERARCHY.md (Documentation)")
            print("  • refactor: Reorganize skill categories (Skills)")
            print()
            return 1
        else:
            print("[OK] Commit message validation passed!")
            # Track successful validation if using dynamic engine
            if self.engine:
                try:
                    result = {
                        'pass': True,
                        'context': self.engine.current_context,
                        'mode': self.engine.current_mode,
                        'gate': 'commit_message',
                        'validation_type': 'commit_message_format'
                    }
                    self.engine.learning_engine.track_validation(str(self.message_file), result)
                except Exception:
                    pass  # Silently continue if learning tracking fails
            return 0


def main() -> int:
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python pre-commit-message.py <message-file>")
        return 1

    validator = CommitMessageValidator(sys.argv[1])

    if not validator.load_message():
        print("\n".join(f"[FAIL] {e}" for e in validator.errors))
        return 1

    if not validator.validate():
        return validator.print_result()

    return validator.print_result()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
