---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - ai-debugging-tools
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-physics-colliders
  - ui-event-handlers
  - build-system-optimization
  - ci-cd-pipeline-setup
  - godot-animation-setup
  - material-mipmap-chains
  - physics-trigger-callbacks
  - terrain-brush-settings
  - terrain-normal-generation
  - ui-anchor-positioning
  - ui-animation-states
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-style-sheets
  - ui-transition-timing
  - ui-z-ordering
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
  - automated-testing-framework
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - debug-build-diagnostic
  - debug-physics-debugger
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  recommended:
  - godot-physics-system
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-pbr-setup
  - material-physics-interactions
  - material-translucency-setup
  - material-visual-debugging
  - navmesh-baking-setup
  - networking-guild-system
  - networking-ngo-setup
  - networking-server-maintenance
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
  - physics-trigger-volumes
  - physics-vehicle-wheels
  - physics-water-waves
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
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
  optional:
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-procedural-generation
  - terrain-shadow-caching
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
skill_density: 42.33
estimated_skills_needed: 127
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Meta Quest Build Workflow

Building an APK for Meta Quest can be repetitive and interrupt your flow state. This workflow leverages the knowledge from `unity-developer` and CI/CD patterns in `antigravity-awesome-skills` to automate the build process of your VR application directly from the terminal without taking up Editor UI interaction time.

## 1. Trigger the Build

Run this workflow when your current scene and project settings are ready for a device test on the Meta Quest.

**Example Instruction for the Agent:**
"Start a new Quest build using `/unity-build-quest`, version 0.1.0."

## 2. Execute Batch Build (Agent Action)

The agent will run Unity in batch mode to execute a build script. 
*(Note: For this step to fully work, a static Editor script must be present. The agent can generate this script if it doesn't exist.)*

// turbo
```bash
# Agent will build the APK asynchronously via Unity CLI
# Assuming Unity is installed in the default location or available in PATH natively/via alias
echo "Triggering Unity Build... (This takes a while depending on project size)"

# Standard Unity CLI build command template:
# "$UNITY_PATH" -quit -batchmode -logFile "Logs/build-log.txt" -projectPath "." -executeMethod BuildScript.BuildAndroid
```

## 3. Review Build Logs

While the build is running, the agent will monitor the `Logs/build-log.txt` file and notify you of any errors or if the build succeeds.

Once the APK is created (typically in the `Builds/` folder), you will be notified, and you can push it to your Quest using sidequest or `adb install`.