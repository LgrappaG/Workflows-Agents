# Workflows Documentation

Master collection of 63 workflows for .agents framework. Each workflow guides developers through complex game development tasks with step-by-step instructions, skill integration, and verification gates.

## Workflow Overview

**Total Workflows:** 63
**Organization:** 12 categories
**Skill Integration:** Each workflow references 5-15 skills
**Validation:** 4-7 verification steps per workflow

## Workflow Categories

### 1. Core Development Workflows (6 workflows)

Essential setup and initialization workflows for new projects.

| Workflow | Purpose | Platforms | Estimated Time |
|----------|---------|-----------|-----------------|
| vibe-project-init | Initialize new .agents project | All | 15 min |
| unity-2d-setup | 2D game project template | PC, Mobile | 20 min |
| unity-3d-setup | 3D game project template | PC, VR/XR | 25 min |
| unity-xr-ar-setup | VR/XR-specific setup | VR/XR, Mobile | 30 min |
| vibe-vr-scaffold | VR gameplay skeleton | VR/XR | 25 min |
| unity-brainstorm-feature | Feature design & planning | All | 60 min |

**Use When:**
- Starting new project
- Setting up for specific platform (mobile, VR, console)
- Planning new feature from scratch

**Key Skills Integrated:**
- csharp-dependency-injection
- unity-architecture-patterns
- project-structure-best-practices

---

### 2. Code Quality Workflows (7 workflows)

Maintain code quality, documentation, and architectural integrity.

| Workflow | Purpose | Complexity | Tools |
|----------|---------|-----------|-------|
| code-review-swarm | Multi-specialist code review | High | Claude + specialists |
| csharp-format-project | Code formatting & style | Medium | Roslyn + analyzers |
| unity-docs-generator | Auto-generate API docs | Low | Reflection + markdown |
| unity-so-architecture | ScriptableObject design | Medium | Architecture patterns |
| unity-record-adr | Architecture Decision Records | Low | Documentation |
| skill-audit | Validate skill quality | High | 8-gate validation |
| technical-debt-audit | Identify tech debt | High | Analysis + reporting |

**Use When:**
- Preparing for code review
- Standardizing code style across project
- Maintaining architecture decisions
- Auditing project health

---

### 3. Testing & QA Workflows (5 workflows)

Test planning, TDD setup, UI testing, and QA coordination.

| Workflow | Purpose | Test Type | Coverage |
|----------|---------|-----------|----------|
| vibe-vr-tdd-setup | VR-specific TDD initialization | Unit/Integration | 40-60% |
| ui-testing-framework | UI automation setup | UI/Integration | Buttons, text, layout |
| load-testing-setup | Performance load testing | Performance | Scalability limits |
| qa-plan | QA strategy & test planning | All | Black-box + regression |
| i18n-testing-workflow | Localization testing | String/Layout | Multi-lang validation |

**Use When:**
- Starting new project test suite
- Setting up continuous integration testing
- Preparing for release QA
- Testing platform-specific features (UI, localization)

---

### 4. Performance Workflows (8 workflows)

Profiling, optimization, and performance monitoring.

| Workflow | Focus | Platforms | Expected Improvement |
|----------|-------|-----------|----------------------|
| unity-performance-audit | Comprehensive baseline | All | Baseline + roadmap |
| unity-profile-audit | Runtime profiling | PC/Console | 15-30% typical |
| unity-asset-audit | Asset usage analysis | All | 20-40% size reduction |
| build-size-optimization | Binary size reduction | PC/Mobile | 30-50% smaller |
| shader-optimization-guide | Shader performance | All | 2-5x GPU speedup |
| memory-profiler-advanced | Deep memory analysis | All | 10-20% savings |
| assets-bundle-strategy | AssetBundle planning | Mobile/WebGL | Better streaming |
| mobile-optimization-audit | Mobile-specific tuning | Mobile | 40-60% improvement |

**Use When:**
- Project feels slow/sluggish
- Target platform has tight performance budget
- Pre-launch optimization required
- Memory or storage limited

**Typical Results:**
- FPS improvement: +10-30%
- Build size: -30-50%
- Memory: -15-25%
- Load time: -20-40%

---

### 5. Build & Deployment Workflows (5 workflows)

Platform-specific build configuration and optimization.

| Workflow | Target Platform | Build Time | Output |
|----------|-----------------|-----------|--------|
| unity-build-quest | Meta Quest VR | 3-5 min | APK |
| android-specific-setup | Android mobile | 2-3 min | APK |
| ios-specific-setup | iOS mobile | 4-6 min | IPA |
| webgl-build-setup | Web (WebGL) | 1-2 min | WASM |
| console-build-setup | PS5/Xbox | 5-10 min | Proprietary format |

