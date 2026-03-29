---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - ai-debugging-tools
  - material-visual-debugging
  - custom-workflow-builder
  - debug-renderer-debugging
  - terrain-performance-tuning
  - ui-performance-optimization
  - debug-performance-profiler
  - debug-script-debugging
  - debug-shader-debugging
  - animation-performance-profiling
  - material-specular-workflow
  - networking-performance-monitoring
  - terrain-path-carving
  - timeline-performance-profiling
  - audio-performance-profiling
  - build-system-optimization
  - csharp-chain-of-responsibility
  - csharp-performance-optimization
  - debug-build-diagnostic
  - debug-performance-charts
  - debug-performance-metrics
  - godot-animation-setup
  - material-pbr-setup
  - navmesh-baking-setup
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-constraint-optimization
  - physics-joint-constraints
  - physics-performance-metrics
  - physics-performance-profiling
  - terrain-biome-definition
  - terrain-memory-management
  - terrain-noise-functions
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-water-integration
  - training-datasets
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-input-validation
  - ui-style-sheets
  - advanced-performance-tuning
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-baking-setup
  - animation-constraint-rigging
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-ducking-sidechains
  - audio-mixer-setup
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - csharp-async-await
  - csharp-builder-pattern
  - data-pipeline-setup
  - engine-migration-guide
  - godot-setup
  - graphics-gpu-profiling
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - material-performance-profiling
  - material-translucency-setup
  - networking-guild-system
  recommended:
  - networking-ngo-setup
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-wind-zones
  - timeline-camera-transitions
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-event-handlers
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
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
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-two-way-binding
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - vfx-trail-rendering
  - debug-memory-profiler
  - graphics-shadow-optimization
  - material-runtime-modification
  - material-triplanar-mapping
  - animation-frame-stepping
  - audio-multi-output-routing
  - csharp-flyweight-pattern
  - csharp-memento-pattern
  optional:
  - csharp-string-optimization
  - debug-runtime-metrics
  - graphics-batching-optimization
  - graphics-frame-debugger
  - material-ambient-occlusion
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
- performance-engineer
complexity_score: 10
skill_density: 40.25
estimated_skills_needed: 161
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# /unity-performance-audit

A structured workflow to profile, diagnose, and fix performance issues in a Unity VR build. Uses the `@unity-debugger` skill for systematic root cause analysis.

---

## Prerequisites

- Unity Profiler available (Unity Editor or Remote Profiler via USB)
- OVR Metrics Tool installed on Quest device (for Quest builds)
- A reproducible "slow" scene or gameplay sequence

---

## Steps

### Step 1: Establish Baseline Metrics

Record current state before touching anything.

```
Profile 300 frames of the problematic sequence.
Note: average frame time (ms), GC.Alloc per frame, draw call count.
```

Expected targets for Quest 2: `< 11ms GPU`, `< 150 draw calls`, `< 1KB GC alloc/frame`
Expected targets for Quest 3: `< 8ms GPU`, `< 200 draw calls`, `< 1KB GC alloc/frame`

---

### Step 2: Identify the Bottleneck Type

Use `@unity-debugger` to classify:

```
Activate @unity-debugger and run the GC Spike Checklist.
Then run the VR Judder / Frame Drop Checklist.
```

Determine whether the bottleneck is:
- **CPU-bound** → proceed to Step 3a
- **GPU-bound** → proceed to Step 3b
- **GC/Memory** → proceed to Step 3c

---

### Step 3a: Fix CPU Bottlenecks

```
Open Profiler → CPU Usage → sort by Self Time (descending).
Identify top 3 methods consuming > 1ms.
```

Common fixes:
- Move heavy calculations from `Update()` to coroutines or Jobs
- Cache all `GetComponent<T>()` calls to `Awake()`
- Use object pooling for frequently spawned objects
- Replace `FindObjectsOfType<T>()` with cached lists

---

### Step 3b: Fix GPU / Draw Call Bottlenecks

```
Open Frame Debugger → enable → step through draw calls.
Find un-batched geometry (check "Why not batched" tooltip).
```

// turbo
Common fixes:
- Enable GPU Instancing on materials with many instances
- Enable Static Batching for non-moving geometry
- Disable shadow casting on small/distant objects
- Bake lightmaps instead of using real-time lights

---

### Step 3c: Fix GC Allocations

```
Open Profiler → CPU → GC.Alloc column → sort descending.
Click the top allocating frame → expand callstack.
```

Apply fixes from `@unity-debugger resources/debugging-playbook.md`:
- Replace LINQ with manual loops
- Replace `new WaitForSeconds(t)` with cached instances
- Replace string concatenation with StringBuilder in hot paths
- Unsubscribe events in `OnDisable` to prevent retention

---

### Step 4: Apply Fixes Incrementally

```
Fix one issue at a time.
Profile after each fix to confirm improvement.
Do NOT fix multiple issues simultaneously — you'll lose causality.
```

---

### Step 5: Validate on Hardware

For Quest builds:
1. Build and deploy to device (`/unity-build-quest`)
2. Open OVR Metrics Tool → enable overlay
3. Confirm: ASW is NOT active (green), GPU time is under budget
4. Run the same 300-frame sequence from Step 1

---

### Step 6: Document Results

Update the project's performance log:

```markdown
## Performance Audit — [Date]
**Scene:** [scene name]
**Platform:** Quest 2 / Quest 3 / PC VR

| Metric | Before | After | Target |
|---|---|---|---|
| GPU frame time | X ms | Y ms | < 11ms |
| Draw calls | X | Y | < 150 |
| GC alloc/frame | X KB | Y KB | < 1KB |

**Root causes fixed:**
1. [description]
2. [description]
```

Save to `.docs/performance/audit-YYYY-MM-DD.md`.