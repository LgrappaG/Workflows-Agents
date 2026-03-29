---
version: 9.0.0
category: Localization & Analytics
agent: Localization Specialist
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ai-debugging-tools
  - animation-mocap-setup
  - ci-cd-pipeline-setup
  - data-pipeline-setup
  - godot-animation-setup
  - godot-setup
  - graphics-hdrp-setup
  - analytics-integration
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - audio-mixer-setup
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - material-visual-debugging
  - navmesh-baking-setup
  - networking-ngo-setup
  - physics-vehicle-setup
  - terrain-performance-tuning
  - custom-workflow-builder
  - ai-learning-adaptation
  - animation-constraint-rigging
  - physics-constraint-optimization
  - physics-joint-constraints
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-cave-systems
  - terrain-memory-management
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-shape-tools
  - ui-performance-optimization
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - material-mipmap-chains
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  recommended:
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - training-datasets
  - vfx-trail-rendering
  - ui-event-handlers
  - automated-testing-framework
  - performance-dashboard
  - ui-context-menus
  - ui-two-way-binding
  - build-system-optimization
  - debug-build-diagnostic
  - ui-dynamic-styling
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-modal-dialogs
  - ui-prefab-variants
  - ui-style-sheets
  - ui-text-binding
  - ui-visual-feedback
  - compatibility-testing
  - csharp-builder-pattern
  - engine-migration-guide
  - networking-guild-system
  - physics-fluid-dynamics
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-list-virtualization
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-z-ordering
  - vfx-builtin-particles
  - debug-performance-charts
  - networking-performance-monitoring
  - networking-server-security
  - animation-performance-profiling
  - debug-performance-metrics
  - debug-performance-profiler
  - performance-profiling-cross-engine
  - physics-performance-metrics
  - timeline-performance-profiling
  - networking-analytics-tracking
  - networking-player-persistence
  - audio-dialogue-system
  - debug-runtime-metrics
  - networking-achievement-tracking
  - networking-encryption
  - prediction-models
  - advanced-performance-tuning
  - audio-performance-profiling
  - cinemachine-virtual-camera
  optional:
  - csharp-performance-optimization
  - material-disney-workflow
  - material-metallic-workflow
  - material-performance-profiling
  - material-specular-workflow
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
complexity_score: 10
skill_density: 156.0
estimated_skills_needed: 156
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Analytics Integration & Telemetry Setup

This workflow implements comprehensive game analytics, crash reporting, performance metrics, and user behavior tracking for data-driven development.

## Prerequisites

- Analytics platform account (Firebase, Amplitude, Segment, or custom)
- Crash reporting service (Firebase Crashlytics, Sentry, or Bugsnag)
- Backend API endpoint (if using custom analytics)
- 1-2 weeks for full integration and testing

## Context

Analytics provide essential insights into player behavior, performance issues, monetization funnels, and helps prioritize development efforts based on real user data.

// turbo-all

## Phase 1: Choose Analytics Platform

**Option A: Firebase (Recommended for beginners)**
```plaintext
Pros: Free tier generous, built-in Crashlytics, easy setup
Analytics include: DAU, retention, funnel analysis, custom events
```

**Option B: Amplitude (Advanced analytics)**
```plaintext
Pros: Advanced cohort analysis, behavioral insights, robust API
Analytics include: User retention, funnel analysis, A/B testing
```

**Option C: Custom Backend**
```plaintext
Pros: Complete control, no vendor lock-in
Cons: Requires infrastructure, more maintenance
```

## Phase 2: Firebase Setup (if chosen)

1. **Create Firebase Project:**
   ```bash
   # Go to firebase.google.com
   # Create new project
   # Register app: Select "Unity"
   # Download GoogleService-Info.plist (iOS) or google-services.json (Android)
   ```

2. **Install Firebase SDK:**
   ```bash
   # Package Manager → Add package from git URL
   # https://github.com/firebase/firebase-sdk-unity.git

   # Or download .unitypackage manually
   # Import: Assets → Firebase → Use Installed Packages
   ```

