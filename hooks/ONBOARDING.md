# First-Time Onboarding - Dynamic Hooks System

**For: AI Assistants & New Developers**  
**Read Time: 15 minutes**  
**Result: You'll understand how the system works and be able to modify it safely**

---

## Start Here: The 15-Minute Ramp-Up

### Minute 1-2: Understand the Problem

**What is this system?**
```
It's a validation framework that checks "skills" for an AI agent project.
Before: 50 hardcoded thresholds scattered across Python files
After: Externalized configuration + dynamic rules + plugin system
```

**Why does it matter?**
- Different projects need different validation rules (strict vs lenient)
- Teams want to add custom validation without modifying core code
- Thresholds should be tunable without code changes

---

### Minute 3-7: Read CLAUDE.md (Key Context)

Open `.agents/hooks/CLAUDE.md` and read sections in this order:

1. **Project Identity** (1 min)
   - What this is, what problem it solves
   
2. **Three Critical Layers** (1 min)
   - Configuration layer (YAML)
   - Runtime layer (Python engine)
   - Hook scripts (entry points)
   
3. **Architecture Decisions** (2 min)
   - Why YAML? Why 3-level merge? Why consensus voting?
   - Understand the intentional design choices
   
4. **What NOT to Change** (1 min)
   - Read the red boxes: `engine/` files, configuration hierarchy, BasePlugin interface
   - These are boundaries you shouldn't cross

5. **What IS OK to Modify** (1 min)
   - Read the green boxes: thresholds, phases, plugins, documentation
   - These are customization points

**Stop if:** Anything unclear. Re-read until it clicks.

---

### Minute 8-10: See How It Actually Works

Run these commands:

```bash
cd .agents/hooks

# 1. Check system health
./hooks.sh status
# You should see: ✓ marks for all components

# 2. See what phase is active
./hooks.sh context
# Shows: Current phase (default: phase_4), current mode (strict/lenient)

# 3. View current configuration
./hooks.sh config
# Shows: First 30 lines of hooks-config.yaml

# 4. Try validating a skill
./hooks.sh skill ../skills/animation-blend/SKILL.md
# Should show: Pass/fail with gate-by-gate results
```

**What you just verified:** System is working, health check passes.

---

### Minute 11-12: Understand the Configuration

Open `config/hooks-config.yaml` and scan:
- Look for thresholds (min_length, max_bytes, file sizes)
- See the three validation modes: strict, lenient, experimental
- Note the approved domains list

Open `config/hooks-context.yaml` and scan:
- See phase_4 (strict production)
- See phase_5_enrichment (lenient development)
- See phase_6_bootstrap (experimental new skills)

**Key insight:** All these values can be changed without restarting anything.

---

### Minute 13-14: Understand the Workflow

When you run `./hooks.sh skill <path>`:

```
1. Hook entry point launches Python script
2. Script creates DynamicHooksEngine instance
3. Engine loads config/hooks-config.yaml (global defaults)
4. Engine checks HOOKS_CONTEXT env var (phase_5_enrichment)
5. Engine loads config/hooks-context.yaml (phase_5 overrides)
6. Engine merges: phase_5 > global (phase_5 wins)
7. Engine loads config/hooks-plugins.yaml (active plugins)
8. Engine loads plugins from plugins/ directory
9. Engine runs all 8 validation gates with merged config
10. Plugins validate additionally (consensus voting)
11. Results tracked to metrics/validation_metrics.json
12. Return pass/fail
```

**Key insight:** Configuration merges at runtime. You can change values and they take effect immediately.

---

### Minute 15: You're Ready

You now know:
- ✅ What this system is (validation framework with dynamic config)
- ✅ Why it matters (external config, phase support, plugins)
- ✅ What you can modify (thresholds, phases, plugins, docs)
- ✅ What you can't modify (engine files, architecture)
- ✅ How to test changes (./hooks.sh commands)

---

## Next: What Do You Want to Do?

### Use Case 1: "I want to relax validation in phase 5"

