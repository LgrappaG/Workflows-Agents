using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.Logic
{
    public class ParkourController : MonoBehaviour
    {
        [Header("Action Database")]
        public List<ParkourAction> availableActions = new List<ParkourAction>();

        [Header("Sensors")]
        public Transform raycastOrigin;
        public float forwardCheckDistance = 1.5f;
        public LayerMask obstacleLayer;

        /// <summary>
        /// Call this externally (e.g. from PlayerController) to attempt a parkour move.
        /// </summary>
        public bool TryParkourAction()
        {
            RaycastHit hit;
            if (Physics.Raycast(raycastOrigin.position, transform.forward, out hit, forwardCheckDistance, obstacleLayer))
            {
                float obstacleHeight = hit.collider.bounds.max.y - transform.position.y;
                float distance = hit.distance;

                foreach (var action in availableActions)
                {
                    if (CheckActionRequirements(action, obstacleHeight, distance))
                    {
                        PerformAction(action, hit);
                        return true;
                    }
                }
            }
            return false;
        }

        private bool CheckActionRequirements(ParkourAction action, float height, float distance)
        {
            return height >= action.minHeight && height <= action.maxHeight &&
                   distance >= action.minDistance && distance <= action.maxDistance;
        }

        private void PerformAction(ParkourAction action, RaycastHit hit)
        {
            Debug.Log($"Performing Parkour Action: {action.actionName} on {hit.collider.name}");
            // Integration with Animator and Target Matching would go here
        }
    }
}
