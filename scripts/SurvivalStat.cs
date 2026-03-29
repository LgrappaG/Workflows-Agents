using UnityEngine;

namespace Antigravity.Logic
{
    [CreateAssetMenu(fileName = "NewSurvivalStat", menuName = "Antigravity/Logic/Survival Stat")]
    public class SurvivalStat : ScriptableObject
    {
        public string statName = "Hunger";
        public float maxValue = 100f;
        public float drainRate = 1f; // Amount per second
        public float damageOnZero = 5f; // Health damage per tick if zero
        public Sprite uiIcon;
    }
}
