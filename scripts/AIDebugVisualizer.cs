using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.Bonus
{
    /// <summary>
    /// Provides runtime visual feedback for AI logic, physics, and world states.
    /// MCP can use this to "see" what's happening inside the engine.
    /// </summary>
    public class AIDebugVisualizer : MonoBehaviour
    {
        public static AIDebugVisualizer Instance { get; private set; }

        private struct DebugRay
        {
            public Vector3 origin;
            public Vector3 direction;
            public Color color;
            public float duration;
            public float startTime;
        }

        private List<DebugRay> _activeRays = new List<DebugRay>();

        private void Awake()
        {
            if (Instance == null) Instance = this;
            else Destroy(gameObject);
        }

        /// <summary>
        /// Draws a debug line that persists for a specified duration in the Editor.
        /// </summary>
        public void DrawVisualRay(Vector3 origin, Vector3 direction, Color color, float duration = 2.0f)
        {
            _activeRays.Add(new DebugRay
            {
                origin = origin,
                direction = direction,
                color = color,
                duration = duration,
                startTime = Time.time
            });
        }

        private void OnDrawGizmos()
        {
            // Clean up old rays
            _activeRays.RemoveAll(r => Time.time > r.startTime + r.duration);

            foreach (var ray in _activeRays)
            {
                Gizmos.color = ray.color;
                Gizmos.DrawRay(ray.origin, ray.direction);
                // Draw a small sphere at the origin for visibility
                Gizmos.DrawWireSphere(ray.origin, 0.05f);
            }
        }

        /// <summary>
        /// Highlights an object with a temporary wireframe sphere.
        /// </summary>
        public void HighlightTarget(Vector3 position, float radius, Color color, float duration = 1.0f)
        {
            // Implementation for temporal spheres could be added here
            Debug.DrawLine(position + Vector3.up, position + Vector3.down, color, duration);
            Debug.DrawLine(position + Vector3.left, position + Vector3.right, color, duration);
        }
    }
}
