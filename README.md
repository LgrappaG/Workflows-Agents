# 🚀 Workflows Agents — Unity Multi-Platform Toolkit v9.0.3

A comprehensive AI automation framework for **Unity game development across all platforms** (VR/XR, Mobile, PC, WebGL, Console), featuring **63 workflows + 585 AI-powered specialist skills** organized in **18 categories**, backed by a **48-agent organizational hierarchy** and **8-gate validation system** for rapid development and production-ready systems.

**NEW in v9.0.3:** 🎉 **Phase 5 Enrichment Release** - 585 total skills (512→585, +73 Phase 5). Phase 5 Complete: Domain-specific YAML enrichment across 40 core skills. Measurable mandates, concrete response patterns, real usage contexts. File sizes optimized 1.5-2.0KB for deep domain expertise (vs 1.2KB baseline). Full documentation coverage (55 pages). Production-grade quality metrics with atomic git history.

**Previous:** v8.2.0 - Phase 3 Skills Expansion (450 skills), v8.1.0 - Phase 2 (300 skills), v8.0.0 - Phase 1 (150 skills).

Inspired by and compatible with [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills).

**Quick Navigation:**
- 📖 [Quick Start Guide](docs/QUICK_START.md) - 5 minute onboarding
- ⚡ [Token Optimization](docs/TOKEN_OPTIMIZATION.md) - 30-50% context savings
- 🐛 [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues & fixes
- 📚 [Full Documentation Index](docs/DOCUMENTATION_INDEX.md) - All references
- 📊 [Version Manifest](VERSION_MANIFEST.json) - Complete inventory
- 🔗 [CHANGELOG.md](CHANGELOG.md) - Full version history

---

## 🎮 The MCP Enhancement Suite (9 Phases)

This suite allows an AI agent to build complex gameplay, AI, and graphics systems autonomously.

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
