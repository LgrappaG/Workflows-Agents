---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - godot-animation-setup
  - ai-debugging-tools
  - ci-cd-pipeline-setup
  - godot-setup
  - graphics-hdrp-setup
  - ui-performance-optimization
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - data-pipeline-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - automated-testing-framework
  - ui-docking-windows
  - ui-drag-drop
  - ui-event-handlers
  - ui-prefab-variants
  - ui-responsive-design
  - build-system-optimization
  - custom-workflow-builder
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-context-menus
  - ui-dynamic-styling
  - ui-keyboard-shortcuts
  - ui-resize-scaling
  - ui-style-sheets
  - ui-touch-input
  - ui-transition-timing
  - ui-two-way-binding
  - compatibility-testing
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  - material-visual-debugging
  - networking-guild-system
  - physics-fluid-dynamics
  - terrain-performance-tuning
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  recommended:
  - ui-scrolling-behavior
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - ai-perception-system
  - material-performance-profiling
  - physics-constraint-optimization
  - physics-performance-metrics
  - ai-learning-adaptation
  - animation-constraint-rigging
  - debug-performance-charts
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-joint-constraints
  - terrain-cave-systems
  - terrain-path-carving
  - advanced-performance-tuning
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-performance-profiling
  - audio-ducking-sidechains
  - audio-performance-profiling
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - csharp-performance-optimization
  - debug-performance-metrics
  - debug-performance-profiler
  - material-mipmap-chains
  - networking-analytics-tracking
  - networking-lobby-system
  - networking-performance-monitoring
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-hair-dynamics
  - physics-performance-profiling
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
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-physics-colliders
  - terrain-procedural-generation
  optional:
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
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
skill_density: 137.0
estimated_skills_needed: 137
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Assets Bundle Strategy & Addressable Assets

Organize assets into bundles for on-demand loading, reducing initial download and memory footprint.

## Prerequisites

- Addressable Assets package installed
- 1-2 weeks for organization and validation

// turbo-all

## Phase 1: Install Addressable Assets

```bash
Window → Package Manager → Addressables
Install: Addressable Assets System
```

## Phase 2: Design Bundle Strategy

```markdown
Recommended structure:

**Bundle 1: Core (Always)**
- UI prefabs, fonts, main menu assets
- Size: 30-50MB
- Load on startup

**Bundle 2: Levels (Per-Level)**
- Level 1: 20MB, Level 2: 25MB, etc.
- Load when level selected
- Unload when complete

**Bundle 3: Characters**
- Player skins: 5-10MB each
- Load on demand

**Bundle 4: Cosmetics (Optional)**
- Player skins, emotes
- Load only if purchased

**Total:** Modular, reduces startup time
```

## Phase 3: Create Addressable Groups

```plaintext
Window → Addressables → Groups
1. Create new group: "Core"
2. Drag prefabs/assets into group
3. Set address: "ui/main_menu"
4. Repeat for each bundle

Advanced options:
- Compression: Enable LZ4
- Load path: Remote delivery URL (for CDN)
```

## Phase 4: Load Assets In-Game

```csharp
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;

public class AssetLoader : MonoBehaviour {
    public async void LoadLevel(string levelName) {
        var handle = Addressables.InstantiateAsync($"levels/{levelName}");
        await handle.Task;

        if (handle.Status == AsyncOperationStatus.Succeeded) {
            var levelInstance = handle.Result;
            Debug.Log("Level loaded!");
        }
    }

    public void UnloadAsset(AsyncOperationHandle handle) {
        Addressables.Release(handle);
    }
}
```

## Phase 5: Remote Delivery Setup (Optional)

```plaintext
For large bundles, host remotely:

1. Build Addressables to custom path
2. Upload to CDN (CloudFlare, AWS, Bunny)
3. Set Load Path in Addressables settings:
   - Profile: Remote URL
   - URL: https://cdn.game.com/addressables/

4. Game downloads on-demand from CDN
```

## Phase 6: Testing & Validation

```plaintext
- [ ] All bundles load without errors
- [ ] Memory freed after unload
- [ ] Initial download < 100MB
- [ ] On-demand bundle download <10 seconds
- [ ] No duplicate assets across bundles
```

## Verification

- [ ] Addressables window shows all groups
- [ ] Build Report shows bundle sizes
- [ ] Remote loading works (if used)
- [ ] Analytics track bundle download times

## Related Topics

- See `/build-size-optimization` for total size management
- Refer to `/memory-profiler-advanced` for memory monitoring