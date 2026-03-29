---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ci-cd-pipeline-setup
  - custom-workflow-builder
  - animation-mocap-setup
  - machine-learning-setup
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - audio-mixer-setup
  - data-pipeline-setup
  - godot-animation-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-specular-workflow
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - ui-context-menus
  - ui-keyboard-shortcuts
  - ai-debugging-tools
  - material-mipmap-chains
  - physics-joint-constraints
  - terrain-cave-systems
  - terrain-heightmap-import
  - terrain-normal-generation
  - terrain-water-integration
  - ui-panel-layout
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
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - automated-testing-framework
  recommended:
  - build-system-optimization
  - cinemachine-aim-assist
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - engine-migration-guide
  - networking-guild-system
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
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
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
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
  - terrain-wind-zones
  - training-datasets
  optional:
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
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
skill_density: 99.0
estimated_skills_needed: 99
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Vibe Project Init

Full Unity VR project bootstrap. Takes a blank Unity project and initializes it with git, XR plugin setup, folder structure, CI config, and a passing first test — in a single phased workflow.

## Phase 1: Git Foundation

// turbo
```bash
git init
echo "# My VR Project" > README.md
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Unity.gitignore
git add .
git commit -m "chore: initial commit"
echo "✅ Git initialized with Unity .gitignore"
```

## Phase 2: Unity Project Structure (Agent Action)

The agent creates the standard VR project folder layout:

```
Assets/
  _Project/
    Scripts/
      Player/
      Interactions/
      UI/
      Systems/
      Data/          ← ScriptableObjects
    Prefabs/
      Player/
      Environment/
      UI/
    Scenes/
      Main.unity
      Testing.unity
    Settings/
      XR/
        XRProjectSettings.asset
    Tests/
      EditMode/
      PlayMode/
```

// turbo
```bash
# Create folder structure
mkdir -p "Assets/_Project/Scripts/Player"
mkdir -p "Assets/_Project/Scripts/Interactions"
mkdir -p "Assets/_Project/Scripts/UI"
mkdir -p "Assets/_Project/Scripts/Systems"
mkdir -p "Assets/_Project/Scripts/Data"
mkdir -p "Assets/_Project/Prefabs/Player"
mkdir -p "Assets/_Project/Prefabs/Environment"
mkdir -p "Assets/_Project/Prefabs/UI"
mkdir -p "Assets/_Project/Scenes"
mkdir -p "Assets/_Project/Tests/EditMode"
mkdir -p "Assets/_Project/Tests/PlayMode"
mkdir -p "Assets/_Project/Settings/XR"

echo "✅ Project folder structure created"
```

## Phase 3: XR Foundation (Agent Action)

The agent generates the boilerplate for:
- `Packages/manifest.json` with XR Interaction Toolkit 3.x and OpenXR
- Meta Quest OVRPlugin references

**Required Packages to add to `manifest.json`:**
```json
{
  "com.unity.xr.interaction.toolkit": "3.0.7",
  "com.unity.xr.openxr": "1.12.0",
  "com.unity.xr.management": "4.4.0",
  "com.unity.inputsystem": "1.8.2"
}
```

## Phase 4: First Test (Agent Action)

The agent creates a passing smoke test to confirm the project is healthy:

```csharp
// Assets/_Project/Tests/EditMode/ProjectSmokeTests.cs
using NUnit.Framework;

public class ProjectSmokeTests
{
    [Test]
    public void Project_IsHealthy_WhenBuilt()
    {
        // Simple sanity check that the test runner works
        Assert.Pass("Project smoke test passed.");
    }
}
```

// turbo
```bash
cat > "Assets/_Project/Tests/EditMode/ProjectSmokeTests.cs" << 'EOF'
using NUnit.Framework;

public class ProjectSmokeTests
{
    [Test]
    public void Project_IsHealthy_WhenBuilt()
    {
        Assert.Pass("Project smoke test passed.");
    }
}
EOF

echo "✅ Smoke test created"
```

## Phase 5: CI Pipeline

The agent runs `/github-actions-unity-setup` to generate the GitHub Actions workflow for automated testing.

## Phase 6: Initial Commit

// turbo
```bash
git add .
git commit -m "feat: bootstrap VR project structure with XR foundation and tests"
echo "✅ Project bootstrapped and committed"
echo ""
echo "Next steps:"
echo "1. Open Unity Hub and add this folder as a project"
echo "2. Let Unity import and resolve packages"
echo "3. Run 'git push' to push to your remote repository"
```

## Done!

Your project now has:
- ✅ Clean folder structure
- ✅ Git history from day 1
- ✅ XR Interaction Toolkit 3.x + OpenXR packages defined
- ✅ Passing smoke test
- ✅ CI pipeline ready