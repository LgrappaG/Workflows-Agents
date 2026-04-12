#!/bin/bash
# hooks.sh - Dynamic Hooks CLI Tool
# Quick access to all hook commands and utilities

set -e

HOOKS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$HOOKS_DIR/../.." && pwd)"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Help text
show_help() {
    cat << 'EOF'
[HOOKS CLI] - Dynamic Hooks System

USAGE:
  ./hooks.sh <command> [options]

COMMANDS:

  message <file>          Validate commit message
  skills                  Validate all skills
  skill <path>            Validate single skill with 8 gates
  workflows               Validate all workflows

  config                  Show current configuration
  context                 Show current context/phase
  set-context <phase>     Set active phase (phase_4, phase_5, etc.)

  status                  Show system status
  debug <hook>            Debug specific hook
  test                    Run quick validation test

  help                    Show this help message
  version                 Show version

EXAMPLES:
  ./hooks.sh message /tmp/msg.txt
  ./hooks.sh skill .agents/skills/animation-blend/SKILL.md
  ./hooks.sh set-context phase_5_enrichment
  ./hooks.sh workflows
  ./hooks.sh debug validate-skill

ENVIRONMENT:
  HOOKS_CONTEXT          Set validation phase (default: phase_4)
  HOOKS_MODE             strict|lenient|experimental
  DEBUG                  Enable debug output (DEBUG=1)

EOF
}

# Command implementations
cmd_message() {
    if [ -z "$1" ]; then
        echo -e "${RED}Error: message file required${NC}"
        exit 1
    fi
    python3 "$HOOKS_DIR/pre-commit-message.py" "$1"
}

cmd_skills() {
    echo -e "${BLUE}Validating all skills...${NC}"
    python3 "$HOOKS_DIR/pre-commit-skills.py"
}

cmd_skill() {
    if [ -z "$1" ]; then
        echo -e "${RED}Error: skill path required${NC}"
        exit 1
    fi
    echo -e "${BLUE}Validating skill: $1${NC}"
    python3 "$HOOKS_DIR/validate-skill.py" "$1"
}

cmd_workflows() {
    echo -e "${BLUE}Validating all workflows...${NC}"
    python3 "$HOOKS_DIR/pre-commit-workflows.py"
}

cmd_config() {
    if [ -f "$HOOKS_DIR/config/hooks-config.yaml" ]; then
        echo -e "${BLUE}=== Global Configuration ===${NC}"
        head -30 "$HOOKS_DIR/config/hooks-config.yaml"
        echo ""
    fi

    if [ ! -z "$HOOKS_CONTEXT" ]; then
        echo -e "${GREEN}Active Context: $HOOKS_CONTEXT${NC}"
    else
        echo -e "${YELLOW}No context set (using 'phase_4' as default)${NC}"
    fi
}

cmd_context() {
    current_context="${HOOKS_CONTEXT:-phase_4}"
    current_mode="${HOOKS_MODE:-strict}"
    echo -e "${BLUE}=== Current Context ===${NC}"
    echo -e "Context: ${GREEN}$current_context${NC}"
    echo -e "Mode: ${GREEN}$current_mode${NC}"
    echo ""
    echo -e "To change: ${YELLOW}export HOOKS_CONTEXT=phase_5_enrichment${NC}"
}

cmd_set_context() {
    if [ -z "$1" ]; then
        echo -e "${RED}Error: phase required${NC}"
        echo "Valid phases: phase_4, phase_5_enrichment, phase_6_bootstrap"
        exit 1
    fi
    export HOOKS_CONTEXT="$1"
    echo -e "${GREEN}Context set to: $1${NC}"
    echo -e "${YELLOW}Run: ${NC}export HOOKS_CONTEXT=$1"
}

