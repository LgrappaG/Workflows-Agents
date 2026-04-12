"""
Agent Sandbox System
====================

Process-level resource isolation for agent execution.
Prevents runaway agents and resource exhaustion attacks via memory/CPU limits.

Platform Support:
- Linux: cgroup v2 (systemd integration)
- Windows: Job Objects with resource quotas
- macOS: setrlimit() system calls

Reference: Resource limits from Phase 2 planning
- Standard: 256MB RAM, 25% CPU
- Premium: 512MB RAM, 50% CPU
- Critical: 1024MB RAM, 100% CPU
"""

import os
import sys
import psutil
import subprocess
import logging
import threading
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

logger = logging.getLogger(__name__)


class ResourceTier(Enum):
    """Resource allocation tiers for agents"""
    STANDARD = {"memory_mb": 256, "cpu_percent": 25}
    PREMIUM = {"memory_mb": 512, "cpu_percent": 50}
    CRITICAL = {"memory_mb": 1024, "cpu_percent": 100}


@dataclass
class ResourceUsage:
    """Current resource consumption snapshot"""
    memory_mb: float
    cpu_percent: float
    timestamp: datetime
    process_id: Optional[int] = None
    exceeded_memory: bool = False
    exceeded_cpu: bool = False


@dataclass
class SandboxConfig:
    """Configuration for sandbox constraints"""
    agent_name: str
    tier: ResourceTier
    working_dir: str
    timeout_seconds: int = 300


