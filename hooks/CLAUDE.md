# AI Assistant Context Guide - Dynamic Hooks System

**Version:** 1.0 | **Status:** Production Ready | **Last Updated:** 2026-04-12

---

## Project Identity

- **Type:** Production validation framework for Agent Project
- **Scope:** 4 hooks + dynamic configuration layer + plugin system
- **Status:** Complete (Phases 1-4), Production Ready
- **Owner:** LgrappaG @ Agent Project
- **Live Since:** 2026-04-12

---

## Core Problem Being Solved

Transform hardcoded validation rules (50+ hardcoded constants scattered across 4 Python files) into a **dynamic, externally-configurable system** that supports:

- ✅ Different validation stringency levels (phases)
- ✅ Custom plugins without code modification
- ✅ Learning-based rule optimization
- ✅ Context-aware validation (dev vs CI vs production)

**Before:** Changing a threshold = edit Python code + git commit + deploy  
**After:** Changing a threshold = edit YAML file + instant effect (no restart needed)

---

## Three Critical Layers (Architecture)

### Layer 1: Configuration (YAML + JSON Schema)
```
config/
├── hooks-config.yaml         ← Global defaults (description min/max, file size, etc)
├── hooks-context.yaml        ← Phase-specific rules (phase_4, phase_5, phase_6)
├── hooks-plugins.yaml        ← Plugin registry (which plugins are active)
└── schemas/
    ├── config-schema.json    ← Validates config is well-formed
    └── plugin-schema.json    ← Validates plugins match interface
```

**What happens here:** Thresholds live in YAML, not Python. Any tool can read/modify them.

### Layer 2: Runtime Engine (Python)
```
engine/
├── dynamic_hooks_engine.py     ← Main orchestrator (decision maker)
├── configuration_loader.py     ← YAML → Python dicts + validation
├── context_resolver.py         ← Detects phase/environment from env vars
├── plugin_manager.py           ← Loads + executes custom plugins
└── learning_engine.py          ← Tracks metrics, suggests improvements
```

**What happens here:** When validation runs, engine loads YAML config, merges settings, applies rules, runs plugins, tracks results.

### Layer 3: Hook Scripts (Python)
```
├── pre-commit-message.py       ← Commit message validation (uses engine)
├── pre-commit-skills.py        ← Skill YAML + naming (uses engine)
├── validate-skill.py           ← 8-gate comprehensive validation (uses engine)
└── pre-commit-workflows.py     ← Workflow definition validation (uses engine)
```

**What happens here:** Scripts call engine, engine does the work. Scripts are thin wrappers now (not hardcoded logic).

---

## Validation Gates (In Order)

When you run `./hooks.sh skill <path>`, these 8 gates execute:

| Gate | What | Example |
|------|------|---------|
| 1 | **Description** | Action verb (configure/implement) + 50-100 chars |
| 2 | **Mandates** | 3+ action items, no vague words (good/bad/well) |
| 3 | **Response** | 3-4 structured steps, clear actions |
| 4 | **File Size** | 600-1200 bytes (phase_5 allows 1500) |
| 5 | **Workflow** | 4-7 steps, valid structure |
| 6 | **YAML Syntax** | Valid YAML + proper naming (-snake-case) |
| 7 | **Approved Domains** | Domain in approved list (animation, audio, etc) |
| 8 | **Quality Check** | Comprehensive final validation |

---

## Architecture Decisions (Why This Way?)

