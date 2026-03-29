---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ai-debugging-tools
  - custom-workflow-builder
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
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
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - godot-animation-setup
  - godot-setup
  - graphics-ambient-occlusion
  recommended:
  - graphics-batching-optimization
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-frame-debugger
  - graphics-geometry-optimization
  - graphics-gpu-profiling
  - graphics-light-baking
  - graphics-memory-profiling
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - machine-learning-setup
  - material-mipmap-chains
  - material-pbr-setup
  - material-translucency-setup
  - material-visual-debugging
  - navmesh-baking-setup
  - networking-ngo-setup
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  optional:
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
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
skill_density: 12.83
estimated_skills_needed: 77
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


// turbo-all

# Clean Unity Project

This workflow cleans temporary folders to solve cache and broken reference issues frequently experienced in Unity projects.

**Warning:** Make sure the Unity Editor and Visual Studio / Rider are closed before running this process!

## 1. Confirm Editor is Closed

```bash
echo "⚠️  Ensure Unity Editor and IDE are closed before proceeding!"
echo "Press Ctrl+C to cancel, or wait 3 seconds to continue..."
sleep 3
```

## 2. Delete Library Folder

Unity will re-import all assets from scratch on next startup:

```bash
rm -rf Library/
echo "✅ Library folder deleted"
```

## 3. Delete Temp Folder

```bash
rm -rf Temp/
echo "✅ Temp folder deleted"
```

## 4. Delete obj Folder

Compilation artifacts:

```bash
rm -rf obj/
echo "✅ obj folder deleted"
```

## 5. Delete Logs Folder

```bash
rm -rf Logs/
echo "✅ Logs folder deleted"
```

## 6. Optional: Clear Package Cache

If having package issues:

```bash
rm -rf Library/PackageCache/
rm -f Packages/packages-lock.json
echo "✅ Package cache cleared"
```

## Done!

Cleanup complete. You can now reopen Unity.

**Note:** The initial startup will take longer than usual as Unity reimports all assets.