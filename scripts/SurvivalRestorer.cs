using UnityEngine;
using Antigravity.Logic;

namespace Antigravity.Utilities
{
    public class SurvivalRestorer : MonoBehaviour
    {
        public string statName = SurvivalHandler.STAT_HUNGER;
        public float amount = 20f;

        private SurvivalHandler _handler;

        private void Start()
        {
            _handler = Object.FindFirstObjectByType<SurvivalHandler>();
        }

        [ContextMenu("Restore")]
        public void Restore()
        {
            if (_handler != null)
            {
                _handler.RestoreStat(statName, amount);
                Debug.Log($"<color=green>Restored {amount} to {statName}.</color>");
            }
            else
            {
                Debug.LogWarning("SurvivalHandler reference is missing.");
            }
        }

        // OnMouseDown and Internal Update removed to prioritize Crosshair interaction from PlayerController
    }
}
