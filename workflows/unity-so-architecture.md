---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - physics-joint-constraints
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-physics-colliders
  - ai-debugging-tools
  - ai-learning-adaptation
  - ai-perception-system
  - material-mipmap-chains
  - terrain-cave-systems
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-shape-tools
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - networking-server-maintenance
  - terrain-advanced-editing
  - terrain-biome-definition
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
  - terrain-performance-tuning
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  recommended:
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - training-datasets
  - vfx-trail-rendering
  - physics-trigger-volumes
  - automated-testing-framework
  - cinemachine-virtual-camera
  - compatibility-testing
  - custom-workflow-builder
  - debug-physics-debugger
  - godot-physics-system
  - material-disney-workflow
  - material-metallic-workflow
  - material-physics-interactions
  - material-specular-workflow
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-collision-callbacks
  - physics-continuous-collision
  - physics-debug-visualization
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-fluid-dynamics
  - physics-force-fields
  - physics-friction-models
  - physics-inertia-calculation
  - physics-layer-masking
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
  optional:
  - physics-trigger-callbacks
  - physics-vehicle-setup
  - physics-vehicle-wheels
  - physics-water-waves
  - timeline-camera-transitions
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
skill_density: 34.33
estimated_skills_needed: 103
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity SO Architecture Scaffold

This workflow uses concepts from `architecture-patterns` and `unity-ecs-patterns` within `antigravity-awesome-skills` to generate a lightweight, event-driven ScriptableObject (SO) architecture for Unity.

By avoiding singletons and driving game flow through SO Events and Variables, your Unity project becomes more modular and easier to test, especially for VR interactions.

// turbo-all
## 1. Scaffold Core SO Architecture Folders

Create the base folder structure for the core ScriptableObject patterns inside `Assets/Core/Architecture`.

```bash
CORE_DIR="Assets/Core/Architecture"
mkdir -p "$CORE_DIR/Events"
mkdir -p "$CORE_DIR/Variables"
mkdir -p "$CORE_DIR/Sets"
```

## 2. Generate Base Event Classes

The agent generates a basic `GameEvent` and `GameEventListener` script using C#.
Variables and Sets will be generated similarly.

```bash
# Agent Action Details:
# The agent will generate `GameEvent.cs`, `GameEventListener.cs`, `FloatVariable.cs`, and `RuntimeSet.cs`
# natively using its programming capabilities into the new directories.
# No hardcoded echo string is necessary here; it will write the files dynamically.
echo "// The AI will generate the architecture scripts in these folders" > "$CORE_DIR/ArchitectureREADME.txt"
```

## 3. Review Generated Architecture

Review the `Assets/Core/Architecture` directory in your Unity editor. You can now start creating highly decoupled GameEvent assets in your Unity Project window, and use the listeners to trigger complex VR behaviors without hardcoding references.