1. Open `config/hooks-context.yaml`
2. Find `phase_5_enrichment` section
3. Increase tolerances:
   ```yaml
   thresholds:
     file_size:
       max_bytes: 1500  # From 1200
   ```
4. Test: `./hooks.sh set-context phase_5_enrichment && ./hooks.sh skill <path>`
5. Result: Skill now passes with relaxed rules

**Time:** 5 minutes  
**Risk:** Low (only affects phase 5)  
**Verify:** Run `./hooks.sh set-context phase_4` after - phase_4 should still be strict

---

### Use Case 2: "I want to add a new approved domain"

1. Open `config/hooks-config.yaml`
2. Find `approved_domains` section
3. Add your domain:
   ```yaml
   approved_domains:
     - animation
     - my-new-domain  # ← Add here
   ```
4. Test: `./hooks.sh skill <skill_with_my-new-domain>`
5. Result: Skill with that domain now passes domain check

**Time:** 3 minutes  
**Risk:** Low (only adds domain)  
**Verify:** All phases still pass global validation

---

### Use Case 3: "I want to understand why this decision was made"

1. Open `DECISIONS.md`
2. Search for the decision (e.g., "YAML for Configuration")
3. Read: Problem → Solution → Why → Trade-offs → Consequences
4. Understand the why

**Example:** Want to know why we use YAML instead of JSON?
→ Go to Decision 1 → See: "Why YAML Over Alternatives" table

**Time:** 5-10 minutes per decision

---

### Use Case 4: "I need to modify something, but I'm not sure if it's safe"

1. Open `MODIFICATION_CHECKLIST.md`
2. Go through "Pre-Modification Interview" (5 questions)
3. If all answers are "yes" → proceed
4. If any answer is "no" → read CLAUDE.md::What NOT to Change

**Example:** Want to edit `engine/dynamic_hooks_engine.py`?
→ Checklist question 2: "Does CLAUDE.md allow this?" → NO
→ Read Why → It's core logic that many things depend on
→ Consider if you can achieve goal by editing config files instead

---

### Use Case 5: "Things are broken, how do I understand what went wrong?"

1. Run `./hooks.sh status` - see if all files are present
2. Run `./hooks.sh config` - see if configuration loaded
3. Open `DEPENDENCIES.md` - "Breakage Scenarios" section
4. Find your scenario and the fix

**Example:** Validation fails with "phase not found" error?
→ Go to DEPENDENCIES.md → "Breakage Scenarios"
→ Find "If HOOKS_CONTEXT env var is set to undefined phase"
→ Fix: Set to valid phase (phase_4, phase_5_enrichment, or phase_6_bootstrap)

---

## Key Documents to Know

| Document | When to Read | Read Time |
|---|---|---|
| **CLAUDE.md** | First time, then anytime you're confused | 5 min |
| **QUICK_REFERENCE.md** | When you want quick lookups | 2 min (skim) |
| **MODIFICATION_CHECKLIST.md** | Before making ANY change | 3-5 min |
| **DECISIONS.md** | When you want to understand WHY | 10-15 min |
| **DEPENDENCIES.md** | When debugging breakages | 5-10 min |
| **README.md** | When you need deep details | 15-20 min |
| **INDEX.md** | When navigating the system | 2-3 min |

---

## Command Cheat Sheet

```bash
# Understand current state
./hooks.sh status              # System health check
./hooks.sh context             # Current phase
./hooks.sh config              # Current configuration

# Switch phases
./hooks.sh set-context phase_4             # Strict (production)
./hooks.sh set-context phase_5_enrichment  # Lenient (dev)
./hooks.sh set-context phase_6_bootstrap   # Experimental (new)

# Validate
./hooks.sh skill <path>        # Single skill with 8 gates
./hooks.sh skills              # All skills
./hooks.sh workflows           # All workflows
./hooks.sh message <file>      # Commit message

# Debugging
./hooks.sh debug validate-skill # Debug hook
./hooks.sh help                # Show all commands
```

