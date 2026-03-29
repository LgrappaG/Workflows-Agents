using UnityEngine;

namespace Antigravity.Core.Utils
{
    /// <summary>
    /// Static utility methods to adjust GameObject positions based on visual Bounds rather than their Pivot.
    /// Useful for snapping objects procedurally generated or instantiated via Editor scripts.
    /// </summary>
    public static class OrientationFitter
    {
        /// <summary>
        /// Attempts to calculate the lowest Y bound of any renderers on the object and snaps it to the target position.
        /// Applies any PlacementProfile specific rotation or offsets.
        /// </summary>
        public static void ApplySmartPlacement(this GameObject go, Vector3 targetPosition, PlacementProfile profile = null)
        {
            if (go == null) return;

            // 1. Initial Position logic
            go.transform.position = targetPosition;

            // 2. Profile Overrides
            if (profile != null)
            {
                go.transform.rotation = Quaternion.Euler(profile.rotationOffset);
                go.transform.position += profile.positionOffset;

                if (!profile.snapToFloor) return;
            }

            // 3. Bounds Calculation (Lowest Y point)
            Renderer[] renderers = go.GetComponentsInChildren<Renderer>();
            if (renderers.Length == 0) return;

            Bounds totalBounds = renderers[0].bounds;
            for (int i = 1; i < renderers.Length; i++)
            {
                totalBounds.Encapsulate(renderers[i].bounds);
            }

            float lowestY = totalBounds.min.y;
            float difference = go.transform.position.y - lowestY;

            // Shift up so the lowest point rests exactly on targetPosition.y
            go.transform.position += new Vector3(0, difference, 0);
        }

        /// <summary>
        /// Injects a new empty GameObject at the calculated edge (bounds) of the mesh to act as a proper Hinge Pivot.
        /// Parents the original mesh to this new hinge, and returns the hinge.
        /// </summary>
        public static GameObject InjectHingeProxy(this GameObject visualMesh, string hingeName, PlacementProfile profile = null)
        {
            Renderer[] renderers = visualMesh.GetComponentsInChildren<Renderer>();
            if (renderers.Length == 0) return visualMesh; // Cannot calculate bounds without a renderer

            Bounds b = renderers[0].bounds;
            foreach (var r in renderers) b.Encapsulate(r.bounds);

            // Default Hinge Position: Leftmost edge (min X), Center Y, Front edge (min Z)
            Vector3 hingePos = new Vector3(b.min.x, visualMesh.transform.position.y, b.min.z);

            if (profile != null)
            {
                // If profile provides custom hinge offset based on bounds dimensions
                Vector3 size = b.size;
                hingePos += new Vector3(size.x * profile.hingeOffset.x, size.y * profile.hingeOffset.y, size.z * profile.hingeOffset.z);
            }

            GameObject hinge = new GameObject(hingeName);
            hinge.transform.position = hingePos;
            hinge.transform.SetParent(visualMesh.transform.parent); // Keep same hierarchy level

            visualMesh.transform.SetParent(hinge.transform, true); // Parent the visual safely

            return hinge;
        }
    }
}