3. **Initialize Firebase in Code:**
   ```csharp
   using Firebase;
   using Firebase.Analytics;
   using Firebase.Crashlytics;

   public class AnalyticsManager : MonoBehaviour
   {
       private void Start()
       {
           FirebaseApp.CheckAndFixDependenciesAsync().ContinueWith(task => {
               if (task.IsCompleted) {
                   if (task.Exception != null) {
                       Debug.LogError(task.Exception);
                   } else {
                       FirebaseAnalytics.LogEvent("app_started");
                       Crashlytics.ReportException(new System.Exception("Test"));
                   }
               }
           });
       }
   }
   ```

## Phase 3:Set Up Standard Events

1. **Firebase Predefined Events:**
   ```csharp
   // Player progression
   FirebaseAnalytics.LogEvent("level_start", new Parameter("level_name", "Level_5"));
   FirebaseAnalytics.LogEvent("level_end",
       new Parameter("level_name", "Level_5"),
       new Parameter("success", true));

   // In-app purchase
   FirebaseAnalytics.LogEvent("in_app_purchase",
       new Parameter("item_name", "Premium Pass"),
       new Parameter("currency", "USD"),
       new Parameter("value", 9.99f));

   // Tutorial completion
   FirebaseAnalytics.LogEvent("tutorial_complete",
       new Parameter("tutorial_type", "basic_controls"));
   ```

2. **Custom Event Tracking:**
   ```csharp
   public class GameEventTracker
   {
       public void TrackPlayerAction(string action, Dictionary<string, object> parameters)
       {
           var params_array = parameters.Select(p =>
               new Parameter(p.Key, p.Value)).ToArray();
           FirebaseAnalytics.LogEvent(action, params_array);
       }

       // Usage example
       public void OnEnemyDefeated(Enemy enemy) {
           TrackPlayerAction("enemy_defeated", new Dictionary<string, object> {
               { "enemy_type", enemy.type },
               { "damage_taken", enemy.damageInflicted },
               { "time_to_defeat", Time.time - enemy.spawnTime }
           });
       }
   }
   ```

## Phase 4: Crash Reporting Configuration

1. **Enable Crashlytics:**
   ```csharp
   using Firebase.Crashlytics;

   void Start()
   {
       #if !DEBUG
       Crashlytics.ReportUncaughtExceptionsAsFatal = true;
       #endif
   }

   void OnException(Exception ex)
   {
       Crashlytics.LogException(ex);
   }
   ```

2. **Add Custom Metadata to Crashes:**
   ```csharp
   // Add context to crash reports
   Crashlytics.SetCustomKey("player_level", currentLevel);
   Crashlytics.SetCustomKey("enemies_defeated", enemyCount);
   Crashlytics.SetCustomKey("playtime_minutes", (int)(Time.time / 60));

   // Track user identifiers
   Crashlytics.SetUserId(playerUID);
   ```

3. **Manual Crash Report (Testing):**
   ```csharp
   #if UNITY_EDITOR
   public void TestCrashReport() {
       Crashlytics.ReportException(new System.Exception("Test crash"));
   }
   #endif
   ```

## Phase 5: Performance Monitoring

1. **Track Frame Rate & Performance:**
   ```csharp
   public class PerformanceMonitor : MonoBehaviour
   {
       private float _fps;
       private int _frameCount;
       private float _timeSinceLastUpdate;

       private void Update()
       {
           _frameCount++;
           _timeSinceLastUpdate += Time.deltaTime;

           if (_timeSinceLastUpdate >= 1f)
           {
               _fps = _frameCount / _timeSinceLastUpdate;

               // Log if FPS drops below threshold
               if (_fps < 30f)
               {
                   FirebaseAnalytics.LogEvent("performance_warning",
                       new Parameter("fps", _fps),
                       new Parameter("scene", SceneManager.GetActiveScene().name));
               }

               _frameCount = 0;
               _timeSinceLastUpdate = 0f;
           }
       }
   }
   ```

2. **Memory Usage Tracking:**
   ```csharp
   public void TrackMemoryUsage()
   {
       long memoryMB = System.GC.GetTotalMemory(false) / 1024 / 1024;
       FirebaseAnalytics.LogEvent("memory_usage",
           new Parameter("memory_mb", memoryMB),
           new Parameter("device", SystemInfo.deviceName));
   }
   ```

