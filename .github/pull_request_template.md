## Description

What does this PR do? Provide a clear summary of your changes.

### Type of Change

- [ ] 🆕 New Skill
- [ ] 🆕 New Workflow
- [ ] 🐛 Bug Fix
- [ ] 📚 Documentation Update
- [ ] ⚡ Performance Improvement
- [ ] 🔧 Configuration / Setup
- [ ] 🧪 Tests or Validation

## Related Issue(s)

Closes #[issue number]

## Changes Made

What specifically changed? List the key modifications:

- [ ] Added `skills/...`
- [ ] Added `workflows/...`
- [ ] Updated `docs/...`
- [ ] Other: _________________

## Validation Checklist

### Pre-Submission

- [ ] ✅ All validation gates pass (8-gate system)
  - [ ] YAML frontmatter is valid
  - [ ] Naming conventions followed (snake_case for skills, /kebab-case for workflows)
  - [ ] Description is clear and actionable
  - [ ] Risk level is appropriate and justified
  - [ ] Mandate is clear (2-3 sentences)
  - [ ] Response pattern is specific
  - [ ] Token efficiency verified (40-60% compression)
  - [ ] No conflicts with existing skills/workflows
- [ ] 🧪 Tested locally:
  ```bash
  python hooks/validate-skill.py skills/your-skill.md    # For skills
  python hooks/validate-workflow.py workflows/your-wf.yaml  # For workflows
  npm run measure-tokens
  npm run validate-compression
  ```
- [ ] 📝 Documentation is updated
- [ ] 💬 Commit message follows [Conventional Commits](https://www.conventionalcommits.org/)
- [ ] 🔄 No merge conflicts with main branch
- [ ] ✨ Code follows project style guide
- [ ] 🚫 No breaking changes (or breaking changes are justified)

## Testing

How have you tested this?

- [ ] Local validation passed
- [ ] Manual testing completed
- [ ] Used on a real Unity project (if applicable)

### Screenshots (if applicable)

Add any relevant screenshots or examples:

## Backwards Compatibility

- [ ] This change is backward compatible
- [ ] This is a breaking change (explain below)

If breaking:

```
What changes for existing users?
How can they migrate?
```

## Performance Impact

- [ ] No performance impact
- [ ] Improves performance (details below)
- [ ] May impact performance (details below)

## Additional Notes

Any additional context, considerations, or follow-up work?

---

**Thank you for contributing to .agents! 🎮✨**

### Reviewer Checklist

- [ ] Code quality is acceptable
- [ ] Fits .agents philosophy and scope
- [ ] Documentation is complete
- [ ] All CI checks pass
- [ ] Validated against 8-gate system
- [ ] Ready to merge