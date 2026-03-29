---
version: 9.0.0
category: Skill & Workflow Management
agent: Tech Lead
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - networking-ngo-setup
  - analytics-integration
  - networking-performance-monitoring
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - networking-guild-system
  - networking-server-maintenance
  - networking-server-security
  - animation-mocap-setup
  - ci-cd-pipeline-setup
  - networking-bandwidth-optimization
  - networking-lobby-system
  - ui-performance-optimization
  - ai-debugging-tools
  - automated-testing-framework
  - data-pipeline-setup
  - machine-learning-setup
  - networking-analytics-tracking
  - networking-leaderboard
  - networking-server-authority
  - terrain-performance-tuning
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - audio-mixer-setup
  - compatibility-testing
  - godot-animation-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - networking-account-recovery
  - networking-achievement-tracking
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-authentication
  - networking-ban-system
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
  - physics-vehicle-setup
  - build-system-optimization
  - performance-dashboard
  - csharp-performance-optimization
  - debug-build-diagnostic
  - debug-performance-charts
  - debug-performance-profiler
  - physics-constraint-optimization
  - terrain-memory-management
  - timeline-performance-profiling
  - ui-context-menus
  - ui-keyboard-shortcuts
  recommended:
  - ui-two-way-binding
  - ai-perception-system
  - animation-constraint-rigging
  - animation-performance-profiling
  - audio-performance-profiling
  - debug-performance-metrics
  - debug-shader-debugging
  - material-performance-profiling
  - physics-joint-constraints
  - physics-performance-metrics
  - physics-performance-profiling
  - terrain-biome-definition
  - terrain-cave-systems
  - terrain-path-carving
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-input-validation
  - ui-prefab-variants
  - ui-text-binding
  - advanced-performance-tuning
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - debug-renderer-debugging
  - debug-script-debugging
  - engine-migration-guide
  - material-mipmap-chains
  - material-visual-debugging
  - performance-profiling-cross-engine
  - physics-chain-dynamics
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-advanced-editing
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
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  optional:
  - ui-drag-drop
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
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
skill_density: 173.0
estimated_skills_needed: 173
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Project Health Check Monitoring

Automated daily health checks: build status, test coverage, performance metrics, crash trends.

## Prerequisites

- CI/CD pipeline (GitHub Actions, Jenkins, etc.)
- Monitoring service (Datadog, New Relic, or custom)
- 2 weeks setup

// turbo-all

## Phase 1: Define Health Metrics

```markdown
**Build Health:**
- Build success rate (target: 100%)
- Build time (target: <30min)
- Test pass rate (target: >95%)

**Performance Health:**
- Average FPS (target: 60 FPS)
- Memory usage (target: <512MB mobile)
- Crash rate (target: <0.1%)

**Code Health:**
- Test coverage (target: >60%)
- Code duplication (target: <5%)
- Technical debt (target: trending down)

**User Health:**
- DAU (Daily Active Users)
- Retention (1-day: >30%)
- Crash reports per session
```

## Phase 2: Create Health Dashboard

```bash
# Tools: Grafana + Prometheus for metrics
# Or: Custom Dashboard via Google Sheets + Apps Script

# Metrics to track:
POST /health-check endpoint monthly:
{
  "build_status": "success",
  "test_pass_rate": 0.98,
  "avg_fps": 58,
  "crash_rate": 0.001,
  "test_coverage": 0.68,
  "players_online": 1234,
  "ccu_peak": 5678
}
```

## Phase 3: Automated Daily Checks

```bash
#!/bin/bash
# health-check.sh - runs daily via cron

# Build check
unity -batchmode -quit -buildTarget Standalone

# Test check
unity -runTests -testResults results.xml

# Profiler check
# Run on dev build, capture memory/fps

# Push metrics
curl -X POST "https://monitoring.game.com/health" \
  -d @health_metrics.json
```

## Phase 4: Alert Thresholds

```markdown
**RED Alert (Immediate Action):**
- Build failure
- Test pass rate <90%
- Crash rate >1%
- Memory leak detected

**YELLOW Alert (This Week):**
- Test pass rate 90-95%
- FPS drops to 50-60
- Crash rate 0.1-1%

**GREEN (Normal Operations)**
- All metrics green
- Trending positive
```

## Phase 5: Health Report Template

```markdown
## Project Health Report - March 19, 2026

### Status: ✅ HEALTHY

**Build:** 100% (36 builds)
**Tests:** 98% (2,450 tests)
**FPS:** 58 avg (target 60)
**Crash Rate:** 0.08% (target <0.1%)
**Memory:** 380MB avg (target <512)
**Test Coverage:** 68% (target >60%)

### Alerts: 0 Red, 1 Yellow
- ⚠️ CPU usage 15% above normal (investigation needed)

### Actions This Week:
- [ ] Optimize shader compilation (improvement +5% build time)
- [ ] Fix memory leak in NetworkManager
- [ ] Add 10 new unit tests (coverage +2%)
```

## Phase 6: Weekly Review Process

```markdown
**Every Monday: 30-minute Health Review**
1. Pull dashboard metrics
2. Identify red/yellow alerts
3. Assign owners for investigations
4. Discuss trends (positive/negative)
5. Prioritize fixes for sprint
```

## Verification Checklist

- [ ] Dashboard configured and live
- [ ] All metrics being collected
- [ ] Alerts triggering correctly
- [ ] Health reports generated weekly
- [ ] Team reviews and acts on reports

## Common Issues

| Issue | Solution |
|---|---|
| "Dashboard shows no data" | Verify metrics are being POST'd to endpoint |
| "False alerts firing" | Tune thresholds based on historical data |
| "Team ignores reports" | Make dashboards visible (Slack bot, email digest) |

## Related Topics

- See `/technical-debt-audit` for code health tracking
- Refer to `/analytics-integration` for user health metrics
- Check `/security-vulnerability-scan` for security monitoring