## Phase 6: User Behavior Funnel Tracking

1. **Onboarding Flow:**
   ```csharp
   public class OnboardingTracker
   {
       public void OnTutorialStarted() =>
           FirebaseAnalytics.LogEvent("tutorial_started");

       public void OnTutorialSkipped() =>
           FirebaseAnalytics.LogEvent("tutorial_skipped");

       public void OnTutorialComplete() =>
           FirebaseAnalytics.LogEvent("tutorial_complete");

       public void OnFirstGameStart() =>
           FirebaseAnalytics.LogEvent("first_game_started");
   }
   ```

2. **Monetization Funnel:**
   ```csharp
   public class MonetizationTracker
   {
       public void TrackIAPView(string itemID) =>
           FirebaseAnalytics.LogEvent("view_item",
               new Parameter("item_id", itemID));

       public void TrackIAPInitiated(string itemID) =>
           FirebaseAnalytics.LogEvent("begin_checkout",
               new Parameter("item_id", itemID));

       public void TrackIAPCompleted(string itemID, double price) =>
           FirebaseAnalytics.LogEvent("purchase",
               new Parameter("item_id", itemID),
               new Parameter("value", price),
               new Parameter("currency", "USD"));
   }
   ```

## Phase 7: A/B Testing Setup (Advanced)

1. **Firebase Remote Config for A/B Tests:**
   ```csharp
   using Firebase.RemoteConfig;

   public void InitializeRemoteConfig()
   {
       var defaults = new Dictionary<string, object>
       {
           { "difficulty_multiplier", 1.0 },
           { "ad_frequency_minutes", 5 },
           { "enable_feature_x", false }
       };

       FirebaseRemoteConfig.DefaultInstance.SetDefaults(defaults);
       FirebaseRemoteConfig.DefaultInstance.FetchAsync().ContinueWith(FetchComplete);
   }

   private void FetchComplete(Task task)
   {
       if (task.IsCompleted)
       {
           FirebaseRemoteConfig.DefaultInstance.ActivateFetched();
           double difficultyMultiplier = FirebaseRemoteConfig.DefaultInstance
               .GetValue("difficulty_multiplier").DoubleValue;

           // Apply A/B test value
           ApplyDifficulty(difficultyMultiplier);
       }
   }
   ```

## Phase 8: Opt-In & Privacy Compliance

1. **GDPR Consent Management:**
   ```csharp
   public class PrivacyManager
   {
       private bool _analyticsConsent;

       public void RequestAnalyticsConsent()
       {
           // Show consent dialog
           // Save consent to PlayerPrefs
           _analyticsConsent = PlayerPrefs.GetInt("AnalyticsConsent", 0) == 1;

           // Disable analytics if not consented
           if (!_analyticsConsent)
           {
               FirebaseAnalytics.SetAnalyticsCollectionEnabled(false);
           }
       }

       public void SetAnalyticsConsent(bool consented)
       {
           _analyticsConsent = consented;
           PlayerPrefs.SetInt("AnalyticsConsent", consented ? 1 : 0);
           FirebaseAnalytics.SetAnalyticsCollectionEnabled(consented);
       }
   }
   ```

## Verification Checklist

- [ ] Analytics platform account created and verified
- [ ] SDK installed and initialized in game
- [ ] Standard events (level_start, level_end, purchase) logging correctly
- [ ] Crash reporting active and receiving test crashes
- [ ] Performance metrics collected (FPS, memory)
- [ ] Funnel events (onboarding, monetization) tracking
- [ ] Console dashboard shows real data
- [ ] Privacy/consent dialog implemented
- [ ] Opt-out working correctly
- [ ] Test data verified in backend dashboard
- [ ] Production build tested on real device

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Events not appearing in dashboard | Check Internet connection, verify API key correct, wait 24h for first data |
| SDK initialization fails | Verify GoogleService files downloaded correctly, check build target platform |
| Crashes not reported | Ensure Crashlytics enabled, app not in dev build mode |
| Privacy concerns | Always show consent dialog before collecting data |

## Related Topics

- See `/gdpr-compliance-setup` for privacy compliance details
- Refer to `/project-health-check` for monitoring dashboards
- Check `/security-vulnerability-scan` for data security