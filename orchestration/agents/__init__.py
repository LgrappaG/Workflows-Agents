"""
Orchestration Agents
====================

4 specialized agents for autonomous goal execution:
- Deploy Agent: Build, package, release, verify
- Sync Agent: Pull, push, merge, conflict resolution
- Validation Agent: 8-gate quality checks
- Knowledge Agent: Learning, optimization, suggestions
"""

from orchestration.agents.base_agent import BaseAgent
from orchestration.agents.deploy_agent import DeployAgent
from orchestration.agents.sync_agent import SyncAgent
from orchestration.agents.validation_agent import ValidationAgent
from orchestration.agents.knowledge_agent import KnowledgeAgent

__all__ = [
    "BaseAgent",
    "DeployAgent",
    "SyncAgent",
    "ValidationAgent",
    "KnowledgeAgent"
]
