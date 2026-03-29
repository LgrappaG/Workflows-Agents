---
version: 9.0.0
category: Performance
agent: Profiling Specialist
difficulty: advanced
estimated_time: 3-6 hours
skills:
  required:
  - ai-debugging-tools
  - audio-performance-profiling
  - ui-performance-optimization
  - terrain-performance-tuning
  - material-performance-profiling
  - physics-performance-metrics
  - debug-performance-charts
  - debug-shader-debugging
  - csharp-performance-optimization
  - debug-performance-profiler
  - networking-performance-monitoring
  - timeline-performance-profiling
  - advanced-performance-tuning
  - animation-performance-profiling
  - audio-mixer-setup
  - debug-performance-metrics
  - debug-renderer-debugging
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-performance-profiling
  - debug-script-debugging
  - material-visual-debugging
  - animation-mocap-setup
  - godot-setup
  - machine-learning-setup
  - audio-ducking-sidechains
  - ci-cd-pipeline-setup
  - custom-workflow-builder
  - data-pipeline-setup
  - godot-animation-setup
  - graphics-hdrp-setup
  - navmesh-baking-setup
  - physics-constraint-optimization
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-pbr-setup
  - material-translucency-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - audio-compression-codecs
  - audio-frequency-analysis
  - audio-streaming-audio
  - audio-dialogue-system
  - audio-multi-output-routing
  - audio-procedural-generation
  - build-system-optimization
  - material-mipmap-chains
  - material-specular-workflow
  - terrain-lightmap-generation
  - ui-context-menus
  - ui-text-binding
  - ui-two-way-binding
  - ai-learning-adaptation
  - ai-perception-system
  - animation-constraint-rigging
  - audio-effects-compression
  - audio-fmod-integration
  - audio-headphone-optimization
  - audio-parameter-automation
  - audio-spatial-3d
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - physics-joint-constraints
  - terrain-advanced-editing
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-dynamic-modification
  - terrain-heightmap-import
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-shape-tools
  - terrain-streaming
  - terrain-water-integration
  - ui-animation-states
  - ui-drag-drop
  - ui-event-handlers
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-panel-layout
  - ui-prefab-variants
  - ui-style-sheets
  - ui-z-ordering
  - material-texture-optimization
  recommended:
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-adaptive-bitrate
  - audio-ambient-soundscapes
  - audio-ambisonics-support
  - audio-attenuation-curves
  - audio-binaural-rendering
  - audio-dynamic-music
  - audio-effects-distortion
  - audio-effects-eq
  - audio-effects-pitch-shift
  - audio-effects-reverb
  - audio-effects-time-stretch
  - audio-environmental-acoustics
  - audio-footstep-generation
  - audio-impact-sounds
  - audio-object-pooling
  - audio-platform-specific-codecs
  - audio-prioritization-system
  - audio-voice-chat
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - engine-migration-guide
  - material-disney-workflow
  - material-metallic-workflow
  - networking-guild-system
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-layer-management
  - terrain-lod-optimization
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-wind-zones
  - timeline-audio-sync
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-dynamic-styling
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-visual-feedback
  - vfx-builtin-particles
  - vfx-trail-rendering
  - analytics-integration
  - csharp-string-optimization
  - graphics-shadow-optimization
  - material-format-selection
  optional:
  - networking-analytics-tracking
  - prediction-models
  - timeline-streaming-optimization
  - unreal-cpp-integration
  - vfx-shader-optimization
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: performance-engineer
secondary_agents:
- production-lead
- performance-engineer
complexity_score: 10
skill_density: 185.0
estimated_skills_needed: 185
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Build Size Optimization Workflow

Reduces game build size by 30-60% through automated analysis, asset compression, and unused code removal.

## Context

Larger builds mean slower downloads, less retained players. Target: <100MB mobile, <50MB WebGL.

// turbo-all

## Phase 1: Build Size Analysis

```bash
# Generate build report
File → Build Settings → Development Build: Enable
→ Build

# Analyze output
Unity → Window → Analysis → Build Report
# Check: Scenes, Assets, Plugins, Mono runtime size
```

## Phase 2: Asset Optimization

1. **Texture Compression:**
   ```plaintext
   For each texture in Project:
   - Set Compression: Compressed (DXT5, ASTC, ETC2)
   - Set Max Size: 1024 or 2048 (not 4096 unless necessary)
   - Disable MipMaps if not needed
   - Remove redundant textures (duplicates)
   ```

2. **Mesh Optimization:**
   ```plaintext
   Model Import Settings:
   - Enable: Optimize Mesh Data
   - Remove: Unused vertices/normals
   - Quantize: Enable (reduces precision)
   - Meshes: Combine where possible
   ```

3. **Audio Compression:**
   ```plaintext
   Audio Clips:
   - Format: Vorbis (mobile) instead of PCM
   - Quality: 80-90% (imperceptible difference)
   - Load Type: Compressed in Memory
   ```

## Phase 3: Code Stripping & Managed Plugins

1. **Enable Stripping:**
   ```plaintext
   Player Settings → Other Settings:
   - Managed Stripping Level: High
   - Strip Engine Code: Enable
   - WebGL Exceptions: Add necessary namespaces
   ```

2. **Remove Unused Plugins:**
   ```plaintext
   Assets/Plugins:
   - Remove .dll/.so files not used in game
   - Check: Unused Facebook SDK, Ads SDK, Analytics
   ```

## Phase 4: Scene Optimization

```plaintext
For each scene:
- Reduce gameobject count
- Remove editor-only elements
- Minimize lighting setup (use baked, not realtime)
- Remove debug scripts before build
```

## Phase 5: Build Asset Bundles (Advanced)

```plaintext
Create Addressable Asset Groups:
- Separate content into bundles
- Load on-demand, not at startup
- Saves boot time + initial download

Example:
- Core gameplay: 30MB (always loaded)
- Level 1-5: 20MB (loaded per level)
- Cosmetics: 15MB (optional download)
```

## Verification

- [ ] Build size <100MB (mobile) or <50MB (WebGL)
- [ ] Build Report analyzed and optimized
- [ ] No VRAM warnings in Profiler
- [ ] All textures compressed
- [ ] Audio uses Vorbis compression
- [ ] Managed Stripping enabled
- [ ] Play verified with stripped build

## Common Issues

| Issue | Solution |
|---|---|
| Build unexpectedly large | Check **Build Report** for bloat, find largest asset |
| Game crashes after stripping | Add exceptions in Player Settings → Managed Stripping |
| Texture blurry after compression | Use Crunch compression instead, higher Quality setting |

## Related Topics

- See `/assets-bundle-strategy` for advanced bundling
- Refer to `/shader-optimization-guide` for shader size
- Check `/memory-profiler-advanced` for runtime optimization