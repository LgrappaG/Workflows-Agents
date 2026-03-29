---
version: 9.0.0
category: Build & Deployment
agent: DevOps Engineer
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - machine-learning-setup
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - ci-cd-pipeline-setup
  - data-pipeline-setup
  - godot-animation-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - ai-learning-adaptation
  - build-system-optimization
  - physics-chain-dynamics
  - terrain-biome-definition
  - terrain-cave-systems
  - ui-panel-layout
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-debugging-tools
  - ai-environmental-awareness
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  recommended:
  - engine-migration-guide
  - material-mipmap-chains
  - networking-guild-system
  - networking-server-maintenance
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
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
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  optional:
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
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
skill_density: 24.0
estimated_skills_needed: 96
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Developer CLI Tool Builder

This workflow guides you through creating a custom CLI tool to manage your `.agents` workflows or generic project tasks.

## 1. Define CLI Requirements

Tell the agent what commands and features the CLI should have.
**Example:**
"I want a CLI tool called `vibe` that can run `vibe-router`, `unity-clean-project`, and `vibe-git-push`."

## 2. Infrastructure Setup (Agent Action)

The agent will initialize a basic Node.js or Python CLI structure.
- **Node.js:** Using `commander` or `yargs`.
- **Python:** Using `click` or `argparse`.

## 3. Command Implementation (Agent Action)

The agent will map your workflows to CLI commands.

```javascript
// Example generated CLI snippet
#!/usr/bin/env node
const { program } = require('commander');

program
  .command('push')
  .description('Push changes with AI message')
  .action(() => {
    // Logic to trigger vibe-git-push workflow
  });

program.parse(process.argv);
```

## 4. Packaging and Linking

The agent will provide instructions to link the CLI globally (e.g., `npm link` or `pip install -e .`) so you can run it from anywhere in your project terminal.