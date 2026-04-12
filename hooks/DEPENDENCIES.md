# Component Dependencies - Dynamic Hooks System

**Version:** 1.0 | **Updated:** 2026-04-12

---

## System Architecture Diagram

```
┌─ LAYER 3: External Integration ────────────────────┐
│                                                     │
│  CI/CD (GitHub Actions)        Git Hooks           │
│  env: HOOKS_CONTEXT=phase_5    pre-commit-msg      │
│  │                              │                   │
│  └─────────────┬────────────────┴──────┐            │
│                │                       │            │
│         ┌──────▼───────────────────────▼──────┐     │
│         │    CLI Interface (hooks.sh)          │     │
│         │  ./hooks.sh skill <path>             │     │
│         │  ./hooks.sh set-context phase_5      │     │
│         │  ./hooks.sh config                   │     │
│         └──────────┬────────────────────────────┘    │
│                    │                                  │
└────────────────────┼──────────────────────────────────┘
                     │
        ┌────────────▼───────────────────┐
        │   LAYER 2: Python Execution    │
        │   ════════════════════════════ │
        │                                │
        │  Hook Entry Scripts:           │
        │  ├─ pre-commit-message.py      │
        │  ├─ pre-commit-skills.py       │
        │  ├─ validate-skill.py          │
        │  └─ pre-commit-workflows.py    │
        │       ↓                         │
        │  DynamicHooksEngine            │
        │  (main orchestrator)           │
        │       ↓                         │
        │  ┌──────────────────────┐      │
        │  │ Configuration Loader │      │
        │  │ Context Resolver     │      │
        │  │ Plugin Manager       │      │
        │  │ Learning Engine      │      │
        │  │ Validators (8 gates) │      │
        │  └──────────────────────┘      │
        │                                │
        └────────────┬───────────────────┘
                     │
        ┌────────────▼──────────────────┐
        │ LAYER 1: Configuration        │
        │ ═════════════════════════     │
        │                               │
        │  config/                      │
        │  ├─ hooks-config.yaml         │
        │  ├─ hooks-context.yaml        │
        │  ├─ hooks-plugins.yaml        │
        │                               │
        │  .env.local                   │
        │  (local overrides)            │
        │                               │
        │  schemas/                     │
        │  ├─ config-schema.json        │
        │  └─ plugin-schema.json        │
        │                               │
        │  metrics/                     │
        │  └─ validation_metrics.json   │
        └───────────────────────────────┘
```

---

## Data Flow (How Information Moves)

### When Validation Runs: `./hooks.sh skill <path>`

```
1. CLI Input
   ├─ ./hooks.sh skill "path/to/SKILL.md"
   │
2. Hook Entry Script (pre-commit-skills.py)
   ├─ Read skill file
   ├─ Initialize DynamicHooksEngine()
   │
3. DynamicHooksEngine.__init__()
   ├─ ConfigurationLoader.load(config/)
   │  ├─ Read config/hooks-config.yaml (global)
   │  ├─ Validate with schemas/config-schema.json
   │  ├─ Return: Python dict of config
   │
   ├─ ContextResolver.detect()
   │  ├─ Check environ['HOOKS_CONTEXT'] (priority 1)
   │  ├─ Check .env.local (priority 2)
   │  ├─ Fallback to 'phase_4' (priority 3)
   │  ├─ Return: current_phase string
   │
   ├─ Read config/hooks-context.yaml
   │  ├─ Get context-specific overrides for current phase
   │  ├─ Merge with global config (context > global)
   │
   ├─ Read config/hooks-plugins.yaml
   │  ├─ Get list of active plugins
   │
   ├─ PluginManager.load_plugins()
   │  ├─ Import each plugin Python module
   │  ├─ Instantiate with plugin config
   │  ├─ Return: list of loaded plugin objects
   │
   ├─ Final Config = deep_merge(global > context > plugins)
   │  ├─ Priority: plugins override context override global
   │
4. DynamicHooksEngine.validate_skill(skill_path)
   ├─ For each enabled gate (1-8):
   │  ├─ Create GateValidator(gate_num, final_config)
   │  ├─ Run validator.execute(skill_path)
   │  ├─ Store result
   │
   ├─ For each plugin:
   │  ├─ Call plugin.on_validate_skill(skill, gate_results)
   │  ├─ Plugin runs custom validation
   │  ├─ Collect plugin results
   │
   ├─ Plugin Consensus Voting
   │  ├─ If 2+ plugins pass: result = PASS
   │  ├─ If 2+ plugins fail: result = FAIL
   │
5. LearningEngine.track(skill_path, results)
   ├─ Append to metrics/validation_metrics.json
   ├─ Record: timestamp, skill, gates, failures
   │
6. Return Results
   ├─ Print validation output
   ├─ Exit with code 0 (pass) or 1 (fail)
   │
7. CLI Captures Exit Code
   ├─ ./hooks.sh skill <path> → exit code determines result
```

