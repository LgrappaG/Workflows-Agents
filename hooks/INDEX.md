# Dynamic Hooks System - Complete Project Index

**Version:** 1.0 | **Status:** Production Ready ✅  
**Last Updated:** 2026-04-12

---

## 🎯 Quick AI Lookup

**"I want to..."** → **Go to:**
- Understand what this system is → **[CLAUDE.md](CLAUDE.md)** (5 min, essential)
- Start working on this system → **[ONBOARDING.md](ONBOARDING.md)** (15 min, recommended first)
- Learn how to modify safely → **[MODIFICATION_CHECKLIST.md](MODIFICATION_CHECKLIST.md)** (3-5 min before any change)
- Understand why decisions were made → **[DECISIONS.md](DECISIONS.md)** (10-15 min)
- Debug system issues → **[DEPENDENCIES.md](DEPENDENCIES.md)** (5-10 min, has breakage scenarios)
- Save memories for next session → **[AI_SESSION_TEMPLATE.md](AI_SESSION_TEMPLATE.md)** (reference)
- Find commands quickly → **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** (2 min skim)
- See implementation progress → **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** (5 min overview)

---

## 📖 Documentation Map

### 🚀 Getting Started
1. **[ONBOARDING.md](ONBOARDING.md)** - 15-minute ramp-up for new people (START HERE)
2. **[SETUP.md](SETUP.md)** - Installation & configuration (2-5 min read)
3. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Daily quick reference card
4. **[hooks.sh help](hooks.sh)** - CLI command reference

### 💡 For AI Assistants & Developers
1. **[CLAUDE.md](CLAUDE.md)** - AI context guide (what to change, what NOT to change)
2. **[README.md](README.md)** - Complete system documentation
3. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Common workflows
4. **[.env.example](.env.example)** - Configuration template
5. **[AI_SESSION_TEMPLATE.md](AI_SESSION_TEMPLATE.md)** - Memory format for AI sessions

### 🏗️ For Architects & Decision-Makers
1. **[DECISIONS.md](DECISIONS.md)** - Architectural decisions with rationale
2. **[DEPENDENCIES.md](DEPENDENCIES.md)** - Component relationships & data flow
3. **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** - What's complete, what's deferred

### 🔧 For System Administrators
1. **[config/hooks-config.yaml](config/hooks-config.yaml)** - Global thresholds
2. **[config/hooks-context.yaml](config/hooks-context.yaml)** - Phase-specific rules
3. **[config/hooks-plugins.yaml](config/hooks-plugins.yaml)** - Plugin registry
4. **[MODIFICATION_CHECKLIST.md](MODIFICATION_CHECKLIST.md)** - Safe modification guide

### 📚 Before Making Changes
1. **[MODIFICATION_CHECKLIST.md](MODIFICATION_CHECKLIST.md)** - Pre-flight checklist
2. **[CLAUDE.md](CLAUDE.md)** - Boundaries (what NOT to change)
3. **[DECISIONS.md](DECISIONS.md)** - Understand the why
4. **[DEPENDENCIES.md](DEPENDENCIES.md)** - Breakage scenarios

---

## 📚 All Documentation Files

| File | Purpose | For Whom | Read Time |
|------|---------|----------|-----------|
| **ONBOARDING.md** | 15-min ramp-up for new people | Everyone first | 15 min |
| **CLAUDE.md** | AI context & system boundaries | AI assistants | 5-8 min |
| **DECISIONS.md** | Why each decision was made | Architects | 10-15 min |
| **MODIFICATION_CHECKLIST.md** | Safe modification guide | Maintainers | 3-5 min (before changes) |
| **DEPENDENCIES.md** | Component relationships | Debuggers | 5-10 min |
| **IMPLEMENTATION_STATUS.md** | Implementation progress | Managers | 5 min |
| **AI_SESSION_TEMPLATE.md** | Memory format | AI assistants | Reference |
| **SETUP.md** | Installation & setup | New users | 5 min |
| **QUICK_REFERENCE.md** | Daily quick lookup | All users | 2 min (skim) |
| **README.md** | Complete documentation | Developers | 15 min |
| **This file (INDEX.md)** | Navigation hub | Everyone | 10 min |

