---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - graphics-lightmap-setup
  - graphics-hdrp-setup
  - graphics-urp-setup
  - physics-hair-dynamics
  - graphics-dynamic-lighting
  - graphics-light-baking
  - graphics-probe-placement
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - physics-constraint-optimization
  - physics-joint-constraints
  - physics-terrain-deformation
  - graphics-bloom-effect
  - graphics-geometry-optimization
  - graphics-motion-blur
  - graphics-realtime-gi
  - physics-chain-dynamics
  - terrain-physics-colliders
  - audio-ducking-sidechains
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-frame-debugger
  - graphics-gpu-profiling
  - graphics-memory-profiling
  - graphics-postprocessing
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-temporal-antialiasing
  - terrain-performance-tuning
  - audio-mixer-setup
  - physics-performance-metrics
  - physics-performance-profiling
  - physics-vehicle-setup
  - ui-performance-optimization
  - terrain-lightmap-generation
  - audio-performance-profiling
  - physics-fluid-dynamics
  - ai-debugging-tools
  - cinemachine-virtual-camera
  - terrain-shape-tools
  - ai-learning-adaptation
  - ai-perception-system
  - ai-threat-assessment
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-dynamic-modification
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - ai-crowd-simulation
  - ai-environmental-awareness
  - animation-constraint-rigging
  - cinemachine-aim-assist
  - csharp-chain-of-responsibility
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-detail-meshes
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightmap-import
  - terrain-lod-optimization
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-streaming
  - terrain-wind-zones
  - ai-behavior-switching
  - ai-communication-network
  - ai-formation-control
  - ai-squad-tactics
  - csharp-async-await
  - custom-workflow-builder
  - godot-animation-setup
  - material-mipmap-chains
  - material-pbr-setup
  - networking-server-maintenance
  - physics-collision-callbacks
  - terrain-cliff-generation
  - terrain-heightfield-editing
  - terrain-layer-management
  - terrain-memory-management
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-texture-painting
  - terrain-transition-zones
  - timeline-camera-transitions
  - training-datasets
  - vfx-trail-rendering
  - animation-humanoid-setup
  - audio-spatial-3d
  - navmesh-baking-setup
  recommended:
  - physics-explosion-forces
  - physics-solver-configuration
  - physics-trigger-callbacks
  - physics-trigger-volumes
  - ui-event-handlers
  - ui-focus-navigation
  - ui-prefab-variants
  - ui-text-binding
  - ui-touch-input
  - audio-compression-codecs
  - audio-dialogue-system
  - audio-dynamic-music
  - audio-multi-output-routing
  - audio-streaming-audio
  - debug-performance-charts
  - networking-ngo-setup
  - physics-angular-momentum
  - physics-buoyancy
  - physics-debug-visualization
  - physics-force-fields
  - physics-layer-masking
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-ragdoll-physics
  - physics-rope-simulation
  - physics-spring-dynamics
  - physics-time-scaling
  - physics-vehicle-wheels
  - ui-anchor-positioning
  - ui-context-menus
  - ui-dynamic-styling
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-panel-layout
  - ui-two-way-binding
  - vfx-builtin-particles
  - advanced-performance-tuning
  - animation-baking-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - animation-performance-profiling
  - audio-adaptive-bitrate
  - audio-ambient-soundscapes
  - audio-ambisonics-support
  - audio-attenuation-curves
  - audio-binaural-rendering
  - audio-effects-compression
  - audio-effects-distortion
  - audio-effects-eq
  - audio-effects-pitch-shift
  - audio-effects-reverb
  - audio-effects-time-stretch
  - audio-environmental-acoustics
  - audio-fmod-integration
  - audio-footstep-generation
  - audio-frequency-analysis
  - audio-headphone-optimization
  - audio-impact-sounds
  - audio-object-pooling
  - audio-parameter-automation
  - audio-platform-specific-codecs
  - audio-prioritization-system
  - audio-procedural-generation
  - audio-voice-chat
  - build-system-optimization
  - ci-cd-pipeline-setup
  - csharp-builder-pattern
  - csharp-performance-optimization
  - data-pipeline-setup
  - debug-build-diagnostic
  - debug-performance-metrics
  - debug-performance-profiler
  - debug-physics-debugger
  - engine-migration-guide
  - godot-physics-system
  - godot-setup
  - machine-learning-setup
  - material-performance-profiling
  - material-physics-interactions
  - material-specular-workflow
  - material-translucency-setup
  - networking-guild-system
  - networking-performance-monitoring
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-aerodynamics
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-continuous-collision
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-friction-models
  - physics-inertia-calculation
  - physics-particle-collisions
  - physics-rolling-resistance
  - physics-suspension-tuning
  - physics-water-waves
  - timeline-audio-sync
  optional:
  - timeline-performance-profiling
  - ui-accessibility
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
complexity_score: 5.0
skill_density: 41.0
estimated_skills_needed: 205
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# /unity-3d-setup

Bootstrap a Unity 3D project with the full production stack: URP pipeline, PBR materials, baked lighting, NavMesh, Cinemachine, Animator, and LOD system. Uses `@unity-3d-expert` for all 3D-specific decisions.

---

## Prerequisites

- Unity 6 LTS with URP template (or URP manually installed)
- Target platform decided: Mobile (URP, low-end) vs PC (URP high-end) vs PC ultra (HDRP)

---

## Steps

### Step 1: Package Installation

Open `Window → Package Manager` and install:

