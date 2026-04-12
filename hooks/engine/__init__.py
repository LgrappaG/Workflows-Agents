"""
Dynamic Hooks Engine - Core orchestrator for dynamic validation system

Provides the main DynamicHooksEngine class that ties together:
- Configuration loading
- Context detection
- Plugin management
- Validation execution
- Learning/metrics tracking
"""

from .configuration_loader import ConfigurationLoader, ConfigurationValidator
from .context_resolver import ContextResolver, EnvironmentInfo
from .plugin_manager import PluginManager
from .learning_engine import LearningEngine

__version__ = "1.0.0"
__all__ = [
    "DynamicHooksEngine",
    "ConfigurationLoader",
    "ContextResolver",
    "PluginManager",
    "LearningEngine",
    "ConfigurationValidator",
    "EnvironmentInfo",
]
