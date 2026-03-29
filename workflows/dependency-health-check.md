---
version: 9.0.0
category: Skill & Workflow Management
agent: Tech Lead
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - networking-server-security
  - material-specular-workflow
  - networking-ngo-setup
  - networking-server-maintenance
  - physics-constraint-optimization
  - ai-debugging-tools
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - networking-guild-system
  - ui-keyboard-shortcuts
  - ui-style-sheets
  - automated-testing-framework
  - build-system-optimization
  - ci-cd-pipeline-setup
  - csharp-chain-of-responsibility
  - graphics-sorting-layers
  - material-mipmap-chains
  - networking-lobby-system
  - networking-performance-monitoring
  - networking-server-authority
  - terrain-biome-definition
  - terrain-noise-functions
  - terrain-shape-tools
  - terrain-water-integration
  - ui-animation-states
  - ui-auto-layout
  - ui-context-menus
  - ui-drag-drop
  - ui-event-handlers
  - ui-focus-navigation
  - ui-input-validation
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-text-binding
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-z-ordering
  - csharp-adapter-pattern
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-baking-setup
  - animation-constraint-rigging
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-ducking-sidechains
  - audio-mixer-setup
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - data-pipeline-setup
  - debug-build-diagnostic
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - engine-migration-guide
  - godot-animation-setup
  - godot-setup
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-bloom-effect
  - graphics-culling-strategies
  recommended:
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
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-temporal-antialiasing
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - material-visual-debugging
  - navmesh-baking-setup
  - networking-account-recovery
  - networking-achievement-tracking
  - networking-analytics-tracking
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-authentication
  - networking-ban-system
  - networking-bandwidth-optimization
  - networking-battle-pass
  - networking-chat-system
  - networking-client-authority
  - networking-cloud-saves
  - networking-connection-management
  - networking-cross-progression
  - networking-encryption
  - networking-friend-system
  - networking-interpolation
  - networking-lag-compensation
  - networking-leaderboard
  - networking-matchmaking
  - networking-message-ordering
  - networking-packet-loss-handling
  - networking-player-persistence
  - networking-player-spawning
  - networking-prediction-reconciliation
  - networking-presence-system
  - networking-pvp-ranking
  - networking-region-selection
  - networking-replay-system
  - networking-reward-distribution
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
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-advanced-editing
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  optional:
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
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
skill_density: 15.9
estimated_skills_needed: 159
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Dependency Health Check Workflow

Audit your Unity project's packages and dependencies for potential issues.

## 1. Trigger the Check

Tell the agent to run the health check:
- "Check my Unity packages for updates"
- "Are any of my dependencies deprecated?"
- "Run a dependency health check"
- "Check package compatibility for Unity 2023"

## 2. Gather Dependency Information (Agent Action)

// turbo
```bash
echo "=== Package Manifest ==="
cat Packages/manifest.json

echo ""
echo "=== Installed Packages ==="
cat Packages/packages-lock.json 2>/dev/null || echo "No lock file found"

echo ""
echo "=== Unity Version ==="
cat ProjectSettings/ProjectVersion.txt
```

## 3. Health Check Categories

The agent evaluates each package against:

### 🔴 Critical Issues
- **Deprecated packages** — Marked for removal in future Unity versions
- **Security vulnerabilities** — Known CVEs or security advisories
- **Incompatible versions** — Package doesn't support current Unity version
- **Conflicting dependencies** — Two packages require incompatible versions

### 🟡 Warnings
- **Major version behind** — Newer major version available (may have breaking changes)
- **Preview/Experimental** — Using non-production packages in production
- **Unsupported platform** — Package doesn't support target platform (Quest, etc.)

### 🔵 Info
- **Minor/Patch updates available** — Safe updates with bug fixes
- **Unused packages** — Installed but not referenced in code

---

## 4. Common Unity Packages to Check

