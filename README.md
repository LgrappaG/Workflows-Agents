# Workflows Agents — Unity Multi-Platform Toolkit v10

A comprehensive AI automation framework for **Unity game development across all platforms** (VR/XR, Mobile, PC, WebGL, Console), featuring **63 workflows + 585 AI-powered specialist skills** organized in **18 categories**, backed by a **48-agent organizational hierarchy** and **8-gate validation system** for rapid development and production-ready systems.

**NEW in v10.0.0:** 🎯 **End-to-End Orchestration System** - 4,446+ LOC autonomous multi-agent orchestration with intelligent error recovery, consensus voting, and production monitoring. 29/29 tests passing (100%). See [CHANGELOG.md](CHANGELOG.md) for details.

**NEW in v9.0.3:** 🎉 **Skills Enrichment Release** - 585 total skills with domain-specific YAML enrichment across 40 core skills. Measurable mandates, concrete response patterns, real usage contexts.

**Previous:** v8.2.0 - Skills Expansion (450 skills), v8.1.0 (300 skills), v8.0.0 (150 skills).

Inspired by and compatible with [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills).

**Quick Navigation:**
- 🤖 [Orchestration System](#-end-to-end-orchestration-system) - Multi-agent autonomous execution
- 📖 [Quick Start Guide](docs/QUICK_START.md) - 5 minute onboarding
- ⚡ [Token Optimization](docs/TOKEN_OPTIMIZATION.md) - 30-50% context savings
- 🐛 [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues & fixes
- 📚 [Full Documentation Index](docs/DOCUMENTATION_INDEX.md) - All references
- 📊 [Version Manifest](VERSION_MANIFEST.json) - Complete inventory
- 🔗 [CHANGELOG.md](CHANGELOG.md) - Full version history

---

## 🤖 End-to-End Orchestration System

**Status: ✅ Production Ready**

Complete multi-agent orchestration system enabling autonomous goal execution with intelligent error recovery and multi-agent consensus.

### System Overview

```
INPUT:  High-level goal (e.g., "deploy-game-release")
  ↓
ORCHESTRATE: Auto-decompose → Resolve dependencies → Route to agents
  ↓
EXECUTE: Deploy, Sync, Validate, Knowledge agents coordinate
  ↓
MONITOR: Error detection, pattern learning, strategy optimization
  ↓
RECOVER: Intelligent recovery with circuit breakers, exponential backoff
  ↓
OUTPUT: Execution report with metrics, errors, recovery details
```

### Key Components

| Component | Purpose | Tests |
|-----------|---------|-------|
| **Foundation** | Orchestrator, State Manager, Heartbeat | 4/4 ✅ |
| **Core Agents** | Deploy, Sync, Validation, Knowledge | 9/9 ✅ |
| **Intelligence** | Error Detection, Learning, Recovery, Routing | 11/11 ✅ |
| **Integration** | Multi-goal workflows, Cross-environment, E2E testing | 9/9 ✅ |
| **TOTAL** | 4,446 LOC with production monitoring | **29/29 ✅** |

### Quick Commands

```bash
# Initialize orchestration system
python orchestration/orchestration_main.py init

# Execute a goal (e.g., deploy game release)
python orchestration/orchestration_main.py deploy-game-release

# Check system status
python orchestration/orchestration_main.py status

# View available goals
python orchestration/orchestration_main.py goals

# Run end-to-end tests
pytest tests/test_phase4_e2e.py -v
```

### Supported Goals

**Deployment Pipeline**
- `deploy-game-release`: Full build → package → deploy → verify
- `deploy-hotfix`: Quick hotfix deployment
- `deployment-verification`: Verify successful deployment

**Quality Assurance**
- `validate-before-deploy`: 8-gate quality validation
- `validate-all-skills`: Quality check all skills
- `gate-approval-decision`: Final approval decision

**Version Control**
- `sync-with-remote`: Sync with git remote
- `resolve-git-conflicts`: Handle merge conflicts
- `sync-team-collaboration`: Multi-user sync

**Learning & Optimization**
- `learn-and-optimize`: Analyze metrics and suggest improvements
- `analyze-metrics`: Deep metric analysis
- `suggest-improvements`: Generate optimization recommendations

### Agents

1. **Deploy Agent** (250 LOC)
   - 4-stage pipeline: Build → Package → Deploy → Verify
   - Error recovery: retry_with_verbose, retry_with_backoff, rollback

2. **Sync Agent** (250 LOC)
   - Git operations with conflict resolution
   - Smart merge strategy (rebase vs merge)

3. **Validation Agent** (250 LOC)
   - 8-gate quality system with adaptive thresholds
   - Gates: Syntax, Naming, Description, Risk, Mandates, Response, Size, Consistency

4. **Knowledge Agent** (250 LOC)
   - Learning from execution history
   - Threshold adjustment recommendations
   - Optimization suggestions

### Intelligence Modules

1. **Error Detection Engine** (380 LOC)
   - Pattern recognition from error logs
   - Anomaly detection with statistical thresholds
   - Error chain identification

2. **Self-Correction Engine** (380 LOC)
   - Learning from successful recovery strategies
   - Confidence scoring for strategy selection
   - Adaptive planning and recommendations

3. **Recovery Manager** (500 LOC)
   - Circuit breaker pattern implementation
   - Exponential backoff with jitter
   - Multi-step rollback sequences

4. **Intelligence Router** (450 LOC)
   - Multi-agent consensus voting (4 strategies)
   - Conflict resolution by priority, confidence, or voting
   - Full audit trail of decisions

### Architecture

**Environment Awareness**
- Detects execution environment and adjusts behavior
- Adaptive thresholds for different contexts
- Optimized for strict and lenient validation modes

**Error Recovery Flow**
```
Error Detected
  ↓
ErrorDetectionEngine (Pattern analysis)
  ↓
SelfCorrectionEngine (Strategy learning)
  ↓
RecoveryManager (Retry logic with circuit breaker)
  ↓
IntelligenceRouter (Multi-agent consensus)
  ↓
Execution (Deploy recovery or escalate)
```

**Metrics Collection**
- Per-agent execution statistics
- Error pattern tracking
- Recovery strategy effectiveness
- Performance benchmarking

### File Structure

```
orchestration/
├── engine/
│   ├── central_orchestrator.py (main routing)
│   ├── state_manager.py (persistence)
│   ├── heartbeat_engine.py (monitoring)
│   └── goal_decomposer.py (sub-goal decomposition)
├── agents/
│   ├── base_agent.py (abstract contract)
│   ├── deploy_agent.py (deployment)
│   ├── sync_agent.py (version control)
│   ├── validation_agent.py (quality)
│   └── knowledge_agent.py (learning)
├── intelligence/
│   ├── error_detection_engine.py
│   ├── self_correction_engine.py
│   ├── recovery_manager.py
│   └── intelligence_router.py
├── config/
│   ├── orchestration-config.yaml
│   └── agent-mapping.yaml
├── error_handlers.py (shared error types)
└── orchestration_main.py (CLI)

tests/
├── test_foundation.py
├── test_agents.py
├── test_intelligence.py
└── test_e2e.py
```

### Production Features

✅ **Autonomous Execution**: Accept goals → Decompose → Execute
✅ **Error Recovery**: Detect → Learn → Recover autonomously
✅ **Consensus Voting**: Multi-agent consensus on decisions
✅ **State Persistence**: Checkpoint recovery from failures
✅ **Performance Metrics**: Comprehensive execution tracking
✅ **Adaptive Thresholds**: Adjusts for different environments

### Test Coverage

```
Foundation:     4/4  tests pass ✅
Core Agents:    9/9  tests pass ✅
Intelligence:  11/11 tests pass ✅
E2E:            9/9  tests pass ✅
─────────────────────────────────────
TOTAL:         29/29 tests pass ✅
```

---

## 🔒 Enterprise Hardening - Phase 1

**Status: ✅ Production Ready**

Security hardening layer protecting all agent execution with policy enforcement, resource isolation, safe file operations, and circuit breaker pattern. Transparent integration — no agent code changes required.

### Security Architecture

Three-layer defense-in-depth architecture:

```
LAYER 1: Policy Enforcement (CentralOrchestrator)
  └─ Question: "Is agent allowed to execute this goal?"
  └─ Decision: YES → Continue, NO → PermissionError
  └─ Audit: Log all policy decisions

LAYER 2: Resource Isolation (AgentSandbox)
  └─ CPU Limits: 25-100% configurable per tier
  └─ Memory Limits: 256MB-1024MB configurable per tier
  └─ Timeout: 60-600 seconds configurable per tier

LAYER 3: Safe Operations (StateManager)
  └─ File validation: Check path whitelist
  └─ Backup creation: Before every write
  └─ Atomic writes: Temp file + rename
  └─ Audit trail: Every operation logged
```

### Security Components

| Component | Purpose | Status |
|-----------|---------|--------|
| **SafeFileOperations** | File I/O with validation + audit trail | ✅ 340 LOC |
| **SafeProcessExecution** | Subprocess execution with shell injection prevention | ✅ 340 LOC |
| **CircuitBreaker** | Failure detection preventing cascading failures | ✅ 368 LOC |
| **PolicyEngine** | Access control enforcement (agent/operation/path) | ✅ 316 LOC |
| **AgentSandbox** | Resource limits (CPU, memory, timeout) | ✅ Configurable |

### Hard Boundaries (Cannot Bypass)

✅ **File System Protection**
- Cannot write to: `/etc`, `/sys`, `/proc`, `/root`, `~/.ssh`, `~/.kube`, `~/.aws`
- Can only write to: `.agents/skills`, `.agents/workflows`, `.agents/state`, `.agents/logs`

✅ **Process Execution Limits**
- Max memory: 256-1024MB per tier (configurable)
- Max CPU: 25-100% per tier (configurable)
- Max timeout: 60-600 seconds per tier (configurable)

✅ **Agent Authorization**
- Allowed agents: DeployAgent, SyncAgent, ValidationAgent, KnowledgeAgent
- Each agent has specific allowed operations

✅ **Circuit Breaker Protection**
- Opens after 5 failures in 60 seconds
- Prevents infinite loops and cascading failures
- Half-opens after 60 seconds to test recovery

✅ **Audit Trail**
- Every file operation logged (path, size, backup status, result)
- Every policy decision logged (allowed/denied, reason, timestamp)
- Location: `.agents/logs/audit.jsonl`

### Configuration

**Sandbox Resource Tiers:**
```yaml
standard:    256MB memory, 25% CPU, 60s timeout
premium:     512MB memory, 50% CPU, 300s timeout  
critical: 1024MB memory, 100% CPU, 600s timeout
```

Override in `.agents/config/hardening-policy.yaml`:
```yaml
agents:
  DeployAgent:
    enabled: true
    allowed_operations: [deploy, validate, status, rollback]
    constraints:
      max_concurrent: 3
      max_memory_mb: 512
      max_cpu_percent: 50
      timeout_sec: 300
```

### Production Features

✅ **Transparent Integration** - Existing agents work unchanged
✅ **Fallback Mode** - Direct execution if hardening disabled (via env var)
✅ **Policy Enforcement** - Pre-flight checks in CentralOrchestrator.execute_goal()
✅ **Safe Persistence** - All StateManager writes protected with SafeFileOperations
✅ **Comprehensive Audit** - Full operation trail for compliance
✅ **Defense-in-Depth** - Multiple security layers, no single point of failure

### Quick Commands

```bash
# Initialize hardening system
python orchestration/orchestration_main.py init

# Execute with hardening enabled (default)
python orchestration/orchestration_main.py deploy-game-release

# Disable hardening for development (if needed)
export HARDENING_ENABLED=false
python orchestration/orchestration_main.py deploy-game-release

# View audit trail
tail -f .agents/logs/audit.jsonl

# Check hardening status
python orchestration/orchestration_main.py status
```

### Integration Points

Hardening is automatically applied at 3 key orchestration locations:

1. **CentralOrchestrator.execute_goal()** - Policy check before goal execution
2. **StateManager._persist_state()** - Safe file operations for all state writes
3. **StateManager.checkpoint()** - Automatic backups for recovery

### Test Coverage

```
SafeFileOperations:    5/5 tests pass ✅
CircuitBreaker:        4/4 tests pass ✅
PolicyEngine:          6/6 tests pass ✅
AgentSandbox:          2/2 tests pass ✅
Integration:           3/3 tests pass ✅
─────────────────────────────────────
TOTAL:                20/20 tests pass ✅
```

### Files

```
.agents/security/
├── safe_operations.py          (SafeFileOperations + SafeProcessExecution)
├── circuit_breaker.py          (CircuitBreaker + CircuitBreakerManager)
├── policy_engine.py            (PolicyEngine + AgentPolicy)
├── hardened_orchestration.py   (Integration decorators + helpers)
└── __init__.py

.agents/config/
├── hardening-policy.yaml       (Agent policies + constraints)
└── hardening-defaults.yaml     (Resource limits, circuit breaker settings)

.agents/orchestration/tests/
└── test_phase1_hardening.py    (20 comprehensive tests)
```

### Documentation

**Detailed hardening documentation:** `.agents/HARDENING_PHASE1_INTEGRATION.md`

---

## 🎮 The MCP Enhancement Suite

### 🧠 Modules & Automated Usage
| Module | What the Agent Can Do | Core Files |
|---|---|---|
| **Logic & Parkour** | Create survival stats, drain rates, and raycast-based movement. | `SurvivalHandler.cs`, `ParkourController.cs` |
| **Narrative** | Lock/Unlock player input and manage Dialogue/Cinematic states. | `NarrativeDirector.cs` |
| **Asset Intel** | Paint worlds with prefabs using Poisson-Disk scattering. | `WorldScaffolder.cs` |
| **AI-NPC** | Give NPCs traits and goals (GOAP) that solve world state problems. | `NPCBrain.cs`, `GPlanner.cs` |
| **Social Manager** | Mark "Points of Interest" and coordinate crowd behaviors. | `SocialManager.cs`, `POITag.cs` |
| **Audio Intel** | Automate biome ambient sounds and material footsteps (Foley). | `AmbienceManager.cs`, `AutoFoley.cs` |
| **Multiplayer** | Sync variables and trigger RPCs across the network instantly. | `NetworkSurvivalHandler.cs`, `ActionSyncer.cs` |
| **UI/UX Vibe** | Theme the entire game UI and bind bars to stats without code. | `UIPalette.cs`, `UIBarBinding.cs` |
| **VFX & Juice** | Add camera shake, impact feel, and mood-based lighting/fog. | `JuiceScaffolder.cs`, `AtmoController.cs` |

### 🛠️ Quick Start Command Examples
- *"Add a **Hunger** stat to the player and link a **UI bar** to it."*
- *"Create an **NPC** with the **Coward** trait that avoids the player."*
- *"Initialize a **Dark Forest** atmosphere and set the **Ambience**."*
- *"Sync the **Death Animation** for all players in multiplayer."*

---

## 🧰 Workflows (63 total)

### Core Development
| Workflow | Use When |
|---|---|
| `/vibe-project-init` | Bootstrap a new Unity VR project from zero |
| `/unity-2d-setup` | Bootstrap a Unity 2D project (URP 2D, Pixel Perfect, Sprite Atlas) |
| `/unity-3d-setup` | Bootstrap a Unity 3D project (URP, NavMesh, Cinemachine 3D, LOD) |
| `/unity-xr-ar-setup` | Set up a new XR/AR Unity project |
| `/vibe-vr-scaffold` | Scaffold folders for a new VR feature |
| `/unity-brainstorm-feature` | Facilitated design session before any feature implementation |

### Code Quality
| Workflow | Use When |
|---|---|
| `/code-review-swarm` | Deep 4-role code review with severity report |
| `/csharp-format-project` | Format all C# files |
| `/unity-docs-generator` | Add XML documentation to C# scripts |
| `/unity-so-architecture` | ScriptableObject event/data architecture |
| `/unity-record-adr` | Write Architecture Decision Records |
| `/skill-audit` | Audit all skills against the 8-gate quality checklist |
| `/technical-debt-audit` | Identify and prioritize technical debt |

### Testing & QA
| Workflow | Use When |
|---|---|
| `/vibe-vr-tdd-setup` | Scaffold EditMode/PlayMode test suite |
| `/ui-testing-framework` | Set up automated UI testing |
| `/load-testing-setup` | Configure load/stress testing |
| `/qa-plan` | Create comprehensive QA plan |
| `/i18n-testing-workflow` | Test internationalization |

### Performance & Optimization
| Workflow | Use When |
|---|---|
| `/unity-performance-audit` | Profile CPU/GPU, fix GC allocators, verify on Quest |
| `/unity-profile-audit` | AI-led performance audit using real-time MCP data |
| `/unity-asset-audit` | Scan project for high-impact assets and optimization tips |
| `/build-size-optimization` | Reduce build size |
| `/shader-optimization-guide` | Optimize shaders for mobile/VR |
| `/memory-profiler-advanced` | Deep memory analysis |
| `/assets-bundle-strategy` | Configure asset bundles |
| `/mobile-optimization-audit` | Audit mobile/Quest performance |

### Debugging & Recovery
| Workflow | Use When |
|---|---|
| `/unity-smart-debug` | Diagnose Unity Console errors |
| `/unity-mcp-check` | Verify direct Unity Editor connection |
| `/unity-clean-project` | Clear Unity caches (Library, Temp) |
| `/error-recovery` | Recover from git conflicts, broken builds |
| `/project-health-check` | Overall project health assessment |

### Build & Deployment
| Workflow | Use When |
|---|---|
| `/unity-build-quest` | Build and deploy Meta Quest APK |
| `/android-specific-setup` | Android SDK, Gradle, deployment |
| `/ios-specific-setup` | iOS provisioning, Xcode setup |
| `/webgl-build-setup` | WebGL HTML5 deployment |
| `/console-build-setup` | PS5/Xbox deployment |

### Git & CI/CD
| Workflow | Use When |
|---|---|
| `/vibe-git-push` | Commit and push with AI-generated message |
| `/vibe-git-sync` | Pull/sync from remote |
| `/github-actions-unity-setup` | Set up CI/CD pipelines for Unity |
| `/changelog-generator` | Generate changelog from git commits |
| `/devops-audit` | Audit DevOps setup |

### Multiplayer & Backend
| Workflow | Use When |
|---|---|
| `/multiplayer-setup` | Set up Netcode, lobbies, matchmaking |
| `/backend-setup` | Set up APIs, databases, cloud services |

### Localization & Analytics
| Workflow | Use When |
|---|---|
| `/localization-setup` | Multi-language framework setup |
| `/analytics-integration` | Firebase, Amplitude, Sentry integration |

### Accessibility & Compliance
| Workflow | Use When |
|---|---|
| `/accessibility-audit` | WCAG, VR comfort, inclusive design |
| `/accessibility-audit-workflow` | Detailed accessibility review |
| `/vr-accessibility` | VR comfort settings, subtitles, colorblind modes |
| `/gdpr-compliance-setup` | GDPR, CCPA, COPPA compliance |

### Security
| Workflow | Use When |
|---|---|
| `/security-audit` | Security vulnerabilities, anti-cheat |
| `/security-vulnerability-scan` | Automated vulnerability scanning |

### Game Design
| Workflow | Use When |
|---|---|
| `/game-balance-review` | Review difficulty curves, economy, retention |
| `/animation-state-machine` | Set up Animator, blend trees, IK |
| `/audio-setup` | Configure spatial audio, music, ambience |

### Skill & Workflow Management
| Workflow | Use When |
|---|---|
| `/create-skill` | Create a new AI skill (with quality checklist) |
| `/create-workflow` | Create a new workflow |
| `/build-dev-cli` | Build a custom dev CLI tool |
| `/skill-pipeline` | Define and execute skill chains |
| `/project-onboarding` | Onboard new team members |
| `/dependency-health-check` | Check Unity packages for updates |
| `/unity-ui-scaffold` | Scaffold VR-optimized UI layouts |
| `/unity-smart-placement-setup` | Configure procedural placement system |

Use `/vibe-router` to describe your goal in plain English — it picks the right workflow or skill automatically.

---

## 🧠 Expert Skills (28 total)

### Unity Specialists
| Skill | Use When |
|---|---|
| `@unity-2d-expert` | Sprite/Tilemap, 2D Physics, URP 2D, Cinemachine 2D |
| `@unity-3d-expert` | URP/HDRP, NavMesh AI, 3D Physics, Cinemachine 3D, LOD |
| `@unity-architect` | Architecture decisions, trade-off analysis, ADR writing |
| `@unity-debugger` | Systematic GC/frame drop/judder/null-ref diagnosis |
| `@unity-tdd-expert` | Writing or fixing Unity EditMode/PlayMode tests |
| `@unity-smart-placement` | Procedural generation, bounds snapping, pivot fixing |

### Code & Review
| Skill | Use When |
|---|---|
| `@csharp-master` | C# code, Unity scripting, GC/memory issues |
| `@code-reviewer` | Production code review with "Ready to merge?" verdict |
| `@brainstorming` | Design-first planning — validates ideas before implementation |

### VR/XR & Performance
| Skill | Use When |
|---|---|
| `@vr-xr-specialist` | XRI v3, Quest optimization, hand tracking, spatial UI |
| `@profiling-specialist` | CPU/GPU profiling, memory analysis, frame timing |
| `@shader-optimizer` | Shader performance, GPU optimization, mobile/VR shaders |
| `@physics-expert` | Physics optimization, collision debugging, rigidbody issues |

### Multiplayer & Backend
| Skill | Use When |
|---|---|
| `@netcode-specialist` | Netcode for GameObjects, Photon, Mirror, state sync |
| `@backend-specialist` | Server architecture, database design, API design |
| `@addressables-specialist` | Asset loading, Addressables system, DLC delivery |

### Platform & Mobile
| Skill | Use When |
|---|---|
| `@mobile-expert` | iOS/Android optimization, device fragmentation |
| `@devops-engineer` | CI/CD pipelines, cloud infrastructure, deployment |

### Content & Design
| Skill | Use When |
|---|---|
| `@game-design-specialist` | Game systems, balance mechanics, economy design |
| `@animator-specialist` | Rigging, blend trees, motion capture, network sync |
| `@audio-designer` | Spatial audio, mixing, FMOD integration |
| `@timeline-specialist` | Cutscenes, cinematics, scripted sequences |
| `@localization-expert` | Multi-language support, translations, RTL text |

### Quality & Compliance
| Skill | Use When |
|---|---|
| `@accessibility-expert` | WCAG 2.1, colorblind modes, motor accessibility |
| `@security-specialist` | OWASP Top 10, encryption, vulnerability scanning |
| `@qa-strategist` | Test planning, automation frameworks, coverage |

### Meta Skills
| Skill | Use When |
|---|---|
| `@skill-improver` | Iterative audit-fix loop for any SKILL.md |
| `@workflow-assistant` | Routing, running, and creating workflows |

> **Pro tip**: Start with `@brainstorming` → validate with `@unity-architect` → implement with `@csharp-master` → review with `@code-reviewer`.

---

## 💻 Install

```bash
# Inject into any Unity project root
git clone https://github.com/LgrappaG/Workflows-Agents.git .agents
```

Open Antigravity (or any compatible AI assistant) in the workspace — workflows and skills are auto-detected.
