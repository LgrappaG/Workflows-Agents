---
version: 9.0.0
category: Testing & QA
agent: QA Lead
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - audio-mixer-setup
  - graphics-hdrp-setup
  - graphics-urp-setup
  - automated-testing-framework
  - ai-debugging-tools
  - graphics-lightmap-setup
  - ci-cd-pipeline-setup
  - godot-animation-setup
  - audio-dialogue-system
  - compatibility-testing
  - material-pbr-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-ducking-sidechains
  - data-pipeline-setup
  - debug-renderer-debugging
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - ui-event-handlers
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - custom-workflow-builder
  - debug-script-debugging
  - debug-shader-debugging
  - godot-setup
  - machine-learning-setup
  - material-translucency-setup
  - material-visual-debugging
  - ui-responsive-design
  - ui-style-sheets
  - audio-dynamic-music
  - audio-frequency-analysis
  - audio-multi-output-routing
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-auto-layout
  - ui-drag-drop
  - ui-focus-navigation
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-text-binding
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  - audio-ambisonics-support
  - audio-binaural-rendering
  - audio-compression-codecs
  - audio-parameter-automation
  - audio-procedural-generation
  - audio-spatial-3d
  - audio-streaming-audio
  - ui-button-events
  - ui-context-menus
  - ui-docking-windows
  - ui-grid-layout
  - ui-prefab-variants
  - ui-theme-switching
  - ui-two-way-binding
  - audio-adaptive-bitrate
  - audio-ambient-soundscapes
  - audio-attenuation-curves
  - audio-effects-compression
  - audio-effects-distortion
  - audio-effects-eq
  - audio-effects-pitch-shift
  - audio-effects-reverb
  - audio-effects-time-stretch
  - audio-environmental-acoustics
  - audio-fmod-integration
  - audio-footstep-generation
  - audio-headphone-optimization
  - audio-impact-sounds
  - audio-object-pooling
  recommended:
  - audio-performance-profiling
  - audio-platform-specific-codecs
  - audio-prioritization-system
  - audio-voice-chat
  - build-system-optimization
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - networking-guild-system
  - physics-fluid-dynamics
  - timeline-audio-sync
  - ui-animation-tweens
  - ui-data-binding
  - ui-dynamic-styling
  - ui-form-submission
  - ui-hierarchy-panel
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-resize-scaling
  - ui-scrolling-behavior
  - ui-tooltips
  - ui-touch-input
  - vfx-builtin-particles
  - cinemachine-virtual-camera
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - material-specular-workflow
  - csharp-chain-of-responsibility
  - graphics-render-queue
  - graphics-temporal-antialiasing
  - physics-joint-constraints
  - terrain-brush-settings
  - terrain-grass-placement
  - terrain-heightmap-import
  - terrain-noise-functions
  - terrain-shape-tools
  - terrain-water-integration
  - terrain-wind-zones
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - cinemachine-aim-assist
  - csharp-async-await
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-frame-debugger
  - graphics-geometry-optimization
  - graphics-gpu-profiling
  - graphics-light-baking
  - graphics-memory-profiling
  - graphics-motion-blur
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-advanced-editing
  optional:
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
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
skill_density: 163.0
estimated_skills_needed: 163
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# i18n Testing & Localization Quality Assurance

This workflow validates that localized content renders correctly, layouts adapt to text length variations, and cultural elements are appropriate for target markets.

## Prerequisites

- Localization framework set up (via `/localization-setup`)
- Translated strings in all target languages
- Native speakers for QA (or use L10n testing services)
- 1-2 weeks per language for thorough testing

## Context

Poor localization ruins user experience. Text overflowing UI, RTL languages broken, or culturally inappropriate content damage reputation and revenue. This workflow prevents those issues.

// turbo-all

## Phase 1: Automated String & Layout Testing

1. **Detect Text Overflow Issues:**
   ```csharp
   public class LocalizationTester
   {
       public void CheckStringLengthVariations()
       {
           var locales = LocalizationSettings.AvailableLocales.Locales;

           foreach (var locale in locales)
           {
               LocalizationSettings.SelectedLocale = locale;

               // Check character length multipliers
               string en_Text = GetLocalizedString("ui/welcome_message"); // ~20 chars

               switch (locale.Identifier.CultureInfo.Name)
               {
                   case "de": // German
                       Assert.IsTrue(en_Text.Length <= 30, "German text too long!");
                       break;
                   case "ja": // Japanese
                       Assert.IsTrue(en_Text.Length <= 10, "Japanese too long"); // Compact
                       break;
               }
           }
       }

       private string GetLocalizedString(string key)
       {
           return new LocalizedString { TableEntryReference = key }.GetLocalizedString();
       }
   }
   ```

