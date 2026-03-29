---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - graphics-hdrp-setup
  - custom-workflow-builder
  - graphics-lightmap-setup
  - graphics-urp-setup
  - physics-fluid-dynamics
  - animation-state-machine
  - ui-animation-states
  - ui-anchor-positioning
  - ui-event-handlers
  - ui-transition-timing
  - ui-auto-layout
  - ui-context-menus
  - ui-dynamic-styling
  - ui-keyboard-shortcuts
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-two-way-binding
  - build-system-optimization
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - godot-animation-setup
  - networking-guild-system
  - physics-vehicle-setup
  - ui-accessibility
  - ui-animation-tweens
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
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
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - animation-mocap-setup
  - graphics-motion-blur
  - animation-humanoid-setup
  - animation-mirror-setup
  - graphics-sorting-layers
  - physics-joint-constraints
  - ai-debugging-tools
  - animation-baking-setup
  - animation-ik-setup
  - ci-cd-pipeline-setup
  - data-pipeline-setup
  - godot-setup
  - navmesh-baking-setup
  - networking-ngo-setup
  - audio-mixer-setup
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
  recommended:
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-temporal-antialiasing
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-physics-colliders
  - physics-layer-masking
  - terrain-wind-zones
  - animation-constraint-rigging
  - debug-renderer-debugging
  - debug-script-debugging
  - material-mipmap-chains
  - physics-collision-callbacks
  - physics-solver-configuration
  - physics-trigger-callbacks
  - terrain-biome-definition
  - terrain-brush-settings
  - terrain-heightmap-import
  - terrain-noise-functions
  - terrain-shape-tools
  - terrain-tree-painting
  - timeline-control-rig
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - debug-physics-debugger
  - debug-shader-debugging
  - godot-physics-system
  - material-disney-workflow
  - material-metallic-workflow
  - material-physics-interactions
  - material-specular-workflow
  - material-visual-debugging
  - networking-server-maintenance
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-continuous-collision
  - physics-debug-visualization
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-force-fields
  - physics-friction-models
  - physics-inertia-calculation
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-particle-collisions
  - physics-performance-metrics
  - physics-performance-profiling
  - physics-ragdoll-physics
  - physics-rolling-resistance
  - physics-rope-simulation
  - physics-spring-dynamics
  - physics-suspension-tuning
  - physics-time-scaling
  - physics-trigger-volumes
  optional:
  - physics-vehicle-wheels
  - physics-water-waves
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-cave-systems
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
skill_density: 20.38
estimated_skills_needed: 163
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Animation State Machine Workflow

Create and configure Unity Animator controllers using `@animator-specialist`.

## 1. Define Animation Requirements

Tell the agent what you need:
- "Set up a character locomotion state machine"
- "Create blend trees for movement"
- "Configure IK for VR hands"
- "Set up animation layers for upper/lower body"

## 2. State Machine Planning (Agent Action)

The agent designs the state machine:

### Basic Locomotion Example

```
┌─────────────────────────────────────────────────────────────┐
│                    CHARACTER ANIMATOR                        │
└─────────────────────────────────────────────────────────────┘

Base Layer (Full Body):
                    ┌──────────┐
        ┌──────────►│  Idle    │◄──────────┐
        │           └────┬─────┘           │
        │                │ Speed > 0.1     │
        │                ▼                 │
        │           ┌──────────┐           │
        │           │  Walk    │           │ Speed < 0.1
        │           └────┬─────┘           │
        │                │ Speed > 0.5     │
        │                ▼                 │
        │           ┌──────────┐           │
        └───────────│  Run     │───────────┘
                    └──────────┘

Upper Body Layer (Additive):
                    ┌──────────┐
                    │  Empty   │
                    └────┬─────┘
                         │ IsAiming
                         ▼
                    ┌──────────┐
                    │  Aim     │
                    └──────────┘
```

## 3. Create Animator Controller

// turbo
```bash
echo "Creating animator structure..."
mkdir -p "Assets/_Project/Animation/Controllers"
mkdir -p "Assets/_Project/Animation/Clips"

echo "✅ Animation folders created"
echo ""
echo "Next: Agent will create the animator controller via script or manual instructions"
```

## 4. Animator Setup Script

The agent can generate an editor script:

