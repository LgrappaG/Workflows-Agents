using UnityEngine;
using System;
using System.Collections.Generic;

namespace Antigravity.Logic
{
    /// <summary>
    /// Manages the core survival mechanics including continuous stat draining and starvation damage.
    /// Provides an event-driven API for UI bindings to avoid per-frame polling.
    /// </summary>
    public class SurvivalHandler : MonoBehaviour
    {
        // Core stat constants to avoid hardcoded strings
        public const string STAT_HUNGER = "Hunger";
        public const string STAT_HEALTH = "Health";

        /// <summary>
        /// Fired whenever a survival stat changes. Provides the stat name and its new normalized value (0.0 to 1.0).
        /// </summary>
        public event Action<string, float> OnStatChanged;

        [Header("Stat Templates")]
        public List<SurvivalStat> statTemplates = new List<SurvivalStat>();

        [Header("Runtime Data")]
        public Dictionary<string, float> currentValues = new Dictionary<string, float>();

        private void Start()
        {
            InitializeStats();
        }

        private void InitializeStats()
        {
            foreach (var template in statTemplates)
            {
                if (!currentValues.ContainsKey(template.statName))
                {
                    currentValues.Add(template.statName, template.maxValue);
                }
            }
        }

        private void Update()
        {
            ProcessStatDrain();
        }

        private void ProcessStatDrain()
        {
            foreach (var template in statTemplates)
            {
                float prev = currentValues[template.statName];
                float current = prev - (template.drainRate * Time.deltaTime);
                current = Mathf.Clamp(current, 0, template.maxValue);

                if (current != prev)
                {
                    currentValues[template.statName] = current;
                    OnStatChanged?.Invoke(template.statName, current / template.maxValue);
                }

                if (current <= 0 && template.damageOnZero > 0)
                {
                    ApplyStarvationDamage(template.damageOnZero * Time.deltaTime);
                }
            }
        }

        private void ApplyStarvationDamage(float damage)
        {
            if (currentValues.ContainsKey(STAT_HEALTH))
            {
                float currentHealth = currentValues[STAT_HEALTH];
                currentValues[STAT_HEALTH] = Mathf.Clamp(currentHealth - damage, 0, 100);

                // Assuming Health max is 100 for now, could be dynamic
                OnStatChanged?.Invoke(STAT_HEALTH, currentValues[STAT_HEALTH] / 100f);
            }
        }

        /// <summary>
        /// Attempts to add a specific amount to a named stat and broadcasts the change.
        /// </summary>
        public void RestoreStat(string statName, float amount)
        {
            if (currentValues.ContainsKey(statName))
            {
                // To safely get max value, we find the template
                float maxVal = 100f;
                foreach (var template in statTemplates)
                {
                    if (template.statName == statName) { maxVal = template.maxValue; break; }
                }

                currentValues[statName] = Mathf.Clamp(currentValues[statName] + amount, 0, maxVal);
                OnStatChanged?.Invoke(statName, currentValues[statName] / maxVal);
            }
        }

        public float GetStatNormalized(string statName)
        {
            // Optimization: Avoid List.Find with lambda to prevent GC allocation every frame.
            // Since statTemplates is small and rarely changes at runtime, a simple loop is allocation-free.
            SurvivalStat targetTemplate = null;
            foreach (var template in statTemplates)
            {
                if (template.statName == statName)
                {
                    targetTemplate = template;
                    break;
                }
            }

            if (targetTemplate != null && currentValues.TryGetValue(statName, out float value))
            {
                return value / targetTemplate.maxValue;
            }
            return 0;
        }
    }
}
