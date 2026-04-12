# Session Memory Template - Dynamic Hooks System

**Use this template if modifying the hooks system. Copy to memory after session completion.**

---

## Session Header

**Session Date:** [YYYY-MM-DD]  
**Model Used:** [claude-opus-4-6 / claude-sonnet-4-6 / etc]  
**AI Session ID:** [Store for reference]  
**Task Category:** [Configuration / Plugin Development / Documentation / Bug Fix / Refactoring]

---

## Work Completed This Session

### Objectives
- [ ] Objective 1: [Describe what you were trying to achieve]
- [ ] Objective 2: [Describe what you were trying to achieve]
- [ ] Objective 3: [Describe what you were trying to achieve]

### Files Modified
```
config/hooks-config.yaml          - [What changed and why]
config/hooks-context.yaml          - [What changed and why]
engine/plugin_manager.py           - [What changed and why]
[other files as applicable]
```

### Tests Run and Results
```
./hooks.sh status                 - ✅ PASS / ❌ FAIL [Why?]
./hooks.sh set-context phase_4    - ✅ PASS / ❌ FAIL [Why?]
./hooks.sh set-context phase_5    - ✅ PASS / ❌ FAIL [Why?]
./hooks.sh skill <path>           - ✅ PASS / ❌ FAIL [Why?]
./hooks.sh skills                 - ✅ PASS / ❌ FAIL [Why?]
```

---

## Key Insights Discovered

