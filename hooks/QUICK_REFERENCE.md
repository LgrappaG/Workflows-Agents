# Quick Reference Card - Dynamic Hooks System

**Version:** 1.0 | **Status:** Production Ready

---

## File Organization

```
.agents/hooks/
├── README.md                          ← Start here for full docs
├── hooks.sh                            ← CLI tool (new!)
├── .env.example                        ← Configuration template
│
├── pre-commit-message.py               ← Commit message validation
├── pre-commit-skills.py                ← Skill YAML & naming
├── validate-skill.py                   ← 8-gate comprehensive
├── pre-commit-workflows.py             ← Workflow validation
│
├── engine/                             ← Read-only (no changes needed)
│   ├── dynamic_hooks_engine.py
│   ├── configuration_loader.py
│   ├── context_resolver.py
│   ├── plugin_manager.py
│   └── learning_engine.py
│
├── config/                             ← Edit these to customize!
│   ├── hooks-config.yaml               ← Global thresholds
│   ├── hooks-context.yaml              ← Phase-specific rules
│   └── hooks-plugins.yaml              ← Plugin registry
│
└── schemas/                            ← Reference only
    ├── config-schema.json
    └── plugin-schema.json
```

---

## Quick Start Commands

### Basic Hook Execution
```bash
# Validate commit message
./hooks.sh message <file>

# Validate all skills
./hooks.sh skills

# Validate single skill (with all 8 gates)
./hooks.sh skill .agents/skills/animation-blend/SKILL.md

# Validate all workflows
./hooks.sh workflows
```

### Configuration Management
```bash
# Check current setting
./hooks.sh context
./hooks.sh config

# Switch phase
./hooks.sh set-context phase_5_enrichment
export HOOKS_CONTEXT=phase_5_enrichment  # Alternative

# View system status
./hooks.sh status
```

### Debugging
```bash
# Debug specific hook
./hooks.sh debug validate-skill

# Run quick test
./hooks.sh test

# Show help
./hooks.sh help
```

---

## File Editing Guide

### Most Frequent Edits

**1. Change validation thresholds**
- File: `.agents/hooks/config/hooks-config.yaml`
- Lines: 20-50 (gates section)
- Example:
  ```yaml
  description:
    min_length: 40  # Changed from 50
    max_length: 120 # Changed from 100
  ```

**2. Add approved skill domain**
- File: `.agents/hooks/config/hooks-config.yaml`
- Lines: 60-80 (domains section)
- Example:
  ```yaml
  approved_domains:
    - animation
    - custom-domain  # Add here
  ```

**3. Phase-specific rules**
- File: `.agents/hooks/config/hooks-context.yaml`
- Lines: 10-40 (contexts section)
- Example:
  ```yaml
  phase_5_enrichment:
    thresholds:
      file_size:
        max_bytes: 1500  # Relaxed for phase 5
  ```

**4. Local development settings**
- File: `.env.local` (create if not exists)
- Example:
  ```bash
  HOOKS_CONTEXT=phase_5_enrichment
  DEBUG=1
  ```

---

## Common Workflows

### Workflow 1: Local Development (Relaxed)
```bash
cp .env.example .env.local
# Edit .env.local:
export HOOKS_CONTEXT=phase_5_enrichment
export DEBUG=1

./hooks.sh set-context phase_5_enrichment
./hooks.sh skill <skill-path>
```

### Workflow 2: Production Validation (Strict)
```bash
./hooks.sh set-context phase_4
./hooks.sh skill <skill-path>
```

### Workflow 3: Debug Single Skill Issue
```bash
./hooks.sh debug validate-skill
# Then run specific test:
./hooks.sh skill .agents/skills/animation-blend/SKILL.md
```

### Workflow 4: Validate Everything
```bash
./hooks.sh status              # Check system
./hooks.sh skills              # All skills
./hooks.sh workflows           # All workflows
```

---

## Configuration Hierarchy

```
┌─ Priority 1: .env.local (highest)
├─ Priority 2: HOOKS_CONTEXT env var
├─ Priority 3: hooks-context.yaml per-phase
├─ Priority 4: hooks-config.yaml global
└─ Priority 5: Hardcoded fallback (lowest)
```

**Example cascade:**
```bash
# Set in .env.local (highest priority)
HOOKS_CONTEXT=phase_5_enrichment

# Loads hooks-context.yaml::phase_5_enrichment settings
# Falls back to hooks-config.yaml if not defined
# Never reaches hardcoded defaults (unless engine fails)
```

---

## Phase Comparison

| Phase | Mode | File Size | Mandates | Response | Use For |
|-------|------|-----------|----------|----------|---------|
| phase_4 | strict | 1,200 | 3+ | 3-4 steps | Production |
| phase_5_enrichment | lenient | 1,500 | 3+ | 3-4 steps | Dev/testing |
| phase_6_bootstrap | experimental | 2,000 | 2+ | relaxed | Bootstrap |

---

## Editing Checklist

- [ ] Theme: What am I changing? (threshold/domain/phase/etc)
- [ ] File: Which config file? (hooks-config.yaml / hooks-context.yaml)
- [ ] Section: Which section? (gates / domains / contexts)
- [ ] Value: What's the new value?
- [ ] Test: Run `./hooks.sh skill <path>` to verify
- [ ] Verify: Check output matches your expectation

---

## Troubleshooting Quick Links

| Issue | Solution |
|-------|----------|
| Hook fails but I don't see why | `./hooks.sh debug <hook>` |
| Want to relax validation | `./hooks.sh set-context phase_5_enrichment` |
| Want strict validation | `./hooks.sh set-context phase_4` |
| Forgot current settings | `./hooks.sh context` |
| System not working | `./hooks.sh status` |
| Don't know what to do | `./hooks.sh help` |

---

## Git Hooks Setup (Optional)

Install into `.git/hooks/commit-msg`:
```bash
#!/bin/bash
./.agents/hooks/hooks.sh message "$1"
exit $?
```

Then commits auto-validate!

---

## Key Points to Remember

✅ **All hooks work out-of-the-box** - No setup needed  
✅ **Edit configs to customize** - Don't modify hook .py files  
✅ **Use hooks.sh CLI** - Easier than remembering python commands  
✅ **Copy .env.example to .env.local** - For persistent settings  
✅ **Read README.md for detailed docs** - This is just quick reference  

---

**Version:** 1.0  
**Status:** Production Ready ✅  
**Last Update:** 2026-04-12
