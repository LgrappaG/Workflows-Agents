---
version: 9.0.0
category: Game Design
agent: Game Design Specialist
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ui-performance-optimization
  - custom-workflow-builder
  - terrain-performance-tuning
  - terrain-water-integration
  - ai-perception-system
  - animation-performance-profiling
  - audio-performance-profiling
  - ci-cd-pipeline-setup
  - csharp-performance-optimization
  - debug-performance-charts
  - debug-performance-profiler
  - godot-animation-setup
  - machine-learning-setup
  - networking-performance-monitoring
  - performance-profiling-cross-engine
  - physics-constraint-optimization
  - physics-performance-metrics
  - physics-performance-profiling
  - terrain-multi-layer-textures
  - terrain-noise-functions
  - terrain-shape-tools
  - timeline-performance-profiling
  - training-datasets
  - ui-context-menus
  - ui-event-handlers
  - ui-input-validation
  - ui-responsive-design
  - advanced-performance-tuning
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-debugging-tools
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
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
  - automated-testing-framework
  - build-system-optimization
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - debug-build-diagnostic
  - debug-performance-metrics
  - engine-migration-guide
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - material-pbr-setup
  recommended:
  - material-performance-profiling
  - material-specular-workflow
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-guild-system
  - networking-ngo-setup
  - networking-server-maintenance
  - performance-dashboard
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  - terrain-biome-definition
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
  - terrain-memory-management
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
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
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
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
  optional:
  - ui-panel-layout
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-scrolling-behavior
  - ui-style-sheets
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: tech-lead
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 33.75
estimated_skills_needed: 135
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# /unity-brainstorm-feature

A guided design-first workflow that prevents premature coding by running the `@brainstorming` skill before activating any implementation skill. Produces a validated design document and a clean implementation handoff.

---

## When to Use

- Starting any non-trivial VR feature or system
- Before making architecture decisions that affect multiple scripts
- When requirements are unclear or feel underspecified
- When you've started coding and realized the design wasn't thought through

---

## Steps

### Step 1: Activate Brainstorming Mode

```
Activate @brainstorming skill.
State the feature idea in 1–2 sentences. Do not write code yet.
```

The `@brainstorming` skill will now take over and guide a structured dialogue.

---

### Step 2: Context Review

The agent will read:
- Existing relevant scripts, scenes, and ScriptableObjects
- Prior ADRs (if any in `.docs/adr/`)
- Current VR performance budget and platform target

**Wait for the agent's Understanding Summary before proceeding.**

---

### Step 3: One-Question Dialogue

Answer the agent's questions one at a time. Expected questions include:
- What platform? (Quest 2 / Quest 3 / PC VR / all)
- What is the success criterion for this feature?
- What are the explicit non-goals?
- Are there performance constraints? (entity count, frame budget)
- Does this need to integrate with the existing event system?

---

### Step 4: Understanding Lock

The agent will produce an **Understanding Summary** (5–7 bullets).

```
Review the summary carefully.
Confirm or correct it before the agent proposes any design.
```

**Do NOT proceed until you explicitly confirm the summary.**

---

### Step 5: Design Proposal

The agent will propose 2–3 architectural approaches with trade-off analysis.

```
Select one approach, or ask for a hybrid.
The agent will present the design incrementally (200–300 words per section).
Confirm each section before the next is presented.
```

---

### Step 6: Document the Design

The agent will write the finalized design to:

```
.docs/design/<feature-name>.md
```

Containing:
- Understanding summary
- Decision log
- Final design
- Testing strategy

---

### Step 7: Architecture Review (Optional)

For complex systems, activate:
```
@unity-architect
```
to validate component boundaries and produce a formal ADR.

---

### Step 8: Implementation Handoff

Once design is documented and confirmed:

```
Activate @csharp-master to begin implementation.
Reference the design document at .docs/design/<feature-name>.md.
```

The implementation skill will follow the validated design document exactly.

---

## Exit Criteria

This workflow is complete only when:
- [ ] Understanding Lock is confirmed
- [ ] Design approach is explicitly accepted
- [ ] Design document is saved to `.docs/design/`
- [ ] Handoff to `@csharp-master` is initiated (or deferred intentionally)