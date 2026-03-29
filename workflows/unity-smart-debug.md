---
version: 9.0.0
category: Debugging & Recovery
agent: Unity Debugger
difficulty: intermediate
estimated_time: 2-4 hours
skills:
  required:
  - ai-debugging-tools
  - debug-shader-debugging
  - material-visual-debugging
  - debug-script-debugging
  - debug-renderer-debugging
  - physics-debug-visualization
  - custom-workflow-builder
  - physics-fluid-dynamics
  - debug-physics-debugger
  - material-physics-interactions
  - physics-buoyancy
  - physics-chain-dynamics
  - physics-collision-callbacks
  - physics-constraint-optimization
  - physics-force-fields
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-layer-masking
  - physics-performance-metrics
  - physics-rope-simulation
  - physics-spring-dynamics
  - physics-time-scaling
  - physics-vehicle-setup
  - physics-vehicle-wheels
  - terrain-physics-colliders
  - ui-event-handlers
  - ui-style-sheets
  - ui-visual-feedback
  - timeline-debug-visualization
  - build-system-optimization
  - cinemachine-virtual-camera
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-stack-traces
  - engine-migration-guide
  - godot-physics-system
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - networking-guild-system
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-continuous-collision
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  recommended:
  - physics-friction-models
  - physics-inertia-calculation
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-particle-collisions
  - physics-performance-profiling
  - physics-ragdoll-physics
  - physics-rolling-resistance
  - physics-solver-configuration
  - physics-suspension-tuning
  - physics-terrain-deformation
  - physics-trigger-callbacks
  - physics-trigger-volumes
  - physics-water-waves
  - timeline-camera-transitions
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  optional:
  - ui-two-way-binding
  - ui-z-ordering
  - unreal-physics
  - vfx-builtin-particles
  - animation-frame-stepping
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- response-patterns-actionability
- mandates-clarity
primary_agent: tech-lead
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 33.67
estimated_skills_needed: 101
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Smart Debug Workflow

When working with complex XR interactions or Physics in Unity, the console logs can become cryptic. This workflow leverages the `debugging-toolkit-smart-debug` skill to instantly analyze a stack trace from the Unity console, find the related script, and propose a hotfix.

## 1. Provide the Error Log

Copy the exact error log or stack trace from your Unity Console and provide it to the agent using this workflow.

**Example Instruction for the Agent:**
"Run `/unity-smart-debug` on this error: NullReferenceException at PlayerVRController.GrabItem() (PlayerVRController.cs:142)"

## 2. Analyze the Code

The agent will use the `view_file` capabilities to automatically read the script mentioned in the Stack Trace (e.g., `PlayerVRController.cs` at line 142).

It will then cross-reference this with common Unity problems such as:
- Attempting to access an unassigned `SerializeField`.
- Calling `GetComponent` on a destroyed GameObject.
- XR Interaction Toolkit lifecycle mismatches (e.g., `SelectEnterEventArgs` missing an interactable).

## 3. Formulate and Apply the Fix

The agent will output exactly why this error happened and what needs to change.

If instructed, the agent will use the file editing tools (`replace_file_content`) to inject the fix directly into the project script. Note: After the agent finishes, Unity will auto-reload the script.