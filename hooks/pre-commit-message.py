#!/usr/bin/env python3
"""
Pre-Commit Message Validator for .agents Framework
Validates commit messages follow conventional commits format
"""

import sys
import re
from pathlib import Path

# Valid commit types
VALID_TYPES = ['feat', 'fix', 'docs', 'refactor', 'perf', 'test', 'chore']

# Scopes related to .agents
VALID_SCOPES = [
    'Phase 1', 'Phase 2', 'Phase 3', 'Phase 4',
    'Machine Learning', 'Multi-Engine', 'Custom Tools',
    'Skills', 'Validation', 'Documentation', 'Hooks',
    'CLI', 'Framework', 'Agent Hierarchy',
    'Materials System', 'UI Toolkit', 'Terrain System',
    'Animation System', 'Graphics & VFX', 'Debugging & Tools',
    'Advanced Systems', 'ML Integration', 'Tools & Extensions'
]


class CommitMessageValidator:
    """Validates commit message format."""

    def __init__(self, message_file: str):
        self.message_file = Path(message_file)
        self.message = ""
        self.errors = []

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

        # Validate format: Type: Description (SCOPE)
        pattern = r'^(feat|fix|docs|refactor|perf|test|chore):\s+(.+)\s+\((.+)\)$'
        match = re.match(pattern, subject)

        if not match:
            self.errors.append(
                f"Invalid format: '{subject}'\n"
                f"Expected: 'Type: Description (SCOPE)'\n"
                f"Valid types: {', '.join(VALID_TYPES)}"
            )
            return False

        commit_type, description, scope = match.groups()

        # Validate type
        if commit_type not in VALID_TYPES:
            self.errors.append(f"Invalid type: '{commit_type}'. Valid types: {', '.join(VALID_TYPES)}")
            return False

        # Validate description
        if len(description) < 5:
            self.errors.append(f"Description too short: '{description}' (minimum 5 characters)")
            return False

        if len(description) > 70:
            self.errors.append(f"Description too long: {len(description)} chars (maximum 70)")
            return False

        # Description should start with lowercase (unless special term)
        if description[0].isupper() and description[0:2] not in ['ML', 'AI', 'UI', 'VR', 'XR', 'CI']:
            self.errors.append(f"Description should start with lowercase: '{description}'")
            return False

        # Validate scope (warning level)
        if scope not in VALID_SCOPES:
            print(f"WARNING: Non-standard scope '{scope}' (consider using standard scopes)")
            print(f"Standard scopes: {', '.join(VALID_SCOPES[:5])} ...")

        # Validate scope format
        if '(' in scope or ')' in scope or ',' in scope:
            self.errors.append(f"Invalid scope format: '{scope}' (avoid parentheses)")
            return False

        return True

    def print_result(self) -> int:
        """Print validation result."""
        if self.errors:
            print("=" * 70)
            print("COMMIT MESSAGE VALIDATION FAILED")
            print("=" * 70)
            print()
            for error in self.errors:
                print(f"✗ {error}\n")

            print("=" * 70)
            print("REQUIRED FORMAT")
            print("=" * 70)
            print("Type: Description (SCOPE)")
            print()
            print("Valid Types:")
            for commit_type in VALID_TYPES:
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
            print("✓ Commit message validation passed!")
            return 0


def main() -> int:
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python pre-commit-message.py <message-file>")
        return 1

    validator = CommitMessageValidator(sys.argv[1])

    if not validator.load_message():
        print("\n".join(f"✗ {e}" for e in validator.errors))
        return 1

    if not validator.validate():
        return validator.print_result()

    return validator.print_result()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
