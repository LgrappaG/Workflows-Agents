"""
Safe Operations System
======================

Wraps file I/O and subprocess operations with security checks and audit logging.
Prevents unauthorized file modifications and shell injection attacks.

Integration Points:
- StateManager._persist_state() - Safe checkpoint writing
- BaseAgent.execute() - Safe subprocess execution
- All file writes in orchestration

Security Features:
- Path validation (whitelist/blacklist)
- Backup creation before writes
- Audit trail logging
- Atomic writes with fsync
"""

import os
import sys
import shutil
import logging
import json
import hashlib
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class PathAccessLevel(Enum):
    """Access control levels for filesystem paths"""
    ALLOW = "allow"
    WARN = "warn"
    DENY = "deny"


@dataclass
class FileOperation:
    """Audit log entry for file operation"""
    timestamp: str
    operation: str  # 'write', 'read', 'delete', 'rename'
    path: str
    size_bytes: int
    hash_sha256: Optional[str] = None
    backup_created: bool = False
    access_level: str = "allow"
    success: bool = True
    error: Optional[str] = None


class SafeFileOperations:
    """
    Protected file operations wrapper.

    All agents should use this instead of open(), write(), etc.
    Provides audit logging, backup/recovery, and policy enforcement.
    """

    # Hard boundaries - paths that must never be modified
    PROTECTED_PATHS = {
        "/etc": PathAccessLevel.DENY,
        "/sys": PathAccessLevel.DENY,
        "/proc": PathAccessLevel.DENY,
        "/root": PathAccessLevel.DENY,
        "~/.ssh": PathAccessLevel.DENY,
        "~/.kube": PathAccessLevel.DENY,
    }

    # Allowed paths for .agents
    ALLOWED_PATHS = {
        ".agents/skills": PathAccessLevel.ALLOW,
        ".agents/workflows": PathAccessLevel.ALLOW,
        ".agents/state": PathAccessLevel.ALLOW,
        ".agents/logs": PathAccessLevel.ALLOW,
        ".agents/backups": PathAccessLevel.ALLOW,
    }

    def __init__(self, audit_log_path: str = ".agents/logs/audit.jsonl"):
        self.audit_log_path = Path(audit_log_path)
        self.audit_log_path.parent.mkdir(parents=True, exist_ok=True)
        self.backup_dir = Path(".agents/backups")
        self.backup_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"SafeFileOperations initialized. Audit log: {self.audit_log_path}")

    def write_file(
        self,
        path: str,
        content: str,
        mode: str = "w",
        create_backup: bool = True
    ) -> bool:
        """
        Safely write file with validation and audit logging.

        Args:
            path: File path to write
            content: Content to write
            mode: File open mode ('w', 'a', 'w+')
            create_backup: Whether to backup existing file first

        Returns:
            True if write successful

        Raises:
            PermissionError: If path is denied
            OSError: If write fails
        """

        path_obj = Path(path).resolve()

        # 1. Check access policy
        access_level = self._check_path_access(str(path_obj))
        if access_level == PathAccessLevel.DENY:
            error_msg = f"Access DENIED to path: {path}"
            logger.error(error_msg)
            self._log_operation(
                operation="write",
                path=str(path_obj),
                size_bytes=len(content),
                access_level=access_level.value,
                success=False,
                error=error_msg
            )
            raise PermissionError(error_msg)

        try:
            # 2. Create backup if file exists
            backup_path = None
            if create_backup and path_obj.exists():
                backup_path = self._create_backup(path_obj)

            # 3. Write file atomically
            # Write to temp file first
            temp_path = path_obj.parent / f".{path_obj.name}.tmp"

            with open(temp_path, mode) as f:
                f.write(content)
                # Ensure data is written to disk
                f.flush()
                os.fsync(f.fileno())

            # Atomic rename
            temp_path.replace(path_obj)

            # 4. Calculate hash for audit log
            content_hash = hashlib.sha256(content.encode()).hexdigest()

            # 5. Log operation
            self._log_operation(
                operation="write",
                path=str(path_obj),
                size_bytes=len(content),
                hash_sha256=content_hash,
                backup_created=backup_path is not None,
                access_level=access_level.value,
                success=True
            )

            logger.info(
                f"File write OK: {path_obj} ({len(content)} bytes) "
                f"sha256={content_hash[:12]}..."
            )
            return True

        except Exception as e:
            logger.error(f"File write FAILED: {path} - {e}")
            self._log_operation(
                operation="write",
                path=str(path_obj),
                size_bytes=len(content),
                access_level=access_level.value,
                success=False,
                error=str(e)
            )
            raise

    def read_file(self, path: str) -> str:
        """
        Safely read file with audit logging.

        Args:
            path: File path to read

        Returns:
            File contents

        Raises:
            PermissionError: If path is denied
            FileNotFoundError: If file doesn't exist
        """

        path_obj = Path(path).resolve()

        # Check access policy
        access_level = self._check_path_access(str(path_obj))
        if access_level == PathAccessLevel.DENY:
            error_msg = f"Access DENIED to read: {path}"
            logger.error(error_msg)
            raise PermissionError(error_msg)

        try:
            with open(path_obj, "r") as f:
                content = f.read()

            # Log operation
            self._log_operation(
                operation="read",
                path=str(path_obj),
                size_bytes=len(content),
                access_level=access_level.value,
                success=True
            )

            return content

        except Exception as e:
            logger.error(f"File read FAILED: {path} - {e}")
            self._log_operation(
                operation="read",
                path=str(path_obj),
                size_bytes=0,
                access_level=access_level.value,
                success=False,
                error=str(e)
            )
            raise

    def _check_path_access(self, path: str) -> PathAccessLevel:
        """
        Check if path access is allowed based on policies.

        Returns:
            PathAccessLevel.ALLOW, WARN, or DENY
        """

        # Check deny list first
        for protected_path, level in self.PROTECTED_PATHS.items():
            if protected_path in path:
                return level

        # Check allow list
        for allowed_path, level in self.ALLOWED_PATHS.items():
            if allowed_path in path:
                return level

        # Default: warn on unknown paths
        logger.warning(f"Path access WARN (not in allowlist): {path}")
        return PathAccessLevel.WARN

    def _create_backup(self, path: Path) -> Optional[str]:
        """
        Create backup copy of file before modification.

        Returns:
            Path to backup file, or None if backup failed
        """

        try:
            timestamp = datetime.now().isoformat().replace(":", "-")
            backup_name = f"{path.stem}_{timestamp}.bak"
            backup_path = self.backup_dir / backup_name

            shutil.copy2(path, backup_path)
            logger.info(f"Backup created: {backup_path}")

            return str(backup_path)

        except Exception as e:
            logger.warning(f"Backup creation failed: {e}")
            return None

    def _log_operation(
        self,
        operation: str,
        path: str,
        size_bytes: int,
        hash_sha256: Optional[str] = None,
        backup_created: bool = False,
        access_level: str = "allow",
        success: bool = True,
        error: Optional[str] = None
    ):
        """
        Write operation to audit log (JSONL format).
        """

        op = FileOperation(
            timestamp=datetime.utcnow().isoformat(),
            operation=operation,
            path=path,
            size_bytes=size_bytes,
            hash_sha256=hash_sha256,
            backup_created=backup_created,
            access_level=access_level,
            success=success,
            error=error
        )

        try:
            with open(self.audit_log_path, "a") as f:
                f.write(json.dumps(asdict(op)) + "\n")
                f.flush()
                os.fsync(f.fileno())
        except Exception as e:
            logger.error(f"Failed to write audit log: {e}")


