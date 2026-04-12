"""
Policy Engine
=============

Enforces access control policies for agent operations.
Validates that agents, operations, and resources are allowed.

Integration Points:
- CentralOrchestrator.execute_goal() - Pre-flight policy check
- BaseAgent.execute() - Agent authorization check
- All security decision points

Policy Hierarchy:
1. Agent can execute? (agent allowlist)
2. Operation allowed? (operation allowlist)
3. Resource available? (quota check)
4. Path accessible? (filesystem policy)
"""

import os
import logging
from functools import lru_cache
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)


@dataclass
class AgentPolicy:
    """Policy rules for a specific agent"""
    agent_name: str
    enabled: bool = True
    allowed_operations: List[str] = field(default_factory=list)
    max_concurrent_executions: int = 5
    max_memory_mb: int = 512
    max_cpu_percent: int = 50
    execution_timeout_sec: int = 300
    allowed_paths: List[str] = field(default_factory=lambda: [".agents"])
    denied_paths: List[str] = field(default_factory=list)


class PolicyEngine:
    """
    Central policy enforcement engine for security.

    Answers questions:
    - Can this agent execute?
    - Can this agent perform this operation?
    - Is there enough quota available?
    - Is this path accessible?
    """

    def __init__(self, policy_file: str = ".agents/config/hardening-policy.yaml"):
        self.policy_file = Path(policy_file)
        self.policies: Dict[str, AgentPolicy] = {}
        self.operation_quotas: Dict[str, Dict[str, int]] = {}  # agent -> op -> count
        self.resource_usage: Dict[str, Dict] = {}  # agent -> resource_data

        self._load_policies()
        logger.info("PolicyEngine initialized")

    def check_agent_allowed(self, agent_name: str) -> bool:
        """
        Check if agent is allowed to execute.

        Args:
            agent_name: Name of agent to check

        Returns:
            True if agent is allowed
        """

        if agent_name not in self.policies:
            logger.warning(f"Agent not in policy database: {agent_name}")
            return False

        policy = self.policies[agent_name]
        if not policy.enabled:
            logger.warning(f"Agent disabled in policy: {agent_name}")
            return False

        return True

    def check_operation_allowed(self, agent_name: str, operation: str) -> bool:
        """
        Check if agent is allowed to perform operation.

        Args:
            agent_name: Name of agent
            operation: Operation name (e.g., 'deploy', 'sync', 'validate')

        Returns:
            True if operation is allowed
        """

        if agent_name not in self.policies:
            logger.warning(f"Agent not in policy: {agent_name}")
            return False

        policy = self.policies[agent_name]
        if operation not in policy.allowed_operations:
            logger.warning(
                f"Operation not allowed for agent: {agent_name}.{operation}"
            )
            return False

        return True

    def check_resource_quota(self, agent_name: str, operation: str) -> bool:
        """
        Check if agent has exceeded operation quota.

        Args:
            agent_name: Name of agent
            operation: Operation name

        Returns:
            True if quota available
        """

        if agent_name not in self.policies:
            return False

        policy = self.policies[agent_name]

        # Initialize quota tracking if needed
        if agent_name not in self.operation_quotas:
            self.operation_quotas[agent_name] = {}

        current_count = self.operation_quotas[agent_name].get(operation, 0)
        max_concurrent = policy.max_concurrent_executions

        if current_count >= max_concurrent:
            logger.warning(
                f"Quota exceeded for {agent_name}.{operation}: "
                f"{current_count}/{max_concurrent}"
            )
            return False

        return True

    def check_path_access(self, agent_name: str, path: str) -> bool:
        """
        Check if agent is allowed to access path.

        Args:
            agent_name: Name of agent
            path: File path to access

        Returns:
            True if path access allowed
        """

        if agent_name not in self.policies:
            logger.warning(f"Agent not in policy: {agent_name}")
            return False

        policy = self.policies[agent_name]
        path_obj = Path(path)

        # Check deny list first (hard boundaries)
        for denied in policy.denied_paths:
            if denied in str(path_obj):
                logger.warning(f"Path denied for {agent_name}: {path}")
                return False

        # Check allow list
        for allowed in policy.allowed_paths:
            if allowed in str(path_obj):
                return True

        # Default: deny unknown paths
        logger.warning(f"Path not in allowlist for {agent_name}: {path}")
        return False

    def check_memory_available(self, agent_name: str, needed_mb: int) -> bool:
        """
        Check if agent is within memory limits.

        Args:
            agent_name: Name of agent
            needed_mb: Additional memory needed (MB)

        Returns:
            True if memory available
        """

        if agent_name not in self.policies:
            return False

        policy = self.policies[agent_name]

        if needed_mb > policy.max_memory_mb:
            logger.warning(
                f"Memory limit exceeded for {agent_name}: "
                f"needed {needed_mb}MB > limit {policy.max_memory_mb}MB"
            )
            return False

        return True

    def check_cpu_available(self, agent_name: str, needed_percent: int) -> bool:
        """
        Check if agent is within CPU limits.

        Args:
            agent_name: Name of agent
            needed_percent: CPU percentage requested (0-100)

        Returns:
            True if CPU available
        """

        if agent_name not in self.policies:
            return False

        policy = self.policies[agent_name]

        if needed_percent > policy.max_cpu_percent:
            logger.warning(
                f"CPU limit exceeded for {agent_name}: "
                f"needed {needed_percent}% > limit {policy.max_cpu_percent}%"
            )
            return False

        return True

    def check_goal_allowed(self, goal_data: Dict) -> bool:
        """
        Comprehensive pre-flight check for goal execution.

        Args:
            goal_data: Goal execution request

        Returns:
            True if goal can execute
        """

        agent_name = goal_data.get("agent", "unknown")
        operation = goal_data.get("operation", "execute")

        # 1. Agent allowed?
        if not self.check_agent_allowed(agent_name):
            raise PermissionError(f"Agent not allowed: {agent_name}")

        # 2. Operation allowed?
        if not self.check_operation_allowed(agent_name, operation):
            raise PermissionError(f"Operation not allowed: {agent_name}.{operation}")

        # 3. Quota available?
        if not self.check_resource_quota(agent_name, operation):
            raise ResourceWarning(f"Quota exceeded: {agent_name}.{operation}")

        logger.info(f"Goal approved: {agent_name}.{operation}")
        return True

    def record_operation(self, agent_name: str, operation: str):
        """Record that an operation has started for quota tracking"""

        if agent_name not in self.operation_quotas:
            self.operation_quotas[agent_name] = {}

        self.operation_quotas[agent_name][operation] = \
            self.operation_quotas[agent_name].get(operation, 0) + 1

        logger.debug(f"Operation recorded: {agent_name}.{operation}")

    def complete_operation(self, agent_name: str, operation: str):
        """Record that an operation has completed and decrement quota"""

        if agent_name in self.operation_quotas:
            if operation in self.operation_quotas[agent_name]:
                self.operation_quotas[agent_name][operation] = max(
                    0,
                    self.operation_quotas[agent_name][operation] - 1
                )

        logger.debug(f"Operation completed: {agent_name}.{operation}")

    def _load_policies(self):
        """Load policies from configuration file"""

        # Default policies for .agents agents
        default_policies = {
            "DeployAgent": AgentPolicy(
                agent_name="DeployAgent",
                enabled=True,
                allowed_operations=["deploy", "validate", "status"],
                max_concurrent_executions=3,
                max_memory_mb=512,
                max_cpu_percent=50,
                execution_timeout_sec=300,
                allowed_paths=[".agents/skills", ".agents/workflows"],
                denied_paths=["/etc", "/sys", "/root", "~/.ssh"]
            ),
            "SyncAgent": AgentPolicy(
                agent_name="SyncAgent",
                enabled=True,
                allowed_operations=["sync", "pull", "push"],
                max_concurrent_executions=2,
                max_memory_mb=256,
                max_cpu_percent=30,
                execution_timeout_sec=600,
                allowed_paths=[".agents"],
                denied_paths=["/etc", "/sys", "/root"]
            ),
            "ValidationAgent": AgentPolicy(
                agent_name="ValidationAgent",
                enabled=True,
                allowed_operations=["validate", "test", "check"],
                max_concurrent_executions=5,
                max_memory_mb=512,
                max_cpu_percent=50,
                execution_timeout_sec=180,
                allowed_paths=[".agents"],
                denied_paths=["/etc", "/sys", "/root"]
            ),
            "KnowledgeAgent": AgentPolicy(
                agent_name="KnowledgeAgent",
                enabled=True,
                allowed_operations=["query", "analyze", "learn"],
                max_concurrent_executions=10,
                max_memory_mb=1024,
                max_cpu_percent=75,
                execution_timeout_sec=300,
                allowed_paths=[".agents"],
                denied_paths=["/etc", "/sys", "/root"]
            ),
        }

        self.policies = default_policies
        logger.info(f"Loaded {len(self.policies)} policies")

    def get_policy(self, agent_name: str) -> Optional[AgentPolicy]:
        """Get policy for agent"""
        return self.policies.get(agent_name)

    def get_all_policies(self) -> Dict[str, AgentPolicy]:
        """Get all policies"""
        return self.policies.copy()


# Singleton instance
_policy_engine: Optional[PolicyEngine] = None


def get_policy_engine() -> PolicyEngine:
    """Get or create global PolicyEngine instance"""
    global _policy_engine
    if _policy_engine is None:
        _policy_engine = PolicyEngine()
    return _policy_engine