**Use When:**
- porting to new platform
- Setting up CI/CD pipeline
- Debugging platform-specific issues
- Preparing store submission

---

### 6. Debugging & Recovery Workflows (5 workflows)

Troubleshooting, debugging, and project health recovery.

| Workflow | Problem Solved | Complexity | Recovery Time |
|----------|---|---|---|
| unity-smart-debug | Active debugging | Low | 5-15 min |
| unity-mcp-check | MCPForUnity validation | Low | 2-5 min |
| unity-clean-project | Project cleanup | Medium | 10-30 min |
| error-recovery | Critical error resolution | High | 30-60 min |
| project-health-check | Overall project audit | High | 45-90 min |

**Use When:**
- Debugging gameplay issues
- Getting "Unknown Error" messages
- Project feels corrupt/slow
- After major refactoring
- Pre-release health check

---

### 7. Git & CI/CD Workflows (7 workflows)

Version control, automation, and continuous deployment.

| Workflow | Purpose | Automation | Frequency |
|----------|---------|-----------|-----------|
| vibe-git-push | Safe push to remote | Manual | Per commit |
| vibe-git-sync | Branch synchronization | Manual | On demand |
| github-actions-unity-setup | CI/CD automation | Automatic | Per push |
| changelog-generator | Auto-generate changelog | Automatic | Per release |
| devops-audit | CI/CD health check | Monthly | Scheduled |

**Use When:**
- Setting up GitHub Actions CI/CD
- Need to sync branches locally
- Generating release notes
- Auditing automation pipelines

---

### 8. Multiplayer & Backend Workflows (2 workflows)

Network architecture and backend integration.

| Workflow | Architecture | Protocol | Latency |
|----------|---|---|---|
| multiplayer-setup | Networking foundation | TCP/UDP | <100ms target |
| backend-setup | Server integration | HTTP/WebSocket | <200ms target |

**Use When:**
- Adding multiplayer features
- Connecting to backend services
- Setting up player synchronization
- Configuring real-time communications

---

### 9. Localization & Analytics Workflows (2 workflows)

Internationalization and user analytics.

| Workflow | Purpose | Scope | Languages |
|----------|---------|-------|-----------|
| localization-setup | Multi-language support | UI + content | 10+ languages |
| analytics-integration | User metrics tracking | Engagement + economy | Real-time |

**Use When:**
- Launching in multiple regions
- Tracking player engagement
- A/B testing features
- Monetization optimization

---

### 10. Accessibility & Compliance Workflows (4 workflows)

Accessibility, compliance, and regulatory requirements.

| Workflow | Standard | Coverage | Audit |
|----------|----------|----------|-------|
| accessibility-audit | WCAG 2.1 Level AA | Full game | 4-6 hz |
| accessibility-audit-workflow | Continuous accessibility | Sprint-based | Per build |
| vr-accessibility | VR-specific accessibility | Motion + mobility | Custom |
| gdpr-compliance-setup | Privacy regulations | EU data handling | Legal review |

**Use When:**
- Targeting accessibility standards
- Launching in EU (GDPR)
- VR accessibility required
- Government/enterprise client requirements

---

### 11. Security Workflows (2 workflows)

Security auditing and vulnerability scanning.

| Workflow | Scope | Threats | Remediation |
|----------|-------|---------|-----------|
| security-audit | Code + architecture | OWASP Top 10 | Prioritized |
| security-vulnerability-scan | Dependency scanning | Known CVEs | Automated patches |

**Use When:**
- Pre-launch security review
- Enterprise client requirements
- Major dependency updates
- Post-incident security hardening

---

### 12. Skill & Workflow Management Workflows (9 workflows)

Meta-workflows for managing the .agents framework itself.

| Workflow | Purpose | Input | Output |
|----------|---------|-------|--------|
| create-skill | Create new skill | Specification | SKILL.md + git commit |
| create-workflow | Create new workflow | Requirements | Workflow.md + git commit |
| build-dev-cli | Development CLI tools | Project config | Executable CLI |
| skill-pipeline | Mass skill operations | Batch spec | Updated skills |
| project-onboarding | New team member setup | User info | Project + guide |
| dependency-health-check | Dependency audit | Project | Health report |
| unity-ui-scaffold | UI template generation | Design | UI prefabs |
| unity-smart-placement-setup | GameObject positioning | Scene | Placed objects |
| vibe-router | Workflow dispatcher | Selection | Guided workflow |

**Use When:**
- Adding new skills/workflows to framework
- Onboarding team members
- Managing large skill batches
- Maintaining framework health