---

## Dependency Graph (What Depends on What)

### Level 1: Configuration Files (Lowest)
```
config/hooks-config.yaml
├─ Global defaults for all validation
├─ Used by: ConfigurationLoader, all validators
├─ Depends on: schemas/config-schema.json (validation)
└─ If breaks: All validation fails

config/hooks-context.yaml
├─ Phase-specific rule overrides
├─ Used by: ContextResolver, ConfigurationLoader
├─ Depends on: HOOKS_CONTEXT env var (which phase to load)
└─ If breaks: Wrong phase rules loaded

config/hooks-plugins.yaml
├─ Plugin registry (which plugins enabled)
├─ Used by: PluginManager
├─ Depends on: Actual plugin files in plugins/
└─ If breaks: Plugins won't load
```

### Level 2: Schema Files (Validation)
```
schemas/config-schema.json
├─ JSON Schema for hooks-config.yaml
├─ Used by: ConfigurationLoader (validates during load)
├─ Depends on: Nothing (checked before use)
└─ If breaks: config/ files rejected as invalid

schemas/plugin-schema.json
├─ JSON Schema for plugins
├─ Used by: PluginManager (validates plugin structure)
├─ Depends on: Nothing (checked before use)
└─ If breaks: Custom plugins rejected
```

### Level 3: Environment (Runtime Inputs)
```
.env.local
├─ Local configuration overrides
├─ Used by: ContextResolver (check for HOOKS_CONTEXT)
├─ Depends on: Nothing (optional file)
└─ If missing: Falls back to phase_4

environ['HOOKS_CONTEXT']
├─ Environment variable set in shell
├─ Used by: ContextResolver (which phase to use)
├─ Depends on: User setting it (or CI/CD setting it)
└─ If not set: Falls back to phase_4
```

### Level 4: Utilities (Support)
```
metrics/validation_metrics.json
├─ Historical validation results
├─ Used by: LearningEngine (analyze patterns)
├─ Created by: LearningEngine.track()
├─ Depends on: Validation runs completing
└─ If broken: Learning just starts fresh

plugins/* (custom plugins)
├─ User-created validation plugins
├─ Used by: PluginManager (dynamic import)
├─ Implements: BasePlugin interface
├─ Depends on: config/hooks-plugins.yaml (enable/disable)
└─ If broken: Validation fails or skips plugin
```

### Level 5: Core Engine (Main Logic)
```
engine/dynamic_hooks_engine.py
├─ Main orchestrator (decision maker)
├─ Used by: All hook entry scripts
├─ Calls: ConfigurationLoader, ContextResolver, PluginManager, Validators
├─ Depends on: Levels 1-4 all working
└─ If broken: Entire system breaks

engine/configuration_loader.py
├─ Loads YAML + validates with JSON schema
├─ Used by: DynamicHooksEngine.__init__()
├─ Depends on: config/ files + schemas/
└─ If broken: config can't be loaded

engine/context_resolver.py
├─ Detects which phase to use
├─ Used by: DynamicHooksEngine.__init__()
├─ Depends on: HOOKS_CONTEXT env var + .env.local
└─ If broken: Wrong phase rules applied

engine/plugin_manager.py
├─ Loads + executes plugins
├─ Used by: DynamicHooksEngine.validate_skill()
├─ Depends on: config/hooks-plugins.yaml + plugins/ directory
└─ If broken: No custom validation runs

engine/learning_engine.py
├─ Tracks metrics, suggests optimizations
├─ Used by: DynamicHooksEngine (after validation)
├─ Depends on: metrics/validation_metrics.json
└─ If broken: Metrics not tracked (validation still works)

validators/dynamic_gate_validators.py
├─ 8 gate implementations
├─ Used by: DynamicHooksEngine.validate_skill()
├─ Depends on: final_config (merged settings)
└─ If broken: Validation gates fail
```

