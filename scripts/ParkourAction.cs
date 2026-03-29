using UnityEngine;

namespace Antigravity.Logic
{
    [CreateAssetMenu(fileName = "NewParkourAction", menuName = "Antigravity/Logic/Parkour Action")]
    public class ParkourAction : ScriptableObject
    {
        public string actionName = "Vault";
        public string animationName = "VaultAnim";

        [Header("Requirements")]
        public float minHeight = 0.5f;
        public float maxHeight = 1.5f;
        public float minDistance = 0.2f;
        public float maxDistance = 2.0f;
        public bool requireWall = true;

        [Header("Ledge Settings")]
        public bool targetMatching = true;
        public Vector3 matchOffset;
    }
}
