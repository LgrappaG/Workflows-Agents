---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - ai-debugging-tools
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - networking-ngo-setup
  - graphics-urp-setup
  - ci-cd-pipeline-setup
  - animation-mocap-setup
  - data-pipeline-setup
  - debug-shader-debugging
  - godot-animation-setup
  - godot-setup
  - animation-mirror-setup
  - audio-mixer-setup
  - debug-renderer-debugging
  - machine-learning-setup
  - material-pbr-setup
  - navmesh-baking-setup
  - physics-vehicle-setup
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - debug-script-debugging
  - material-translucency-setup
  - material-visual-debugging
  - analytics-integration
  - networking-performance-monitoring
  - custom-workflow-builder
  - terrain-performance-tuning
  - ui-performance-optimization
  - networking-server-security
  - animation-performance-profiling
  - cinemachine-virtual-camera
  - debug-performance-charts
  - debug-performance-metrics
  - debug-performance-profiler
  - performance-dashboard
  - performance-profiling-cross-engine
  - timeline-performance-profiling
  - audio-performance-profiling
  - automated-testing-framework
  - csharp-performance-optimization
  - physics-performance-metrics
  - physics-performance-profiling
  - advanced-performance-tuning
  - compatibility-testing
  - material-disney-workflow
  - material-metallic-workflow
  - material-performance-profiling
  - material-specular-workflow
  - networking-guild-system
  - networking-server-maintenance
  - timeline-camera-transitions
  - networking-analytics-tracking
  - networking-cloud-saves
  - ui-event-handlers
  - build-system-optimization
  - csharp-chain-of-responsibility
  - graphics-gpu-profiling
  - networking-bandwidth-optimization
  - networking-connection-management
  - networking-encryption
  - networking-lag-compensation
  - networking-lobby-system
  - networking-replay-system
  - physics-joint-constraints
  - terrain-brush-settings
  - ui-context-menus
  - ui-two-way-binding
  - ui-visual-feedback
  - ai-learning-adaptation
  - animation-constraint-rigging
  - cinemachine-aim-assist
  - debug-build-diagnostic
  - graphics-memory-profiling
  - graphics-motion-blur
  - graphics-shadow-optimization
  - material-mipmap-chains
  - networking-achievement-tracking
  - networking-leaderboard
  - networking-player-persistence
  - networking-prediction-reconciliation
  - networking-presence-system
  - networking-reward-distribution
  - networking-server-authority
  - physics-constraint-optimization
  - terrain-cave-systems
  - terrain-grass-placement
  - terrain-heightmap-import
  - terrain-memory-management
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-shape-tools
  - terrain-water-integration
  - terrain-wind-zones
  - ui-anchor-positioning
  - ui-auto-layout
  - ui-input-validation
  recommended:
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-panel-layout
  - ui-prefab-variants
  - ui-text-binding
  - ui-touch-input
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - csharp-async-await
  - csharp-builder-pattern
  - engine-migration-guide
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-frame-debugger
  - graphics-geometry-optimization
  - graphics-light-baking
  - graphics-postprocessing
  - graphics-probe-placement
  - graphics-realtime-gi
  - graphics-reflection-probes
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - networking-account-recovery
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-authentication
  - networking-ban-system
  - networking-battle-pass
  - networking-chat-system
  - networking-client-authority
  - networking-cross-progression
  - networking-friend-system
  - networking-interpolation
  - networking-matchmaking
  - networking-message-ordering
  - networking-packet-loss-handling
  - networking-player-spawning
  - networking-pvp-ranking
  - networking-region-selection
  - networking-rollback-resimulation
  - networking-rpc-system
  - networking-server-load-balancing
  - networking-server-replication
  - networking-spectator-mode
  - networking-state-synchronization
  - networking-statistics-synchronization
  - networking-trading-system
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-heightfield-editing
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - training-datasets
  - ui-accessibility
  - ui-animation-states
  - ui-animation-tweens
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-focus-navigation
  optional:
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-list-virtualization
  - ui-modal-dialogs
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
skill_density: 201.0
estimated_skills_needed: 201
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# iOS-Specific Setup & Deployment

