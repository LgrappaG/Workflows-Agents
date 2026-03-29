---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - material-performance-profiling
  - physics-performance-metrics
  - ui-performance-optimization
  - animation-performance-profiling
  - audio-performance-profiling
  - debug-performance-profiler
  - physics-performance-profiling
  - timeline-performance-profiling
  - terrain-performance-tuning
  - csharp-performance-optimization
  - debug-performance-metrics
  - physics-constraint-optimization
  - advanced-performance-tuning
  - ai-debugging-tools
  - custom-workflow-builder
  - debug-performance-charts
  - networking-performance-monitoring
  - performance-dashboard
  - performance-profiling-cross-engine
  - terrain-biome-definition
  - terrain-splat-mapping
  - ui-input-validation
  - graphics-gpu-profiling
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
  - build-system-optimization
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  - material-disney-workflow
  recommended:
  - material-metallic-workflow
  - material-mipmap-chains
  - material-specular-workflow
  - material-visual-debugging
  - networking-guild-system
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
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
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
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
primary_agent: code-reviewer
secondary_agents:
- production-lead
- performance-engineer
complexity_score: 10
skill_density: 25.5
estimated_skills_needed: 102
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Performance Audit (AI-Led)

This workflow uses the `PerformanceRecorder` script to gather data and the `@unity-debugger` skill to analyze it.

## 1. Ensure Equipment is Ready (Agent Action)

Check if `PerformanceRecorder` exists in the project and is active in the scene.

// turbo
```bash
# Agent uses mcp_mcp-unity_get_gameobject to find "PerformanceRecorder"
```

## 2. Gather Real-Time Data

The agent reads the serialized fields of the `PerformanceRecorder` component or parses the latest `[MCP_PERF_STAT]` log from the console.

| Metric | Current Value | Target (Quest 2) | Status |
|---|---|---|---|
| FPS | (agent fills) | 72 | |
| Memory | (agent fills) | < 512 MB | |
| Batches | (agent fills) | < 100 | |

## 3. Analyze & Recommend

The agent activates `@unity-debugger` and provides:
- **Bottleneck Identification**: Is it CPU (logic/scripts), GPU (batches/triangles), or GC (memory spikes)?
- **Actionable Fixes**: Specific scripts to optimize or textures to compress.
- **Verification Plan**: Steps to confirm the fix works.

## 4. Execute Fixes (Optional)

Using MCP `update_gameobject` or direct file edits, the agent can apply suggested optimizations (e.g., disabling real-time lights, lowering texture res).