---

## 🚀 Quick Start

### 30-Second Start
```bash
cd .agents/hooks
./hooks.sh help
./hooks.sh status
```

### 2-Minute Setup
```bash
cd .agents/hooks
cp .env.example .env.local
./hooks.sh status
./hooks.sh skills
```

### 5-Minute Full Setup
- See [SETUP.md](SETUP.md)

---

## 📚 Hook Reference

### 1. Commit Message Validation
**File:** `pre-commit-message.py`  
**Purpose:** Validate conventional commits  
**Usage:**
```bash
./hooks.sh message <file>
```
**Configured in:** `config/hooks-config.yaml::commit_message`

### 2. Skill Validation (Fast)
**File:** `pre-commit-skills.py`  
**Purpose:** YAML & naming validation  
**Usage:**
```bash
./hooks.sh skills          # All skills
./hooks.sh skill <path>    # Single skill (8 gates)
```
**Configured in:** `config/hooks-config.yaml::gates`

### 3. Comprehensive Validation (8 Gates)
**File:** `validate-skill.py`  
**Purpose:** Full quality validation  
**Details:** Gates 1-8 detailed validation  
**Usage:**
```bash
./hooks.sh skill <path>
```
**Configured in:** Complete in stdout

### 4. Workflow Validation
**File:** `pre-commit-workflows.py`  
**Purpose:** Validate workflow definitions  
**Usage:**
```bash
./hooks.sh workflows
```
**Configured in:** `config/hooks-config.yaml::workflow`

---

## ⚙️ Configuration Guide

### Where to Edit

| Task | File | Section |
|------|------|---------|
| Change thresholds | `config/hooks-config.yaml` | `gates` |
| Add domain | `config/hooks-config.yaml` | `approved_domains` |
| Add phase rules | `config/hooks-context.yaml` | `contexts` |
| Local settings | `.env.local` | Any `HOOKS_*` var |

### Configuration Hierarchy

1. **`.env.local`** - Highest priority (local overrides)
2. **`hooks-context.yaml`** - Phase-specific rules
3. **`hooks-config.yaml`** - Global defaults
4. **Hardcoded fallback** - Lowest priority (always works)

### Quick Configuration Changes

```bash
# Edit global thresholds
vim config/hooks-config.yaml

# Add phase-specific rule
vim config/hooks-context.yaml

# Set local preferences
cp .env.example .env.local
# Edit as needed

# Verify changes
./hooks.sh config
./hooks.sh context
```

---

## 🛠️ CLI Tool Reference

### Basic Commands
```bash
./hooks.sh message <file>      # Validate commit message
./hooks.sh skills              # Validate all skills
./hooks.sh skill <path>        # Validate single skill
./hooks.sh workflows           # Validate all workflows
```

### Configuration
```bash
./hooks.sh config              # Show current config
./hooks.sh context             # Show current phase
./hooks.sh set-context <phase> # Switch phase
```

### Utilities
```bash
./hooks.sh status              # System status
./hooks.sh debug <hook>        # Debug hook
./hooks.sh test                # Quick test
./hooks.sh help                # Show help
./hooks.sh version             # Version info
```

---

## 📋 Common Workflows

### Workflow 1: Validate Single Skill
```bash
./hooks.sh skill .agents/skills/animation-blend/SKILL.md
```

### Workflow 2: Validate All Skills
```bash
./hooks.sh skills
```

### Workflow 3: Switch to Development Mode
```bash
./hooks.sh set-context phase_5_enrichment
./hooks.sh skill <path>  # Uses relaxed rules
```

### Workflow 4: Debug Validation Issues
```bash
./hooks.sh debug validate-skill
./hooks.sh skill <path>
```

### Workflow 5: Check What's Configured
```bash
./hooks.sh status
./hooks.sh context
./hooks.sh config
```

---

## 🔧 Engine Architecture

