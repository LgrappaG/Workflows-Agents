---
version: 9.0.0
category: Accessibility & Compliance
agent: Accessibility Expert
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - audio-ducking-sidechains
  - audio-mixer-setup
  - ui-focus-navigation
  - audio-object-pooling
  - audio-dialogue-system
  - audio-multi-output-routing
  - audio-parameter-automation
  - audio-prioritization-system
  - audio-ambisonics-support
  - audio-binaural-rendering
  - audio-effects-distortion
  - audio-effects-reverb
  - audio-footstep-generation
  - audio-frequency-analysis
  - audio-spatial-3d
  - timeline-audio-sync
  - ui-accessibility
  - ui-animation-states
  - ai-debugging-tools
  - audio-adaptive-bitrate
  - audio-ambient-soundscapes
  - audio-attenuation-curves
  - audio-compression-codecs
  - audio-dynamic-music
  - audio-effects-compression
  - audio-effects-eq
  - audio-effects-pitch-shift
  - audio-effects-time-stretch
  - audio-environmental-acoustics
  - audio-fmod-integration
  - audio-headphone-optimization
  - audio-impact-sounds
  - audio-performance-profiling
  - audio-platform-specific-codecs
  - audio-procedural-generation
  - audio-streaming-audio
  - audio-voice-chat
  - custom-workflow-builder
  - ui-drag-drop
  - ui-style-sheets
  - ui-keyboard-shortcuts
  - ui-text-binding
  - ui-tooltips
  - ui-visual-feedback
  - vfx-builtin-particles
  - ai-environmental-awareness
  - cinemachine-aim-assist
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - physics-chain-dynamics
  - terrain-blending-shaders
  - terrain-erosion-simulation
  - terrain-sound-surfaces
  - terrain-streaming
  - ui-animation-tweens
  - ui-auto-layout
  - ui-docking-windows
  - ui-event-handlers
  - ui-grid-layout
  - ui-responsive-design
  - ui-theme-switching
  - ui-transition-timing
  - ui-z-ordering
  - vfx-trail-rendering
  - graphics-postprocessing
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - build-system-optimization
  - csharp-async-await
  - csharp-builder-pattern
  - engine-migration-guide
  recommended:
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-mipmap-chains
  - networking-guild-system
  - networking-server-maintenance
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-splat-mapping
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - training-datasets
  - ui-anchor-positioning
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-dynamic-styling
  - ui-form-submission
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-scrolling-behavior
  - ui-touch-input
  - ui-two-way-binding
  - graphics-depth-of-field
  - graphics-bloom-effect
  - graphics-sorting-layers
  - ci-cd-pipeline-setup
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-culling-strategies
  - graphics-dynamic-lighting
  - graphics-frame-debugger
  - graphics-geometry-optimization
  - graphics-gpu-profiling
  - graphics-light-baking
  - graphics-memory-profiling
  - graphics-motion-blur
  - graphics-probe-placement
  optional:
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: tech-lead
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 161.0
estimated_skills_needed: 161
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Accessibility Audit Workflow

Ensure game is playable for all players including those with disabilities (colorblindness, hearing loss, motor impairment, visual impairment).

## Prerequisites

- Accessibility knowledge (basics)
- ColorOracle or similar colorblind simulator (free)
- Screen reader software (NVDA for Windows, is free)

// turbo-all

## Phase 1: Colorblind Accessibility Testing

1. **Install Colorblind Simulator:**
   ```bash
   # ColorOracle: colororacleapp.com (free)
   # Simulates: Protanopia, Deuteranopia, Tritanopia
   ```

2. **Test Game With Simulator:**
   ```plaintext
   Play entire game with colorblind mode enabled:
   - Can you distinguish all important UI elements?
   - Can you tell health bar color (red) from enemy status?
   - Can you read text contrast?

   Fix: Use icons + colors, not colors alone
   - Red health bar → Add heart icon
   - Green button → Add checkmark icon
   ```

## Phase 2: Motor Accessibility

```plaintext
Considerations:
- Can game be played with one hand?
- Are button holds too long (>2 seconds)?
- Is rapid tapping required (problematic for tremors)?

Implement:
- Remappable controls (allow any key)
- Toggle options for held buttons
- Assist modes: Auto-aim, slower enemies
```

## Phase 3: Audio Accessibility (Hearing Loss)

```csharp
public class AudioAccessibility
{
    public void AddCaptions() {
        // For every sound effect, show visual indicator
        // Example: Footstep sound → show footprint animation

        // Subtitle important dialogue
        // Use visual effects to replace audio cues
    }

    public void ImplementVisualFeedback() {
        // Enemy alert: Sound + red screen flash
        // Pickup: Sound + particle effect
        // Damage: Sound + screen shake
    }
}
```

## Phase 4: Visual Accessibility (Vision Loss)

```plaintext
Implement:
- Zoomable UI (up to 200%)
- High contrast mode
- Larger text options
- Text-to-speech for dialogue (TTS)
- Screen reader support (basic)
```

## Phase 5: Test Checklist

```markdown
WCAG 2.1 Level AA Checklist:

**Perceivable:**
- [ ] Color not only means of information
- [ ] At least 4.5:1 contrast (normal text)
- [ ] No flashing more than 3x per second
- [ ] Audio description for videos

**Operable:**
- [ ] All interactive elements keyboard accessible
- [ ] No traps (can exit any UI)
- [ ] Enough time for tasks (no 5-second timeout)
- [ ] No seizure-inducing animations

**Understandable:**
- [ ] Clear labels on buttons
- [ ] Consistent navigation
- [ ] Plain language (avoid jargon)
- [ ] Help available

**Robust:**
- [ ] Compatible with assistive technologies
- [ ] Proper HTML semantics (if Web)
- [ ] No breaking bugs in assistive tech
```

## Phase 6: Automated Accessibility Testing

```csharp
public class AccessibilityValidator
{
    public void ValidateTextContrast() {
        var texts = GameObject.FindObjectsOfType<Text>();

        foreach (var text in texts) {
            float contrast = CalculateContrastRatio(text.color, text.GetComponentInParent<Image>().color);
            Assert.IsTrue(contrast >= 4.5f, $"Text {text.name} contrast too low: {contrast}");
        }
    }

    private float CalculateContrastRatio(Color foreground, Color background) {
        // WCAG formula for relative luminance
        float lum1 = GetRelativeLuminance(foreground);
        float lum2 = GetRelativeLuminance(background);
        return (Mathf.Max(lum1, lum2) + 0.05f) / (Mathf.Min(lum1, lum2) + 0.05f);
    }
}
```

## Phase 7: Assistive Technology Support

```markdown
If Web/PC build:
- Support screen readers (NVDA, JAWS)
- Keyboard-only navigation
- No mouse-only interactions

If Mobile:
- Support device accessibility features
- iOS VoiceOver compatible
- Android TalkBack compatible
```

## Verification

- [ ] Colorblind simulator: game playable
- [ ] Motor: playable one-handed or with assist mode
- [ ] Audio: captions present, visual feedback for sounds
- [ ] Visual: high contrast mode, zoomable UI
- [ ] Text contrast: 4.5:1 minimum
- [ ] Keyboard navigation: all features reachable
- [ ] No flashing animations

## Common Issues

| Issue | Solution |
|---|---|
| Text unreadable on colored background | Increase contrast, use drop shadow |
| Can't tell red from green | Add icons/symbols, use patterning |
| Buttons too small | Min 44x44 pixels |
| No way to remap controls | Implement rebind UI |

## Related Topics

- See `/ui-testing-framework` for automated testing
- Refer to `/i18n-testing-workflow` for visual testing approaches