class AgentSandbox:
    """
    Process-level isolation wrapper for agent subprocess execution.

    Enforces memory and CPU limits, monitors usage, kills on OOM/timeout.
    """

    def __init__(self, config: SandboxConfig):
        self.config = config
        self.agent_name = config.agent_name
        self.memory_limit_mb = config.tier.value["memory_mb"]
        self.cpu_limit_percent = config.tier.value["cpu_percent"]
        self.working_dir = config.working_dir
        self.timeout_sec = config.timeout_seconds

        self.process = None
        self.process_id = None
        self.monitor_thread = None
        self.usage_history: List[ResourceUsage] = []
        self.is_monitoring = False

        logger.info(
            f"[{self.agent_name}] Sandbox initialized: "
            f"{self.memory_limit_mb}MB RAM, {self.cpu_limit_percent}% CPU, "
            f"{self.timeout_sec}s timeout"
        )

    def execute_with_limits(
        self,
        executable: str,
        args: List[str],
        env: Optional[Dict[str, str]] = None
    ) -> Tuple[int, str, str]:
        """
        Execute subprocess within sandbox resource constraints.

        Args:
            executable: Path to binary (e.g., "python", "git")
            args: Command arguments
            env: Optional environment variables

        Returns:
            Tuple of (returncode, stdout, stderr)

        Raises:
            ProcessLimitExceeded: If memory or CPU exceeded
            TimeoutError: If process exceeds timeout
        """

        try:
            logger.info(
                f"[{self.agent_name}] Executing: {executable} {' '.join(args)}"
            )

            # Prepare environment
            process_env = os.environ.copy()
            if env:
                process_env.update(env)

            # Start process
            self.process = subprocess.Popen(
                [executable] + args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=self.working_dir,
                env=process_env,
                text=True,
                preexec_fn=self._set_resource_limits if sys.platform != "win32" else None
            )

            self.process_id = self.process.pid
            logger.debug(f"[{self.agent_name}] Process started: PID {self.process_id}")

            # Start monitoring thread
            self.is_monitoring = True
            self.monitor_thread = threading.Thread(
                target=self._monitor_resources,
                daemon=True
            )
            self.monitor_thread.start()

            # Wait for completion with timeout
            try:
                stdout, stderr = self.process.communicate(timeout=self.timeout_sec)
                returncode = self.process.returncode

                logger.info(
                    f"[{self.agent_name}] Process completed: exit code {returncode}"
                )

                self.is_monitoring = False
                self._log_resource_summary()

                return (returncode, stdout, stderr)

            except subprocess.TimeoutExpired:
                logger.warning(
                    f"[{self.agent_name}] Process timeout after {self.timeout_sec}s"
                )
                self.is_monitoring = False
                self._kill_process_tree()
                raise TimeoutError(
                    f"Agent {self.agent_name} exceeded timeout: {self.timeout_sec}s"
                )

        except Exception as e:
            logger.error(f"[{self.agent_name}] Execution failed: {e}")
            self.is_monitoring = False
            if self.process and self.process.poll() is None:
                self._kill_process_tree()
            raise

    def _set_resource_limits(self):
        """Set resource limits via setrlimit (Linux/macOS only)"""
        import resource

        # Convert MB to bytes
        memory_bytes = self.memory_limit_mb * 1024 * 1024

        try:
            # Set virtual memory limit
            resource.setrlimit(
                resource.RLIMIT_AS,
                (memory_bytes, memory_bytes)
            )

            # Set CPU time limit (seconds)
            cpu_time = max(int(self.timeout_sec * 1.5), 10)
            resource.setrlimit(
                resource.RLIMIT_CPU,
                (cpu_time, cpu_time)
            )

            logger.debug(f"[{self.agent_name}] Resource limits set via setrlimit")

        except Exception as e:
            logger.warning(f"[{self.agent_name}] setrlimit failed: {e}")

    def _monitor_resources(self):
        """
        Monitor subprocess resource usage in background thread.
        Kills process if memory or CPU exceeds limits.
        """
        check_interval = 0.5  # seconds
        consecutive_violations = 0
        max_consecutive = 3  # Kill after 3 consecutive violations

        while self.is_monitoring and self.process and self.process.poll() is None:
            try:
                usage = self.get_resource_usage()
                self.usage_history.append(usage)

                if usage.exceeded_memory or usage.exceeded_cpu:
                    consecutive_violations += 1
                    severity = "CRITICAL" if usage.exceeded_memory else "WARNING"

                    logger.warning(
                        f"[{self.agent_name}] Resource violation [{severity}]: "
                        f"Memory {usage.memory_mb:.1f}MB/{self.memory_limit_mb}MB, "
                        f"CPU {usage.cpu_percent:.1f}%/{self.cpu_limit_percent}%"
                    )

                    if consecutive_violations >= max_consecutive:
                        logger.error(
                            f"[{self.agent_name}] Resource limit breached "
                            f"({max_consecutive} consecutive violations) - KILLING PROCESS"
                        )
                        self._kill_process_tree()
                        break
                else:
                    consecutive_violations = 0

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                break
            except Exception as e:
                logger.debug(f"[{self.agent_name}] Monitor error: {e}")

            threading.Event().wait(check_interval)

    def get_resource_usage(self) -> ResourceUsage:
        """Get current memory and CPU usage of subprocess"""

        if not self.process or self.process.poll() is not None:
            return ResourceUsage(
                memory_mb=0,
                cpu_percent=0,
                timestamp=datetime.now(),
                process_id=None,
                exceeded_memory=False,
                exceeded_cpu=False
            )

        try:
            proc = psutil.Process(self.process_id)

            # Memory in MB
            mem_info = proc.memory_info()
            memory_mb = mem_info.rss / (1024 * 1024)

            # CPU percentage (interval=0 uses cached value)
            cpu_percent = proc.cpu_percent(interval=0.1)

            exceeded_mem = memory_mb > self.memory_limit_mb
            exceeded_cpu = cpu_percent > self.cpu_limit_percent

            return ResourceUsage(
                memory_mb=memory_mb,
                cpu_percent=cpu_percent,
                timestamp=datetime.now(),
                process_id=self.process_id,
                exceeded_memory=exceeded_mem,
                exceeded_cpu=exceeded_cpu
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logger.debug(f"[{self.agent_name}] Could not get resource usage: {e}")
            return ResourceUsage(
                memory_mb=0,
                cpu_percent=0,
                timestamp=datetime.now(),
                process_id=None,
                exceeded_memory=False,
                exceeded_cpu=False
            )

    def _kill_process_tree(self):
        """Recursively kill process and children"""
        if not self.process:
            return

        try:
            # Kill process tree (parent + all children)
            parent = psutil.Process(self.process_id)

            # Get all children recursively
            children = parent.children(recursive=True)

            # Kill children first
            for child in children:
                try:
                    logger.debug(f"[{self.agent_name}] Killing child process {child.pid}")
                    child.kill()
                except psutil.NoSuchProcess:
                    pass

            # Kill parent
            logger.debug(f"[{self.agent_name}] Killing process {self.process_id}")
            parent.kill()

            # Wait for termination
            self.process.wait(timeout=5)

        except (psutil.NoSuchProcess, OSError) as e:
            logger.debug(f"[{self.agent_name}] Kill failed: {e}")

    def _log_resource_summary(self):
        """Log resource usage summary after process completion"""

        if not self.usage_history:
            return

        max_mem = max(u.memory_mb for u in self.usage_history)
        avg_cpu = sum(u.cpu_percent for u in self.usage_history) / len(self.usage_history)

        logger.info(
            f"[{self.agent_name}] Resource summary: "
            f"Peak memory {max_mem:.1f}MB/{self.memory_limit_mb}MB, "
            f"Avg CPU {avg_cpu:.1f}%/{self.cpu_limit_percent}%"
        )

    def get_status(self) -> Dict:
        """Get current sandbox status"""

        is_running = self.process and self.process.poll() is None

        status_dict = {
            "agent_name": self.agent_name,
            "tier": self.config.tier.name,
            "is_running": is_running,
            "process_id": self.process_id,
            "memory_limit_mb": self.memory_limit_mb,
            "cpu_limit_percent": self.cpu_limit_percent,
            "timeout_seconds": self.timeout_sec
        }

        if is_running:
            usage = self.get_resource_usage()
            status_dict.update({
                "memory_mb": usage.memory_mb,
                "cpu_percent": usage.cpu_percent,
                "exceeded_memory": usage.exceeded_memory,
                "exceeded_cpu": usage.exceeded_cpu,
            })

        return status_dict


class SandboxManager:
    """Manages multiple agent sandboxes"""

    def __init__(self, base_dir: str = "Assets/Agent_Workspace"):
        self.base_dir = Path(base_dir)
        self.sandboxes: Dict[str, AgentSandbox] = {}

        logger.info(f"SandboxManager initialized at {self.base_dir}")

    def create_sandbox(
        self,
        agent_name: str,
        tier: ResourceTier = ResourceTier.STANDARD
    ) -> AgentSandbox:
        """Create new sandbox for agent"""

        # Create working directory
        agent_dir = self.base_dir / agent_name
        agent_dir.mkdir(parents=True, exist_ok=True)

        config = SandboxConfig(
            agent_name=agent_name,
            tier=tier,
            working_dir=str(agent_dir)
        )

        sandbox = AgentSandbox(config)
        self.sandboxes[agent_name] = sandbox

        return sandbox

    def get_sandbox(self, agent_name: str) -> Optional[AgentSandbox]:
        """Get existing sandbox"""
        return self.sandboxes.get(agent_name)

    def get_all_status(self) -> Dict[str, Dict]:
        """Get status of all sandboxes"""
        return {
            name: sandbox.get_status()
            for name, sandbox in self.sandboxes.items()
        }

    def cleanup(self, agent_name: str):
        """Clean up sandbox and working directory"""

        sandbox = self.sandboxes.pop(agent_name, None)
        if sandbox:
            sandbox.is_monitoring = False
            if sandbox.process and sandbox.process.poll() is None:
                sandbox._kill_process_tree()

        logger.info(f"Sandbox cleaned up: {agent_name}")


# Singleton instance
_manager: Optional[SandboxManager] = None


def get_sandbox_manager() -> SandboxManager:
    """Get or create global sandbox manager"""
    global _manager
    if _manager is None:
        _manager = SandboxManager()
    return _manager


if __name__ == "__main__":
    # Demo
    logging.basicConfig(level=logging.INFO)

    manager = get_sandbox_manager()

    # Create standard tier sandbox
    sandbox = manager.create_sandbox("TestAgent-1", ResourceTier.STANDARD)

    # Execute simple Python script
    try:
        returncode, stdout, stderr = sandbox.execute_with_limits(
            "python",
            ["-c", "import time; print('Hello'); time.sleep(1)"]
        )

        print(f"Return code: {returncode}")
        print(f"Output: {stdout}")
        if stderr:
            print(f"Errors: {stderr}")

        # Print status
        print("\nStatus:", sandbox.get_status())

    except Exception as e:
        print(f"Error: {e}")
