---
version: 9.0.0
category: Performance
agent: Profiling Specialist
difficulty: advanced
estimated_time: 3-6 hours
skills:
  required:
  - material-performance-profiling
  - debug-performance-profiler
  - ui-performance-optimization
  - terrain-performance-tuning
  - timeline-performance-profiling
  - audio-performance-profiling
  - physics-performance-metrics
  - physics-performance-profiling
  - animation-performance-profiling
  - debug-performance-charts
  - advanced-performance-tuning
  - csharp-performance-optimization
  - graphics-gpu-profiling
  - networking-performance-monitoring
  - performance-dashboard
  - performance-profiling-cross-engine
  - graphics-shader-compiler
  - debug-performance-metrics
  - graphics-frame-debugger
  - graphics-shadow-optimization
  - graphics-bloom-effect
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-memory-profiling
  - graphics-probe-placement
  - graphics-reflection-probes
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-light-baking
  - graphics-realtime-gi
  - physics-constraint-optimization
  - terrain-blending-shaders
  - terrain-shadow-caching
  - automated-testing-framework
  - compatibility-testing
  - custom-workflow-builder
  - graphics-culling-strategies
  - graphics-geometry-optimization
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - graphics-urp-setup
  - ai-debugging-tools
  - build-system-optimization
  - material-mipmap-chains
  - material-specular-workflow
  - terrain-normal-generation
  - ui-prefab-variants
  - ui-text-binding
  - ui-two-way-binding
  - audio-ducking-sidechains
  - csharp-chain-of-responsibility
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - terrain-advanced-editing
  - terrain-cave-systems
  - terrain-erosion-simulation
  - terrain-lightmap-generation
  - terrain-multi-layer-textures
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-shape-tools
  - terrain-water-integration
  - ui-context-menus
  - ui-hierarchy-panel
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-panel-layout
  recommended:
  - ui-touch-input
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
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - material-disney-workflow
  - material-metallic-workflow
  - material-uv-mapping
  - networking-guild-system
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-terrain-deformation
  - terrain-biome-definition
  - terrain-brush-settings
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-neighbor-blending
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-wind-zones
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-input-validation
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-theme-switching
  - ui-tooltips
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  optional:
  - vfx-builtin-particles
  - vfx-trail-rendering
  - material-triplanar-mapping
  - vfx-shader-graph-advanced
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
skill_density: 153.0
estimated_skills_needed: 153
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Shader Optimization Guide

Optimize shaders to reduce GPU time, power consumption, and heat on mobile/VR devices.

## Prerequisites

- Shader knowledge (basics)
- Target platform profiling data
- 1 week for optimization

// turbo-all

## Phase 1: Identify Expensive Shaders

```csharp
// Use Unity Profiler: Window → Analysis → Profiler
// Monitor: GPU time, Draw Calls, Batches
// Identify shaders taking >5ms per frame
```

## Phase 2: Common Optimization Techniques

1. **Reduce Per-Pixel Computation:**
   ```glsl
   // BEFORE: Expensive per-pixel calculation
   float4 frag(v2f i) : SV_Target {
       float3 normalMap = normalize(tex2D(_NormalMap, i.uv));
       float3 worldNormal = mul(normalMap, i.tangentToWorld);
       float3 finalNormal = UnpackNormal(worldNormal);
       // ... complex lighting math ...
       return float4(finalNormal * lighting, 1.0);
   }

   // AFTER: Baked normal maps, simpler math
   float4 frag(v2f i) : SV_Target {
       float3 baked = tex2D(_BakedNormal, i.uv).rgb;
       return float4(baked, 1.0);
   }
   ```

2. **Use Mipmap Chains:**
   ```plaintext
   - Enable Mipmaps on all textures
   - Reduces cache misses, improves performance
   - Costs 33% more memory; worth it
   ```

3. **Reduce Texture Lookups:**
   ```glsl
   // Mobile: Limit to 2-3 texture samples max
   // VR: Limit to 1-2 texture samples max

   // BEFORE: 5 texture lookups
   float4 frag(v2f i) : SV_Target {
       float4 col1 = tex2D(_Tex1, i.uv);
       float4 col2 = tex2D(_Tex2, i.uv);
       float4 col3 = tex2D(_Tex3, i.uv);
       float4 col4 = tex2D(_Tex4, i.uv);
       float4 col5 = tex2D(_Tex5, i.uv);
       return col1 + col2 + col3 + col4 + col5;
   }

   // AFTER: PackedTexture technique
   float4 frag(v2f i) : SV_Target {
       float4 packed = tex2D(_PackedTexture, i.uv); // RGBA contains all
       return packed;
   }
   ```

4. **Prefer Vertex Shader Computation:**
   ```glsl
   // Move expensive calculations from fragment to vertex shader
   // Vertex shader runs once per vertex, fragment shader runs per pixel
   // Mobile has ~4 pixels per vertex; savings: 4x reduction
   ```

## Phase 3: Mobile-Specific Optimizations

1. **Avoid Expensive Operations:**
   ```plaintext
   AVOID on mobile:
   - Division (use multiplication by reciprocal instead)
   - Pow() function (use approximation)
   - sqrt() and normalize() (precompute if possible)
   - Complex trigonometry (sin, cos, tan - use lookup tables)

   PREFER:
   - Integer operations
   - Lookups in precomputed textures
   - SIMD operations (available on modern GPUs)
   ```

2. **Reduce Precision Where Possible:**
   ```glsl
   // Use lowp (16-bit) for color, uv coordinates
   // Use mediump (16-bit) for intermediate calculations
   // Use highp (32-bit) only for critical calculations

   varying lowp vec4 vColor;
   varying mediump vec2 vUV;
   varying highp float vDepth;
   ```

## Phase 4: VR-Specific Optimizations

1. **Shadow Optimization:**
   ```plaintext
   VR Impact Analysis:
   - Realtime shadows: 20-30% GPU time
   - Solution: Use baked shadow maps + dynamic light 1-2 lights max
   ```

2. **Post-Processing:**
   ```plaintext
   Each post-process effect costs 0.5-2ms:
   - Bloom: 1ms
   - Depth of Field: 2ms
   - Screen Space Reflections: 3ms

   For VR 90 FPS: Budget only 1-2 effects max
   ```

## Phase 5: Profiling & Validation

```csharp
// Create profiling shader
#if UNITY_EDITOR
void ProfileShaders() {
    // Render scene with each shader variant
    // Measure GPU time
    // Log results
}
#endif
```

## Verification Checklist

- [ ] GPU profiling shows <5ms shader time
- [ ] Mobile shader uses 2-3 textures max
- [ ] VR shader uses 1-2 textures
- [ ] No expensive operations (division, pow, sqrt per pixel)
- [ ] Lowp precision used for colors
- [ ] Shader variants stripped for target platform

## Todo: Shader Optimization

- [ ] Profile each shader with Profiler
- [ ] Identify 3 most expensive shaders
- [ ] Reduce texture samples
- [ ] Move vertex calculations where possible
- [ ] Test on target device

## Related Topics

- See `/build-size-optimization` for shader compilation size
- Refer to `/memory-profiler-advanced` for VRAM optimization
- Check `/performance-audits` for GPU bottleneck identification