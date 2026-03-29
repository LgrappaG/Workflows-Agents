---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 2-3 hours
skills:
  required:
  - ui-performance-optimization
  - networking-performance-monitoring
  - ai-debugging-tools
  - csharp-performance-optimization
  - timeline-performance-profiling
  - custom-workflow-builder
  - networking-guild-system
  - terrain-performance-tuning
  - audio-performance-profiling
  - material-performance-profiling
  - physics-performance-metrics
  - physics-performance-profiling
  - debug-performance-charts
  - debug-performance-profiler
  - ui-data-binding
  - ui-drag-drop
  - ui-style-sheets
  - ui-text-binding
  - ui-two-way-binding
  - material-mipmap-chains
  - physics-constraint-optimization
  - advanced-performance-tuning
  - animation-performance-profiling
  - build-system-optimization
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-performance-metrics
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  - material-visual-debugging
  - networking-ngo-setup
  - networking-server-maintenance
  - networking-server-security
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-fluid-dynamics
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-docking-windows
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - csharp-chain-of-responsibility
  - ai-perception-system
  - machine-learning-setup
  - networking-packet-loss-handling
  - ai-environmental-awareness
  - ai-learning-adaptation
  - animation-mocap-setup
  - data-pipeline-setup
  - godot-animation-setup
  - material-specular-workflow
  - networking-connection-management
  - networking-server-authority
  recommended:
  - physics-joint-constraints
  - terrain-biome-definition
  - terrain-memory-management
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-shape-tools
  - terrain-water-integration
  - material-format-selection
  - material-texture-optimization
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-baking-setup
  - animation-constraint-rigging
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - audio-ducking-sidechains
  - audio-mixer-setup
  - automated-testing-framework
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-string-optimization
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-account-recovery
  - networking-achievement-tracking
  - networking-analytics-tracking
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-authentication
  - networking-ban-system
  - networking-bandwidth-optimization
  - networking-battle-pass
  - networking-chat-system
  - networking-client-authority
  - networking-cloud-saves
  - networking-cross-progression
  - networking-encryption
  - networking-friend-system
  - networking-interpolation
  - networking-lag-compensation
  - networking-leaderboard
  - networking-lobby-system
  - networking-matchmaking
  - networking-message-ordering
  - networking-player-persistence
  - networking-player-spawning
  - networking-prediction-reconciliation
  - networking-presence-system
  - networking-pvp-ranking
  - networking-region-selection
  - networking-replay-system
  - networking-reward-distribution
  - networking-rollback-resimulation
  - networking-rpc-system
  - networking-server-load-balancing
  - networking-server-replication
  - networking-spectator-mode
  - networking-state-synchronization
  - networking-statistics-synchronization
  - networking-trading-system
  - physics-chain-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
  optional:
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: code-reviewer
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 34.4
estimated_skills_needed: 172
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# AI-Powered Code Review Swarm

This workflow runs a structured, production-grade code review using a **4-role expert swarm**. Each role reviews the code from a distinct perspective. The orchestrator then compiles the findings into a final report with severity tiering and a "Ready to merge?" verdict.

## 1. Specify the Target Files

Tell the agent what to review.
**Example Instructions:**
- "Review all scripts in `Assets/Scripts/VR/`."
- "Run a Swarm review on my last commit."
- "Review `PlayerController.cs` and `HealthSystem.cs`."

## 2. Swarm Review (Agent Action)

The agent reads the target files and evaluates from **4 expert roles**, keeping each perspective separate.

### A. 📊 Static Analyzer
- **Focus:** Code quality, standards, and readability.
- **Checks:**
  - Naming conventions (PascalCase, _camelCase).
  - Undocumented magic numbers or strings.
  - Unused variables, imports, or dead code.
  - Missing XML documentation on public APIs.

### B. ⚡ Performance Expert
- **Focus:** Memory management, CPU hot paths, and bottlenecks.
- **Checks:**
  - Allocations inside `Update()` or tight loops.
  - Unoptimized data structure choices.
  - Unnecessary re-computation or redundant function calls.
  - LINQ or string concatenation in performance-sensitive paths.

### C. 🏗️ Architecture Lead
- **Focus:** SOLID principles, coupling, and design patterns.
- **Checks:**
  - "God Class" violations (Single Responsibility Principle).
  - Hard-coded dependencies — should use Dependency Injection.
  - Tight coupling between unrelated systems.
  - Missing or incorrect use of interfaces and abstractions.

### D. 🎮 Unity Specialist
- **Focus:** Unity Engine best practices, lifecycle, and VR/XR performance.
- **Checks:**
  - `GetComponent()` / `Find()` calls in `Update()` or loops.
  - Incorrect use of `Awake`, `Start`, `OnEnable`, `OnDisable` order.
  - GC-generating patterns (string concatenation, boxing, closures in coroutines).
  - Material/Shader inefficiency, excess Draw Calls, lack of batching.
  - Missing Object Pooling for frequently spawned objects.

---

## 3. Severity Classification

Each issue is classified using this system:

| Icon | Severity | Definition |
|------|----------|------------|
| 🔴 | **Critical** | Bugs, data loss risks, security issues, broken core functionality |
| 🟡 | **Important** | Bad architecture, missing features/tests, poor error handling |
| 🔵 | **Minor** | Code style, naming, small optimizations, documentation gaps |

---

// turbo
## 4. Generate the Consolidated Report

The orchestrator compiles all 4 roles into a single `swarm-review-results.md` file.

```bash
echo "# 🤖 AI Swarm Code Review Results" > swarm-review-results.md
echo "" >> swarm-review-results.md
echo "## Reviewed Files" >> swarm-review-results.md
echo "- (agent lists files here)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "## 📊 Static Analysis" >> swarm-review-results.md
echo "(agent output)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "## ⚡ Performance Report" >> swarm-review-results.md
echo "(agent output)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "## 🏗️ Architecture Review" >> swarm-review-results.md
echo "(agent output)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "## 🎮 Unity & XR Optimization" >> swarm-review-results.md
echo "(agent output)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "---" >> swarm-review-results.md
echo "## 🔥 Executive Summary — Priority Fixes" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "### 🔴 Critical (Must Fix Before Merge)" >> swarm-review-results.md
echo "(list)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "### 🟡 Important (Should Fix)" >> swarm-review-results.md
echo "(list)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "### 🔵 Minor (Nice to Have)" >> swarm-review-results.md
echo "(list)" >> swarm-review-results.md
echo "" >> swarm-review-results.md
echo "## Assessment" >> swarm-review-results.md
echo "**Ready to merge?** [Yes / No / Yes with fixes]" >> swarm-review-results.md
echo "**Reasoning:** (1-2 sentence technical verdict)" >> swarm-review-results.md
```

---

## 5. Review and Apply

After `swarm-review-results.md` is generated:

1. **Read the Assessment section first** — get the "Ready to merge?" verdict.
2. **Address Critical issues immediately** before any merge.
3. Instruct the agent to apply specific fixes:

**Example:**
> "Apply all 🔴 Critical fixes from the Swarm report to `PlayerController.cs`."
> "Fix the 🟡 Important architecture issue in `NetworkManager.cs` — extract the `IConnectionHandler` interface."