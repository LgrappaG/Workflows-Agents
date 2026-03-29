using UnityEngine;
using System.Collections.Generic;
using System.Linq;

namespace Antigravity.AI
{
    /// <summary>
    /// Global manager that tracks Points of Interest and coordinates crowd behaviors.
    /// Singleton pattern used for easy access by GOAP actions.
    /// </summary>
    public class SocialManager : MonoBehaviour
    {
        private static SocialManager _instance;
        public static SocialManager Instance => _instance;

        private List<POITag> _allPOIs = new List<POITag>();

        private void Awake()
        {
            if (_instance == null) _instance = this;
            else Destroy(gameObject);
        }

        /// <summary>
        /// Registers a POI into the global database.
        /// </summary>
        public void RegisterPOI(POITag poi)
        {
            if (!_allPOIs.Contains(poi)) _allPOIs.Add(poi);
        }

        /// <summary>
        /// Removes a POI from the database.
        /// </summary>
        public void UnregisterPOI(POITag poi)
        {
            _allPOIs.Remove(poi);
        }

        /// <summary>
        /// Finds the nearest available POI of a specific type.
        /// </summary>
        /// <param name="origin">Search origin position.</param>
        /// <param name="type">Type of POI needed.</param>
        /// <returns>The nearest available POITag or null.</returns>
        public POITag FindNearestPOI(Vector3 origin, POITag.POIType type)
        {
            POITag best = null;
            float minDistance = float.MaxValue;

            foreach (var p in _allPOIs)
            {
                if (p != null && p.type == type && !p.IsFull)
                {
                    float dist = Vector3.Distance(origin, p.transform.position);
                    if (dist < minDistance)
                    {
                        minDistance = dist;
                        best = p;
                    }
                }
            }

            return best;
        }
    }
}
