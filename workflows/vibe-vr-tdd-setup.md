---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - physics-vehicle-setup
  - ci-cd-pipeline-setup
  - custom-workflow-builder
  - godot-animation-setup
  - physics-joint-constraints
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - data-pipeline-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-specular-workflow
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-physics-colliders
  - ai-debugging-tools
  - animation-constraint-rigging
  - material-mipmap-chains
  - physics-collision-callbacks
  - terrain-cave-systems
  - terrain-normal-generation
  - terrain-water-integration
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
  - automated-testing-framework
  recommended:
  - cinemachine-aim-assist
  - compatibility-testing
  - csharp-async-await
  - csharp-chain-of-responsibility
  - debug-physics-debugger
  - godot-physics-system
  - material-physics-interactions
  - networking-server-maintenance
  - networking-server-security
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  - physics-center-of-mass
  - physics-cloth-simulation
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
  - physics-trigger-callbacks
  - physics-trigger-volumes
  - physics-vehicle-wheels
  - physics-water-waves
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  optional:
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
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
complexity_score: 5.0
skill_density: 33.0
estimated_skills_needed: 99
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# VR TDD Scaffold Workflow

This workflow uses the `tdd-workflow` skill from `antigravity-awesome-skills` to instantly scaffold Unity Test Framework assemblies (`.asmdef`) for EditMode and PlayMode tests, along with a base template for testing VR interactions.

Test-driven design is crucial for stable XR development. Setting up tests manually in Unity takes a lot of clicks. This automates the setup for a new feature.

## 1. Specify Feature Name

To scaffold tests properly, the agent needs to know the name of the feature you want to test.

**Example Instruction for the Agent:**
"Please run the TDD scaffold for a new feature called `InventorySystem`."

## 2. Scaffold Directories and Assembly Definitions

The agent will automatically create the `Tests/EditMode` and `Tests/PlayMode` folder structure inside `Assets/Features/[FeatureName]`, along with the corresponding `.asmdef` files to ensure they only compile in the Unity Test Runner.

// turbo-all
```bash
# Example agent automation (Agent will replace [FeatureName] with the actual target)
FEATURE_DIR="Assets/Features/YourNewFeature"
TESTS_DIR="$FEATURE_DIR/Tests"

mkdir -p "$TESTS_DIR/EditMode"
mkdir -p "$TESTS_DIR/PlayMode"

# Scaffold EditMode Asmdef
echo '{
    "name": "YourNewFeature.Tests.EditMode",
    "rootNamespace": "",
    "references": [
        "UnityEngine.TestRunner",
        "UnityEditor.TestRunner"
    ],
    "includePlatforms": [
        "Editor"
    ],
    "excludePlatforms": [],
    "allowUnsafeCode": false,
    "overrideReferences": true,
    "precompiledReferences": [
        "nunit.framework.dll"
    ],
    "autoReferenced": false,
    "defineConstraints": [
        "UNITY_INCLUDE_TESTS"
    ],
    "versionDefines": [],
    "noEngineReferences": false
}' > "$TESTS_DIR/EditMode/YourNewFeature.Tests.EditMode.asmdef"

# Scaffold PlayMode Asmdef
echo '{
    "name": "YourNewFeature.Tests.PlayMode",
    "rootNamespace": "",
    "references": [
        "UnityEngine.TestRunner",
        "UnityEditor.TestRunner",
        "Unity.XR.Interaction.Toolkit"
    ],
    "includePlatforms": [],
    "excludePlatforms": [],
    "allowUnsafeCode": false,
    "overrideReferences": true,
    "precompiledReferences": [
        "nunit.framework.dll"
    ],
    "autoReferenced": false,
    "defineConstraints": [
        "UNITY_INCLUDE_TESTS"
    ],
    "versionDefines": [],
    "noEngineReferences": false
}' > "$TESTS_DIR/PlayMode/YourNewFeature.Tests.PlayMode.asmdef"
```

## 3. Generate Base Test Templates

The agent will then create a base `[FeatureName]EditModeTest.cs` and `[FeatureName]PlayModeTest.cs` script within the respective folders.

**Now you can ask the agent to write the first failing test!**