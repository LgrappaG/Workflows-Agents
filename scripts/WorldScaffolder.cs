using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.AssetIntelligence
{
    /// <summary>
    /// Automates the distribution of environment assets (foliage, loot) using Poisson Disk Sampling principles.
    /// MCP can configure and trigger this to build worlds rapidly.
    /// </summary>
    public class WorldScaffolder : MonoBehaviour
    {
        [Header("Scattering Setup")]
        public GameObject[] prefabsToScatter;
        public float regionSize = 50f;
        public float minDistanceBetweenSpoons = 2f;
        public int rejectionSamples = 30;

        [Header("Placement Rules")]
        public LayerMask groundLayer;
        public float minScale = 0.8f;
        public float maxScale = 1.2f;
        public bool randomRotationY = true;

        /// <summary>
        /// Main entry point for MCP to trigger scattering.
        /// </summary>
        [ContextMenu("Scatter Assets")]
        public void ScatterAssets()
        {
            ClearExistingAssets();
            List<Vector2> points = GeneratePoints();

            foreach (Vector2 point in points)
            {
                Vector3 worldPos = new Vector3(point.x - regionSize / 2, 50, point.y - regionSize / 2);
                worldPos += transform.position;

                if (Physics.Raycast(worldPos, Vector3.down, out RaycastHit hit, 100f, groundLayer))
                {
                    PlaceAsset(hit.point);
                }
            }
        }

        private List<Vector2> GeneratePoints()
        {
            // Simplified Poisson-like distribution
            // In a full implementation, this would use a proper Poisson Disk grid.
            // For the initial scaffold, we use a jittered grid approach.
            List<Vector2> points = new List<Vector2>();
            float step = minDistanceBetweenSpoons;

            for (float x = 0; x < regionSize; x += step)
            {
                for (float y = 0; y < regionSize; y += step)
                {
                    Vector2 point = new Vector2(x, y);
                    point += new Vector2(Random.Range(-step / 2, step / 2), Random.Range(-step / 2, step / 2));
                    points.Add(point);
                }
            }
            return points;
        }

        private void PlaceAsset(Vector3 position)
        {
            if (prefabsToScatter == null || prefabsToScatter.Length == 0) return;

            GameObject prefab = prefabsToScatter[Random.Range(0, prefabsToScatter.Length)];
            GameObject instance = Instantiate(prefab, position, Quaternion.identity, transform);

            if (randomRotationY)
            {
                instance.transform.Rotate(0, Random.Range(0, 360f), 0);
            }

            float scale = Random.Range(minScale, maxScale);
            instance.transform.localScale = Vector3.one * scale;
        }

        public void ClearExistingAssets()
        {
            for (int i = transform.childCount - 1; i >= 0; i--)
            {
                DestroyImmediate(transform.GetChild(i).gameObject);
            }
        }
    }
}
