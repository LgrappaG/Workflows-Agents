---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - physics-performance-metrics
  - physics-performance-profiling
  - ui-performance-optimization
  - audio-performance-profiling
  - physics-constraint-optimization
  - terrain-performance-tuning
  - graphics-frame-debugger
  - graphics-shadow-optimization
  - debug-performance-charts
  - debug-performance-profiler
  - graphics-sorting-layers
  - material-performance-profiling
  - networking-performance-monitoring
  - advanced-performance-tuning
  - animation-performance-profiling
  - csharp-performance-optimization
  - graphics-batching-optimization
  - graphics-depth-of-field
  - graphics-gpu-profiling
  - graphics-memory-profiling
  - graphics-shader-compiler
  - performance-profiling-cross-engine
  - physics-hair-dynamics
  - physics-joint-constraints
  - timeline-performance-profiling
  - debug-performance-metrics
  - graphics-ambient-occlusion
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-dynamic-lighting
  - graphics-geometry-optimization
  - graphics-hdrp-setup
  - graphics-light-baking
  - graphics-lightmap-setup
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-temporal-antialiasing
  - graphics-urp-setup
  - performance-dashboard
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-terrain-deformation
  - terrain-physics-colliders
  - physics-time-scaling
  - ai-debugging-tools
  - audio-ducking-sidechains
  - physics-buoyancy
  - physics-collision-callbacks
  - physics-debug-visualization
  - physics-force-fields
  - physics-layer-masking
  - physics-object-pooling
  - physics-solver-configuration
  - physics-spring-dynamics
  - physics-trigger-callbacks
  - debug-physics-debugger
  - godot-physics-system
  - material-physics-interactions
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-continuous-collision
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-friction-models
  - physics-inertia-calculation
  - physics-networked-synchronization
  - physics-particle-collisions
  - physics-ragdoll-physics
  - physics-rolling-resistance
  - physics-rope-simulation
  - physics-suspension-tuning
  - physics-trigger-volumes
  - physics-vehicle-setup
  - physics-vehicle-wheels
  - physics-water-waves
  - unreal-physics
  - audio-compression-codecs
  - audio-effects-compression
  - audio-effects-eq
  - audio-multi-output-routing
  - debug-shader-debugging
  - material-mipmap-chains
  - terrain-blending-shaders
  - terrain-memory-management
  - terrain-multi-layer-textures
  - ui-touch-input
  recommended:
  - ai-perception-system
  - audio-binaural-rendering
  - audio-dialogue-system
  - audio-effects-distortion
  - audio-effects-reverb
  - audio-footstep-generation
  - audio-frequency-analysis
  - audio-object-pooling
  - audio-parameter-automation
  - audio-procedural-generation
  - audio-streaming-audio
  - build-system-optimization
  - csharp-chain-of-responsibility
  - debug-renderer-debugging
  - terrain-biome-definition
  - terrain-brush-settings
  - terrain-lightmap-generation
  - terrain-normal-generation
  - terrain-shadow-caching
  - terrain-splat-mapping
  - terrain-wind-zones
  - ui-animation-states
  - ui-context-menus
  - ui-event-handlers
  - ui-keyboard-shortcuts
  - ui-style-sheets
  - ui-transition-timing
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-adaptive-bitrate
  - audio-ambient-soundscapes
  - audio-ambisonics-support
  - audio-attenuation-curves
  - audio-dynamic-music
  - audio-effects-pitch-shift
  - audio-effects-time-stretch
  - audio-environmental-acoustics
  - audio-fmod-integration
  - audio-headphone-optimization
  - audio-impact-sounds
  - audio-mixer-setup
  - audio-platform-specific-codecs
  - audio-prioritization-system
  - audio-spatial-3d
  - audio-voice-chat
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - csharp-async-await
  - csharp-builder-pattern
  - custom-workflow-builder
  - debug-build-diagnostic
  - debug-script-debugging
  - engine-migration-guide
  - material-visual-debugging
  - networking-guild-system
  - networking-server-maintenance
  - terrain-advanced-editing
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lod-optimization
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-procedural-generation
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - timeline-audio-sync
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  optional:
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
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
- performance-engineer
complexity_score: 10
skill_density: 27.57
estimated_skills_needed: 193
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Mobile Optimization Audit