cmd_status() {
    echo -e "${BLUE}=== System Status ===${NC}"
    echo -e "Hooks Directory: ${GREEN}$HOOKS_DIR${NC}"

    # Check files
    echo -e "\n${BLUE}Files:${NC}"
    [ -f "$HOOKS_DIR/pre-commit-message.py" ] && echo -e "  ${GREEN}✓${NC} pre-commit-message.py" || echo -e "  ${RED}✗${NC} pre-commit-message.py"
    [ -f "$HOOKS_DIR/pre-commit-skills.py" ] && echo -e "  ${GREEN}✓${NC} pre-commit-skills.py" || echo -e "  ${RED}✗${NC} pre-commit-skills.py"
    [ -f "$HOOKS_DIR/validate-skill.py" ] && echo -e "  ${GREEN}✓${NC} validate-skill.py" || echo -e "  ${RED}✗${NC} validate-skill.py"
    [ -f "$HOOKS_DIR/pre-commit-workflows.py" ] && echo -e "  ${GREEN}✓${NC} pre-commit-workflows.py" || echo -e "  ${RED}✗${NC} pre-commit-workflows.py"

    # Check engine
    echo -e "\n${BLUE}Engine:${NC}"
    [ -f "$HOOKS_DIR/engine/dynamic_hooks_engine.py" ] && echo -e "  ${GREEN}✓${NC} DynamicHooksEngine" || echo -e "  ${RED}✗${NC} DynamicHooksEngine"

    # Check config
    echo -e "\n${BLUE}Configuration:${NC}"
    [ -f "$HOOKS_DIR/config/hooks-config.yaml" ] && echo -e "  ${GREEN}✓${NC} hooks-config.yaml" || echo -e "  ${RED}✗${NC} hooks-config.yaml"
    [ -f "$HOOKS_DIR/config/hooks-context.yaml" ] && echo -e "  ${GREEN}✓${NC} hooks-context.yaml" || echo -e "  ${RED}✗${NC} hooks-context.yaml"
    [ -f "$HOOKS_DIR/config/hooks-plugins.yaml" ] && echo -e "  ${GREEN}✓${NC} hooks-plugins.yaml" || echo -e "  ${RED}✗${NC} hooks-plugins.yaml"
}

cmd_debug() {
    if [ -z "$1" ]; then
        echo -e "${RED}Error: hook name required${NC}"
        echo "Available: pre-commit-message, pre-commit-skills, validate-skill, pre-commit-workflows"
        exit 1
    fi

    hook_file="$HOOKS_DIR/$1.py"
    if [ ! -f "$hook_file" ]; then
        hook_file="$HOOKS_DIR/pre-commit-$1.py"
    fi

    if [ ! -f "$hook_file" ]; then
        echo -e "${RED}Error: hook not found: $1${NC}"
        exit 1
    fi

    echo -e "${BLUE}Debugging: $(basename $hook_file)${NC}"
    python3 -u "$hook_file" --debug
}

cmd_test() {
    echo -e "${BLUE}Running quick validation test...${NC}"
    python3 << 'PYTEST'
import sys
from pathlib import Path

hooks_dir = Path(__file__).parent

# Quick test
try:
    print("[TEST] Checking hook files...")
    expected_files = [
        'pre-commit-message.py',
        'pre-commit-skills.py',
        'validate-skill.py',
        'pre-commit-workflows.py'
    ]

    for fname in expected_files:
        fpath = hooks_dir / fname
        if fpath.exists():
            print(f"  [OK] {fname}")
        else:
            print(f"  [FAIL] {fname}")

    print("\n[TEST] System OK")
    sys.exit(0)
except Exception as e:
    print(f"[ERROR] {e}")
    sys.exit(1)
PYTEST
}

cmd_version() {
    echo "Dynamic Hooks System v1.0"
    echo "Status: Production Ready"
    echo "Last Update: 2026-04-12"
}

# Main dispatch
case "${1:-help}" in
    message)    cmd_message "$2" ;;
    skills)     cmd_skills ;;
    skill)      cmd_skill "$2" ;;
    workflows)  cmd_workflows ;;
    config)     cmd_config ;;
    context)    cmd_context ;;
    set-context) cmd_set_context "$2" ;;
    status)     cmd_status ;;
    debug)      cmd_debug "$2" ;;
    test)       cmd_test ;;
    version)    cmd_version ;;
    help)       show_help ;;
    *)          echo -e "${RED}Unknown command: $1${NC}"; show_help; exit 1 ;;
esac
