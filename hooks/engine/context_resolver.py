"""
Context Resolver for Dynamic Hooks System
Detects current phase and environment automatically
"""

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from datetime import datetime
import yaml

class ContextResolver:
    """
    Detects current validation context (phase, environment, branch)
    based on multiple detection strategies with priority order
    """

    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize context resolver

        Args:
            config: Context detection configuration from hooks-context.yaml
        """
        self.config = config or {}
        self.detection_cache = {}

    def resolve(self) -> str:
        """
        Resolve current context name with highest priority match

        Returns:
            Context name (e.g., 'phase_5_enrichment', 'ci_strict', 'local_development')
        """
        # Check cache
        if "resolved_context" in self.detection_cache:
            return self.detection_cache["resolved_context"]

        # Try detection in priority order
        detection_methods = [
            ("env_var", self._detect_env_var),
            ("git_branch", self._detect_git_branch),
            ("git_tag", self._detect_git_tag),
            ("version_file", self._detect_version_file),
            ("date_range", self._detect_date_range),
        ]

        context_detection = self.config.get("context_detection", {})
        merged_rules = {}

        # Merge all detection rules by priority
        for method_name, method_func in detection_methods:
            if method_name in context_detection:
                merged_rules[method_name] = context_detection[method_name]

        # Detect context based on priority
        for method_name, method_func in detection_methods:
            if method_name in merged_rules:
                context = method_func(merged_rules[method_name])
                if context:
                    self.detection_cache["resolved_context"] = context
                    return context

        # Fallback to default
        context = self.config.get("context_detection", {}).get("fallback", {}).get("context", "default")
        self.detection_cache["resolved_context"] = context
        return context

    def _detect_env_var(self, rules: Dict[str, Any]) -> Optional[str]:
        """
        Detect context from environment variable (highest priority)

        Expected format:
        - HOOKS_CONTEXT=phase_5_enrichment
        - HOOKS_CONTEXT=ci_strict
        """
        var_name = rules.get("variable", "HOOKS_CONTEXT")
        var_value = os.getenv(var_name)

        if not var_value:
            return None

        # If pattern matching is enabled, extract phase number
        if rules.get("extract_phase"):
            match = re.search(r"phase_(\d+)", var_value)
            if match:
                return f"phase_{match.group(1)}"

        return var_value

    def _detect_git_branch(self, rules: Dict[str, Any]) -> Optional[str]:
        """
        Detect context from current git branch

        Expected format:
        - main, master → 'main' context
        - develop → 'develop' context
        - feature/* → 'feature' context
        - hotfix/*, phase-5 → from branch name
        """
        try:
            current_branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

        # Check exact branch contexts
        branches = self.config.get("branches", {})
        if current_branch in branches:
            return current_branch

        # Check wildcard patterns
        for pattern, context_name in branches.items():
            if "*" in pattern:
                # Convert glob pattern to regex
                regex_pattern = pattern.replace("*", ".*")
                if re.match(f"^{regex_pattern}$", current_branch):
                    return context_name

        return None

    def _detect_git_tag(self, rules: Dict[str, Any]) -> Optional[str]:
        """
        Detect context from git tags

        Expected format:
        - phase-4, phase-5 → 'phase_4', 'phase_5'
        """
        try:
            # Get current commit
            current_commit = subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()

            # Get tags pointing to current commit
            tags = subprocess.check_output(
                ["git", "tag", "--points-at", current_commit],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip().split("\n")

            tags = [t for t in tags if t]  # Remove empty strings

            # Look for phase tags
            pattern = rules.get("pattern", "^phase-\\d+$")
            for tag in tags:
                if re.match(pattern, tag):
                    if rules.get("extract_phase"):
                        # Extract phase number: phase-5 → 5
                        match = re.search(r"phase-(\d+)", tag)
                        if match:
                            return f"phase_{match.group(1)}"
                    return tag

        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

        return None

    def _detect_version_file(self, rules: Dict[str, Any]) -> Optional[str]:
        """
        Detect context from version file

        Expected format in .agents/version.yaml:
        current_phase: 5
        """
        path = rules.get("path", ".agents/version.yaml")
        field = rules.get("field", "current_phase")

        if not Path(path).exists():
            return None

        try:
            with open(path, 'r') as f:
                version_data = yaml.safe_load(f) or {}

            phase = version_data.get(field)
            if phase:
                return f"phase_{phase}"

        except (yaml.YAMLError, IOError):
            pass

        return None

    def _detect_date_range(self, rules: Dict[str, Any]) -> Optional[str]:
        """
        Detect context based on date ranges

        Expected format:
        ranges:
          - phase: 4
            start: "2026-02-01"
            end: "2026-04-30"
        """
        ranges = rules.get("ranges", [])
        today = datetime.now().date()

        for range_item in ranges:
            phase = range_item.get("phase")
            start_str = range_item.get("start")
            end_str = range_item.get("end")

            try:
                start = datetime.strptime(start_str, "%Y-%m-%d").date()
                end = datetime.strptime(end_str, "%Y-%m-%d").date()

                if start <= today <= end:
                    return f"phase_{phase}"

            except (ValueError, TypeError):
                continue

        return None

    def detect_environment(self) -> str:
        """
        Detect whether running in CI/CD or locally

        Returns:
            'ci_strict' if in GitHub Actions, else 'local_development'
        """
        # Check GitHub Actions environment
        if os.getenv("GITHUB_ACTIONS") == "true" or os.getenv("CI") == "true":
            return "ci_strict"

        # Check for git pre-commit hook
        if os.getenv("PRE_COMMIT") == "true":
            return "pre_commit"

        # Default to local
        return "local_development"

    def get_detection_info(self) -> Dict[str, Any]:
        """
        Get detailed detection information for debugging

        Returns:
            Dictionary with detection results
        """
        return {
            "context": self.resolve(),
            "environment": self.detect_environment(),
            "branch": self._detect_git_branch(self.config.get("context_detection", {}).get("branch", {})),
            "phase_detected_by": self._get_detection_method(),
            "timestamp": datetime.now().isoformat(),
        }

    def _get_detection_method(self) -> str:
        """Get name of detection method that matched"""
        if os.getenv("HOOKS_CONTEXT"):
            return "env_var:HOOKS_CONTEXT"

        try:
            subprocess.check_output(
                ["git", "rev-parse", "--git-dir"],
                stderr=subprocess.DEVNULL
            )
            # Git is available, check which method matched
            if self._detect_version_file(self.config.get("context_detection", {}).get("version_file", {})):
                return "version_file"
            if self._detect_git_tag(self.config.get("context_detection", {}).get("git_tag", {})):
                return "git_tag"
            if self._detect_git_branch(self.config.get("context_detection", {}).get("git_branch", {})):
                return "git_branch"

        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

        if self._detect_date_range(self.config.get("context_detection", {}).get("date_range", {})):
            return "date_range"

        return "fallback:default"

    def clear_cache(self):
        """Clear detection cache"""
        self.detection_cache.clear()


class EnvironmentInfo:
    """Helper class for environment information"""

    @staticmethod
    def is_ci() -> bool:
        """Check if running in CI/CD environment"""
        return (
            os.getenv("GITHUB_ACTIONS") == "true" or
            os.getenv("CI") == "true" or
            os.getenv("GITLAB_CI") == "true" or
            os.getenv("CIRCLECI") == "true"
        )

    @staticmethod
    def is_docker() -> bool:
        """Check if running in Docker"""
        return Path("/.dockerenv").exists()

    @staticmethod
    def is_git_repo() -> bool:
        """Check if current directory is git repository"""
        try:
            subprocess.check_output(
                ["git", "rev-parse", "--git-dir"],
                stderr=subprocess.DEVNULL
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    @staticmethod
    def get_current_branch() -> Optional[str]:
        """Get current git branch"""
        try:
            return subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None
