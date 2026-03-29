---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - material-specular-workflow
  - ci-cd-pipeline-setup
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - data-pipeline-setup
  - godot-animation-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - ui-modal-dialogs
  - ai-debugging-tools
  - animation-constraint-rigging
  - csharp-chain-of-responsibility
  - physics-joint-constraints
  - terrain-biome-definition
  - terrain-cave-systems
  - terrain-noise-functions
  - terrain-shape-tools
  - terrain-water-integration
  - ui-context-menus
  - ui-event-handlers
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-panel-layout
  - ui-prefab-variants
  - ui-style-sheets
  - ui-two-way-binding
  - ui-visual-feedback
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  recommended:
  - build-system-optimization
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - material-mipmap-chains
  - networking-guild-system
  - networking-server-maintenance
  - networking-server-security
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
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
skill_density: 21.8
estimated_skills_needed: 109
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Creating a Workflow

Workflows are structured markdown files that define a sequence of steps to accomplish a specific task. They enable reusable automation and consistent execution.

## 1. File Location
All workflow files must be created with a `.md` extension in one of the following directories (relative to your workspace root):
- `.agents/workflows/`
- `.agent/workflows/`
- `_agents/workflows/`
- `_agent/workflows/`

*Example:* `.agents/workflows/my-awesome-workflow.md`

## 2. File Structure: YAML Frontmatter
Every workflow file MUST begin with YAML frontmatter containing a `description`. This description acts as the title or trigger hint for the workflow.

```markdown
---
description: A short title or description of what the workflow does.
---
```

## 3. Writing the Steps
Below the frontmatter, write out the specific instructions, steps, or commands required to execute the workflow using standard Markdown. Be as clear, specific, and chronological as possible.

```markdown
# My Workflow Title

1. **Step One:** Explain what to do conceptually.
2. **Step Two:** If a command is needed, provide the exact shell command:
   ```bash
   npm install some-package
   ```
```

## 4. Automation Annotations (Turbo Mode)
You can instruct the agent to automatically execute commands without asking for user confirmation using "turbo" annotations.

### Single Step Automation `// turbo`
Place `// turbo` exactly one line above a step to auto-run only that specific step's commands.

```markdown
// turbo
1. Create a necessary directory structure:
   ```bash
   mkdir -p src/components
   ```
2. This step will NOT be auto-run because it lacks the annotation.
```

### Full Workflow Automation `// turbo-all`
Place `// turbo-all` anywhere in the document (usually at the top after the frontmatter) to auto-run **EVERY** safe command in the entire workflow.

```markdown
---
description: Fully Automated Setup
---
// turbo-all

# Setup Steps
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the service:
   ```bash
   npm run dev
   ```
```

## 5. Usage
Once saved, the workflow will be automatically detected and available to use via `/filename-without-ext`. For example, a file named `deploy-app.md` becomes the `/deploy-app` command.