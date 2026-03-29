# Contributing to .agents

Thank you for your interest in contributing to .agents! This framework powers game developers worldwide with 512 AI-powered skills and 63 production-ready workflows. Your contributions matter.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Contributing Skills](#contributing-skills)
- [Contributing Workflows](#contributing-workflows)
- [Pull Request Process](#pull-request-process)
- [Quality Standards](#quality-standards)

## Code of Conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing. We expect all contributors to uphold these standards.

## Getting Started

### Prerequisites

- Git and basic command line familiarity
- Python 3.8+ (for validation scripts)
- Text editor (VS Code, Sublime, etc.)
- Familiarity with YAML and Markdown

### Setup

```bash
# 1. Fork the repository
# Visit: https://github.com/LgrappaG/Workflows-Agents
# Click "Fork" in the top right

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/Workflows-Agents.git
cd Workflows-Agents/.agents

# 3. Add upstream remote
git remote add upstream https://github.com/LgrappaG/Workflows-Agents.git

# 4. Create a feature branch
git checkout -b feature/your-feature-name
```

## How to Contribute

### 1. **Reporting Bugs** 🐛

Before opening an issue, check if it's already reported:

```bash
# Search existing issues
gh issue list --search "your keywords" --state all
```

If not, open a new issue using the [Bug Report](/.github/ISSUE_TEMPLATE/bug_report.md) template:

- **Title**: `[BUG] Clear, concise description`
- **Description**: What went wrong?
- **Steps to Reproduce**: How to trigger the bug?
- **Expected Behavior**: What should happen?
- **Actual Behavior**: What actually happens?
- **Environment**: OS, Python version, project version, etc.

### 2. **Requesting Features** ✨

Great ideas drive the framework forward! Use the [Feature Request](/.github/ISSUE_TEMPLATE/feature_request.md) template:

- **Title**: `[FEATURE] Clear description`
- **Use Case**: Why is this needed? What problem does it solve?
- **Proposed Solution**: How might this work?
- **Alternatives**: Other approaches considered?

### 3. **Contributing Code** 💻

#### For Skills

Each skill is a YAML file in `skills/` with these key sections:

```yaml
---
name: "Unique Skill Name"
category: "Core Development"
summary: "One-line summary"
mandate: "What this skill does (2-3 sentences)"
risk_level: "low"  # low, medium, high, critical
---

## Description
Detailed explanation of what the skill does and when to use it.

## Key Capabilities
- Point 1
- Point 2
- Point 3

## Example Interaction
How a user might invoke and use this skill.

# Response Pattern
Expected format and structure of responses.
```

**Before submitting a skill:**

1. Run validation:
   ```bash
   python hooks/validate-skill.py skills/YOUR_SKILL.md
   ```

2. Check 8-gate validation passes:
   - ✅ YAML Frontmatter valid
   - ✅ Skill naming convention (snake_case)
   - ✅ Description quality (clear, actionable)
   - ✅ Risk level justified
   - ✅ Mandate clarity
   - ✅ Response pattern is actionable
   - ✅ Token efficiency (40-60% compression)
   - ✅ No conflicts with existing skills

3. Ensure it fits a category:
   - Materials System, UI Toolkit, Terrain System
   - Navigation, Cinemachine, Timeline & Cutscenes
   - Audio System, Physics, Networking & Multiplayer
   - Animation System, Graphics & VFX, Debugging & Tools
   - Scripting & Advanced C#, ML/Advanced Systems
   - Multi-Engine Support, Custom Tools & Extensions

#### For Workflows

Workflows are complex sequences that solve real problems. Create in `workflows/` as YAML:

```yaml
---
name: "/workflow-name"
description: "What problem this solves"
phases: 3
estimated_tokens: 2000
---

## Purpose
Why would someone use this workflow?

## Prerequisites
What must be done first?

## Phase 1: Initialize
Steps to set up...

## Phase 2: Build
Steps to implement...

## Phase 3: Validate
Steps to verify...

## Success Criteria
- [ ] Criteria 1
- [ ] Criteria 2
```

**Before submitting a workflow:**

```bash
python hooks/validate-workflow.py workflows/YOUR_WORKFLOW.yaml
```

### 4. **Improving Documentation** 📚

Documentation improvements are always welcome:

- Fix typos or clarity issues
- Add examples or clarifications
- Translate key docs to other languages
- Improve code comments

Simply edit and submit a PR!

## Pull Request Process

### Before You Submit

```bash
# 1. Sync with latest upstream
git fetch upstream
git rebase upstream/main

# 2. Run all validation hooks
python hooks/validate-skill.py skills/*.md    # If adding skills
python hooks/validate-workflow.py workflows/*  # If adding workflows
python hooks/pre-commit-message.py             # Validate commit message

# 3. Test locally
npm run measure-tokens          # Check token efficiency
npm run validate-compression    # Verify compression
```

### Submitting Your PR

```bash
# 1. Commit with conventional format
git add .
git commit -m "feat: add feature-name

More detailed explanation if needed.

Fixes #123 (if closing an issue)"

# 2. Push to your fork
git push origin feature/your-feature-name

# 3. Create PR on GitHub
# GitHub will show a "Compare & pull request" button
```

### PR Template

Your PR should follow the [template](/.github/pull_request_template.md):

```markdown
## Description
What does this PR do?

## Type
- [ ] New Skill
- [ ] New Workflow
- [ ] Bug Fix
- [ ] Documentation
- [ ] Performance Improvement

## Related Issues
Closes #123

## Checklist
- [ ] All validation gates pass (8-gate system)
- [ ] Tests pass (if applicable)
- [ ] Documentation updated
- [ ] Commit message follows conventional format
- [ ] No merge conflicts
```

### Review Process

1. **Automated Checks** (15 minutes)
   - YAML frontmatter validation
   - Naming conventions
   - Risk levels justified
   - Token limits

2. **Maintainer Review** (24-48 hours)
   - Code quality
   - Fit with .agents philosophy
   - Documentation completeness
   - Backwards compatibility

3. **Community Review** (optional)
   - Other developers may provide feedback
   - Engage constructively

4. **Merge** ✅
   - Once approved, maintainer merges
   - Your contribution is live!

## Quality Standards

### Skill Quality Checklist

- **Clarity**: Anyone can understand the skill's purpose within 30 seconds
- **Actionability**: Response patterns include concrete, executable steps
- **Safety**: No XSS, SQL injection, or other OWASP Top 10 vulnerabilities
- **Consistency**: Follows naming conventions and structure
- **Token Efficiency**: 40-60% compression vs. verbose alternatives
- **No Duplication**: Doesn't conflict with existing skills/workflows
- **Risk Assessment**: Risk level accurately reflects potential impact

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add authentication skill
fix: resolve validation gate timing issue
docs: update CONTRIBUTING guide
style: format Python scripts with Black
test: add validation tests
chore: bump version to 9.0.1
```

### Code Style

- **Python**: PEP 8 (use `black` and `flake8`)
- **YAML**: 2-space indents, clear structure
- **Markdown**: Consistent heading hierarchy, clear sections

## Questions?

- 💬 **Ask in Issues**: Create a discussion for big questions
- 📖 **Read Docs**: Check [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)
- 🤝 **Ask Maintainers**: Tag `@LgrappaG` in discussions

## Attribution

Your contributions will be recognized:
- In [CHANGELOG.md](CHANGELOG.md) under your release
- In commit history with your GitHub handle
- In skills/workflows you create (with your name in comments if requested)

---

## Additional Resources

- [Quick Start Guide](docs/QUICK_START.md)
- [Framework Complete Overview](FRAMEWORK_COMPLETE.md)
- [Integration Guide](INTEGRATION_GUIDE.md)
- [Validation Hooks Documentation](VALIDATION_HOOKS.md)
- [Agent Hierarchy](AGENT_HIERARCHY.md)

**Thank you for contributing! Together we're building the future of AI-powered game development. 🎮✨**