```csharp
#if UNITY_EDITOR
using UnityEditor;
using UnityEditor.Animations;
using UnityEngine;

public class AnimatorSetup : MonoBehaviour
{
    [MenuItem("Tools/Animation/Create Locomotion Controller")]
    public static void CreateLocomotionController()
    {
        // Create controller
        var controller = AnimatorController.CreateAnimatorControllerAtPath(
            "Assets/_Project/Animation/Controllers/CharacterAnimator.controller");

        // Add parameters
        controller.AddParameter("Speed", AnimatorControllerParameterType.Float);
        controller.AddParameter("IsGrounded", AnimatorControllerParameterType.Bool);
        controller.AddParameter("Jump", AnimatorControllerParameterType.Trigger);

        // Get base layer
        var rootStateMachine = controller.layers[0].stateMachine;

        // Create states
        var idleState = rootStateMachine.AddState("Idle");
        var walkState = rootStateMachine.AddState("Walk");
        var runState = rootStateMachine.AddState("Run");
        var jumpState = rootStateMachine.AddState("Jump");

        // Set default
        rootStateMachine.defaultState = idleState;

        // Create transitions
        var idleToWalk = idleState.AddTransition(walkState);
        idleToWalk.AddCondition(AnimatorConditionMode.Greater, 0.1f, "Speed");
        idleToWalk.duration = 0.15f;

        var walkToRun = walkState.AddTransition(runState);
        walkToRun.AddCondition(AnimatorConditionMode.Greater, 0.5f, "Speed");
        walkToRun.duration = 0.2f;

        var runToWalk = runState.AddTransition(walkState);
        runToWalk.AddCondition(AnimatorConditionMode.Less, 0.5f, "Speed");
        runToWalk.duration = 0.2f;

        var walkToIdle = walkState.AddTransition(idleState);
        walkToIdle.AddCondition(AnimatorConditionMode.Less, 0.1f, "Speed");
        walkToIdle.duration = 0.15f;

        Debug.Log("Locomotion controller created!");
    }
}
#endif
```

## 5. Blend Tree Setup

For smooth movement blending:

```csharp
// 2D Blend Tree for directional movement
[MenuItem("Tools/Animation/Create Movement Blend Tree")]
public static void CreateMovementBlendTree()
{
    var controller = AssetDatabase.LoadAssetAtPath<AnimatorController>(
        "Assets/_Project/Animation/Controllers/CharacterAnimator.controller");

    var rootStateMachine = controller.layers[0].stateMachine;

    // Create blend tree state
    var blendTreeState = rootStateMachine.AddState("Locomotion");
    var blendTree = new BlendTree();

    // Configure 2D blend
    blendTree.blendType = BlendTreeType.FreeformDirectional2D;
    blendTree.blendParameter = "VelocityX";
    blendTree.blendParameterY = "VelocityZ";

    // Add motions (assign clips manually)
    // blendTree.AddChild(idleClip, new Vector2(0, 0));
    // blendTree.AddChild(walkForwardClip, new Vector2(0, 1));
    // etc.

    blendTreeState.motion = blendTree;
}
```

## 6. VR Hand IK Setup

```csharp
public class VRHandIK : MonoBehaviour
{
    [SerializeField] private Animator _animator;
    [SerializeField] private Transform _leftHandTarget;
    [SerializeField] private Transform _rightHandTarget;

    private void OnAnimatorIK(int layerIndex)
    {
        if (_animator == null) return;

        // Left hand
        _animator.SetIKPositionWeight(AvatarIKGoal.LeftHand, 1f);
        _animator.SetIKRotationWeight(AvatarIKGoal.LeftHand, 1f);
        _animator.SetIKPosition(AvatarIKGoal.LeftHand, _leftHandTarget.position);
        _animator.SetIKRotation(AvatarIKGoal.LeftHand, _leftHandTarget.rotation);

        // Right hand
        _animator.SetIKPositionWeight(AvatarIKGoal.RightHand, 1f);
        _animator.SetIKRotationWeight(AvatarIKGoal.RightHand, 1f);
        _animator.SetIKPosition(AvatarIKGoal.RightHand, _rightHandTarget.position);
        _animator.SetIKRotation(AvatarIKGoal.RightHand, _rightHandTarget.rotation);
    }
}
```

## 7. Animation Best Practices

| Practice | Reason |
|----------|--------|
| Use root motion for movement | More natural locomotion |
| Set up avatar masks | Blend upper/lower body |
| Use transition duration 0.1-0.25s | Smooth but responsive |
| Avoid "Any State" transitions | Hard to debug |
| Name states clearly | Maintainability |

## 8. Checklist

- [ ] All states have exit conditions
- [ ] No orphaned states
- [ ] Parameters named consistently
- [ ] Transitions have appropriate duration
- [ ] Layers configured correctly
- [ ] IK targets assigned
- [ ] Animation events set up

## Example Commands

- "Set up locomotion state machine for my VR character"
- "Create a 2D blend tree for omnidirectional movement"
- "Configure IK for hand tracking"
- "Add an attack animation layer"