# .agents Quick Start Guide

Get your game developed with AI assistance in 5 minutes.

## 1. What is .agents?

The `.agents` project is a complete AI-powered workflow system for Unity game development. It provides:
- **47 workflows** (automated step-by-step guides)
- **22 specialized skills** (expert advisors for specific tasks)
- **Runtime C# library** (production-ready gameplay systems)
- **Documentation** (best practices, patterns, troubleshooting)

## 2. How to Activate Workflows

All workflows are accessible via `/` prefix in chat:

```
/android-specific-setup
/build-size-optimization
/accessibility-audit-workflow
... etc
```

**Example:**
```
User: /build-size-optimization
Assistant: Analyzes your game's build and helps optimize it
```

## 3. How to Invoke Skills

Skills are triggered with `@` prefix. Use when you need expert advice:

```
@mobile-expert - iOS/Android optimization
@backend-specialist - Server architecture
@game-design-specialist - Game balance
@accessibility-expert - WCAG compliance
... etc
```

**Example:**
```
User: My iOS game crashes on iPhone 11 after 30 minutes.
Assistant: [@mobile-expert] Diagnoses: Likely memory leak. Profile with Memory Profiler, check event unsubscriptions...
```

## 4. Common First Workflows

**Just starting project?**
1. `/vibe-project-init` - Bootstrap project structure
2. `/collaboration-setup` - Set up team workflow

**Setting up for mobile?**
1. `/android-specific-setup` - Android configuration
2. `/ios-specific-setup` - iOS configuration
3. `@mobile-expert` - Optimization consultation

**Shipping soon?**
1. `/technical-debt-audit` - Clean up codebase
2. `/security-vulnerability-scan` - Find vulnerabilities
3. `/accessibility-audit-workflow` - Test accessibility
4. `/project-health-check` - Pre-launch verification

## 5. Workflow vs Skill Differences

| Aspect | Workflow | Skill |
|--------|----------|-------|
| **What** | Step-by-step guide | Expert consultation |
| **When** | Need specific instructions | Need strategic advice |
| **Example** | "Here are build steps" | "Root cause is X, fix by Y" |
| **Trigger** | `/filename` | `@skillname` |

## 6. File Organization

```
.agents/
├── workflows/          # 47 automated guides (.md files)
├── skills/             # 22 expert advisors (SKILL.md + resources/)
├── scripts/            # 50+ C# runtime systems
├── docs/               # Guides, references, troubleshooting
├── README.md           # Master index
├── mcp_config.json     # System configuration
└── ...
```

## 7. Getting Help

- `@simple-assistant` or generic problem → Asks which workflow/skill fits
- `/help` → Lists all workflows
- `/troubleshooting-guide` → Common issues database
- Discord/GitHub issues → Community support

## 8. Key Principles

✅ **Workflows are reproducible** - Run same workflow, get same result
✅ **Skills give context** - Apply expert knowledge to your specific problem
✅ **Everything is documented** - No black boxes, see the reasoning
✅ **Built for scale** - Works for 1-person team to 100+ person studio

## Next Steps

1. Read your specific platform docs (`/android-specific-setup` or `/ios-specific-setup`)
2. Join the community (Discord/GitHub) for questions
3. Check `/troubleshooting-guide` if you get stuck
4. Refer to skill documentation for deep dives

**Happy developing! 🚀**
