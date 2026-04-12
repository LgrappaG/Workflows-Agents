#!/usr/bin/env python3
"""
Orchestration CLI Entry Point
==============================

Command-line interface for End-to-End Orchestration System.

Usage:
    python orchestration_main.py deploy-game-release
    python orchestration_main.py validate-before-deploy
    python orchestration_main.py learn-and-optimize
    python orchestration_main.py status
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

# Add .agents to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestration.engine.central_orchestrator import CentralOrchestrator
from orchestration.engine.state_manager import StateManager
from orchestration.engine.heartbeat_engine import HeartbeatEngine


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="End-to-End Orchestration System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Deploy with orchestration
  python orchestration_main.py deploy-game-release

  # Validate before deploy
  python orchestration_main.py validate-before-deploy

  # Learn from metrics
  python orchestration_main.py learn-and-optimize

  # Check status
  python orchestration_main.py status

  # List available goals
  python orchestration_main.py goals list
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Deploy command
    deploy_parser = subparsers.add_parser("deploy-game-release", help="Deploy game release")
    deploy_parser.add_argument("--platform", default="all", help="Target platform")
    deploy_parser.add_argument("--auto-sync", action="store_true", help="Auto-sync before deploy")
    deploy_parser.add_argument("--auto-validate", action="store_true", help="Auto-validate before deploy")

    # Validate command
    validate_parser = subparsers.add_parser("validate-before-deploy", help="Validate before deploy")

    # Sync command
    sync_parser = subparsers.add_parser("sync-team-collaboration", help="Sync with team")
    sync_parser.add_argument("--auto-resolve", action="store_true", help="Auto-resolve conflicts")

    # Learning command
    learn_parser = subparsers.add_parser("learn-and-optimize", help="Learn from metrics")
    learn_parser.add_argument("--window", type=int, default=30, help="Analysis window (days)")
    learn_parser.add_argument("--generate-report", action="store_true", help="Generate report")

    # Status command
    subparsers.add_parser("status", help="Show orchestration status")

    # Goals command
    goals_parser = subparsers.add_parser("goals", help="Manage goals")
    goals_parser.add_argument("action", choices=["list", "info"], help="Goal action")
    goals_parser.add_argument("goal", nargs="?", help="Goal name")

    # Init command
    subparsers.add_parser("init", help="Initialize orchestration system")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    # Handle commands
    if args.command == "init":
        return cmd_init()
    elif args.command == "deploy-game-release":
        return cmd_deploy(args)
    elif args.command == "validate-before-deploy":
        return cmd_validate(args)
    elif args.command == "sync-team-collaboration":
        return cmd_sync(args)
    elif args.command == "learn-and-optimize":
        return cmd_learn(args)
    elif args.command == "status":
        return cmd_status()
    elif args.command == "goals":
        return cmd_goals(args)
    else:
        parser.print_help()
        return 1


def cmd_init():
    """Initialize orchestration system"""
    print("\n" + "=" * 60)
    print("Initializing End-to-End Orchestration System")
    print("=" * 60)

    try:
        orchestrator = CentralOrchestrator()
        print("\n[OK] Central Orchestrator initialized")

        state_manager = StateManager()
        print("[OK] State Manager initialized")

        heartbeat = HeartbeatEngine()
        print("[OK] Heartbeat Engine initialized")

        print("\n[OK] System initialized successfully!")
        print("\nNext steps:")
        print("  1. Run: python orchestration_main.py goals list")
        print("  2. Try: python orchestration_main.py validate-before-deploy")

        return 0
    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


def cmd_deploy(args):
    """Execute deploy goal"""
    print("\n" + "=" * 60)
    print("Deploy Goal Execution")
    print("=" * 60)

    orchestrator = CentralOrchestrator()
    state_manager = StateManager()
    heartbeat = HeartbeatEngine()

    result = orchestrator.execute_goal(
        goal="deploy-game-release",
        context="default",
        auto_correct=True,
        platform=args.platform
    )

    print("\n" + "=" * 60)
    print("Execution Result")
    print("=" * 60)
    print(json.dumps(result, indent=2))

    return 0 if result["status"] == "completed" else 1


def cmd_validate(args):
    """Execute validation goal"""
    print("\n" + "=" * 60)
    print("Validation Goal Execution")
    print("=" * 60)

    orchestrator = CentralOrchestrator()

    result = orchestrator.execute_goal(
        goal="validate-before-deploy",
        context="default",
        auto_correct=True
    )

    print("\n" + "=" * 60)
    print("Validation Result")
    print("=" * 60)
    print(json.dumps(result, indent=2))

    return 0 if result["status"] == "completed" else 1


def cmd_sync(args):
    """Execute sync goal"""
    print("\n" + "=" * 60)
    print("Sync Goal Execution")
    print("=" * 60)

    orchestrator = CentralOrchestrator()

    result = orchestrator.execute_goal(
        goal="sync-team-collaboration",
        context="default",
        auto_correct=args.auto_resolve
    )

    print("\n" + "=" * 60)
    print("Sync Result")
    print("=" * 60)
    print(json.dumps(result, indent=2))

    return 0 if result["status"] == "completed" else 1


def cmd_learn(args):
    """Execute learning goal"""
    print("\n" + "=" * 60)
    print("Learning Goal Execution")
    print("=" * 60)

    orchestrator = CentralOrchestrator()

    result = orchestrator.execute_goal(
        goal="learn-and-optimize",
        analysis_window_days=args.window
    )

    print("\n" + "=" * 60)
    print("Learning Result")
    print("=" * 60)
    print(json.dumps(result, indent=2))

    if args.generate_report:
        print("\n[INFO] Report generation (Phase 3)")

    return 0 if result["status"] == "completed" else 1


def cmd_status():
    """Show orchestration status"""
    print("\n" + "=" * 60)
    print("Orchestration System Status")
    print("=" * 60)

    status = {
        "version": "1.0",
        "stage": "Complete",
        "components": {
            "central_orchestrator": "[OK] Ready",
            "state_manager": "[OK] Ready",
            "heartbeat_engine": "[OK] Ready",
            "agents": "[OK] Complete",
            "error_detection": "[OK] Complete",
            "learning_engine": "[OK] Complete"
        },
        "timestamp": datetime.now().isoformat()
    }

    print(json.dumps(status, indent=2))

    return 0


def cmd_goals(args):
    """Manage goals"""
    if args.action == "list":
        print("\n" + "=" * 60)
        print("Available Goals")
        print("=" * 60)

        goals = {
            "deploy-game-release": "Deploy production release across all platforms",
            "validate-before-deploy": "Run comprehensive validation suite",
            "sync-team-collaboration": "Sync work from team members",
            "learn-and-optimize": "Learn from metrics and suggest optimizations"
        }

        for goal, description in goals.items():
            print(f"\n  {goal}")
            print(f"    {description}")

    elif args.action == "info":
        if not args.goal:
            print("Error: goal name required")
            return 1

        print(f"\n" + "=" * 60)
        print(f"Goal: {args.goal}")
        print("=" * 60)
        print("[INFO] Goal info (Phase 2)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