```
✅ Universal RP (URP)                  ← for most projects
✅ Cinemachine
✅ AI Navigation (NavMesh)             ← replaces built-in NavMesh
✅ Input System
✅ ProBuilder (optional, for geometry)
✅ Terrain Tools (optional, for open world)
```

> For photorealistic PC/console: use **HDRP** instead of URP. Activate `@unity-3d-expert` to evaluate.

---

### Step 2: URP Asset Configuration

Open `UniversalRenderPipelineAsset` (in `Assets/Settings/`):

**Mobile (Quest, Android, iOS):**
- Main Light: `Per Pixel`
- Additional Lights: `Off`
- Shadow Distance: `20`
- Cascade Count: `2`
- HDR: `Off`

**PC (mid-range target):**
- Main Light: `Per Pixel`
- Additional Lights: `Per Pixel`, max `4`
- Shadow Distance: `100`
- Cascade Count: `4`
- HDR: `On`
- MSAA: `2x` or `4x`

Activate `@unity-3d-expert` for URP asset tuning per platform.

---

### Step 3: Lighting Setup

1. Open `Window → Rendering → Lighting`

2. **Mixed Lighting** (recommended for most 3D games):
   - Lighting Mode: `Shadowmask`
   - Directional Light Mode: `Mixed`

3. **Lightmap settings (URP)**:
   - Lightmapper: `Progressive GPU`
   - Lightmap Resolution: `20` (hero assets), `5` (background)
   - Max Lightmap Size: `1024` (mobile), `2048` (PC)

4. Mark all static geometry as **Static** (`Contribute GI`)

5. Add **Light Probe Group** for dynamic character areas

6. Click **Generate Lighting** — bake before profiling

---

### Step 4: Physics Configuration

`Edit → Project Settings → Physics`:
- Layer Collision Matrix: disable Player ↔ Player, Enemy ↔ Enemy
- Solver Type: `Temporal Gauss Seidel` (Unity 6 default — better stability)
- Default Max Angular Speed: `7` (prevents spinning physics objects)
- Default Solver Iterations: `6` (default), increase to `8` for precision

---

### Step 5: NavMesh Setup (AI Navigation Package)

1. Add `NavMesh Surface` component to your level/terrain
2. Set **Agent Type**: Humanoid (`Radius: 0.4`, `Height: 2.0`, `Step Height: 0.4`)
3. Click **Bake** — inspect NavMesh overlay in Scene view
4. For dynamic obstacles: add `NavMesh Obstacle` (Carve mode) to moving blockers

```
Activate @unity-3d-expert for:
- Complex multi-floor NavMesh (OffMeshLinks)
- NavMesh for non-humanoid agents
- Runtime NavMesh baking (procedural levels)
```

---

### Step 6: Cinemachine Camera

1. `GameObject → Cinemachine → Virtual Camera`

**Third-person follow camera:**
- Body: `Cinemachine 3rd Person Follow`
  - Shoulder Offset: `(0.5, 0.4, 0)`
  - Camera Distance: `4`
- Aim: `Cinemachine POV` or `Composer`

**Add camera collision:**
- `CinemachineCollider` extension
  - Strategy: `Pull Camera Forward`
  - Collision Filter: `Default` layer

2. Add `CinemachineImpulseSource` to shake sources (explosions, footsteps)
3. Add `CinemachineImpulseListener` to the Virtual Camera

---

### Step 7: Animator & Blend Tree

1. Create `AnimatorController` asset in `Assets/Animation/`
2. Set up **Base Layer**:
   - Idle state (default)
   - Locomotion **Blend Tree** (1D: Speed → Idle/Walk/Run)
   - Jump state with `Has Exit Time: Off`, `Transition Duration: 0.1`
3. Add **Additive Layer** (weight: 1) for upper body (aiming, talking)
   - Assign **Avatar Mask** (Upper Body)

```
Activate @unity-3d-expert for:
- 8-directional 2D blend trees
- IK setup (aim, look-at, foot placement)
- Animator Override Controllers for character variants
```

---

### Step 8: LOD Group — Standard Setup

For every significant mesh:
1. Name sub-meshes: `MeshName_LOD0`, `MeshName_LOD1`, `MeshName_LOD2`
2. Add `LOD Group` component to root
3. Use **Tools → Setup LOD Groups** (from `@unity-3d-expert` patterns if Editor utility added)
4. Thresholds: `50% → 15% → 2% → Culled`

---

### Step 9: Folder Structure

```
Assets/
├── Art/
│   ├── Materials/
│   ├── Models/        ← FBX files
│   ├── Textures/      ← Albedo, Normal, Metallic maps
│   └── VFX/
├── Audio/
│   ├── Music/
│   └── SFX/
├── Prefabs/
│   ├── Characters/
│   ├── Environment/
│   └── Systems/
├── Scenes/
├── Scripts/
│   ├── AI/
│   ├── Camera/
│   ├── Characters/
│   ├── Systems/
│   └── UI/
├── Settings/          ← URP Asset, Input Actions, NavMesh Agents
└── Animation/         ← Animator Controllers, Avatar Masks, Clips
```

---

### Step 10: Verify with @unity-3d-expert

```
Activate @unity-3d-expert to verify:
- Draw calls within budget (Stats window)
- No real-time-only lights on static geometry
- NavMesh correctly baked (no islands, no gaps)
- LOD Groups functioning (gizmo view in Scene)
- Character controller clips correctly (no wall-clipping at speed)
```

Then run `/unity-performance-audit` to baseline the project before adding gameplay.