class SafeProcessExecution:
    """
    Protected subprocess execution wrapper.

    Prevents shell injection attacks by:
    - Banning shell metacharacters
    - Using allowlist of approved executables
    - Validating all arguments
    """

    # Shell metacharacters that are dangerous
    SHELL_METACHARACTERS = {'|', '&', ';', '`', '$', '(', ')', '<', '>', '\n', '\r'}

    # Approved executables (whitelist)
    APPROVED_EXECUTABLES = {
        'python',
        'python3',
        'git',
        'npm',
        'pip',
        'pip3',
        'node',
        'bash',
        'sh',
    }

    def __init__(self, audit_log_path: str = ".agents/logs/audit.jsonl"):
        self.audit_log_path = Path(audit_log_path)
        logger.info("SafeProcessExecution initialized")

    def execute_safe(
        self,
        executable: str,
        args: List[str],
        shell: bool = False
    ) -> tuple:
        """
        Execute subprocess safely with validation.

        Args:
            executable: Binary to execute (must be in allowlist)
            args: Command arguments (must not contain shell metacharacters)
            shell: Whether to use shell (always False for safety)

        Returns:
            Tuple of (return_code, stdout, stderr)

        Raises:
            PermissionError: If executable not approved
            ValueError: If shell metacharacters detected in args
        """

        import subprocess

        # 1. Check executable whitelist
        if executable not in self.APPROVED_EXECUTABLES:
            error_msg = f"Executable not approved: {executable}"
            logger.error(error_msg)
            raise PermissionError(error_msg)

        # 2. Validate arguments for shell injection
        for arg in args:
            if any(metachar in arg for metachar in self.SHELL_METACHARACTERS):
                error_msg = f"Shell metacharacter detected in args: {arg}"
                logger.error(error_msg)
                raise ValueError(error_msg)

        # 3. Execute with shell=False (always safe)
        try:
            result = subprocess.run(
                [executable] + args,
                shell=False,  # Never use shell
                capture_output=True,
                text=True,
                timeout=60
            )

            logger.info(
                f"Process executed: {executable} {' '.join(args)} "
                f"(exit code: {result.returncode})"
            )

            return (result.returncode, result.stdout, result.stderr)

        except subprocess.TimeoutExpired:
            error_msg = f"Process timeout: {executable}"
            logger.error(error_msg)
            raise TimeoutError(error_msg)
        except Exception as e:
            logger.error(f"Process execution failed: {e}")
            raise


# Singleton instances
_safe_file_ops: Optional[SafeFileOperations] = None
_safe_process: Optional[SafeProcessExecution] = None


def get_safe_file_operations() -> SafeFileOperations:
    """Get or create global SafeFileOperations instance"""
    global _safe_file_ops
    if _safe_file_ops is None:
        _safe_file_ops = SafeFileOperations()
    return _safe_file_ops


def get_safe_process_execution() -> SafeProcessExecution:
    """Get or create global SafeProcessExecution instance"""
    global _safe_process
    if _safe_process is None:
        _safe_process = SafeProcessExecution()
    return _safe_process