| Package | Check For |
|---------|-----------|
| `com.unity.xr.interaction.toolkit` | XRI 3.x migration, deprecated APIs |
| `com.unity.xr.oculus` | Quest SDK version, passthrough support |
| `com.unity.inputsystem` | Legacy Input Manager conflicts |
| `com.unity.netcode.gameobjects` | Version compatibility, transport layer |
| `com.unity.addressables` | Catalog version, build script updates |
| `com.unity.render-pipelines.universal` | URP version matches Unity |
| `com.unity.textmeshpro` | Now built into Unity 2023+ |

---

## 5. Generate Health Report

// turbo
```bash
cat > dependency-health-report.md << 'REPORT_HEADER'
# Dependency Health Report

Generated: $(date +%Y-%m-%d)

## Summary

| Status | Count |
|--------|-------|
| 🔴 Critical | 0 |
| 🟡 Warning | 0 |
| 🔵 Info | 0 |
| ✅ Healthy | 0 |

---

## Detailed Findings

(Agent populates this section)

---

## Recommended Actions

(Agent provides prioritized action items)

REPORT_HEADER

echo "Report template created. Agent will populate findings."
```

## 6. Report Format

The agent generates findings like:

```markdown
### 🔴 Critical

#### com.unity.xr.oculus (v4.0.0)
- **Issue:** Deprecated. Use `com.meta.xr.sdk.all` instead
- **Impact:** May break in Unity 2025
- **Action:** Migrate to Meta XR SDK
- **Guide:** https://developer.oculus.com/documentation/unity/unity-import/

### 🟡 Warning

#### com.unity.netcode.gameobjects (v1.5.0)
- **Issue:** v1.8.0 available with important fixes
- **Impact:** Missing connection stability improvements
- **Action:** Update after testing multiplayer flows
- **Breaking Changes:** None in minor version

### 🔵 Info

#### com.unity.textmeshpro (v3.0.6)
- **Issue:** Now included in Unity 2023+ core
- **Impact:** Redundant package
- **Action:** Can remove explicit dependency
```

---

## 7. Auto-Fix Safe Updates (Optional)

If requested, the agent can apply safe updates:

```bash
# Backup manifest first
cp Packages/manifest.json Packages/manifest.json.backup

# Update specific package (patch version only)
# Agent modifies manifest.json
```

**Rules for auto-fix:**
- ✅ Patch versions (1.0.0 → 1.0.1) — Safe
- ⚠️ Minor versions (1.0.0 → 1.1.0) — Ask first
- ❌ Major versions (1.0.0 → 2.0.0) — Never auto-update

---

## 8. Deprecated API Scan

The agent also scans C# code for deprecated Unity APIs:

```bash
# Find deprecated API usage
grep -rn "GetComponent<" --include="*.cs" Assets/Scripts/ | head -20
grep -rn "FindObjectOfType" --include="*.cs" Assets/Scripts/ | head -20
grep -rn "SendMessage" --include="*.cs" Assets/Scripts/ | head -20
```

Common deprecations to flag:
- `WWW` → `UnityWebRequest`
- `Application.LoadLevel` → `SceneManager.LoadScene`
- `OnGUI` → UI Toolkit / uGUI
- `FindObjectOfType` (in Update) → Cached reference

---

## 9. Platform Compatibility Matrix

The agent verifies packages support target platforms:

| Package | Standalone | Android/Quest | iOS | WebGL |
|---------|------------|---------------|-----|-------|
| XR Interaction Toolkit | ✅ | ✅ | ❌ | ❌ |
| Addressables | ✅ | ✅ | ✅ | ⚠️ |
| Netcode for GameObjects | ✅ | ✅ | ✅ | ❌ |

---

## 10. Schedule Regular Checks

Recommended frequency:
- **Before major releases** — Full health check
- **Monthly** — Quick update scan
- **After Unity upgrade** — Compatibility verification

---

## Example Commands

- "Run a full dependency health check"
- "Check if my packages support Quest 3"
- "Find deprecated API usage in my scripts"
- "What packages need updates?"
- "Is my project ready for Unity 2024 upgrade?"