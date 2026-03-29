using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.VFX
{
    /// <summary>
    /// Binds particle effects to specific game events via tag or naming convention.
    /// </summary>
    public class VFXAutoBinder : MonoBehaviour
    {
        [System.Serializable]
        public struct VFXMap
        {
            public string key;
            public GameObject prefab;
        }

        public VFXMap[] vfxLibrary;
        private Dictionary<string, GameObject> _vfxDict;

        private void Awake()
        {
            _vfxDict = new Dictionary<string, GameObject>(System.StringComparer.OrdinalIgnoreCase);

            if (vfxLibrary == null) return;
            foreach (var map in vfxLibrary)
            {
                if (!string.IsNullOrEmpty(map.key) && !_vfxDict.ContainsKey(map.key))
                {
                    _vfxDict[map.key] = map.prefab;
                }
            }
        }

        /// <summary>
        /// Spawns a VFX at a location based on a key (e.g., "DustStep", "ImpactBlood").
        /// </summary>
        public void SpawnVFX(string key, Vector3 position, Quaternion rotation)
        {
            if (_vfxDict != null && _vfxDict.TryGetValue(key, out GameObject prefab) && prefab != null)
            {
                Instantiate(prefab, position, rotation);
            }
        }
    }
}
