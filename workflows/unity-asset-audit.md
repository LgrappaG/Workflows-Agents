---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - ui-performance-optimization
  - terrain-performance-tuning
  - debug-performance-profiler
  - material-performance-profiling
  - physics-performance-metrics
  - advanced-performance-tuning
  - csharp-performance-optimization
  - debug-performance-charts
  - networking-performance-monitoring
  - timeline-performance-profiling
  - physics-constraint-optimization
  - animation-performance-profiling
  - audio-performance-profiling
  - custom-workflow-builder
  - debug-performance-metrics
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-performance-profiling
  - graphics-shadow-optimization
  - ai-debugging-tools
  - graphics-frame-debugger
  - graphics-gpu-profiling
  - graphics-sorting-layers
  - material-mipmap-chains
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-heightmap-import
  - terrain-shape-tools
  - terrain-streaming
  - terrain-water-integration
  - ui-animation-states
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-prefab-variants
  - ui-responsive-design
  - ui-style-sheets
  - ui-transition-timing
  - debug-asset-dependencies
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
  - build-system-optimization
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - engine-migration-guide
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  recommended:
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-geometry-optimization
  - graphics-hdrp-setup
  - graphics-light-baking
  - graphics-lightmap-setup
  - graphics-memory-profiling
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-temporal-antialiasing
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - networking-guild-system
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-cave-systems
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
  - terrain-normal-generation
  - terrain-path-carving
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
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-tweens
  optional:
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-focus-navigation
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: code-reviewer
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 25.6
estimated_skills_needed: 128
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Asset Audit (AI-Led)

This workflow uses MCP to scan the Project window and identify assets that might be hurting performance (especially on Meta Quest).

## 1. Discover Large Textures (Agent Action)

The agent scans the `Assets/` directory for `.png`, `.jpg`, and `.tga` files.

// turbo
```bash
# Agent uses find_by_name or mcp search tools
```

## 2. Inspect Import Settings

For each large texture, the agent checks:
- **Max Size**: Is it > 1024 on Quest?
- **Compression**: Is it using ASTC/ETC2?
- **Mip Maps**: Are they enabled for 3D textures?

## 3. High-DPI Audit

The agent lists all assets above a certain file size (e.g., > 10MB) and asks:
> "This 4K texture `Skybox_SuperHighRes.png` is 50MB. Should we downscale it to 1024 for the Quest build?"

## 4. Unused Asset Detection (Heuristic)

The agent cross-references the current scene's hierarchy with the AssetDatabase to identify assets that are not currently being used.

## 5. Optimization Report

The agent produces a `asset-optimization-plan.md` with:
- [ ] 🔴 Critical: Textures with no compression
- [ ] 🟡 Major: Overly large UI textures
- [ ] 🔵 Minor: Missing Mip Maps on 3D props