---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: advanced
estimated_time: 3-6 hours
skills:
  required:
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - animation-mocap-setup
  - godot-animation-setup
  - animation-mirror-setup
  - audio-mixer-setup
  - ci-cd-pipeline-setup
  - custom-workflow-builder
  - data-pipeline-setup
  - godot-setup
  - material-pbr-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - machine-learning-setup
  - material-translucency-setup
  - ui-event-handlers
  - ui-touch-input
  - ui-context-menus
  - build-system-optimization
  - ui-anchor-positioning
  - ui-focus-navigation
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-panel-layout
  - ui-prefab-variants
  - ui-style-sheets
  - ui-two-way-binding
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - networking-guild-system
  - physics-fluid-dynamics
  - ui-accessibility
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-list-repeater
  - ui-list-virtualization
  - ui-overflow-handling
  - ui-performance-optimization
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  recommended:
  - cinemachine-virtual-camera
  - graphics-motion-blur
  - physics-joint-constraints
  - terrain-brush-settings
  - terrain-heightmap-import
  - terrain-path-carving
  - ai-debugging-tools
  - ai-learning-adaptation
  - animation-constraint-rigging
  - cinemachine-aim-assist
  - material-mipmap-chains
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-cave-systems
  - terrain-grass-placement
  - terrain-physics-colliders
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - timeline-control-rig
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - csharp-async-await
  - csharp-chain-of-responsibility
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
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  optional:
  - terrain-heightfield-editing
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
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
skill_density: 16.88
estimated_skills_needed: 135
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity XR/AR Setup Workflow

This workflow will guide you through setting up a basic Unity project for XR (VR/AR) development using the XR Interaction Toolkit and AR Foundation.

## 1. Install Unity Editor and Modules
Ensure you have the right modules installed from Unity Hub:
- **Android Build Support** (with OpenJDK, Android SDK & NDK Tools) - For Meta Quest / ARCore
- **iOS Build Support** - For Apple Vision / ARKit
- **Universal Windows Platform Build Support** - For HoloLens

## 2. Create a New Project
Create a new project using the **3D (URP)** or **3D Core** template (URP is highly recommended for XR).

## 3. Install XR Packages
Open the Package Manager (Window > Package Manager), switch to "Unity Registry", and install:
- **XR Plugin Management**: The core manager for XR loaders.
- **XR Interaction Toolkit (XRI)**: Provides interactions like grab, hover, and locomotion.
- **AR Foundation**: (Optional if VR only) Required for AR features.
- **OpenXR Plugin**: Recommended for broad device compatibility.

## 4. Import XR Interaction Toolkit Starter Assets
After installing XRI, in the Package Manager under XR Interaction Toolkit, expand the "Samples" section and import **Starter Assets**. This gives you pre-built controllers and input actions.

## 5. Configure XR Plugin Management
1. Go to **Edit > Project Settings > XR Plugin Management**.
2. For PC (Stand-alone): Check **OpenXR**.
3. For Android (Quest/ARCore): Check **OpenXR** (and/or Oculus if specifically using Oculus legacy).
4. For iOS: Check **Apple ARKit**.

## 6. Setup the Scene
1. Delete the default Main Camera.
2. Right-click in Hierarchy: **XR > XR Origin (VR)** or **XR Origin (AR)** depending on your project.
3. Add an **XR Interaction Manager** to the scene (Right-click > XR > XR Interaction Manager).
4. If doing AR, also add an **AR Session** and configure the AR Camera Background on the XR Origin's camera.

## 7. Apply Interaction Profiles (OpenXR)
1. Go to **Edit > Project Settings > XR Plugin Management > OpenXR**.
2. Add Interaction Profiles for your target devices (e.g., Oculus Touch Controller Profile, Microsoft Mixed Reality Motion Controller Profile, Valve Index).

## 8. Build Settings
1. Go to **File > Build Settings**.
2. Switch to your target platform (Android / iOS / Windows).
3. If building for Android (Quest):
   - Set Texture Compression to ASTC.
   - In Player Settings > Resolution and Presentation, ensure "Start in Fullscreen Mode" is true.
   - In Player Settings > Other Settings, set Minimum API Level to the device requirement (e.g., Android 10/API 29 for Quest 2).
4. Click **Build and Run** with your device connected.