### Level 6: Hook Scripts (Entry Points)
```
pre-commit-message.py
├─ Validates commit messages
├─ Used by: CLI (./hooks.sh message), git hooks
├─ Calls: DynamicHooksEngine
├─ Depends on: engine/ working + config/ loaded
└─ If broken: Commit message validation fails

pre-commit-skills.py
├─ Validates all skills + skill names
├─ Used by: CLI (./hooks.sh skills), CI/CD
├─ Calls: DynamicHooksEngine
├─ Depends on: engine/ working + config/ loaded
└─ If broken: Skill validation fails

validate-skill.py
├─ Validates single skill with 8 gates
├─ Used by: CLI (./hooks.sh skill <path>), detailed checks
├─ Calls: DynamicHooksEngine
├─ Depends on: engine/ working + config/ loaded
└─ If broken: Comprehensive validation fails

pre-commit-workflows.py
├─ Validates workflow definitions
├─ Used by: CLI (./hooks.sh workflows)
├─ Calls: DynamicHooksEngine
├─ Depends on: engine/ working + config/ loaded
└─ If broken: Workflow validation fails
```

### Level 7: CLI Tool (User Interface)
```
hooks.sh
├─ Command dispatcher
├─ Used by: Command line, CI/CD, git hooks
├─ Calls: Python scripts above
├─ Depends on: All Python modules available
└─ If broken: Can't run any validation

.env.example
├─ Configuration template
├─ Used by: Users (copy to .env.local)
├─ Depends on: Nothing (reference only)
└─ If wrong: Users get confused about options
```

### Level 8: Integration Points (External)
```
GitHub Actions (.github/workflows/)
├─ CI/CD that runs validation
├─ Calls: hooks.sh scripts
├─ Sets: env.HOOKS_CONTEXT
├─ Depends on: All levels 1-7 working

.git/hooks/commit-msg
├─ Pre-commit hook (auto-runs on git commit)
├─ Calls: hooks.sh message <msg-file>
├─ Depends on: hooks.sh + all Python modules
└─ If broken: Can't commit messages

Team's local environment
├─ Developer's machine with hooks installed
├─ Calls: hooks.sh via .env.local
├─ Depends on: Python 3.8+, PyYAML, jsonschema
└─ If broken: Local validation doesn't work
```

---

## Critical Load Order (What Must Load First)

```
SEQUENCE (must happen in order):
  1. ConfigurationLoader reads config/hooks-config.yaml
     └─ validates with schemas/config-schema.json
     └─ validates with schemas/plugin-schema.json

  2. ContextResolver detects HOOKS_CONTEXT (env var or .env.local)
     └─ looks up context in hooks-context.yaml

  3. Deep merge final_config:
     └─ global defaults (from step 1)
     └─ + context overrides (from step 2)
     └─ + plugin configs (if plugins enabled)

  4. PluginManager loads plugins from plugins/
     └─ uses final_config settings
     └─ validates each with plugin-schema.json

  5. Validators use final_config
     └─ all 8 gates get merged settings

  6. Plugins execute (after validators)
     └─ plugins use results from validators

  7. Consensus voting on plugin results
     └─ need 2+ plugin agreement

  8. LearningEngine tracks results
     └─ appends to metrics/validation_metrics.json
```

**If this order is violated:** system breaks

---

## External Dependencies (Out of Scope)

```
Python Runtime
├─ Version: 3.8+ required
├─ Used by: All Python code
├─ Provides: os, sys, json, pathlib, etc

PyYAML
├─ Version: 6.0+ required
├─ Used by: ConfigurationLoader (load YAML files)
├─ Provides: yaml.safe_load(), yaml.dump()
├─ Package: pip install PyYAML

jsonschema
├─ Version: 4.0+ required
├─ Used by: ConfigurationLoader (validate with JSON schema)
├─ Provides: jsonschema.validate(), jsonschema.ValidationError
├─ Package: pip install jsonschema

Git (optional)
├─ Used by: .git/hooks integration
├─ Provides: git commit hooks mechanism

Bash/Shell (optional)
├─ Used by: hooks.sh CLI tool
├─ Requirement: Bash available in PATH
```