### Engine Modules (Read-Only)
```
engine/
├── dynamic_hooks_engine.py    - Main orchestrator
├── configuration_loader.py    - YAML loading
├── context_resolver.py        - Phase detection
├── plugin_manager.py          - Plugin system
├── learning_engine.py         - Metrics tracking
└── __init__.py                - Package init
```

### You Should NOT Edit
- Any files in `engine/` directory
- These are used internally by hooks

---

## 📊 Phase Comparison

| Feature | Phase 4 | Phase 5 | Phase 6 |
|---------|---------|---------|---------|
| Mode | strict | lenient | experimental |
| Description | 50-100 | 50-150 | 30-150 |
| File Size | 1,200 | 1,500 | 2,000 |
| Mandates | 3+ | 3+ | 2+ |
| Best For | Production | Development | Bootstrap |
| Command | `set-context phase_4` | `set-context phase_5_enrichment` | `set-context phase_6_bootstrap` |

---

## ✅ Validation Checklist

Before committing:
```bash
# 1. Validate message
./hooks.sh message <file>

# 2. Validate skill
./hooks.sh skill <skill-path>

# 3. Check all
./hooks.sh skills
./hooks.sh workflows
```

---

## 📞 Troubleshooting

| Problem | Solution | File to Check |
|---------|----------|---|
| "What is this system?" | Read ONBOARDING.md (15 min) | ONBOARDING.md |
| "Is this change safe?" | Check MODIFICATION_CHECKLIST.md | MODIFICATION_CHECKLIST.md |
| "What can/can't I modify?" | Read CLAUDE.md::What IS/NOT OK | CLAUDE.md |
| "Why is it designed this way?" | Read DECISIONS.md | DECISIONS.md |
| "What broke and why?" | Check DEPENDENCIES.md::Breakage Scenarios | DEPENDENCIES.md |
| "What commands are available?" | Run `./hooks.sh help` or see QUICK_REFERENCE.md | QUICK_REFERENCE.md |
| "What's the current status?" | Run `./hooks.sh status` | System status |
| "Is there an example I can follow?" | See MODIFICATION_CHECKLIST.md::Modification Patterns | MODIFICATION_CHECKLIST.md |
| "How do I save progress for next session?" | Use AI_SESSION_TEMPLATE.md | AI_SESSION_TEMPLATE.md |
| "Need comprehensive overview?" | Read README.md | README.md |

---

## 📚 Documentation Files

| File | Purpose | Read Time |
|------|---------|-----------|
| **SETUP.md** | Install & setup | 5 min |
| **QUICK_REFERENCE.md** | Daily commands | 5 min |
| **README.md** | Complete guide | 15 min |
| **QUICK_REFERENCE.md** | Command reference | 2 min |
| **config/hooks-config.yaml** | Global config | Reference |
| **config/hooks-context.yaml** | Phase rules | Reference |
| **This file** | Project index | 10 min |

---

## 🎯 For Different Roles

### Developers
1. Read: `SETUP.md` (5 min)
2. Read: `QUICK_REFERENCE.md` (5 min)
3. Start: `./hooks.sh help`
4. Go to: `README.md` if detailed help needed

### DevOps/Admins
1. Read: `README.md` (15 min)
2. Edit: `config/hooks-config.yaml` as needed
3. Edit: `config/hooks-context.yaml` for phases
4. Document: Changes in version control

### New Team Members
1. Read: `SETUP.md` (5 min)
2. Follow: Setup steps
3. Use: `./hooks.sh help` for commands
4. Reference: `QUICK_REFERENCE.md` daily

---

## 🔄 Workflow Integration

### Git Workflow
```bash
# After edits
./hooks.sh skills              # Validate
git add .                       # Stage
git commit -m "feat: ..."      # Git hook validates message
# If using .git/hooks/commit-msg, validation auto-runs
```

### CI/CD Integration
```bash
# In GitHub Actions
- name: Validate Skills
  run: |
    export HOOKS_CONTEXT=ci_strict
    .agents/hooks/hooks.sh skills
```

