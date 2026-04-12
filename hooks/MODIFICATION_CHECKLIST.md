# Modification Checklist - Dynamic Hooks System

**Use this before modifying the hooks system to ensure safety and completeness.**

---

## Pre-Modification Interview

**Before you make ANY change, answer these questions:**

### 1. What Am I Changing?
- [ ] Configuration threshold (e.g., max_length, file_size)
- [ ] Phase-specific rule (e.g., phase_5 is too strict)
- [ ] New gate / validation rule
- [ ] Hook script logic
- [ ] Engine module (dynamic_hooks_engine.py, etc)
- [ ] Plugin system
- [ ] Documentation only
- [ ] Something else: _______________

**STOP:** If you selected "Engine module" → Read CLAUDE.md::What NOT to Change first

### 2. Does CLAUDE.md Allow This?
- [ ] Read CLAUDE.md::What NOT to Change
- [ ] Read CLAUDE.md::What IS OK to Modify
- [ ] My change is in the "OK" list
- [ ] If NOT in OK list → STOP and escalate

### 3. Will This Affect All Phases or Just One?
- [ ] All phases (global change) → edit `config/hooks-config.yaml`
- [ ] One phase (e.g., phase_5 only) → edit `config/hooks-context.yaml`
- [ ] Just plugins → edit `config/hooks-plugins.yaml`
- [ ] Unclear → Ask before proceeding

### 4. Will Existing CI/CD Need Updates?
- [ ] GitHub Actions workflows (`.github/workflows/`)
- [ ] Git hooks (`.git/hooks/commit-msg`)
- [ ] Team's pre-commit configuration
- [ ] Nothing (local-only change)
- [ ] Not sure → Check before proceeding

### 5. Does This Require a DECISIONS.md Entry?
- [ ] Yes - This is an architectural decision → Add entry to DECISIONS.md
- [ ] No - Just tuning existing values
- [ ] Maybe → When in doubt, add entry

### 6. Will This Break Backward Compatibility?
- [ ] No - Old usage patterns still work
- [ ] Yes - Will require users to change something
- [ ] Unsure → Think through carefully

If "Yes": Need migration plan before proceeding

---

## During Modification Checklist

**As you make changes, verify each step:**

### Step 1: Understand Current Behavior
- [ ] Run `./hooks.sh config` to see current configuration
- [ ] Run `./hooks.sh context` to see active phase
- [ ] Understand what you're changing and why
- [ ] Document the "before" state