---

## Files That Must Exist

```
CRITICAL (system won't work without):
  .agents/hooks/config/hooks-config.yaml
  .agents/hooks/config/hooks-context.yaml
  .agents/hooks/config/hooks-plugins.yaml
  .agents/hooks/engine/dynamic_hooks_engine.py
  .agents/hooks/engine/configuration_loader.py
  .agents/hooks/schemas/config-schema.json

REQUIRED (for full functionality):
  .agents/hooks/engine/context_resolver.py
  .agents/hooks/engine/plugin_manager.py
  .agents/hooks/engine/learning_engine.py
  .agents/hooks/pre-commit-*.py (all 4 hooks)

OPTIONAL (system works without):
  .env.local (uses .env.example if missing)
  plugins/* (custom plugins)
  metrics/validation_metrics.json (auto-created)
  .git/hooks/commit-msg (manual git hook)
```

---

## Breakage Scenarios (What Breaks What)

### If config/hooks-config.yaml is deleted:
- ❌ ConfigurationLoader fails to load defaults
- ❌ All validation fails immediately
- **Fix:** Restore from git or use backup

### If HOOKS_CONTEXT env var is set to undefined phase:
- ❌ ContextResolver can't find rules in hooks-context.yaml
- ⚠️ Falls back to 'phase_4' (might not be intended)
- **Fix:** Set to valid phase: phase_4, phase_5_enrichment, or phase_6_bootstrap

### If hooks-context.yaml is missing a phase:
- ❌ ContextResolver looks for phase in file, not found
- ❌ Falls back to global defaults (wrong rules might apply)
- **Fix:** Add phase entry to hooks-context.yaml

### If schemas/config-schema.json is broken:
- ❌ ConfigurationLoader can't validate config files
- ❌ All validation fails (maybe silently)
- **Fix:** Restore from git

### If engine/dynamic_hooks_engine.py is modified incorrectly:
- ❌ Main orchestrator breaks
- ❌ ALL validation fails
- **Fix:** Restore from git or rewrite carefully

### If plugin is enabled but file doesn't exist:
- ❌ PluginManager tries to import, gets ImportError
- ❌ Validation fails (can't find plugin)
- **Fix:** Remove from hooks-plugins.yaml or create plugin file

### If .env.local has syntax error:
- ⚠️ ContextResolver might use wrong env vars
- ⚠️ Validation might use unexpected phase
- **Fix:** Fix .env.local syntax or delete it (falls back to defaults)

### If metrics/validation_metrics.json is corrupted:
- ⚠️ LearningEngine can't read historical data
- ⚠️ Learning suggestions won't work
- ✅ Validation still works (learning is non-critical)
- **Fix:** Delete file (auto-recreated on next run)

---

## Modification Impact Matrix

| If You Change | Then These Break | Then These Need Update |
|---|---|---|
| hooks-config.yaml thresholds | Validation behavior changes | Test with all phases, maybe DECISIONS.md |
| hooks-context.yaml phases | Different phase rules | Document in CLAUDE.md if adding new phase |
| engine/* (edit code) | EVERYTHING | Multiple things depend on this |
| plugin registry | Plugin execution | Plugins might not load |
| .env.example | User confusion | Not breaking but causes confusion |
| Pre-commit hook scripts | Exact validation behavior | Nothing breaks, but might not get new features |
| Schema files | Config validation | All config files must re-validate |

---

## Recommended Update Frequency

| Component | Review | Update |
|---|---|---|
| config/hooks-config.yaml | Weekly | When thresholds need tuning |
| config/hooks-context.yaml | Monthly | When phase rules need adjustment |
| config/hooks-plugins.yaml | Quarterly | When adding/removing plugins |
| engine/ files | Annually | If bugs found or architecture changes |
| `.env.example` | Quarterly | If adding env vars |
| DECISIONS.md | Per change | Document architectural decisions |
| CLAUDE.md | Quarterly | Keep "What NOT to Change" accurate |

---

**Version:** 1.0  
**Status:** Reference  
**Last Updated:** 2026-04-12