2. **Detect Missing Translations:**
   ```csharp
   public void CheckCompleteness()
   {
       var missingTranslations = new List<string>();

       foreach (var locale in LocalizationSettings.AvailableLocales.Locales)
       {
           LocalizationSettings.SelectedLocale = locale;

           // Sample all strings, log any that return English fallback
           var strings = GetAllStringsForTable("UIStrings");
           foreach (var str in strings)
           {
               try
               {
                   string result = new LocalizedString {
                       TableEntryReference = str
                   }.GetLocalizedString();

                   if (result.Contains("[") && result.Contains("]"))
                       missingTranslations.Add($"{locale}: {str}");
               }
               catch { }
           }
       }

       Debug.Log($"Missing translations: {missingTranslations.Count}");
       foreach (var missing in missingTranslations)
           Debug.LogWarning(missing);
   }
   ```

## Phase 2: UI Layout Verification

1. **Test Text Expansion Scenarios:**
   ```plaintext
   Known text length variations:
   - English vs German: +35%
   - English vs French: +20%
   - English vs Spanish: +25%
   - English vs Portuguese: +20%
   - English vs Japanese: -60% (more compact)
   - English vs Chinese: -40% (more compact)

   Test approach:
   - Set all text to longest locale (German)
   - Verify no overflow or truncation
   - Check button sizes accommodate text
   ```

2. **Check RTL (Right-to-Left) Rendering:**
   ```csharp
   public void TestRTLLayout()
   {
       // Switch to Arabic
       var arabicLocale = LocalizationSettings.AvailableLocales.Locales
           .First(l => l.Identifier.CultureInfo.Name == "ar");
       LocalizationSettings.SelectedLocale = arabicLocale;

       // Verify text alignment is right-aligned
       Text textComponent = GetComponent<Text>();
       Assert.AreEqual(textComponent.alignment, TextAnchor.MiddleRight);

       // Verify button layout mirrors correctly
       RectTransform rt = GetComponent<RectTransform>();
       Assert.AreEqual(rt.anchorMin.x, 1); // Anchored to right
   }
   ```

3. **Screenshot Regression Testing:**
   ```csharp
   public void CaptureLocalizationScreenshots()
   {
       var locales = new[] { "en", "de", "ja", "ar", "es", "fr" };

       foreach (var locale in locales)
       {
           SwitchLocale(locale);
           string filename = $"Screenshots/Localization_{locale}.png";
           ScreenCapture.CaptureScreenshot(filename);
           Debug.Log($"Captured: {filename}");
       }
   }
   ```

## Phase 3: Cultural Appropriateness Review

1. **Content Sensitivity Assessment:**
   ```markdown
   Review checklist for each market:

   Japan:
   - [ ] No references to death/ghosts inappropriately
   - [ ] Age/hierarchy respected
   - [ ] Honorifics used correctly in dialogue

   China:
   - [ ] No religious content (Buddhism, Taoism)
   - [ ] No political references
   - [ ] No ghost/skeleton imagery (culturally sensitive)
   - [ ] Taiwan not referenced as independent

   Germany/Austria:
   - [ ] No Nazi or WWII references
   - [ ] No swastika symbols

   Brazil/Latin America:
   - [ ] Masculinity themes appropriate
   - [ ] Color symbolism checked (white ≠ death)

   Middle East:
   - [ ] Right-to-left layout
   - [ ] No pig/alcohol references
   - [ ] Gender separation appropriate if applicable
   ```

2. **Color & Symbol Significance:**
   ```plaintext
   Colors have different meanings:
   - Red: Luck (China), danger (USA)
   - White: Purity (USA), death (Asia)
   - Purple: Royalty (UK), mourning (Thailand)

   Symbols:
   - Thumbs up: Offensive in parts of Middle East
   - Clapping: Not appropriate as OK sign in some cultures
   - Hand gestures: Highly culture-specific
   ```

## Phase 4: Font & Typography Testing

1. **CJK Font Rendering:**
   ```csharp
   public void TestCJKFontQuality()
   {
       // Switch to Chinese
       LocalizationSettings.SelectedLocale = GetLocale("zh");

       // Verify characters render clearly
       Text textComponent = GetComponent<Text>();
       Assert.IsNotEmpty(textComponent.text);

       // Check for garbled/square characters
       bool hasSquares = textComponent.text.Contains("□");
       Assert.IsFalse(hasSquares, "Missing CJK font characters!");

       // Verify font size readable (CJK needs larger sizes)
       Assert.IsTrue(textComponent.fontSize >= 36, "CJK font too small");
   }
   ```

