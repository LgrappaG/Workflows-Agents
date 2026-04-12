# Setup Guide - Dynamic Hooks System

**Quick Setup Time:** 2 minutes  
**Full Setup Time:** 5 minutes

---

## Option 1: Minimal Setup (2 minutes)

Just use hooks as-is:

```bash
cd .agents/hooks

# You're ready! Start using:
./hooks.sh help
./hooks.sh status
./hooks.sh skills
```

**Result:** Hooks work with built-in configuration ✅

---

## Option 2: Optimized Setup (5 minutes)

Configure for your workflow:

### Step 1: Create .env.local file
```bash
cd .agents/hooks
cp .env.example .env.local
```

### Step 2: Edit .env.local for your workflow

**For Local Development:**
```bash
# In .env.local
HOOKS_CONTEXT=phase_5_enrichment
HOOKS_MODE=lenient
DEBUG=1
```

**For Production/CI:**
```bash
# In .env.local
HOOKS_CONTEXT=phase_4
HOOKS_MODE=strict
DEBUG=0
```

### Step 3: Make hooks.sh executable
```bash
chmod +x .agents/hooks/hooks.sh
```

### Step 4: (Optional) Add to PATH for easier access
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$PATH:$HOME/<project>/.agents/hooks"

# Now you can run from anywhere:
hooks.sh skill <path>
```

### Step 5: (Optional) Setup Git hooks
```bash
# Create .git/hooks/commit-msg
mkdir -p .git/hooks

cat > .git/hooks/commit-msg << 'EOF'
#!/bin/bash
./.agents/hooks/hooks.sh message "$1"
exit $?
EOF

chmod +x .git/hooks/commit-msg
```

**Result:** Complete workflow setup ✅

---

## Quick Configuration Options

### Most Common Setups

#### Setup A: Developer (Flexible)
```bash
# .env.local
HOOKS_CONTEXT=phase_5_enrichment
DEBUG=1
```

#### Setup B: Production (Strict)
```bash
# .env.local
HOOKS_CONTEXT=phase_4
DEBUG=0
```

#### Setup C: Bootstrap/New Skills (Relaxed)
```bash
# .env.local
HOOKS_CONTEXT=phase_6_bootstrap
DEBUG=1
```

---

## Verifying Setup

```bash
# Check everything is working
./hooks.sh status

# Expected output:
# ✓ pre-commit-message.py
# ✓ pre-commit-skills.py
# ✓ validate-skill.py
# ✓ pre-commit-workflows.py
# ✓ DynamicHooksEngine
# ✓ hooks-config.yaml
# ✓ hooks-context.yaml
# ✓ hooks-plugins.yaml
```

---

## Project Structure After Setup

```
.agents/
├── hooks/
│   ├── hooks.sh                  ← Your main CLI tool
│   ├── .env.local                ← Your local config (created)
│   ├── .env.example              ← Reference template
│   ├── README.md                 ← Full documentation
│   ├── QUICK_REFERENCE.md        ← This quick guide
│   ├── pre-commit-*.py           ← Hook scripts
│   ├── validate-skill.py
│   ├── engine/                   ← Engine (read-only)
│   ├── config/                   ← Configs to customize
│   └── schemas/                  ← Reference schemas

.git/
└── hooks/
    └── commit-msg                ← Git hook (optional)
```

---

## Daily Usage

### For Local Development
```bash
# Make changes
vim .agents/skills/my-skill/SKILL.md

# Validate
.agents/hooks/hooks.sh skill .agents/skills/my-skill/SKILL.md

# Commit
git commit -m "feat: add my skill"  # Hooks run automatically
```

### For Validation
```bash
# Quick check all
.agents/hooks/hooks.sh skills

# Deep dive on one
.agents/hooks/hooks.sh skill <path>

# Debug issues
.agents/hooks/hooks.sh debug validate-skill
```

### For Configuration Changes
```bash
# Edit config
vim .agents/hooks/config/hooks-config.yaml

# Verify change
.agents/hooks/hooks.sh config

# Test with new settings
.agents/hooks/hooks.sh skill <path>
```

---

## Troubleshooting Setup

### Problem: "hooks.sh not found"
**Solution:** 
```bash
# Make it executable
chmod +x .agents/hooks/hooks.sh

# Or use python directly
cd .agents/hooks
python3 pre-commit-skills.py
```

### Problem: "Permission denied" on .git/hooks
**Solution:**
```bash
chmod +x .git/hooks/commit-msg
```

### Problem: Environment variables not loading
**Solution:**
```bash
# Source the .env.local before running
source .env.local
.agents/hooks/hooks.sh status
```

### Problem: "Python not found"
**Solution:** Use python3 explicitly or check PATH

---

## Next Steps

1. ✅ Run `./hooks.sh help` to see all commands
2. ✅ Read `QUICK_REFERENCE.md` for common tasks
3. ✅ Read `README.md` for detailed documentation
4. ✅ Edit `.env.local` for your preferences
5. ✅ Set up Git hooks if desired

---

## Support Resources

| Need | Resource |
|------|----------|
| Quick commands | `./hooks.sh help` |
| Common tasks | `QUICK_REFERENCE.md` |
| Detailed docs | `README.md` |
| Configuration | `.env.example` |
| Current settings | `./hooks.sh context` |
| System status | `./hooks.sh status` |

---

**Setup Complete!** 🎉

Your Dynamic Hooks System is ready to use.

Start with: `./hooks.sh help`
