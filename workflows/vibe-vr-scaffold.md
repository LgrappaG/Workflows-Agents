---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - terrain-cave-systems
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
  - animation-baking-setup
  - animation-constraint-rigging
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-ducking-sidechains
  - audio-mixer-setup
  - build-system-optimization
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - debug-build-diagnostic
  - engine-migration-guide
  - godot-animation-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - material-pbr-setup
  - material-specular-workflow
  - material-translucency-setup
  - navmesh-baking-setup
  recommended:
  - networking-guild-system
  - networking-ngo-setup
  - networking-server-maintenance
  - networking-server-security
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
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
  optional:
  - terrain-water-integration
  - terrain-wind-zones
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
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
skill_density: 22.5
estimated_skills_needed: 90
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


// turbo-all

# Vibe Coding VR Scaffold

As a VR developer, when developing new features quickly in the "Vibe Coding" style, this scaffolding generates a standard folder structure to ensure the project remains organized.

This workflow prepares the necessary subfolders for the new module you will be working on under your Unity project's `Assets/Features` directory.

## 1. Specify Feature Name

Tell the agent the feature name:
- "Scaffold a new VR Grab feature"
- "Create folders for Teleportation system"

## 2. Create the Folder Structure

```bash
FEATURE_NAME="NewVRFeature"
BASE_PATH="Assets/Features/$FEATURE_NAME"

mkdir -p "$BASE_PATH/Scripts"
mkdir -p "$BASE_PATH/Prefabs"
mkdir -p "$BASE_PATH/Materials"
mkdir -p "$BASE_PATH/ScriptableObjects"

echo "✅ VR Feature folders created under '$BASE_PATH'!"
```

## 3. Create Assembly Definition (Optional)

For better compilation times, create an assembly definition:

```bash
cat > "$BASE_PATH/Scripts/${FEATURE_NAME}.asmdef" << 'EOF'
{
    "name": "FEATURE_NAME",
    "rootNamespace": "Project.Features.FEATURE_NAME",
    "references": [
        "Unity.XR.Interaction.Toolkit",
        "Unity.InputSystem"
    ],
    "includePlatforms": [],
    "excludePlatforms": [],
    "allowUnsafeCode": false,
    "overrideReferences": false,
    "precompiledReferences": [],
    "autoReferenced": true,
    "defineConstraints": [],
    "versionDefines": [],
    "noEngineReferences": false
}
EOF

echo "✅ Assembly definition created!"
```

## 4. Next Steps

After running the scaffold:
1. Rename the `NewVRFeature` folder from within Unity to match your feature name
2. Update the assembly definition name if created
3. Start implementing your feature scripts in the `Scripts` folder