### Step 2: Make Changes
- [ ] Edit ONLY the files you identified in Pre-Modification Interview
- [ ] Make minimal changes (don't "improve" unrelated code)
- [ ] Add comments explaining WHY if not obvious
- [ ] Keep changes focused on single purpose

### Step 3: Verify Files Exist
- [ ] Run `./hooks.sh status` to ensure no files broken
- [ ] Verify config files are well-formed (YAML syntax check)
- [ ] Check schemas exist (`schemas/config-schema.json`, etc)

### Step 4: Test in Isolation
- [ ] Run `./hooks.sh config` to see merged configuration
- [ ] If changed phase rules: `./hooks.sh set-context phase_X`
- [ ] Run single validation: `./hooks.sh skill <test-skill-path>`
- [ ] Check result is as expected

### Step 5: Test All Phases
- [ ] `./hooks.sh set-context phase_4 && ./hooks.sh skill <path>`
- [ ] `./hooks.sh set-context phase_5_enrichment && ./hooks.sh skill <path>`
- [ ] `./hooks.sh set-context phase_6_bootstrap && ./hooks.sh skill <path>`
- [ ] All three phases produce expected results

### Step 6: Run Comprehensive Tests
- [ ] `./hooks.sh skills` (validate all skills - should all pass)
- [ ] `./hooks.sh workflows` (validate all workflows)
- [ ] `./hooks.sh message <commit-msg-file>` (test commit message validation)

---

## Post-Modification Verification

**Before declaring modification complete:**

### Documentation Updates
- [ ] Updated QUICK_REFERENCE.md if commands changed
- [ ] Updated README.md if architecture changed
- [ ] Updated CLAUDE.md if decision changed
- [ ] Updated .env.example if new env vars added
- [ ] Updated INDEX.md if structure changed
- [ ] Added entry to DECISIONS.md if architectural change

### Backward Compatibility Check
- [ ] Old `HOOKS_CONTEXT` values still work
- [ ] Old hook scripts still work
- [ ] Existing CI/CD doesn't need changes (or has plan for migration)
- [ ] Team doesn't need to change their setup

### Code Quality
- [ ] No hardcoded values introduced (all config in YAML)
- [ ] No commented-out code left behind
- [ ] No debug print statements left (`print()`, `pdb`, etc)
- [ ] No temporary files committed
- [ ] Code follows existing style (same indentation, naming, etc)

### Testing
- [ ] All tests pass (if test suite exists)
- [ ] No regressions in existing functionality
- [ ] New functionality (if any) has been tested
- [ ] Edge cases considered

### Metrics & Learning
- [ ] If modified learning_engine.py: metrics format still valid
- [ ] If modified validation: learning still tracks correctly
- [ ] `metrics/validation_metrics.json` still readable

---

## Modification Patterns (Copy-Paste Safe)

### Pattern 1: Add New Approved Domain

**What to change:** `config/hooks-config.yaml`

```yaml
# BEFORE:
approved_domains:
  - animation
  - audio

# AFTER:
approved_domains:
  - animation
  - audio
  - my-new-domain    # ← Add your domain
```

**Test:**
```bash
./hooks.sh skill .agents/skills/my-new-domain-skill/SKILL.md
# Should pass Gate 7 (domain check)
```

**Update needed:** No other files need changes

---

### Pattern 2: Relax Validation in Phase 5

**What to change:** `config/hooks-context.yaml`

```yaml
# BEFORE:
phase_5_enrichment:
  thresholds:
    description:
      min_length: 50

# AFTER:
phase_5_enrichment:
  thresholds:
    description:
      min_length: 30  # ← Relaxed for dev
```

**Test:**
```bash
./hooks.sh set-context phase_5_enrichment
./hooks.sh skill .agents/skills/test-skill/SKILL.md
# Should now pass with shorter description
```

**Update needed:** Maybe update QUICK_REFERENCE.md example if illustrating phase differences

---

### Pattern 3: Enable/Disable Plugin

**What to change:** `config/hooks-plugins.yaml`

```yaml
# BEFORE:
ml_skill_validator:
  enabled: true

# AFTER:
ml_skill_validator:
  enabled: false  # ← Temporarily disabled
```

**Test:**
```bash
./hooks.sh skill .agents/skills/ml-skill/SKILL.md
# Should run without ML plugin checks
```

**Update needed:** Document why plugin disabled (Git commit message)

---

### Pattern 4: Tighten Global Validation

**What to change:** `config/hooks-config.yaml`

```yaml
# BEFORE (global):
description:
  min_length: 50
  max_length: 100

# AFTER (global):
description:
  min_length: 60      # ← Tighter
  max_length: 90      # ← Tighter
```

**Test all phases:**
```bash
./hooks.sh set-context phase_4 && ./hooks.sh skills
./hooks.sh set-context phase_5_enrichment && ./hooks.sh skills
./hooks.sh set-context phase_6_bootstrap && ./hooks.sh skills
```

**Update needed:** 
- [ ] Update DECISIONS.md with rationale
- [ ] Update README.md if this changes fundamentally how system works
- [ ] Commit with clear message: "tighten: increase description min_length to 60"

---

## When to Escalate (Don't Fix Alone)

**STOP and ask for help if:**

- [ ] You need to modify `engine/` directory
- [ ] Validation results are completely different after your change
- [ ] Git history shows your change introduced regressions
- [ ] You're unsure whether change breaks backward compatibility
- [ ] CLAUDE.md::What NOT to Change prevents what you need to do
- [ ] Change requires coordinating with other teams
- [ ] You're tempted to modify hook script logic itself
- [ ] Performance degrades noticeably (> 10% slower)

**How to escalate:**
1. Document what you were trying to do
2. Explain why it's blocked
3. Share the CLAUDE.md section that's preventing you
4. Ask: "How should I handle this?"

---

## Rollback Procedure (If Something Breaks)

**If your changes broke validation, here's how to revert:**

```bash
# See what you changed
git status

# See the diff
git diff config/hooks-config.yaml

# Option 1: Revert specific file
git restore config/hooks-config.yaml

# Option 2: Revert entire commit
git revert <commit-hash>

# Verify it works
./hooks.sh skills
```

**After rollback:**
- [ ] Verify `./hooks.sh skills` passes again
- [ ] Document what went wrong
- [ ] Plan better approach
- [ ] Try again (or escalate)

---

## Common Mistakes to Avoid

| Mistake | Why Bad | How to Avoid |
|---------|--------|---|
| Editing engine files | Breaks core logic | Read CLAUDE.md::What NOT to Change |
| Hardcoding values in Python | Defeats purpose of dynamic system | All config goes in YAML |
| Not testing all 3 phases | Changes might break phase_4 or phase_6 | Always: `./hooks.sh set-context` + test each |
| Forgetting to update docs | Future you won't know why changed | Update README/QUICK_REF/CLAUDE when appropriate |
| Modifying multiple files at once | Hard to debug if broken | Change one file at a time, test after each |
| Testing only one skill | May miss edge cases | Test multiple skills if possible |
| Not verifying backward compatibility | Breaks existing workflows | Old steps must still work |
| Adding `# TODO` comments | Technical debt pules up | Either fix it now or escalate, not add comment |

---

## Success Criteria for Modifications

After your modification is complete, you should be able to say:

- [ ] ✅ I know exactly what I changed and why
- [ ] ✅ `./hooks.sh status` shows all systems healthy
- [ ] ✅ All phases (4, 5, 6) produce expected results
- [ ] ✅ Backward compatibility is preserved
- [ ] ✅ Related documentation is updated
- [ ] ✅ No hardcoded values introduced
- [ ] ✅ I can explain the change to someone else clearly
- [ ] ✅ Git commit message explains why (not just what)

If you can't check one of these boxes → Don't commit yet, investigate further

---

**Version:** 1.0  
**Status:** Ready to Use  
**Last Updated:** 2026-04-12