---

## How to Use Workflows

### Step 1: Select Workflow

Choose from 63 workflows matching your needs:

```bash
# List all workflows
ls .agents/workflows/*.md

# Search for workflow
grep -l "keyword" .agents/workflows/*.md
```

### Step 2: Read Workflow

Each workflow contains:
- **Purpose:** What the workflow accomplishes
- **Prerequisites:** Required skills/tools
- **Steps:** 4-7 sequential steps
- **Verification:** Checkpoints to validate progress
- **Integration:** Skills to reference

### Step 3: Execute Workflow

Follow 4-7 steps sequentially:

```
Step 1: [Action] - Expected result
Step 2: [Action] - Expected result
...
Step 7: [Verification] - Success criteria
```

### Step 4: Verify Completion

Check that:
- ✅ All verification gates passed
- ✅ No errors or warnings
- ✅ Output matches expectations
- ✅ Changes committed to git

---

## Workflow Integration with Skills

Each workflow integrates 5-15 skills from the .agents skill library:

**Example:**
`vibe-vr-scaffold` workflow uses:
- unity-3d-expert (skill)
- vr-xr-specialist (skill)
- csharp-dependency-injection (skill)
- unity-architecture-patterns (skill)
- + 5-10 more skills

**To reference a skill in a workflow:**
1. Check skill exists: `ls .agents/skills/{skill-name}/SKILL.md`
2. Link in workflow markdown: `See [skill-name](./skills/{skill-name}/SKILL.md)`
3. Follow skill's response patterns during workflow execution

---

## Common Workflow Combinations

### Setup Phase (Day 1)
1. vibe-project-init
2. unity-3d-setup (or platform-specific)
3. csharp-format-project
4. project-onboarding (if team project)

### Development Phase (Ongoing)
- Use workflows per sprint/feature
- Typical: 2-3 workflows per sprint
- Run health checks every 2 weeks

### Pre-Launch Phase (Week -4)
1. project-health-check
2. security-audit
3. performance-audit (mobile: mobile-optimization-audit)
4. qa-plan
5. accessibility-audit
6. gdpr-compliance-setup (if EU launch)

### Release Phase (Week 0)
1. build-size-optimization
2. platform-specific builds (unity-build-quest, ios-specific-setup, etc.)
3. changelog-generator
4. devops-audit

---

## Workflow Requirements & Timing

| Workflow | Time | Team | Tools | Difficulty |
|----------|------|------|-------|------------|
| vibe-project-init | 15 min | 1 | Git + Editor | Easy |
| security-audit | 4-6 hours | 2-3 | Analysis tools | Hard |
| code-review-swarm | 2-4 hours | 3-5 | Peer review | Hard |
| performance-audit | 3-4 hours | 1-2 | Profiler | Medium |
| qa-plan | 2-3 hours | 1-2 | Documentation | Medium |
| project-health-check | 2-3 hours | 1 | Analysis tools | Medium |

---

## Workflow Status Tracking

Track workflow usage in git commits:

```
feat(workflows): execute vibe-vr-scaffold

- Platform: Meta Quest 3
- Time: 25 minutes
- Verification: All steps passed (7/7)
- Next: Implement gameplay mechanics

Co-Authored-By: Team <email>
```

---

## Common Issues & Solutions

**Issue:** Workflow has unmet prerequisites
**Solution:** Run prerequisite workflow first (see workflow docs)

**Issue:** Verification step fails
**Solution:** Review step output, check skill instructions, rerun step

**Issue:** Workflow steps take longer than expected
**Solution:** Parallel work possible in some workflows; review "Optional" sections

**Issue:** Team disagreement on workflow approach
**Solution:** See workflow "Alternatives" section, or escalate in architecture review

---

## Framework Statistics

- **Total Workflows:** 63
- **Average Steps:** 5.5 per workflow
- **Total Steps:** 346+
- **Skill References:** 310+ integration points
- **Platform Coverage:** 6+ platforms (PC, Mobile, VR/XR, Console, WebGL)
- **Average Time per Workflow:** 45 minutes
- **Validation Coverage:** 100% (all workflows have verification gates)

---

## Next Steps

1. **Choose Workflow:** Select from 63 based on your task
2. **Read Prerequisites:** Ensure you have required skills/tools
3. **Execute Steps:** Follow 4-7 sequential steps
4. **Verify:** Check all gates passed
5. **Commit:** Git commit with workflow reference
6. **Repeat:** Use additional workflows as needed

**For Framework Maintenance:**
- See `create-workflow` workflow to add new workflows
- See `skill-pipeline` for bulk skill operations
- See `dependency-health-check` for framework audits

