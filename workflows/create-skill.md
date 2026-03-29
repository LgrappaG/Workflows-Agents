---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ai-debugging-tools
  - debug-shader-debugging
  - physics-hair-dynamics
  - physics-joint-constraints
  - custom-workflow-builder
  - debug-renderer-debugging
  - debug-script-debugging
  - material-visual-debugging
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-terrain-deformation
  - terrain-physics-colliders
  - ui-event-handlers
  - ui-visual-feedback
  - ai-environmental-awareness
  - ai-learning-adaptation
  - ai-perception-system
  - csharp-chain-of-responsibility
  - material-mipmap-chains
  - material-specular-workflow
  - physics-layer-masking
  - physics-trigger-volumes
  - terrain-biome-definition
  - terrain-cave-systems
  - terrain-noise-functions
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-water-integration
  - ui-context-menus
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-panel-layout
  - ui-prefab-variants
  - ui-two-way-binding
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - automated-testing-framework
  - build-system-optimization
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-physics-debugger
  - engine-migration-guide
  - godot-physics-system
  - material-disney-workflow
  - material-metallic-workflow
  - material-physics-interactions
  - networking-guild-system
  - networking-server-maintenance
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  recommended:
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-collision-callbacks
  - physics-continuous-collision
  - physics-debug-visualization
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-force-fields
  - physics-friction-models
  - physics-inertia-calculation
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-particle-collisions
  - physics-performance-metrics
  - physics-performance-profiling
  - physics-ragdoll-physics
  - physics-rolling-resistance
  - physics-rope-simulation
  - physics-solver-configuration
  - physics-spring-dynamics
  - physics-suspension-tuning
  - physics-time-scaling
  - physics-trigger-callbacks
  - physics-vehicle-setup
  - physics-vehicle-wheels
  - physics-water-waves
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-brush-settings
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
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-wind-zones
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  optional:
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-focus-navigation
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: unity-architect
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 32.5
estimated_skills_needed: 130
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Create Skill Workflow

This workflow guides creation of a new **production-quality** skill in `.agents/skills/`. Skills must meet the Antigravity Awesome Skills quality standard to be effective and auto-discoverable.

## 1. Define the Skill

Provide the skill name and purpose.

**Example:**
> "Create a `shader-debugger` skill that helps diagnose Unity HLSL shader issues."

The agent will derive:
- `skill-name`: lowercase-with-hyphens (e.g., `shader-debugger`)
- `description`: a prompt-friendly trigger description

---

// turbo
## 2. Scaffold the Skill Directory

```bash
SKILL_NAME="your-skill-name"
mkdir -p ".agents/skills/$SKILL_NAME"
```

---

## 3. Generate the SKILL.md (Quality Standard)

The agent creates `.agents/skills/[skill-name]/SKILL.md` using **all required sections**:

### Required YAML Frontmatter
```yaml
---
name: skill-name
description: When to activate this skill — phrase it as a trigger condition for the AI.
risk: low | medium | high
source: workspace
date_added: 'YYYY-MM-DD'
---
```

### Required Markdown Sections

```markdown
# Skill Title

One-line summary of the persona or capability.

## Use this skill when
- [specific scenario 1]
- [specific scenario 2]

## Do NOT use this skill when
- [anti-pattern / out-of-scope situation]

## Core Mandates

### 1. [Mandate Name]
[Specific, actionable rule — not vague advice]

### 2. [Mandate Name]
[Specific, actionable rule]

## Response Format
[How the AI should structure its answer — numbered steps, tables, code blocks, etc.]

## Example Interactions
- "[Example user request]"
- "[Example user request]"
```

### Quality Checklist (Agent Must Verify Before Saving)

- [ ] YAML frontmatter has `name`, `description`, `risk`, `source`, `date_added`
- [ ] "Use this skill when" has ≥ 2 specific bullet points
- [ ] "Do NOT use this skill when" has ≥ 1 bullet point (prevents misuse)
- [ ] "Core Mandates" has ≥ 2 numbered sections with actionable rules
- [ ] "Response Format" specifies concrete structure (numbered list, table, code block)
- [ ] "Example Interactions" has ≥ 2 real-world examples
- [ ] File is named exactly `SKILL.md` (not `skill-name.md`)

---

## 4. Verify and Extend

After creation:
1. Review the `SKILL.md` in the editor.
2. Optionally add supporting files:
   - `scripts/` — helper scripts the skill can reference
   - `examples/` — reference implementations
   - `resources/` — cheat sheets, spec docs, or templates