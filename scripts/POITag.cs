using UnityEngine;

namespace Antigravity.AI
{
    /// <summary>
    /// Tagging component to mark objects as Points of Interest for NPCs.
    /// </summary>
    public class POITag : MonoBehaviour
    {
        public enum POIType
        {
            Food,
            Rest,
            Social,
            Work,
            Danger
        }

        [Tooltip("The type of interest this object provides.")]
        public POIType type = POIType.Social;

        [Tooltip("How many NPCs can use this POI simultaneously.")]
        public int capacity = 1;

        private int _currentUsers = 0;

        public bool IsFull => _currentUsers >= capacity;

        public void RegisterUser() => _currentUsers++;
        public void UnregisterUser() => _currentUsers = Mathf.Max(0, _currentUsers - 1);

        private void OnEnable()
        {
            SocialManager.Instance?.RegisterPOI(this);
        }

        private void OnDisable()
        {
            SocialManager.Instance?.UnregisterPOI(this);
        }
    }
}