This workflow guides iOS-specific project setup, code signing, provisioning profiles, TestFlight beta testing, and App Store release configuration.

## Prerequisites

- Xcode 15+ installed
- Apple Developer Account ($99/year)
- iOS deployment target: 14.4+ (recommended 15.0+)
- Unity 2022 LTS with iOS Build Support
- Mac for final build (simulator testing possible on Windows)
- 5GB free disk space

## Context

iOS development requires Apple's ecosystem integration: code signing, provisioning profiles, and App Store Connect configuration. This workflow ensures secure, compliant builds.

// turbo-all

## Phase 1: Apple Developer Setup

1. **Enroll in Apple Developer Program:**
   - Visit developer.apple.com → Register
   - Complete identity verification
   - Obtain Team ID (10-character code)

2. **Create App Identifier:**
   - App Store Connect → Apps → New App
   - Select organization type: Individual or Company
   - Create Bundle ID: `com.company.gamename` (reverse domain style)
   - Enable capabilities needed by your game

3. **Configure Certificates:**
   ```plaintext
   Keychain Access → Certificate Assistant → Request a Certificate
   - From a Certificate Authority
   - Create Apple Development Certificate
   - Upload to Certificates.p8 (private key)
   ```

## Phase 2: Provisioning Profiles & Signing

1. **Create Development Provisioning Profile:**
   - Developer.apple.com → Certificates, IDs & Profiles
   - Register test devices via UDID
   - Create profile: Development → Select App ID → Select Certificates → Select Devices
   - Download `.mobileprovision` file

2. **Create Distribution Provisioning Profile:**
   ```plaintext
   For App Store distribution:
   - Type: App Store
   - Select same App ID and Distribution Certificate
   - Download `.mobileprovision` file
   ```

3. **Import into Xcode:**
   ```bash
   # Copy profiles to Xcode
   cp your_profile.mobileprovision "~/Library/MobileDevice/Provisioning Profiles/"
   ```

## Phase 3: Unity iOS Player Settings

1. **Configure iOS Build Settings:**
   ```plaintext
   File → Build Settings → iOS
   - Target Device: iPhone, iPad, or both
   - SDK: Latest (e.g., iOS 17.2)
   - Supported Orientations: Set Portrait/Landscape
   ```

2. **Player Settings Configuration:**
   - **Company Name**: Your company
   - **Product Name**: Game name
   - **Package Name**: Bundle ID (e.g., com.company.game)
   - **Version**: 1.0.0
   - **Bundle Version**: 1

3. **Graphics & Performance:**
   - **Graphics APIs**: Metal (default, recommended)
   - **Script Settings**: IL2CPP backend
   - **Manage Stripping Level**: High
   - **GPU Instancing**: Enable

4. **Capabilities (Player Settings → Other Settings):**
   ```plaintext
   Enable required capabilities:
   - Network: Allows Arbitrary Loads (if needed)
   - HomeKit: If applicable
   - HealthKit: If applicable
   - Permissions in Info.plist:
     - Camera Usage Description
     - Microphone Usage Description
     - Photo Library Usage Description
   ```

## Phase 4: Generate Xcode Project

1. **Build Xcode Project from Unity:**
   ```bash
   # File → Build and Run (Mac only)
   # Or custom build script:
   unity -batchmode -quit -executeMethod BuildTools.BuildiOS
   ```

2. **Verify Generated Xcode Project:**
   ```plaintext
   Open generated project:
   - YourGame.xcodeproj
   - Check: Signing & Capabilities tab
   - Verify Team ID is set correctly
   - Confirm provisioning profile selected
   ```

## Phase 5: Local Testing & Profiling

