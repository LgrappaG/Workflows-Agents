using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.Audio
{
    /// <summary>
    /// Manages biome-aware ambient sounds by analyzing environment density.
    /// Works with WorldScaffolder to automate audio placement.
    /// </summary>
    public class AmbienceManager : MonoBehaviour
    {
        [System.Serializable]
        public struct AmbienceZone
        {
            public string zoneName;
            public AudioClip clip;
            public float minTreeDensity;
            [Range(0, 1)] public float volume;
        }

        public List<AmbienceZone> zones = new List<AmbienceZone>();
        public AudioSource ambientSource;

        private void Start()
        {
            if (ambientSource == null) ambientSource = gameObject.AddComponent<AudioSource>();
            ambientSource.loop = true;
            ambientSource.playOnAwake = false;
        }

        /// <summary>
        /// Analyzes the surroundings and picks the appropriate ambience.
        /// MCP can call this after world generation.
        /// </summary>
        public void UpdateAmbience(float localDensity)
        {
            AmbienceZone bestZone = zones[0];
            foreach (var zone in zones)
            {
                if (localDensity >= zone.minTreeDensity)
                {
                    bestZone = zone;
                }
            }

            if (ambientSource.clip != bestZone.clip)
            {
                ambientSource.clip = bestZone.clip;
                ambientSource.volume = bestZone.volume;
                ambientSource.Play();
                Debug.Log($"[AmbienceManager] Switched to {bestZone.zoneName} context.");
            }
        }
    }
}
