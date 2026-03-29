---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - custom-workflow-builder
  - ai-debugging-tools
  - graphics-render-queue
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
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - physics-fluid-dynamics
  - physics-vehicle-setup
  - material-specular-workflow
  - ui-context-menus
  - ui-text-binding
  - ui-two-way-binding
  - animation-mirror-setup
  - animation-mocap-setup
  - data-pipeline-setup
  - machine-learning-setup
  - material-pbr-setup
  - material-visual-debugging
  - navmesh-baking-setup
  - physics-chain-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-panel-layout
  - ui-prefab-variants
  - terrain-noise-functions
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - audio-mixer-setup
  - build-system-optimization
  - ci-cd-pipeline-setup
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  - godot-animation-setup
  - godot-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-translucency-setup
  - networking-guild-system
  - networking-ngo-setup
  - physics-constraint-optimization
  - physics-terrain-deformation
  - terrain-physics-colliders
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  recommended:
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-performance-optimization
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - terrain-layer-management
  - animation-constraint-rigging
  - csharp-chain-of-responsibility
  - material-mipmap-chains
  - physics-buoyancy
  - terrain-cave-systems
  - terrain-heightmap-import
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-water-integration
  - material-procedural-generation
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
  - automated-testing-framework
  - cinemachine-aim-assist
  - compatibility-testing
  - csharp-async-await
  - debug-physics-debugger
  - godot-physics-system
  - material-physics-interactions
  - networking-server-maintenance
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-collision-callbacks
  - physics-continuous-collision
  - physics-debug-visualization
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-force-fields
  - physics-friction-models
  - physics-inertia-calculation
  - physics-layer-masking
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-particle-collisions
  - physics-performance-metrics
  - physics-performance-profiling
  - physics-ragdoll-physics
  - physics-rolling-resistance
  - physics-rope-simulation
  - physics-solver-configuration
  - physics-spring-dynamics
  - physics-suspension-tuning
  - physics-time-scaling
  - physics-trigger-callbacks
  - physics-trigger-volumes
  optional:
  - physics-vehicle-wheels
  - physics-water-waves
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
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
skill_density: 32.8
estimated_skills_needed: 164
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Smart Placement Utility Setup

This workflow injects three core scripts (`MaterialRegistry.cs`, `PlacementProfile.cs`, `OrientationFitter.cs`) into your Unity project. These scripts solve common issues with procedural generation and third-party 3D assets, specifically:
- **Broken Pivots:** Calculates physical mesh bounds to snap objects accurately to the floor instead of relying on broken asset origin points.
- **Door/Chest Hinges:** Automatically injects an empty proxy GameObject at the edge of the calculated bounds to act as a proper rotation hinge.
- **Material Management:** Centralizes material creation (transparent, URP, Standard) to prevent duplicate material generation and pink missing shader errors string procedural or MCP-based instantiation.

## 1. Create the Utils Folder
Ensure the target directory exists.
```bash
mkdir -p Assets/Scripts/Utils
```

## 2. Inject `MaterialRegistry.cs`
Creates the ScriptableObject database for centralized material caching.

```csharp
// Target: Assets/Scripts/Utils/MaterialRegistry.cs
using UnityEngine;
using System.Collections.Generic;

#if UNITY_EDITOR
using UnityEditor;
#endif

namespace Antigravity.ThiefGame.Utils
{
    [CreateAssetMenu(fileName = "MaterialRegistry", menuName = "Thief Game/Utils/Material Registry")]
    public class MaterialRegistry : ScriptableObject
    {
        [System.Serializable]
        public class MaterialDefinition
        {
            public string id;
            public Material material;
        }

        public List<MaterialDefinition> materials = new List<MaterialDefinition>();

        private static MaterialRegistry _instance;
        public static MaterialRegistry Instance
        {
            get
            {
                if (_instance == null)
                {
#if UNITY_EDITOR
                    string[] guids = UnityEditor.AssetDatabase.FindAssets("t:MaterialRegistry");
                    if (guids.Length > 0)
                    {
                        string path = UnityEditor.AssetDatabase.GUIDToAssetPath(guids[0]);
                        _instance = UnityEditor.AssetDatabase.LoadAssetAtPath<MaterialRegistry>(path);
                    }
#endif
                }
                return _instance;
            }
        }

        public Material GetMaterial(string id)
        {
            var match = materials.Find(m => m.id == id);
            return match?.material;
        }

#if UNITY_EDITOR
        public Material GetOrCreateMaterial(string id, Color defaultColor, bool isTransparent = false)
        {
            Material mat = GetMaterial(id);
            if (mat != null) return mat;

            // Generate fallback
            if (!UnityEditor.AssetDatabase.IsValidFolder("Assets/Materials"))
                UnityEditor.AssetDatabase.CreateFolder("Assets", "Materials");

            string path = $"Assets/Materials/{id}.mat";
            mat = UnityEditor.AssetDatabase.LoadAssetAtPath<Material>(path);

            if (mat == null)
            {
                Shader shader = Shader.Find("Universal Render Pipeline/Lit");
                if (shader == null) shader = Shader.Find("Standard");

                mat = new Material(shader);
                if (shader.name.Contains("Universal Render Pipeline"))
                    mat.SetColor("_BaseColor", defaultColor);
                else
                    mat.color = defaultColor;

                if (isTransparent)
                {
                    if (shader.name.Contains("Universal Render Pipeline"))
                    {
                        mat.SetFloat("_Surface", 1); // Transparent
                        mat.SetFloat("_Blend", 0); // Alpha
                        mat.renderQueue = 3000;
                    }
                    else
                    {
                        mat.SetFloat("_Mode", 3);
                        mat.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.One);
                        mat.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.OneMinusSrcAlpha);
                        mat.SetInt("_ZWrite", 0);
                        mat.DisableKeyword("_ALPHATEST_ON");
                        mat.DisableKeyword("_ALPHABLEND_ON");
                        mat.EnableKeyword("_ALPHAPREMULTIPLY_ON");
                        mat.renderQueue = 3000;
                    }
                }

                UnityEditor.AssetDatabase.CreateAsset(mat, path);
                UnityEditor.AssetDatabase.SaveAssets();
            }

            materials.Add(new MaterialDefinition { id = id, material = mat });
            UnityEditor.EditorUtility.SetDirty(this);
            UnityEditor.AssetDatabase.SaveAssets();

            return mat;
        }
#endif
    }
}
```