1. **Test on Simulator (Mac):**
   ```bash
   xcodebuild -scheme YourGame -configuration Debug -sdk iphonesimulator -derivedDataPath build
   ```

2. **Test on Device (Tethered to Mac):**
   ```bash
   # Connect iPhone via USB
   # In Xcode: Select device from scheme dropdown
   # Build & Run (⌘R)
   ```

3. **Profile Performance:**
   - Use Xcode Instruments: Product → Profile
   - Monitor: CPU, Memory, GPU metrics
   - Check FPS via Xcode Console output

## Phase 6: TestFlight Beta Distribution

1. **Build Release Binary:**
   ```plaintext
   In Xcode:
   - Set scheme to Release
   - Archive: Product → Archive
   - Distribute: Select App Store Connect
   - Configure signing with Distribution Certificate
   ```

2. **Upload to App Store Connect:**
   ```bash
   # Automatic via Xcode:
   # Select archive → Distribute App → App Store Connect → Upload
   ```

3. **Configure TestFlight Settings:**
   - App Store Connect → Your App → TestFlight
   - Add Beta Testers (internal team or external via email)
   - Write Build Notes (what to test)
   - Select OS versions to test on

4. **Distribute Build:**
   ```plaintext
   - Testers receive email invite
   - Download via TestFlight app
   - Provide feedback for 7-14 days
   - Collect crash reports via Crashlytics
   ```

## Phase 7: App Store Release

1. **Prepare App Store Listing:**
   - Screenshots: 5- per device type (6.5", 5.5", etc.)
   - Preview video: 30 seconds max
   - Description, Keywords, Category
   - Content Rating Questionnaire (ESRB)

2. **Version Release Notes:**
   ```plaintext
   Example:
   Version 1.0.0 - Launch
   - Initial release
   - 60 FPS gameplay
   - Supports iPhone 12+
   - Optimized for A15 Bionic chip
   ```

3. **Submit for Review:**
   - App Store Connect → Your App → Pricing & Availability
   - Select countries/regions
   - Agree to export compliance (ITAR/EAR)
   - Submit for Review

4. **Monitor Review Status:**
   - Typically 24-48 hours
   - App Store Connect → Your App → Activity
   - Respond to any review feedback

## Phase 8: Post-Launch Monitoring

1. **Monitor App Store Connect Analytics:**
   - Sales, downloads, crashes
   - Crashes & Exceptions tab
   - Set up notifications for critical crashes

2. **Integrate Crash Reporting:**
   - Use Firebase Crashlytics
   - Or use Sentry for iOS

3. **Monitor Performance Metrics:**
   - App Store Connect → Metrics
   - Track: Crash rate, ANR equivalents, battery drain

## Verification Checklist

- [ ] Apple Developer Account active
- [ ] Bundle ID registered and valid
- [ ] Code signing certificates installed
- [ ] Provisioning profiles downloaded and verified
- [ ] Xcode project builds without warnings
- [ ] TestFlight build successfully uploaded
- [ ] 5+ beta testers confirmed build receipt
- [ ] No crashes in beta testing phase
- [ ] App Store listing complete with screenshots
- [ ] Build submitted for App Store review
- [ ] Launch version available on App Store

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| "Code signing identity missing" errors | Verify provisioning profile in Xcode Build Settings |
| TestFlight build stuck "Processing" | Can take 15 min; wait or check Console.developer.apple.com for errors |
| "Export failed: Your Team has no enrolled Account Holder" | Add account holder role in App Store Connect → Users |
| Crashes on specific iOS versions | Test on multiple iOS 14, 15, 16, 17 simulators |
| Build rejected: "Inadequate Encryption" | Add NSLocalNetworkUsageDescription to Info.plist if using local network |

## Related Topics

- See `/analytics-integration` for crash reporting setup
- Refer to `@mobile-expert` skill for iOS-specific patterns
- Check `/gdpr-compliance-setup` for user data handling