### Pre-commit Framework
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: validate-skills
        name: Validate Skills
        entry: .agents/hooks/hooks.sh skills
        language: system
        stages: [commit]
```

---

## 📈 Project Statistics

- **Total Files:** 27
- **Total Code:** 3,800+ LOC
- **Hooks:** 4 production hooks
- **Engine:** 6 Python modules
- **Config:** 3 YAML files
- **Schemas:** 2 JSON files
- **Documentation:** 1,000+ lines

---

## ✨ Key Features

✅ **Production Ready** - Tested and validated  
✅ **4 Hooks** - Message, skills, workflows, validation  
✅ **8 Validation Gates** - Comprehensive quality checks  
✅ **Dynamic Configuration** - Edit YAML, not code  
✅ **Phase Support** - Different rules per phase  
✅ **CLI Tool** - Easy command-line access  
✅ **Backward Compatible** - 100% compatible  
✅ **Well Documented** - Complete guides  

---

## 🚀 Next Steps

1. **Read:** `SETUP.md` (2-5 minutes)
2. **Run:** `./hooks.sh help`
3. **Try:** `./hooks.sh status`
4. **Configure:** Edit `.env.local`
5. **Use:** Start with `./hooks.sh skills`

---

**Happy validating!** 🎉

---

**Last Updated:** 2026-04-12  
**Status:** Production Ready ✅  
**Version:** 1.0

---

## ✨ What's New (This Session - 2026-04-12)

**Added 7 New Documents for AI & Developer Efficiency:**

1. **[CLAUDE.md](CLAUDE.md)** - AI Assistant Context Guide
   - Project identity, architecture, decision boundaries
   - What's safe to modify, what's not
   - Testing procedures, common patterns
   - For: AI assistants, new developers starting work

2. **[DECISIONS.md](DECISIONS.md)** - Architectural Decision Record
   - 7 major decisions with full rationale
   - Alternatives considered & why rejected
   - Trade-offs & consequences documented
   - For: Understanding the "why" behind design choices

3. **[MODIFICATION_CHECKLIST.md](MODIFICATION_CHECKLIST.md)** - Safe Modification Guide
   - Pre-modification interview (5 questions)
   - During modification steps (6 phases)
   - Post-modification verification (3 checks)
   - Common modification patterns with examples
   - When to escalate instead of trying alone
   - For: Anyone planning to modify the system

4. **[DEPENDENCIES.md](DEPENDENCIES.md)** - Component Relationships
   - System architecture diagram (data flow)
   - Dependency graph (what depends on what)
   - Critical load order
   - Breakage scenarios with fixes
   - Modification impact matrix
   - For: Understanding system structure & debugging

5. **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** - Progress Report
   - Phase-by-phase completion status
   - Known limitations & why
   - Testing coverage summary
   - Performance metrics
   - What could be better (deferred enhancements)
   - For: Project status overview & handoff readiness

6. **[AI_SESSION_TEMPLATE.md](AI_SESSION_TEMPLATE.md)** - Memory Format
   - Template for AI sessions to document work
   - What to include in session memory
   - How to summarize findings for next session
   - Lessons learned capture
   - For: AI assistants to record work systematically

7. **[ONBOARDING.md](ONBOARDING.md)** - First-Time Ramp-Up
   - 15-minute quick start for new people
   - Key documents explained
   - Use cases with step-by-step guides
   - Command cheat sheet
   - Common questions answered
   - For: New developers/AI assistants starting

**Also Updated:**
- **[INDEX.md](INDEX.md)** - Added Quick AI Lookup section
- **[.gitignore](.gitignore)** - Created with helpful comments (file tracking clarification)

**Total New Content:**
- 7 new documentation files (~70 pages equivalent)
- 1 new .gitignore file
- 2 update existing INDEX.md for navigation

**Why These Documents Exist:**
The system was complete and production-ready, but lacked explicit documentation of:
- Architectural decisions and rationale
- Safe modification procedures
- System dependencies and data flow
- AI-friendly context for future sessions
- Implementation progress tracking

These new documents make the system more maintainable and easier for AI assistants to work with in future sessions.
