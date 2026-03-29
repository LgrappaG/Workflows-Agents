---
version: 9.0.0
category: Git & CI/CD
agent: DevOps Engineer
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - automated-testing-framework
  - compatibility-testing
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - godot-animation-setup
  - graphics-hdrp-setup
  - ui-context-menus
  - ui-event-handlers
  - ui-keyboard-shortcuts
  - ai-debugging-tools
  - animation-constraint-rigging
  - animation-mirror-setup
  - ci-cd-pipeline-setup
  - csharp-chain-of-responsibility
  - material-mipmap-chains
  - networking-ngo-setup
  - physics-joint-constraints
  - terrain-path-carving
  - terrain-wind-zones
  - ui-anchor-positioning
  - ui-prefab-variants
  - ui-two-way-binding
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
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mocap-setup
  - audio-ducking-sidechains
  - audio-mixer-setup
  - build-system-optimization
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - data-pipeline-setup
  - debug-build-diagnostic
  - engine-migration-guide
  - godot-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  recommended:
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-guild-system
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
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
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-normal-generation
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
  - training-datasets
  - ui-accessibility
  - ui-animation-states
  - ui-animation-tweens
  optional:
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
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
complexity_score: 5.0
skill_density: 25.75
estimated_skills_needed: 103
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# GitHub Actions for Unity Setup

This workflow automates the creation of a CI/CD pipeline for your Unity project, ensuring every push is tested and (optionally) built for Meta Quest or other platforms.

## 1. Select the CI/CD Components

The agent will ask which parts of the pipeline you want to enable:
- **Unit Testing:** Runs EditMode and PlayMode tests.
- **Build Automation:** Builds an APK (Android/Quest) or executable (Windows/Mac).
- **Static Analysis:** Runs C# linting and project validation.

## 2. Generate Workflow Files (Agent Action)

The agent will create the `.github/workflows/unity-main.yml` file.

### Key Actions Used:
- `game-ci/unity-test-runner@v2`: For running tests.
- `game-ci/unity-builder@v2`: For building the project.
- `game-ci/unity-request-activation-file@v2`: For license handling.

## 3. Configuration Guide

The agent will provide a step-by-step guide on how to set up the necessary GitHub Secrets:
- `UNITY_LICENSE`: Your Unity personal or pro license.
- `UNITY_EMAIL`: Your Unity ID email.
- `UNITY_PASSWORD`: Your Unity ID password.

## 4. Final Steps

Once the files are created, the agent will offer to:
1. Commit the new workflow files to a new branch.
2. Push the changes to GitHub.
3. Verify the "Actions" tab on your repository.

**Example Instruction:**
"Set up a GitHub Action that runs all my PlayMode tests on every pull request to the `main` branch."