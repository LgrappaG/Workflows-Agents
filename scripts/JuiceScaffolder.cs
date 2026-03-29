using UnityEngine;
using System.Collections;

namespace Antigravity.VFX
{
    /// <summary>
    /// Handles procedural "juice" like screen shakes and chromatic aberration pulses.
    /// MCP can tie this to survival damage or parkour landings.
    /// </summary>
    public class JuiceScaffolder : MonoBehaviour
    {
        public static JuiceScaffolder Instance { get; private set; }

        private void Awake()
        {
            if (Instance == null) Instance = this;
            else Destroy(gameObject);
        }

        /// <summary>
        /// Simple camera shake logic.
        /// </summary>
        public void RequestShake(float duration, float magnitude)
        {
            StartCoroutine(ShakeCoroutine(duration, magnitude));
        }

        private IEnumerator ShakeCoroutine(float duration, float magnitude)
        {
            Vector3 originalPos = transform.localPosition;
            float elapsed = 0.0f;

            while (elapsed < duration)
            {
                float x = Random.Range(-1f, 1f) * magnitude;
                float y = Random.Range(-1f, 1f) * magnitude;

                transform.localPosition = new Vector3(x, y, originalPos.z);
                elapsed += Time.deltaTime;
                yield return null;
            }

            transform.localPosition = originalPos;
        }

        /// <summary>
        /// Logic for brief time-scale slowdown (Hit-stop/Impact feel).
        /// </summary>
        public void DoHitStop(float duration, float scale = 0.1f)
        {
            StartCoroutine(HitStopCoroutine(duration, scale));
        }

        private IEnumerator HitStopCoroutine(float duration, float scale)
        {
            Time.timeScale = scale;
            yield return new WaitForSecondsRealtime(duration);
            Time.timeScale = 1.0f;
        }
    }
}