## 3. Inject `PlacementProfile.cs`
Creates the custom profile rules for handling broken assets individually.

```csharp
// Target: Assets/Scripts/Utils/PlacementProfile.cs
using UnityEngine;

namespace Antigravity.ThiefGame.Utils
{
    [CreateAssetMenu(fileName = "NewPlacementProfile", menuName = "Thief Game/Utils/Placement Profile")]
    public class PlacementProfile : ScriptableObject
    {
        [Tooltip("If true, the object's lowest render bounds will be snapped to the target position.")]
        public bool snapToFloor = true;
        
        [Tooltip("Euler rotation offset applied when placing this object.")]
        public Vector3 rotationOffset = Vector3.zero;
        
        [Tooltip("Positional offset applied after snapping (useful for objects with bad pivots).")]
        public Vector3 positionOffset = Vector3.zero;

        [Tooltip("If true, the door/chest will have a hinge proxy injected at the lowest-left bound.")]
        public bool requiresHingeInjection = false;
        
        [Tooltip("Offset from the calculated bounds for the hinge (X=width, Y=height, Z=depth).")]
        public Vector3 hingeOffset = Vector3.zero;
    }
}
```

## 4. Inject `OrientationFitter.cs`
Creates the extension methods that perform the physical bounds calculations and dynamic Hinge injection.

```csharp
// Target: Assets/Scripts/Utils/OrientationFitter.cs
using UnityEngine;

namespace Antigravity.ThiefGame.Utils
{
    public static class OrientationFitter
    {
        public static void ApplySmartPlacement(this GameObject go, Vector3 targetPosition, PlacementProfile profile = null)
        {
            if (go == null) return;

            go.transform.position = targetPosition;

            if (profile != null)
            {
                go.transform.rotation = Quaternion.Euler(profile.rotationOffset);
                go.transform.position += profile.positionOffset;
                if (!profile.snapToFloor) return;
            }

            Renderer[] renderers = go.GetComponentsInChildren<Renderer>();
            if (renderers.Length == 0) return;

            Bounds totalBounds = renderers[0].bounds;
            for (int i = 1; i < renderers.Length; i++)
            {
                totalBounds.Encapsulate(renderers[i].bounds);
            }

            float lowestY = totalBounds.min.y;
            float difference = go.transform.position.y - lowestY;

            go.transform.position += new Vector3(0, difference, 0);
        }

        public static GameObject InjectHingeProxy(this GameObject visualMesh, string hingeName, PlacementProfile profile = null)
        {
            Renderer[] renderers = visualMesh.GetComponentsInChildren<Renderer>();
            if (renderers.Length == 0) return visualMesh; 

            Bounds b = renderers[0].bounds;
            foreach (var r in renderers) b.Encapsulate(r.bounds);

            Vector3 hingePos = new Vector3(b.min.x, visualMesh.transform.position.y, b.min.z);

            if (profile != null)
            {
                Vector3 size = b.size;
                hingePos += new Vector3(size.x * profile.hingeOffset.x, size.y * profile.hingeOffset.y, size.z * profile.hingeOffset.z);
            }

            GameObject hinge = new GameObject(hingeName);
            hinge.transform.position = hingePos;
            hinge.transform.SetParent(visualMesh.transform.parent); 

            visualMesh.transform.SetParent(hinge.transform, true); 

            return hinge;
        }
    }
}
```

## 5. Next Steps
Once injected, you can right-click in the project to create `Thief Game/Utils/Material Registry` and `Placement Profile` data containers. Update your generation logic or MCP commands to invoke `OrientationFitter.ApplySmartPlacement()` on any spawned third-party 3D asset.