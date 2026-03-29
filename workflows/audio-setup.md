---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - audio-mixer-setup
  - audio-dynamic-music
  - audio-multi-output-routing
  - audio-ambisonics-support
  - audio-attenuation-curves
  - audio-ducking-sidechains
  - audio-ambient-soundscapes
  - audio-spatial-3d
  - audio-adaptive-bitrate
  - audio-dialogue-system
  - audio-footstep-generation
  - audio-prioritization-system
  - graphics-lightmap-setup
  - audio-binaural-rendering
  - audio-compression-codecs
  - audio-effects-compression
  - audio-effects-distortion
  - audio-effects-eq
  - audio-effects-pitch-shift
  - audio-effects-reverb
  - audio-effects-time-stretch
  - audio-environmental-acoustics
  - audio-fmod-integration
  - audio-frequency-analysis
  - audio-headphone-optimization
  - audio-impact-sounds
  - audio-object-pooling
  - audio-parameter-automation
  - audio-performance-profiling
  - audio-platform-specific-codecs
  - audio-procedural-generation
  - audio-streaming-audio
  - audio-voice-chat
  - graphics-hdrp-setup
  - graphics-urp-setup
  - timeline-audio-sync
  - custom-workflow-builder
  - ui-auto-layout
  - godot-setup
  - ui-anchor-positioning
  - godot-animation-setup
  - graphics-ambient-occlusion
  - graphics-reflection-probes
  - graphics-sorting-layers
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-grid-layout
  - ui-prefab-variants
  - ui-responsive-design
  - ui-style-sheets
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - build-system-optimization
  - ci-cd-pipeline-setup
  - csharp-builder-pattern
  - data-pipeline-setup
  - debug-build-diagnostic
  - engine-migration-guide
  - graphics-batching-optimization
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-frame-debugger
  - graphics-geometry-optimization
  - graphics-gpu-profiling
  recommended:
  - graphics-light-baking
  - graphics-memory-profiling
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-temporal-antialiasing
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-guild-system
  - networking-ngo-setup
  - physics-fluid-dynamics
  - physics-vehicle-setup
  - ui-accessibility
  - ui-animation-states
  - ui-animation-tweens
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-focus-navigation
  - ui-form-submission
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-resize-scaling
  - ui-scrolling-behavior
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-two-way-binding
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - csharp-async-await
  - physics-joint-constraints
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-water-integration
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-debugging-tools
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - cinemachine-aim-assist
  - csharp-chain-of-responsibility
  - material-disney-workflow
  - material-metallic-workflow
  optional:
  - material-mipmap-chains
  - material-specular-workflow
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: unity-architect
secondary_agents:
- production-lead
complexity_score: 5.0
skill_density: 16.0
estimated_skills_needed: 144
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Audio Setup Workflow

Configure audio systems for your game using `@audio-designer`.

## 1. Define Audio Requirements

Tell the agent what you need:
- "Set up spatial audio for VR"
- "Create an adaptive music system"
- "Configure ambient soundscapes"
- "Set up audio mixer with groups"

## 2. Audio Architecture (Agent Action)

### Recommended Structure

```
Audio/
├── Mixers/
│   └── MasterMixer.mixer
├── Music/
│   ├── Exploration/
│   └── Combat/
├── SFX/
│   ├── Player/
│   ├── Enemies/
│   ├── UI/
│   └── Environment/
├── Ambience/
│   ├── Indoor/
│   └── Outdoor/
└── Voice/
    └── Dialogue/
```

## 3. Create Audio Mixer

// turbo
```bash
mkdir -p "Assets/_Project/Audio/Mixers"
mkdir -p "Assets/_Project/Audio/Music"
mkdir -p "Assets/_Project/Audio/SFX"
mkdir -p "Assets/_Project/Audio/Ambience"
mkdir -p "Assets/_Project/Audio/Voice"

echo "✅ Audio folder structure created"
```

### Mixer Structure

```
Master
├── Music (Volume, Low Pass Filter)
│   ├── Exploration
│   └── Combat
├── SFX (Volume)
│   ├── Player
│   ├── Environment
│   └── UI
├── Ambience (Volume)
└── Voice (Volume, Ducking)
```

## 4. Audio Manager

