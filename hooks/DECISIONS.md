# Architectural Decision Record - Dynamic Hooks System

**Version:** 1.0 | **Status:** Production Ready | **Last Updated:** 2026-04-12

---

## Decision 1: YAML for Configuration Storage

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
Hardcoded validation thresholds were scattered across 4 Python files:
- 50+ hardcoded constants (description min/max, file sizes, step counts, domain lists)
- Changing a threshold required editing Python code
- No way to have different thresholds for different phases without code duplication
- Knowledge of threshold purpose buried in code comments

### Solution
Move ALL thresholds to external YAML configuration files:
- `config/hooks-config.yaml` - Global defaults
- `config/hooks-context.yaml` - Phase/environment specific overrides
- `config/hooks-plugins.yaml` - Plugin registry

### Why YAML Over Alternatives

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **YAML** (chosen) | Human-readable, supports comments, hierarchical, Python-native | Requires schema validation | ✅ CHOSEN |
| JSON | Strict schema validation, widely supported | No comments, verbose, less human-friendly | Rejected |
| Environment variables only | Simple, no files to parse | Unversioned, can't document rationale, no structure | Rejected |
| TOML | Good for config, comments | Less hierarchical than YAML, less common | Rejected |
| Python files | Already in codebase | Still hardcoded (doesn't solve problem) | Rejected |

### Trade-offs Accepted
- ✅ Need JSON schema validation (ConfigurationLoader must validate YAML structure)
- ✅ Multiple files to maintain (acceptable because clear separation of concerns)
- ✅ Merge logic for three-level hierarchy (acceptable, encapsulated in ConfigurationLoader)

### Alternatives Rejected
- **Hardcoded + environment overrides:** Doesn't solve maintainability, still has Pythoncode
- **All config in single file:** Makes phases unmaintainable, unclear which threshold applies where
- **Config API (live editing):** Out of scope, too complex for current phase

### Consequences
- ✅ Thresholds now single source of truth (YAML files)
- ✅ Non-technical users can modify thresholds
- ✅ Git tracks all threshold changes (audit trail)
- ✅ Different phases can have completely different rule sets
- ⚠️ Must validate YAML structure (catching user typos)

---

## Decision 2: Three-Level Configuration Merge Hierarchy

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
Need both:
- Global defaults that apply to all validations
- Phase-specific overrides (phase_4 strict, phase_5 lenient, phase_6 experimental)
- Plugin-specific customizations (without modifying core config)

If all in one file = hard to understand which rule applies when  
If in separate files = how do we merge them?

### Solution
Three-level hierarchy with explicit precedence:

```
Priority 1 (HIGHEST): Plugin-specific settings
Priority 2: Context-specific settings (phase_5_enrichment overrides phase_4)
Priority 3 (LOWEST): Global defaults
```

**Example:**
```yaml
# Level 3: Global (hooks-config.yaml)
description:
  min_length: 50

# Level 2: Context (hooks-context.yaml :: phase_5_enrichment)
thresholds:
  description:
    min_length: 30

# Level 1: Plugin (hooks-plugins.yaml)
custom_validator:
  config:
    description:
      min_length: 20

# Result when using custom_validator in phase_5: min_length = 20
```

### Merge Algorithm
```python
config = load("config/hooks-config.yaml")              # Level 3
context = load("config/hooks-context.yaml")[HOOKS_CONTEXT]  # Level 2
plugins = load("config/hooks-plugins.yaml")            # Level 1
final = deep_merge(config, context, plugins)           # plugin > context > global
```

### Why This Order (Plugin > Context > Global)?

| Order | Reasoning |
|-------|-----------|
| **Plugin at top** | Plugins are closest to actual validation, need most power |
| **Context in middle** | Phases are organizational, should override global defaults |
| **Global at bottom** | Fallback for anything not specified elsewhere |

### Alternatives Rejected
- **Flat merge (all equal):** Unclear what wins in conflicts
- **Global > Context > Plugin:** Plugins couldn't override poorly-set phases
- **No hierarchy (separate configs used separately):** Requires switching files manually each time

### Trade-offs Made
- ✅ Merge logic complexity (acceptable, hidden in ConfigurationLoader)
- ✅ Multiple files to understand (acceptable, documented clearly)
- ⚠️ Plugins can override everything (mitigated by only enabling trusted plugins)

### Consequences
- ✅ Themes/domains/teams can use phase_5, strict rules in phase_4, relaxed in phase_6
- ✅ Custom plugins can enforce their own stricter rules if needed
- ✅ Easy to understand precedence (plugin > context > global, always)
- ⚠️ Must document which file to edit for which change

---

## Decision 3: Plugin Consensus Voting (Majority Rule)

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
Multiple plugins will validate the same skill:
- Plugin A: Check custom domains → PASS
- Plugin B: Check ML-specific fields → FAIL
- Plugin C: Check documentation quality → PASS

What's the final result? How do we prevent one strict plugin from blocking all contributions?

### Solution
**Consensus voting:** Need 2+ plugins to pass for test to PASS

- If 2/3 pass → result = PASS
- If 2/3 fail → result = FAIL
- Single plugins alone don't block or pass validation

### Voting Examples

| Scenario | A | B | C | Result | Reasoning |
|----------|---|---|---|--------|-----------|
| All pass | ✅ | ✅ | ✅ | ✅ PASS | Consensus: pass |
| 2 pass, 1 fail | ✅ | ✅ | ❌ | ✅ PASS | Majority: 2/3 pass |
| 1 pass, 2 fail | ✅ | ❌ | ❌ | ❌ FAIL | Majority: 2/3 fail |
| All fail | ❌ | ❌ | ❌ | ❌ FAIL | Consensus: fail |

### Alternatives Rejected

| Approach | How it Works | Why Rejected |
|----------|---|---|
| **Unanimous** | Need ALL plugins to pass | Too strict, one plugin blocks everything |
| **First-pass-wins** | First plugin result = final | Skips validation by other plugins |
| **Weighted voting** | Some plugins count more | Too complex, hard to explain |
| **Any-plugin-passes** | Only need 1 to pass | Ignores real failures |
| **Consensus (chosen)** | Need majority (2+) | Balanced, fair, extensible |

### Why Consensus?
- **Fair:** No single plugin can block/pass
- **Extensible:** Can add plugins without breaking majority (need 2+)
- **Simple:** Easy to explain and understand
- **Scalable:** Works with 2 plugins or 10 plugins

### Consequences
- ✅ Prevents single strict plugin from blocking all contributions
- ✅ Prevents false positives from single overzealous plugin
- ✅ Encourages building multiple plugins that agree
- ⚠️ If all plugins fail → result fails (no false passthrough)

---

## Decision 4: Learning Engine as Report-Only (No Auto-Modifications)

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
Should the system automatically learn optimal thresholds from historical data?

**Option A - Auto-modify:** System changes thresholds based on what works  
**Option B - Report-only:** System suggests changes, user applies manually

### Solution
**Report-Only Mode:** Learning engine tracks metrics and suggests changes via JSON file, user reviews and applies manually.

```python
# What learning engine does:
engine.track(skill, result)  # Record pass/fail per gate
suggestions = engine.suggest_optimizations()  # Analyze patterns
write("metrics/suggestions.json", suggestions)  # Save suggestions

# What user does:
# 1. Review metrics/suggestions.json
# 2. If agree: manually edit hooks-config.yaml or hooks-context.yaml
# 3. Test with ./hooks.sh skill <path>
# 4. If works: commit changes
```

### Why NOT Auto-Modify?

| Concern | Impact | Solution |
|---------|--------|----------|
| Threshold changes affect all contributors | High | Require human review before applying |
| Auto-tuned thresholds might be too loose | High | Visible suggestions stay conservative |
| No audit trail for why changed | Medium | Manual change = git commit with rationale |
| Production validation might drift | High | Strict phase_4 never auto-changed |

### Alternatives Rejected
- **Fully automatic:** Too risky, thresholds affect all contributors
- **Voting-based:** Same as automatic (no human in loop)
- **No learning at all:** Gives up optimization opportunity

### Trade-offs Made
- ✅ Manual process means slower optimization (acceptable)
- ✅ More work for maintainers (only to approve suggestions, not constant tuning)
- ⚠️ Suggestions might be ignored (mitigated by clear metrics + visualization)

### Consequences
- ✅ All threshold changes are intentional (human-reviewed)
- ✅ Git history shows why thresholds changed (commit messages)
- ✅ Can revert bad suggestions (git revert)
- ✅ Phase_4 (production) always stays strict unless explicitly changed
- ⚠️ Optimization slower than automatic system

---

## Decision 5: Environment Variable for Phase Detection

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
Need to switch validation phases (phase_4 → phase_5_enrichment → phase_6_bootstrap).

How should the system know which phase to use?

### Solution
Use `HOOKS_CONTEXT` environment variable:

```bash
# CLI
export HOOKS_CONTEXT=phase_5_enrichment
./hooks.sh skill <path>     # Uses phase_5 rules

# Or in .env.local
HOOKS_CONTEXT=phase_5_enrichment

# Or in CI/CD
env:
  HOOKS_CONTEXT: ci_strict
```

### Alternatives Rejected

| Option | How it Works | Why Rejected |
|--------|---|---|
| **Auto-detect from version file** | Read project version → phase | Requires version file, doesn't work in CI |
| **Auto-detect from branch** | Branch name → phase | Doesn't work in CI/CD, fragile |
| **Config file detection** | Look for phase marker file | Auto-magic, unreliable, hard to debug |
| **CLI flag only** | `./hooks.sh --phase=5 skill <path>` | Doesn't work for git hooks, hard to configure |
| **Env var (chosen)** | `HOOKS_CONTEXT=phase_5` | Standard, CI/CD friendly, explicit, debuggable |

### Why Environment Variables?
- ✅ Standard across Unix/Linux/Windows
- ✅ CI/CD systems can set via `env:` section
- ✅ Local can override with `.env.local`
- ✅ Easy to debug (`echo $HOOKS_CONTEXT`)
- ✅ Python reads via `os.getenv()`
- ✅ Explicit (no magic detection)

### Consequences
- ✅ Clear what phase is active (`./hooks.sh context` shows it)
- ✅ CI/CD can configure per pipeline step
- ✅ Local developers can customize via `.env.local`
- ⚠️ User must remember to set (no auto-detection)

---

## Decision 6: Backward Compatibility Wrapper

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
We're refactoring 4 hook scripts to use the new engine. Can't break existing usage:
- `.git/hooks/commit-msg` might already call old scripts
- GitHub Actions workflows configured for old entry points
- Teams have integrated old hooks into CI/CD pipelines

### Solution
Keep old hook scripts as thin wrappers:

```python
# OLD: pre-commit-skills.py (before refactor)
DESCRIPTION_MIN = 50
DESCRIPTION_MAX = 100
# ... hardcoded logic ...

# NEW: pre-commit-skills.py (after refactor)
engine = DynamicHooksEngine()
result = engine.validate_skill(skill_path)
# ... same output as before ...
```

Old API stays identical, implementation changes internally.

### Trade-offs Made
- ✅ Extra wrapper layer adds 2-3% performance overhead (acceptable)
- ✅ Must maintain compatibility with old behavior (documented in CLAUDE.md)
- ✅ Old and new code run in parallel during transition (acceptable)

### Why This Approach?
- **Zero breaking changes:** Existing users not affected
- **Gradual migration:** Can move to new system incrementally
- **Git hooks still work:** Pre-commit hooks don't need reconfiguration
- **CI/CD continues:** Existing pipelines keep working
- **Test coverage preserved:** Old tests still pass

### Alternative Rejected
- **Full replacement:** Break existing integrations, high risk
- **New entry points only:** Force everyone to update configurations
- **Dual system (old + new):** Confusing, hard to maintain

### Consequences
- ✅ Production continues uninterrupted
- ✅ Teams can migrate at their own pace
- ✅ New features available via engine without requiring migration
- ⚠️ Must keep old and new in sync during transition period

---

## Decision 7: JSON Schema v7 for Config Validation

**Date Decided:** 2026-04-12  
**Status:** ✅ IMPLEMENTED

### Problem
YAML configs are flexible but error-prone:
- Typos in field names (e.g., `desription` instead of `description`)
- Invalid values (e.g., `max_length: "not a number"`)
- Missing required fields
- Wrong structure (e.g., nested differently than expected)

Need schema validation to catch these before validation runs.

### Solution
Use JSON Schema v7 to validate YAML structure:

```json
{
  "type": "object",
  "properties": {
    "gates": {
      "type": "object",
      "properties": {
        "description": {
          "type": "object",
          "properties": {
            "min_length": { "type": "integer", "minimum": 0 },
            "max_length": { "type": "integer" }
          },
          "required": ["min_length", "max_length"]
        }
      }
    }
  }
}
```

### Why JSON Schema v7?

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **JSON Schema v7** | Human-readable, widely supported, Python library exists | Draft is older (v2020-12 exists) | ✅ CHOSEN |
| Pydantic | Powerful, Python-native | Python-only, requires defining classes | Rejected |
| OpenAPI Schema | Comprehensive | Overkill for this use case | Rejected |
| YAML Schema | Native to YAML | Less tooling support, non-standard | Rejected |
| No schema | Simpler | Can't catch errors early | Rejected |

### Why v7 (not v2020-12)?
- ✅ Better Python tooling support (`jsonschema` library)
- ✅ More stable/mature
- ✅ No need for newer features (v7 sufficient for our use case)
- ⚠️ Missing some v2020-12 features (acceptable trade-off)

### Consequences
- ✅ User typos caught immediately (schema validation fails)
- ✅ Clear error messages (which field is wrong)
- ✅ Can't proceed with invalid config (gates execution)
- ⚠️ Schema files themselves are authoritative (must be correct)

---

## Future Decisions Deferred (Out of Scope)

These decisions intentionally NOT made (kept for future phases):

| Decision | Why Deferred |
|----------|---|
| Automatic threshold optimization | Requires more historical data + testing |
| Web dashboard for metrics | Nice-to-have, not core functionality |
| Multi-project aggregation | Scope creep, first phase focuses on single project |
| Plugin discovery/marketplace | Future: teams share plugins across projects |
| Real-time monitoring/alerts | Future: when metrics mature |
| Language support (i18n) | Not core to 1.0, can add later |

---

## Decision Reversals (If Any)

None yet (system is new, decisions have held up).

---

**Document Status:** Complete  
**Last Updated:** 2026-04-12  
**Review Frequency:** When adding new decisions