### Non-Obvious Discovery #1
[What did you learn that wasn't obvious from reading the code?]
- **Where:** Which file/line
- **Why it matters:** How does this affect future work
- **Share with:** Future AI sessions, team

### Non-Obvious Discovery #2
[Another insight]

### Edge Cases Found
- Edge case A and how to handle it
- Edge case B and how to handle it

---

## Configuration Changes Made

### Change #1: [Description]
```yaml
# File: config/hooks-config.yaml
# Before:
old_value: 50

# After:
old_value: 100

# Rationale: [Why make this change]
```

### Change #2: [Description]
[Similar format]

---

## Plugin Development (If Applicable)

### Plugin Created/Modified
```
Plugin Name: [Name]
File: plugins/[plugin_name].py
Status: Working / Needs Debugging / Deferred

Behavior:
  Input: [What plugin validates]
  Logic: [How it validates]
  Output: [What result it produces]

Tested with:
  - Phase 4: [Result]
  - Phase 5: [Result]
  - Phase 6: [Result]
```

---

## Issues Encountered and Solutions

### Issue #1: [Problem Description]
- **Error:** [Exact error message or behavior]
- **Root cause:** [Why it happened]
- **Solution:** [How you fixed it]
- **Prevention:** [How to avoid next time]
- **Time spent:** 15 min

### Issue #2: [Another issue]
[Similar format]

---

## Performance Observations

| Metric | Before | After | Impact |
|--------|--------|-------|--------|
| Validation time (single skill) | 2.3s | [new value] | [+/- and why] |
| Validation time (all skills) | 15s | [new value] | [+/- and why] |
| Config load time | 150ms | [new value] | [+/- and why] |
| Memory usage | 45MB | [new value] | [+/- and why] |

---

## Documentation Updates

- [ ] Updated QUICK_REFERENCE.md (if commands changed)
- [ ] Updated README.md (if architecture changed)
- [ ] Updated CLAUDE.md (if decision changed)
- [ ] Updated SETUP.md (if installation changed)
- [ ] Updated DECISIONS.md (if architectural decision)
- [ ] Updated INDEX.md (if structure changed)
- [ ] Created/updated examples (if applicable)

**Files NOT updated:** [Why?]

---

## Validation Against Checklist

Used MODIFICATION_CHECKLIST.md? [YES / NO]

Pre-Modification Interview:
- [x] What am I changing? [Answer from checklist]
- [x] Does CLAUDE.md allow this? [Answer]
- [x] Affects which phase? [Answer]
- [x] CI/CD updates needed? [Answer]

During Modification:
- [x] Verified files exist with `./hooks.sh status`
- [x] Tested in isolation
- [x] Tested all 3 phases
- [x] Ran comprehensive tests

Post-Modification:
- [x] Documentation updated
- [x] Backward compatibility verified
- [x] No hardcoded values introduced
- [x] Can explain changes clearly

---

## Recommendations for Next Session

### Should Do
- [ ] [Action] because [reason]
- [ ] [Action] because [reason]
- [ ] [Action] because [reason]

### Improvements Identified
- [ ] [Improvement] - Priority: High / Medium / Low
- [ ] [Improvement] - Priority: High / Medium / Low

### Tests That Should Be Added
- [ ] Test for [scenario]
- [ ] Test for [scenario]

### Documentation That Needs Updating
- [ ] [Section] in [file] is outdated
- [ ] [New section] should be added

### Discussion Topics for Team
- [ ] [Topic] - pros/cons of this decision
- [ ] [Topic] - needs team consensus

---

## Implementation Notes

### Technical Details (Not Obvious from Code)
- [Detail 1]: [Explanation]
- [Detail 2]: [Explanation]
- [Gotcha 1]: [How to avoid it]
- [Gotcha 2]: [How to avoid it]

### Why Certain Decisions Were Made
- [Decision A]: Chose X over Y because [reasoning]
- [Decision B]: Chose X over Y because [reasoning]

### Non-Standard Patterns Used
- [Pattern 1]: Why this pattern was needed
- [Pattern 2]: Why this pattern was needed

---

## Session Metrics

| Metric | Value |
|--------|-------|
| Files modified | [N] |
| Files created | [N] |
| Lines added | [N] |
| Lines removed | [N] |
| Commands run | [N] |
| Tests passed | [N] of [M] |
| Time spent | [Nmin] |
| Complexity level | Simple / Moderate / Complex / Difficult |

---

## Lessons Learned

### What Went Well
- [Approach that worked well]
- [Good decision made]
- [Efficient process]

### What Was Challenging
- [Difficultpart]
- [Confusing section]
- [Time-consuming task]

### What To Improve Next Time
- [Process improvement]
- [Tool improvement]
- [Understanding improvement]

---

## Files to Review Later

```
Mark files that should be reviewed by human/other AI session:
- [ ] config/hooks-config.yaml (line 45-67) - Needs review for correctness
- [ ] engine/learning_engine.py (line 120) - Performance concern
- [ ] [File] (line range) - [Why]
```

---

## Compatibility Check

- [x] Old hook scripts still work
- [x] Old HOOKS_CONTEXT values still work
- [x] Existing CI/CD unaffected
- [x] Git hooks continue working
- [x] No breaking changes to API
- [x] Team can use without migration

**Compatibility note:** [Any breaking changes? How to migrate?]

---

## When to Re-Read This Memory

**Read this memory if:**
- You're continuing work on this system
- Someone asks "What changed in the last session?"
- You're investigating why something works a certain way
- You need to understand the current system state
- You're debugging an issue related to your changes

**Update this memory if:**
- Session results are overturned (e.g., "that approach didn't work")
- New insights emerge about this work
- Follow-up session makes related changes

---

## Related Sessions

**Previous sessions (if any):**
- Session [date] - [brief description of work]
- Session [date] - [brief description of work]

**Follow-up sessions (if any):**
- Session [date] - [brief description of work]
- Session [date] - [brief description of work]

---

## Quick Reference for Next Session

**If you're picking up this work:**

1. **Understanding context:** Read CLAUDE.md (5 min)
2. **Verify system health:** Run `./hooks.sh status` (30 sec)
3. **See what changed:** Check this memory (2-3 min)
4. **Review files modified:** Read files listed above (varies)
5. **Test the changes:** Run `./hooks.sh skills` (2-3 min)
6. **Continue work:** Pick up from "Recommendations" section

**If you're working on something else:**
- This session modified: [List key files]
- May affect your work in: [List related areas]
- No action needed unless: [Conditions]

---

**Memory Status:** Complete & Ready  
**Last Updated:** [Session end date/time]  
**Next Review:** [Recommended date]
