---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ui-accessibility
  - ui-performance-optimization
  - ui-style-sheets
  - ui-event-handlers
  - ui-focus-navigation
  - ui-prefab-variants
  - ui-text-binding
  - ui-animation-states
  - graphics-hdrp-setup
  - ui-anchor-positioning
  - ui-button-events
  - ui-drag-drop
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-transition-timing
  - ui-animation-tweens
  - ui-auto-layout
  - ui-dynamic-styling
  - ui-grid-layout
  - ui-mouse-interaction
  - ui-panel-layout
  - ui-responsive-design
  - ui-visual-feedback
  - ui-z-ordering
  - build-system-optimization
  - csharp-builder-pattern
  - custom-workflow-builder
  - debug-build-diagnostic
  - engine-migration-guide
  - graphics-lightmap-setup
  - graphics-urp-setup
  - networking-guild-system
  - physics-fluid-dynamics
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-form-submission
  - ui-hierarchy-panel
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-overflow-handling
  - ui-resize-scaling
  - ui-scrolling-behavior
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-two-way-binding
  - vfx-builtin-particles
  - ai-debugging-tools
  - graphics-render-queue
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - godot-animation-setup
  - graphics-ambient-occlusion
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
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  recommended:
  - graphics-temporal-antialiasing
  - terrain-performance-tuning
  - networking-server-maintenance
  - terrain-wind-zones
  - ai-perception-system
  - animation-constraint-rigging
  - animation-mirror-setup
  - animation-mocap-setup
  - material-mipmap-chains
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-chain-dynamics
  - physics-constraint-optimization
  - terrain-biome-definition
  - terrain-brush-settings
  - terrain-grass-placement
  - terrain-vegetation-placement
  - terrain-water-integration
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
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
  - godot-setup
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - material-visual-debugging
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
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
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  optional:
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - training-datasets
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
skill_density: 18.62
estimated_skills_needed: 149
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity UI Scaffold

Scaffold VR-optimized UI layouts using MCP and the `UIPalette` system for brand consistency.

## 1. Plan the Layout (Agent Action)

The agent uses `@brainstorming` to determine:
- **Interaction Type**: Gaze, Ray, or Direct Touch?
- **Hierarchy**: Main menu, HUD, or Settings panel?
- **Placement**: World-space (2m distance) or Screen-space (Overlay)?

## 2. Generate the Canvas (MCP Action)

The agent creates a new `Canvas` with an `XROrigin`-compatible `CanvasScaler`.

// turbo
```bash
# Agent uses mcp_mcp-unity_create_gameobject for "MainCanvas"
# Agent uses mcp_mcp-unity_update_component to set RenderMode to WorldSpace
echo "Canvas created with World Space render mode"
```

## 3. Apply the Visual Palette

The agent adds or updates the `UIPalette` component to ensure colors and fonts match the project standard.

// turbo
```bash
# Agent updates the UIPalette.cs fields via MCP
echo "UIPalette applied to canvas"
```

## 4. Scaffold Elements

The agent creates the UI hierarchy:

### Structure:
```
[Canvas] (World Space for VR)
    └── [Panel] (Background)
        └── [VerticalLayoutGroup] (Spacing/Padding)
            ├── [Header] (TextMeshPro)
            ├── [Button] (Interactable with TextMeshPro)
            ├── [Button] (Interactable with TextMeshPro)
            └── [Button] (Interactable with TextMeshPro)
```

### Elements to add:
- [ ] **Background Panel**: Semi-transparent dark neutral
- [ ] **Header**: TextMeshPro with Header size
- [ ] **Buttons**: VR-sized (0.3m x 0.1m) with `XRSimpleInteractable` if needed

## 5. Bind Interactions

Using MCP, the agent wires up button `OnClick` events to specific C# methods or ScriptableObject event channels.

## 6. Generate Controller Script

The agent generates a controller script for the UI:

```csharp
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class MainMenuController : MonoBehaviour
{
    [SerializeField] private Button _playButton;
    [SerializeField] private Button _settingsButton;
    [SerializeField] private Button _quitButton;

    private void Start()
    {
        _playButton.onClick.AddListener(OnPlayClicked);
        _settingsButton.onClick.AddListener(OnSettingsClicked);
        _quitButton.onClick.AddListener(OnQuitClicked);
    }

    private void OnPlayClicked() => Debug.Log("Play Clicked");
    private void OnSettingsClicked() => Debug.Log("Settings Clicked");
    private void OnQuitClicked() => Application.Quit();

    private void OnDestroy()
    {
        _playButton.onClick.RemoveListener(OnPlayClicked);
        _settingsButton.onClick.RemoveListener(OnSettingsClicked);
        _quitButton.onClick.RemoveListener(OnQuitClicked);
    }
}
```

## 7. Best Practices Applied

- Uses **TextMeshPro** for all text (crisp in VR)
- Sets up **Raycast Target** only on necessary elements to save performance
- Configures **Canvas Scaler** and **Graphic Raycaster** correctly for the target platform
- Groups elements logically for easy animation
- References `@accessibility-expert` for inclusive design considerations

## 8. Final Verification

The agent verifies:
- [ ] Canvas render mode is correct for target platform
- [ ] All buttons have proper navigation setup
- [ ] Text is readable at intended distance (VR: 0.5-3m)
- [ ] Controller script compiles without errors