---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-physics-colliders
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - custom-workflow-builder
  - material-specular-workflow
  - csharp-chain-of-responsibility
  - physics-trigger-volumes
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-debugging-tools
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - csharp-async-await
  - debug-physics-debugger
  - godot-physics-system
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - material-physics-interactions
  - networking-server-maintenance
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-collision-callbacks
  - physics-continuous-collision
  - physics-debug-visualization
  recommended:
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
  - physics-trigger-callbacks
  - physics-vehicle-setup
  - physics-vehicle-wheels
  - physics-water-waves
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
  optional:
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- response-patterns-actionability
- mandates-clarity
primary_agent: unity-architect
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 28.33
estimated_skills_needed: 85
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Architecture Decision Record (ADR) Workflow

When you use workflows like `/unity-ai-code-review` or `/unity-so-architecture` to make structural, tooling, or pattern changes to your Unity codebase, you should document *why* those decisions were made. 

This workflow uses the `architecture-decision-records` skill to create standardized markdown documents that explain your VR project's architecture history.

// turbo-all
## 1. Scaffold the ADR Folder

It all starts by keeping our records in a dedicated folder.

```bash
mkdir -p "Docs/ADRs"
```

## 2. Agent Analyzes the Decision

You explain the recent architectural choice to the agent, or specify a recently completed task (e.g., "We just switched to an Event-driven ScriptableObject architecture for the grab system.")

**Example Instruction for the Agent:**
"Please create an `/unity-record-adr` about deciding to use Unity's XR Interaction Toolkit over a custom physics hand grabber. We chose XRIT because of long-term maintainability, but the trade-off is somewhat heavier GC overhead."

## 3. Agent Generates the ADR

The agent will format your input into a standardized ADR template containing:
- Status
- Context
- Decision
- Consequences

It will save it sequentially, like `Docs/ADRs/0001-use-xrit-for-grabbing.md`.

You now have a permanent log of *why* things are the way they are in your code base, making it easier for new developers or future-you to understand the project constraints!