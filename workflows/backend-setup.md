---
version: 9.0.0
category: Multiplayer & Backend
agent: Backend Specialist
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - networking-ngo-setup
  - networking-statistics-synchronization
  - networking-guild-system
  - networking-lobby-system
  - networking-server-maintenance
  - networking-server-security
  - networking-analytics-tracking
  - networking-cloud-saves
  - networking-player-persistence
  - networking-leaderboard
  - networking-pvp-ranking
  - networking-server-authority
  - networking-server-replication
  - ai-debugging-tools
  - networking-achievement-tracking
  - networking-authentication
  - networking-connection-management
  - networking-encryption
  - networking-matchmaking
  - networking-packet-loss-handling
  - networking-performance-monitoring
  - networking-prediction-reconciliation
  - networking-region-selection
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - networking-account-recovery
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-ban-system
  - networking-bandwidth-optimization
  - networking-battle-pass
  - networking-chat-system
  - networking-client-authority
  - networking-cross-progression
  - networking-friend-system
  - networking-interpolation
  - networking-lag-compensation
  - networking-message-ordering
  - networking-player-spawning
  - networking-presence-system
  - networking-replay-system
  - networking-reward-distribution
  - networking-rollback-resimulation
  - networking-rpc-system
  - networking-server-load-balancing
  - networking-spectator-mode
  - networking-state-synchronization
  - networking-trading-system
  - animation-mocap-setup
  - machine-learning-setup
  - terrain-noise-functions
  - ui-keyboard-shortcuts
  - ui-two-way-binding
  - ai-learning-adaptation
  - animation-constraint-rigging
  - automated-testing-framework
  - ci-cd-pipeline-setup
  - compatibility-testing
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - godot-animation-setup
  - material-mipmap-chains
  - physics-joint-constraints
  - terrain-biome-definition
  - terrain-cave-systems
  - terrain-grass-placement
  - terrain-heightmap-import
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-shape-tools
  - terrain-vegetation-placement
  - terrain-water-integration
  recommended:
  - ui-context-menus
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-list-repeater
  - ui-panel-layout
  - ui-prefab-variants
  - ui-text-binding
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - audio-ducking-sidechains
  - audio-mixer-setup
  - build-system-optimization
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-pbr-setup
  - material-translucency-setup
  - material-visual-debugging
  - navmesh-baking-setup
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-heightfield-editing
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-performance-tuning
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-wind-zones
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  optional:
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-focus-navigation
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
complexity_score: 5.0
skill_density: 19.25
estimated_skills_needed: 154
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Backend Setup Workflow

Scaffold backend infrastructure for your game using `@backend-specialist`.

## 1. Define Backend Requirements

Tell the agent what you need:
- "Set up a leaderboard API"
- "Create player save cloud sync"
- "Build matchmaking backend"
- "Set up analytics pipeline"

## 2. Architecture Decision (Agent Action)

The agent recommends based on your needs:

| Use Case | Recommended Stack |
|----------|-------------------|
| Simple leaderboards | Firebase Realtime DB |
| Player accounts/saves | PlayFab or Firebase Auth + Firestore |
| Matchmaking | Photon or Unity Relay + Lobby |
| Analytics | Unity Analytics or GameAnalytics |
| Custom logic | Cloud Functions (Firebase/AWS Lambda) |

## 3. Service Selection

### BaaS Options (Backend-as-a-Service)

| Service | Best For | Pricing |
|---------|----------|---------|
| Firebase | Quick setup, realtime data | Free tier generous |
| PlayFab | Full game backend | Free up to 100K MAU |
| AWS GameLift | Dedicated servers | Pay per use |
| Photon | Multiplayer | CCU-based |
| Unity Gaming Services | Integrated with Unity | Free tier available |

## 4. Setup Steps

### Option A: Firebase Setup

// turbo
```bash
echo "=== Firebase Setup Guide ==="
echo ""
echo "1. Create project at https://console.firebase.google.com"
echo "2. Download google-services.json (Android) or GoogleService-Info.plist (iOS)"
echo "3. Place in Assets/StreamingAssets/"
echo ""
echo "Required Unity packages:"
echo "  - com.google.firebase.auth"
echo "  - com.google.firebase.firestore"
echo "  - com.google.firebase.analytics"
```

### Option B: PlayFab Setup

// turbo
```bash
echo "=== PlayFab Setup Guide ==="
echo ""
echo "1. Create account at https://playfab.com"
echo "2. Create a new Title"
echo "3. Get Title ID from Settings"
echo ""
echo "Required: PlayFab Unity SDK"
echo "  - Download from PlayFab documentation"
echo "  - Import PlayFabSDK.unitypackage"
```

## 5. Common Patterns

### Player Authentication
```csharp
// Firebase Anonymous Auth
public async Task<string> SignInAnonymously()
{
    var auth = FirebaseAuth.DefaultInstance;
    var result = await auth.SignInAnonymouslyAsync();
    return result.User.UserId;
}
```

### Cloud Save
```csharp
// Firestore save
public async Task SavePlayerData(string playerId, PlayerData data)
{
    var db = FirebaseFirestore.DefaultInstance;
    var docRef = db.Collection("players").Document(playerId);
    await docRef.SetAsync(data);
}
```

### Leaderboard
```csharp
// Get top 10 scores
public async Task<List<LeaderboardEntry>> GetTopScores()
{
    var db = FirebaseFirestore.DefaultInstance;
    var query = db.Collection("leaderboard")
        .OrderByDescending("score")
        .Limit(10);

    var snapshot = await query.GetSnapshotAsync();
    return snapshot.Documents.Select(d => d.ConvertTo<LeaderboardEntry>()).ToList();
}
```

## 6. Security Rules

The agent generates security rules:

```javascript
// Firestore Rules Example
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Players can only read/write their own data
    match /players/{playerId} {
      allow read, write: if request.auth != null && request.auth.uid == playerId;
    }

    // Leaderboard: anyone can read, only server can write
    match /leaderboard/{entry} {
      allow read: if true;
      allow write: if false; // Use Cloud Functions
    }
  }
}
```

## 7. Testing Checklist

- [ ] Authentication works (anonymous/social)
- [ ] Data persists across sessions
- [ ] Offline handling graceful
- [ ] Rate limiting in place
- [ ] Error handling comprehensive

## 8. Generate Config

// turbo
```bash
mkdir -p Assets/Config

cat > Assets/Config/BackendConfig.cs << 'EOF'
// Auto-generated backend configuration
public static class BackendConfig
{
    // TODO: Replace with your actual values
    public const string FirebaseProjectId = "your-project-id";
    public const string PlayFabTitleId = "your-title-id";
    public const string ApiBaseUrl = "https://your-api.com";
}
EOF

echo "✅ Backend config created: Assets/Config/BackendConfig.cs"
echo "⚠️  Remember to update with your actual credentials!"
```

## Example Commands

- "Set up Firebase for player saves and leaderboards"
- "Create PlayFab backend for my multiplayer game"
- "Design the API for my inventory system"
- "Set up cloud functions for server-authoritative actions"