Comprehensive audit of your project for mobile and Quest standalone performance using `@mobile-expert` and `@profiling-specialist`.

## 1. Specify Target Devices

Tell the agent your target platforms:
- "Audit for Quest 2 and Quest 3"
- "Check mobile performance for mid-range Android"
- "Optimize for iPhone 12 and above"

## 2. Device Tier Analysis (Agent Action)

The agent categorizes target devices:

| Tier | Devices | GPU Budget | Memory |
|------|---------|------------|--------|
| High | Quest 3, iPhone 15, Galaxy S24 | 8ms | 6GB+ |
| Mid | Quest 2, iPhone 12, Galaxy A54 | 10ms | 4GB |
| Low | Quest 1, iPhone X, Galaxy A32 | 12ms | 2GB |

## 3. Performance Capture

// turbo
```bash
echo "=== Mobile Performance Audit ==="
echo "Date: $(date '+%Y-%m-%d')"
echo ""
echo "Project Settings Check:"
cat ProjectSettings/ProjectSettings.asset 2>/dev/null | grep -E "targetDevice|graphicsJobs|prebakeCollision" | head -10
echo ""
echo "Quality Settings:"
cat ProjectSettings/QualitySettings.asset 2>/dev/null | head -30
```

## 4. Audit Categories

### A. Rendering Budget

| Check | Quest 2 Target | Quest 3 Target |
|-------|----------------|----------------|
| Draw calls | < 100 | < 150 |
| Triangles | < 500K | < 750K |
| Texture memory | < 512MB | < 1GB |
| Shader complexity | Mobile/URP | URP Lit |

### B. CPU Budget

| Check | Target |
|-------|--------|
| Frame time (scripts) | < 4ms |
| Physics | < 2ms |
| Animation | < 1ms |
| Total | < 11ms (90fps) |

### C. Memory Budget

| Category | Quest 2 | Quest 3 |
|----------|---------|---------|
| Total app | < 2GB | < 3GB |
| Textures | < 512MB | < 1GB |
| Meshes | < 256MB | < 512MB |
| Audio | < 64MB | < 128MB |

### D. Thermal Management

- [ ] No sustained high CPU/GPU usage
- [ ] Frame rate stable after 30 minutes
- [ ] Battery drain acceptable for session length

## 5. Common Issues to Flag

The agent checks for:

```markdown
### 🔴 Critical
- [ ] Realtime shadows on mobile (bake instead)
- [ ] Uncompressed textures > 2K
- [ ] Complex shaders (Standard shader on Quest)
- [ ] No LOD groups on detailed meshes

### 🟡 Important
- [ ] Missing texture compression (ASTC)
- [ ] Audio not compressed (use Vorbis)
- [ ] Unused assets in build
- [ ] Physics layers not optimized

### 🔵 Minor
- [ ] Quality settings not tiered
- [ ] Missing application focus handling
- [ ] No thermal throttling response
```

## 6. Generate Audit Report

// turbo
```bash
cat > mobile-audit-report.md << 'EOF'
# Mobile Performance Audit Report

Generated: $(date '+%Y-%m-%d')

## Target Devices
(Agent fills in)

## Current Performance
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Frame rate | | 72fps | |
| Draw calls | | <100 | |
| Memory | | <2GB | |

## Issues Found

### 🔴 Critical
(Agent fills in)

### 🟡 Important
(Agent fills in)

### 🔵 Minor
(Agent fills in)

## Recommended Actions
(Prioritized list)

## Estimated Impact
(Performance gain from fixes)
EOF

echo "✅ Audit report created: mobile-audit-report.md"
```

## 7. Apply Optimizations

After review, instruct the agent:
- "Fix all critical mobile issues"
- "Apply texture compression to all assets"
- "Set up quality tiers for Quest 2/3"

## Example Commands

- "Audit my project for Quest 2 standalone"
- "Check if my game will run on mid-range Android"
- "Find thermal throttling issues"
- "Optimize textures for mobile"