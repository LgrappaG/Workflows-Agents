using UnityEngine;
using Antigravity.Narrative;
using Antigravity.Logic;

namespace Antigravity.Audio
{
    /// <summary>
    /// Coordinates music transitions based on narrative state and gameplay urgency (e.g. survival stats).
    /// </summary>
    public class MusicDirector : MonoBehaviour
    {
        [Header("Music Tracks")]
        public AudioSource mainMusicSource;
        public AudioClip roamTrack;
        public AudioClip tenseTrack;
        public AudioClip dialogueTrack;

        [Header("Settings")]
        public float fadeSpeed = 1.0f;
        public float tensionThreshold = 20f; // Cross-reference with Hunger/Thirst

        private SurvivalHandler _playerSurvival;

        private void Start()
        {
            _playerSurvival = FindFirstObjectByType<SurvivalHandler>();
            if (mainMusicSource == null) mainMusicSource = gameObject.AddComponent<AudioSource>();
            mainMusicSource.loop = true;
            mainMusicSource.clip = roamTrack;
            mainMusicSource.Play();
        }

        private void Update()
        {
            UpdateMusicContext();
        }

        private void UpdateMusicContext()
        {
            // Check Narrative State
            if (NarrativeDirector.Instance != null && NarrativeDirector.Instance.currentState == NarrativeDirector.NarrativeState.Dialogue)
            {
                SwitchTrack(dialogueTrack, 0.4f); // Duck volume for dialogue
                return;
            }

            // Check Survival Urgency
            if (_playerSurvival != null)
            {
                bool isTense = false;
                foreach (var val in _playerSurvival.currentValues.Values)
                {
                    if (val < tensionThreshold) isTense = true;
                }

                if (isTense) SwitchTrack(tenseTrack, 1.0f);
                else SwitchTrack(roamTrack, 0.8f);
            }
        }

        private void SwitchTrack(AudioClip newClip, float targetVolume)
        {
            if (mainMusicSource.clip == newClip)
            {
                mainMusicSource.volume = Mathf.MoveTowards(mainMusicSource.volume, targetVolume, fadeSpeed * Time.deltaTime);
                return;
            }

            // Simplified abrupt switch for scaffold - in full version use cross-fade
            mainMusicSource.Stop();
            mainMusicSource.clip = newClip;
            mainMusicSource.volume = 0;
            mainMusicSource.Play();
        }
    }
}