```csharp
using UnityEngine;
using UnityEngine.Audio;

public class AudioManager : MonoBehaviour
{
    public static AudioManager Instance { get; private set; }

    [SerializeField] private AudioMixer _masterMixer;
    [SerializeField] private AudioSource _musicSource;
    [SerializeField] private AudioSource _ambienceSource;

    private const string MasterVolume = "MasterVolume";
    private const string MusicVolume = "MusicVolume";
    private const string SFXVolume = "SFXVolume";

    private void Awake()
    {
        if (Instance != null)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    public void SetVolume(string parameter, float normalizedValue)
    {
        // Convert 0-1 to dB (-80 to 0)
        float dB = normalizedValue > 0 ? Mathf.Log10(normalizedValue) * 20 : -80f;
        _masterMixer.SetFloat(parameter, dB);
    }

    public void PlayMusic(AudioClip clip, float fadeDuration = 1f)
    {
        StartCoroutine(CrossfadeMusic(clip, fadeDuration));
    }

    private System.Collections.IEnumerator CrossfadeMusic(AudioClip newClip, float duration)
    {
        float startVolume = _musicSource.volume;

        // Fade out
        while (_musicSource.volume > 0)
        {
            _musicSource.volume -= startVolume * Time.deltaTime / duration;
            yield return null;
        }

        // Switch clip
        _musicSource.clip = newClip;
        _musicSource.Play();

        // Fade in
        while (_musicSource.volume < startVolume)
        {
            _musicSource.volume += startVolume * Time.deltaTime / duration;
            yield return null;
        }
    }
}
```

## 5. Spatial Audio for VR

```csharp
using UnityEngine;

[RequireComponent(typeof(AudioSource))]
public class SpatialAudioSource : MonoBehaviour
{
    [SerializeField] private AudioSource _audioSource;

    [Header("Spatial Settings")]
    [SerializeField] private float _minDistance = 1f;
    [SerializeField] private float _maxDistance = 20f;
    [SerializeField] private AnimationCurve _rolloffCurve;

    private void Awake()
    {
        ConfigureSpatialAudio();
    }

    private void ConfigureSpatialAudio()
    {
        _audioSource.spatialBlend = 1f; // Full 3D
        _audioSource.minDistance = _minDistance;
        _audioSource.maxDistance = _maxDistance;
        _audioSource.rolloffMode = AudioRolloffMode.Custom;
        _audioSource.SetCustomCurve(AudioSourceCurveType.CustomRolloff, _rolloffCurve);

        // VR-specific: Use HRTF spatialization
        _audioSource.spatialize = true;
        _audioSource.spatializePostEffects = true;
    }
}
```

## 6. Adaptive Music System

```csharp
public class AdaptiveMusicDirector : MonoBehaviour
{
    [SerializeField] private AudioSource _layerBase;
    [SerializeField] private AudioSource _layerPercussion;
    [SerializeField] private AudioSource _layerMelody;

    private float _intensity = 0f;

    public void SetIntensity(float intensity)
    {
        _intensity = Mathf.Clamp01(intensity);

        // Crossfade layers based on intensity
        _layerBase.volume = 1f;
        _layerPercussion.volume = Mathf.Clamp01(_intensity * 2f); // Kicks in at 50%
        _layerMelody.volume = Mathf.Clamp01((_intensity - 0.5f) * 2f); // Kicks in at 50%
    }

    // Called by gameplay events
    public void OnCombatStart() => SetIntensity(0.8f);
    public void OnCombatEnd() => SetIntensity(0.2f);
    public void OnBossEncounter() => SetIntensity(1f);
}
```

## 7. Ambient Soundscape

```csharp
public class AmbienceManager : MonoBehaviour
{
    [System.Serializable]
    public class AmbienceLayer
    {
        public AudioClip Clip;
        public float Volume = 1f;
        public float MinInterval = 5f;
        public float MaxInterval = 15f;
    }

    [SerializeField] private AudioSource _loopSource;
    [SerializeField] private AudioSource _oneShotSource;
    [SerializeField] private AmbienceLayer[] _randomSounds;

    private void Start()
    {
        StartCoroutine(PlayRandomSounds());
    }

    private System.Collections.IEnumerator PlayRandomSounds()
    {
        while (true)
        {
            foreach (var layer in _randomSounds)
            {
                yield return new WaitForSeconds(Random.Range(layer.MinInterval, layer.MaxInterval));
                _oneShotSource.PlayOneShot(layer.Clip, layer.Volume);
            }
        }
    }
}
```

## 8. Audio Settings UI

```csharp
public class AudioSettingsUI : MonoBehaviour
{
    [SerializeField] private Slider _masterSlider;
    [SerializeField] private Slider _musicSlider;
    [SerializeField] private Slider _sfxSlider;

    private void Start()
    {
        _masterSlider.onValueChanged.AddListener(v => AudioManager.Instance.SetVolume("MasterVolume", v));
        _musicSlider.onValueChanged.AddListener(v => AudioManager.Instance.SetVolume("MusicVolume", v));
        _sfxSlider.onValueChanged.AddListener(v => AudioManager.Instance.SetVolume("SFXVolume", v));
    }
}
```

## 9. Audio Checklist

- [ ] Audio mixer with proper groups
- [ ] Volume exposed to settings
- [ ] Spatial audio configured for VR
- [ ] Music crossfade system
- [ ] Ambient soundscapes
- [ ] UI sounds responsive
- [ ] Audio compressed appropriately
- [ ] No clipping/distortion

## Example Commands

- "Set up spatial audio for my VR game"
- "Create an adaptive music system with combat/exploration modes"
- "Configure ambient soundscapes for outdoor/indoor areas"
- "Set up audio mixer with volume controls"