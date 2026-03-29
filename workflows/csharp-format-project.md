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
  - material-disney-workflow
  - material-metallic-workflow
  - ui-prefab-variants
  - ui-style-sheets
  - csharp-chain-of-responsibility
  - godot-animation-setup
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-shape-tools
  - terrain-water-integration
  - ui-event-handlers
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
  - automated-testing-framework
  - build-system-optimization
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - data-pipeline-setup
  - debug-build-diagnostic
  - engine-migration-guide
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-mipmap-chains
  - material-pbr-setup
  recommended:
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-guild-system
  - networking-ngo-setup
  - networking-server-maintenance
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
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  optional:
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
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
skill_density: 25.75
estimated_skills_needed: 103
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


// turbo-all

# C# Code Formatter (dotnet format)

When "Vibe Coding", the formatting of rapidly written C# code can sometimes become misaligned. This workflow runs the `dotnet format` command to bring all C# code in the project up to standard.

**Prerequisites:**
- .NET SDK must be installed
- A `.sln` (Solution) file must exist in your project

## 1. Check Prerequisites

```bash
# Check if dotnet is available
if ! command -v dotnet &> /dev/null; then
    echo "❌ .NET SDK not found. Please install from https://dotnet.microsoft.com/download"
    exit 1
fi

# Check for solution file
if ! ls *.sln 1> /dev/null 2>&1; then
    echo "⚠️  No .sln file found. Open Unity and select Assets > Open C# Project first."
    exit 1
fi

echo "✅ Prerequisites met"
```

## 2. Format the Code

```bash
dotnet format --verbosity normal
echo "✅ Code formatting complete!"
```

## 3. Optional: Format with Specific Rules

For stricter formatting:

```bash
# Format with analyzers
dotnet format --severity info

# Format only whitespace
dotnet format whitespace

# Format only style rules
dotnet format style
```

## 4. Verify Changes

```bash
# Show what files were modified
git status --short
echo "Review changes above. Use 'git diff' to see details."
```

## Tips

- Add an `.editorconfig` file to customize formatting rules
- Run formatting before each commit for consistency
- Consider adding to pre-commit hooks for automation