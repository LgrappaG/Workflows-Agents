using UnityEngine;
using UnityEngine.Rendering;

namespace Antigravity.VFX
{
    /// <summary>
    /// Manages the visual "vibe" of the scene by swapping Post-Processing profiles.
    /// MCP can use this to instantly change the game's mood.
    /// </summary>
    public class AtmoController : MonoBehaviour
    {
        public Volume globalVolume;

        [System.Serializable]
        public struct AtmoProfile
        {
            public string name;
            public VolumeProfile profile;
            public Color ambientColor;
            public float fogDensity;
        }

        public AtmoProfile[] profiles;

        /// <summary>
        /// Switches the entire scene atmosphere based on a profile name.
        /// </summary>
        public void SetAtmosphere(string profileName)
        {
            foreach (var p in profiles)
            {
                if (string.Equals(p.name, profileName, System.StringComparison.OrdinalIgnoreCase))
                {
                    ApplyProfile(p);
                    return;
                }
            }
            Debug.LogWarning($"[AtmoController] Profile '{profileName}' not found.");
        }

        private void ApplyProfile(AtmoProfile p)
        {
            if (globalVolume != null) globalVolume.profile = p.profile;
            RenderSettings.ambientLight = p.ambientColor;
            RenderSettings.fogDensity = p.fogDensity;
            RenderSettings.fog = p.fogDensity > 0;

            Debug.Log($"[AtmoController] Mood shifted to: {p.name}");
        }
    }
}