### Decision 1: YAML for Configuration
- **Why:** Thresholds should be human-readable + editable without code
- **Chosen YAML over:** JSON (can't have comments), env-only (unversioned)
- **Trade-off:** Need JSON schema validation to catch typos

### Decision 2: Three-Level Configuration Merge
```
Priority Order (highest → lowest):
  Level 3: Plugin-specific settings
  Level 2: Context settings (phase_5_enrichment overrides phase_4)
  Level 1: Global defaults (fallback)
```
- **Why:** Allows plugins to override context, context to override global
- **Trade-off:** Merge complexity (solved by ConfigurationLoader)

### Decision 3: Plugin Consensus Voting
- **What:** Multiple plugins validate skill → need 2+ to pass for PASS result
- **Why:** Prevents single plugin from blocking valid contributions
- **Alternative rejected:** Unanimous (too strict), first-pass (skips real checks)

### Decision 4: Learning Engine as Report-Only
- **What:** Tracks metrics, suggests changes in JSON file, user applies manually
- **Why:** Threshold changes affect all contributors → need human review
- **Alternative rejected:** Auto-apply threshold changes (risky, unreviewed)

### Decision 5: Environment Variable for Context
- **What:** `HOOKS_CONTEXT=phase_5_enrichment` switches validation rules
- **Why:** CI/CD friendly + `.env.local` fits Python conventions
- **Alternative rejected:** Config file detection (auto-magic, unreliable)

### Decision 6: Backward Compatibility Wrapper
- **What:** Old hook scripts still work, they import from engine internally
- **Why:** Existing CI/CD + git hooks must not break
- **Trade-off:** Added wrapper layer (acceptable for safety)

---

## Configuration Hierarchy (How Settings Are Applied)

When validation runs:

```
Step 1: Load global defaults from hooks-config.yaml
           ↓
Step 2: Detect HOOKS_CONTEXT env var (e.g., "phase_5_enrichment")
           ↓
Step 3: Load context-specific overrides from hooks-context.yaml
           ↓
Step 4: Load plugin configs from hooks-plugins.yaml
           ↓
Step 5: Deep merge: plugin > context > global (plugins win)
           ↓
Step 6: Apply merged config to validators + plugins
           ↓
Step 7: Execute validation with merged settings
```

**Example:**
```yaml
# Global (hooks-config.yaml)
description:
  min_length: 50

# Context (hooks-context.yaml :: phase_5_enrichment)
thresholds:
  description:
    min_length: 30  # Loosened for phase 5

# Result: Phase 5 uses min_length=30 (overrides global 50)
```

---

## Phase Definitions

### Phase 4: `phase_4` (STRICT - Production)
- **Mode:** strict (100% of thresholds applied)
- **Use for:** Production code, final validations
- **File size limit:** 1,200 bytes
- **Description length:** 50-100 chars (tight)
- **All 8 gates:** Enabled

### Phase 5: `phase_5_enrichment` (LENIENT - Development)
- **Mode:** lenient (120% tolerance, looser requirements)
- **Use for:** Local development, testing new content
- **File size limit:** 1,500 bytes (relaxed)
- **Description length:** 50-150 chars (wider range)
- **All 8 gates:** Enabled (but with relaxed thresholds)

### Phase 6: `phase_6_bootstrap` (EXPERIMENTAL - Bootstrap)
- **Mode:** experimental (150% tolerance)
- **Use for:** New skill creation, bootstrap phase
- **File size limit:** 2,000 bytes (very relaxed)
- **Description length:** 30-150 chars (minimal requirements)
- **Gates enabled:** 1-5 only (gates 6-8 optional)

---

## What NOT to Change (Architecture Boundaries)

These changes would break the system or violate design:

**🚫 Do NOT modify:**
- `engine/` directory structure (core logic, read-only)
- Hook script execution order (message → skills → workflows)
- Configuration hierarchy order (plugin > context > global is intentional)
- `BasePlugin` class interface (contracts with custom plugins)
- File size thresholds in `phase_4` (production strict mode requirement)
- `HOOKS_CONTEXT` environment variable name (CI/CD depends on it)
- Schema validation (config integrity critical)

---

## What IS OK to Modify (Customization Points)

These changes are safe and expected:

**✅ DO modify:**
- **Threshold values** in `config/hooks-config.yaml` (intended customization)
- **Phase-specific rules** in `config/hooks-context.yaml` (per-phase tuning)
- **Plugin registry** in `config/hooks-plugins.yaml` (plugin management)
- **CLI commands** in `hooks.sh` (tooling improvements)
- **Documentation** files (SETUP.md, QUICK_REFERENCE.md, README.md, etc)
- **Metrics** in `metrics/validation_metrics.json` (auto-populated, safe to review)

---

## Key Files by Purpose

| File | Purpose | When to Read | When to Modify |
|------|---------|--------------|---|
| `hooks.sh` | CLI dispatcher | Learning commands | Adding new commands |
| `config/hooks-config.yaml` | Global defaults | Understanding thresholds | Tuning validation globally |
| `config/hooks-context.yaml` | Phase rules | Understanding phases | Phase-specific tuning |
| `config/hooks-plugins.yaml` | Plugin registry | Seeing active plugins | Adding/removing plugins |
| `engine/dynamic_hooks_engine.py` | Main orchestrator | Understanding flow | 🚫 Don't modify |
| `engine/configuration_loader.py` | Config loading | Understanding config merge | 🚫 Don't modify |
| `engine/context_resolver.py` | Phase detection | Understanding phase switching | 🚫 Don't modify |
| `engine/plugin_manager.py` | Plugin execution | Understanding plugin system | 🚫 Don't modify |
| `pre-commit-*.py` | Hook entry points | Understanding which hook does what | Only if adding entirely new hook |
| `schemas/*.json` | Config validation | Understanding required fields | Only if changing config format |

---

## Common Modification Patterns

### Pattern 1: Relax Validation for Development
**Goal:** Allow longer descriptions in phase 5  
**How:**
```yaml
# Edit config/hooks-context.yaml
phase_5_enrichment:
  thresholds:
    description:
      min_length: 30  # Was 50
```
**Test:** `./hooks.sh set-context phase_5_enrichment && ./hooks.sh skill <path>`

### Pattern 2: Add Custom Validation Rule (Plugin)
**Goal:** Add custom domain validation  
**How:**
1. Create `plugins/custom_domain_validator.py`
2. Implement `BasePlugin` interface
3. Register in `config/hooks-plugins.yaml`:
```yaml
custom_domain_validator:
  enabled: true
  module: "plugins.custom_domain_validator"
  hooks: ["validate_skill"]
```
4. Plugin executes during validation automatically

### Pattern 3: Add New Approved Domain
**Goal:** Allow "game-design" as valid domain  
**How:**
```yaml
# Edit config/hooks-config.yaml
approved_domains:
  - animation
  - audio
  - game-design  # ← Add here
```

### Pattern 4: Enable/Disable a Plugin
**Goal:** Temporarily disable a plugin  
**How:**
```yaml
# Edit config/hooks-plugins.yaml
custom_domain_validator:
  enabled: false  # ← Set to false
```

---

## Testing the System

Verify system health after modifications:

```bash
# Check all files present
./hooks.sh status

# View current configuration
./hooks.sh config

# Check current phase
./hooks.sh context

# Switch phase
./hooks.sh set-context phase_5_enrichment

# Validate single skill
./hooks.sh skill .agents/skills/animation-blend/SKILL.md

# Validate all skills
./hooks.sh skills

# See available commands
./hooks.sh help
```

---

## How This Fits in Agent Project

1. **Pre-commit:** Hooks run on `git commit` automatically (if .git/hooks/commit-msg configured)
2. **Phase support:** Different projects/teams use different phases (Phase 4 strict for core, Phase 5 lenient for research)
3. **Extensibility:** Teams add custom validation via plugins
4. **Learning:** Metrics collected across all validations, used to optimize thresholds
5. **Central CLI:** `hooks.sh` makes validation accessible to non-technical contributors

---

## Known Limitations (By Design)

| Limitation | Why | Workaround |
|---|---|---|
| Learning engine is report-only | Human review needed for rule changes | Check `metrics/suggestions.json` manually |
| Plugin voting uses simple majority | Prevents deadlock | 2+ plugins must pass for PASS |
| Context detection via env var | No auto-magic detection | Set `HOOKS_CONTEXT` explicitly in CI/CD |
| Metrics require manual review | No automated tuning | Review metrics file, apply suggestions manually |
| Schema validation uses JSON Schema v7 | Python compatibility | If need newer schema, migrate carefully |

---

## For Future Modifications

When you modify this system:

1. **Always preserve backward compatibility**
   - Old `HOOKS_CONTEXT` values must keep working
   - Old hook scripts must keep working

2. **Keep config files as YAML**
   - Don't convert to JSON (human readability important)
   - Schema enforcement is enough for safety

3. **Update relevant docs**
   - If new hook: update `QUICK_REFERENCE.md`
   - If config structure change: update `DECISION.md`
   - If phase change: update phase comparison table

4. **Test all 3 phases**
   - Any config change: test with `phase_4`, `phase_5`, `phase_6`

5. **Verify metrics format**
   - If changing learning engine: ensure metrics schema is backward compatible

---

## Questions to Ask Before Modifying

- **What am I changing?** (config threshold / new gate / plugin / hook script / etc)
- **Does this violate "What NOT to Change"?** If yes, stop and escalate
- **Which phase(s) does this affect?** (all phases or just one?)
- **Will CI/CD need updates?** (GitHub Actions, .git/hooks, etc)
- **Should I add a DECISION entry?** (if architectural change → yes)
- **Does this affect backward compatibility?** (old usage must keep working)

---

**Version:** 1.0  
**Status:** Production Ready ✅  
**Last Updated:** 2026-04-12