---

## Modification Pattern: Safe vs Risky

### ✅ SAFE - Do These

```bash
# Editing config (always safe)
vim config/hooks-config.yaml   # Global thresholds
vim config/hooks-context.yaml  # Phase-specific rules
vim config/hooks-plugins.yaml  # Enable/disable plugins

# Editing documentation (always safe)
vim QUICK_REFERENCE.md
vim README.md
vim CLIPBOARD.md

# Testing in isolation (safe)
./hooks.sh set-context phase_5_enrichment
./hooks.sh skill <path>
```

### 🚫 RISKY - Don't Do These

```bash
# Editing engine (breaks things)
vim engine/dynamic_hooks_engine.py          # ❌ Core logic
vim engine/configuration_loader.py          # ❌ Config system
vim engine/context_resolver.py              # ❌ Phase detection

# Editing schemas (breaks validation)
vim schemas/config-schema.json              # ❌ Config validation

# Adding hardcoded values (breaks dynamicism)
vim pre-commit-skills.py                    # ❌ Should use config
# ... hardcoded_threshold = 50              # NO! Use config
```

---

## Testing Your Changes

### Never Do This
```bash
vim config/hooks-config.yaml
# Make one change
```

### Always Do This Instead
```bash
vim config/hooks-config.yaml
# Make one change

# Test immediately
./hooks.sh status              # Verify files OK
./hooks.sh config              # See merged config
./hooks.sh set-context phase_4 && ./hooks.sh skill <path>
./hooks.sh set-context phase_5_enrichment && ./hooks.sh skill <path>
./hooks.sh set-context phase_6_bootstrap && ./hooks.sh skill <path>

# If OK: done
# If NOT OK: revert with git restore config/hooks-config.yaml
```

---

## Common Questions

**Q: Can I add a new validation gate?**  
A: Possibly. Read CLAUDE.md::What NOT to Change. Gates are internal. You'd need to modify `validators/dynamic_gate_validators.py` which is risky. Better approach: create a plugin instead.

**Q: Can I change how plugins vote?**  
A: No. Consensus voting (need 2+ to pass) is intentional architectural decision. See DECISIONS.md::Decision 3.

**Q: Why does phase_5 allow bigger files than phase_4?**  
A: Intentional. Phase 5 is for enriched content (development). See hooks-context.yaml and CLAUDE.md::Phase Definitions.

**Q: My custom plugin isn't loading. What's wrong?**  
A: Check: (1) Plugin in hooks-plugins.yaml with enabled=true (2) Plugin file exists in plugins/ (3) Plugin has correct interface. See DEPENDENCIES.md::Plugin loading for full checklist.

**Q: Can I auto-apply learning suggestions?**  
A: No. Currently report-only (check metrics/suggestions.json). See DECISIONS.md::Decision 4 for why.

**Q: Can I use environment variables to customize phases?**  
A: Yes! Set `HOOKS_CONTEXT=phase_5_enrichment` to switch. See CLAUDE.md::Configuration Hierarchy.

---

## You're Now Ready!

You can:
- ✅ Understand what needs changing
- ✅ Know what's safe to modify
- ✅ Know what to NOT modify
- ✅ Test your changes properly
- ✅ Debug when things break
- ✅ Find answers in documentation

---

## Before You Leave

**Bookmark these for quick reference:**
- `QUICK_REFERENCE.md` - Fastest lookup
- `MODIFICATION_CHECKLIST.md` - Before every change
- `CLAUDE.md::What's OK to Modify` - Am I allowed?
- `DEPENDENCIES.md::Breakage Scenarios` - Debugging

**Remember:**
1. Always run `./hooks.sh status` first
2. Always test all 3 phases
3. Always check MODIFICATION_CHECKLIST.md before changing
4. Always read the relevant decision/doc before deciding

---

**Onboarding Complete!** 🎉

You're ready to work with this system safely and confidently.

Good luck! 🚀
