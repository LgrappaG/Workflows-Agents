using UnityEngine;

namespace Antigravity.AI
{
    [CreateAssetMenu(fileName = "NewTrait", menuName = "Antigravity/AI/NPC Trait")]
    public class NPCTrait : ScriptableObject
    {
        public string traitName = "Aggressive";

        [Header("Movement Modifiers")]
        public float speedMultiplier = 1.0f;
        public float accelerationMultiplier = 1.0f;

        [Header("Detection Modifiers")]
        public float visionRangeMultiplier = 1.0f;
        public float interactionDistanceMultiplier = 1.0f;

        [Header("Decision Modifiers")]
        public float bravery = 0.5f; // 0 = Coward, 1 = Brave
        public float socializeWillingness = 0.5f;
    }
}