2. **Accented Characters & Diacritics:**
   ```plaintext
   Test strings with special characters:
   - French: "café", "naïve", "élève"
   - Spanish: "ñoño", "mañana"
   - Portuguese: "açúcar", "não"
   - Czech: "řeka", "dvě"
   - Polish: "zł" (currency)

   Verify: No garbling, correct rendering
   ```

## Phase 5: Number & Date Formatting

1. **Locale-Specific Formatting:**
   ```csharp
   public void TestNumberFormatting()
   {
       var locales = new[] { "en-US", "de-DE", "fr-FR", "ja-JP", "zh-CN" };

       foreach (var locale in locales)
       {
           var culture = new System.Globalization.CultureInfo(locale);
           double price = 1234.56;
           string formatted = price.ToString("C", culture);

           Debug.Log($"{locale}: {formatted}");
           // en-US: $1,234.56
           // de-DE: 1.234,56 €
           // fr-FR: 1 234,56 €
           // ja-JP: ¥1,235 (rounds to whole number)
           // zh-CN: ¥1,234.56
       }
   }
   ```

2. **Date & Time Formatting:**
   ```csharp
   public void TestDateFormatting()
   {
       var dateTime = new System.DateTime(2024, 12, 25);

       // Different locales format dates differently
       Debug.Log(dateTime.ToString("d", new System.Globalization.CultureInfo("en-US"))); // 12/25/2024
       Debug.Log(dateTime.ToString("d", new System.Globalization.CultureInfo("de-DE"))); // 25.12.2024
       Debug.Log(dateTime.ToString("d", new System.Globalization.CultureInfo("fr-FR"))); // 25/12/2024
       Debug.Log(dateTime.ToString("d", new System.Globalization.CultureInfo("ja-JP"))); // 2024/12/25
   }
   ```

## Phase 6: Audio Localization Testing (If Applicable)

1. **Verify Dubbed Audio:**
   ```plaintext
   Testing checklist:
   - [ ] Audio lip-sync matches translated text length
   - [ ] Voice acting quality consistent with budget
   - [ ] No audio crackling or quality loss
   - [ ] Timing matches original for cutscenes
   - [ ] Subtitles synchronized with audio
   ```

## Phase 7: Native Speaker QA

1. **Create QA Checklist Template:**
   ```markdown
   For each native speaker QA session:

   - [ ] Read through all UI text for naturalness
   - [ ] Play 2-3 hours gameplay reporting issues
   - [ ] Check for typos, grammar errors
   - [ ] Verify tone matches target audience
   - [ ] Assess if colloquialisms work for region
   - [ ] Report any culturally inappropriate content
   - [ ] Test all button interactions work
   - [ ] Verify placeholder text removed
   - [ ] Check dates/times display correctly
   - [ ] Test edge cases (very long names, special characters)

   Feedback categories:
   - CRITICAL: Breaks gameplay or offensive
   - MAJOR: Poor experience, unnatural translation
   - MINOR: Typo or stylistic improvement
   ```

## Phase 8: Bug Reporting & Fixes

1. **Use Localization Bug Tracker:**
   ```markdown
   Template for localization bugs:
   - Locale: [Language]
   - Issue: [Description]
   - Steps to reproduce: [Steps]
   - Expected: [What should happen]
   - Actual: [What happens]
   - Screenshot: [If applicable]
   - Severity: [CRITICAL/MAJOR/MINOR]
   ```

## Verification Checklist

- [ ] All strings render without truncation
- [ ] RTL languages display correctly
- [ ] CJK fonts configured and rendering
- [ ] Numbers formatted per locale
- [ ] Dates formatted per locale
- [ ] Color/symbols reviewed for cultural sensitivity
- [ ] At least 2 hours gameplay tested per language
- [ ] Native speaker QA completed
- [ ] All critical issues resolved
- [ ] Regression tested after fixes
- [ ] Final approval from native speakers obtained

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Japanese text displays as boxes | Configure CJK font, increase font size to 40+ |
| RTL text reads left-to-right | Manually mirror layout, set anchor to right |
| German text overflows button | Increase button width 35%, use flexible layout |
| Missing accents (é, ñ, ç) | Verify font includes diacritics, check encoding |
| Numbers display incorrectly (1,234 vs 1.234) | Use CultureInfo for formatting |

## Related Topics

- See `/localization-setup` for implementation
- Refer to `/accessibility-audit-workflow` for inclusion testing
- Check analytics for language adoption rates