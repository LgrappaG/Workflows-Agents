using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.Audio
{
    /// <summary>
    /// Detects ground material via raycast and plays appropriate footstep sounds.
    /// MCP can use this to automate foley for any Character Controller.
    /// </summary>
    public class AutoFoley : MonoBehaviour
    {
        [System.Serializable]
        public struct MaterialAudio
        {
            public string textureTag;
            public AudioClip[] clips;
        }

        public List<MaterialAudio> materialLibrary = new List<MaterialAudio>();
        public AudioSource foleySource;

        public void PlayFootstep()
        {
            if (foleySource == null) return;

            if (Physics.Raycast(transform.position + Vector3.up, Vector3.down, out RaycastHit hit, 2f))
            {
                string detectedMaterial = "Default";

                // Detection logic via Tag or Texture Name
                if (hit.collider.CompareTag("Water")) detectedMaterial = "Water";
                else detectedMaterial = hit.collider.sharedMaterial?.name ?? "Default";

                MaterialAudio foundAudioSet = default;
                foreach (var m in materialLibrary)
                {
                    if (detectedMaterial.Contains(m.textureTag))
                    {
                        foundAudioSet = m;
                        break;
                    }
                }

                if (foundAudioSet.clips != null && foundAudioSet.clips.Length > 0)
                {
                    AudioClip clip = foundAudioSet.clips[Random.Range(0, foundAudioSet.clips.Length)];
                    foleySource.PlayOneShot(clip);
                }
            }
        }
    }
}
