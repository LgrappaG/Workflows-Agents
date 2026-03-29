---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 2-3 hours
skills:
  required:
  - ai-debugging-tools
  - networking-server-maintenance
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-learning-adaptation
  - custom-workflow-builder
  - terrain-wind-zones
  - ai-behavior-switching
  - ai-communication-network
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - material-mipmap-chains
  - material-visual-debugging
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
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
  recommended:
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
  - training-datasets
  - vfx-trail-rendering
  - ui-text-binding
  - ui-form-submission
  - ui-accessibility
  - analytics-integration
  - behavior-memory-management
  - networking-player-persistence
  - automated-testing-framework
  - build-system-optimization
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - networking-guild-system
  - physics-fluid-dynamics
  - timeline-camera-transitions
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-focus-navigation
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  optional:
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-prefab-variants
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: code-reviewer
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 17.83
estimated_skills_needed: 107
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Game Balance Review Workflow

Deep analysis of your game's balance using `@game-design-specialist`.

## 1. Define Review Scope

Tell the agent what to review:
- "Review our difficulty progression"
- "Analyze the in-game economy"
- "Check player retention mechanics"
- "Balance the loot drop rates"

## 2. Data Collection (Agent Action)

The agent gathers balance-relevant data:

// turbo
```bash
echo "=== Game Balance Data Collection ==="
echo ""
echo "Looking for design documents..."
find . -name "*.md" -path "*/design/*" 2>/dev/null | head -10
echo ""
echo "Looking for ScriptableObject data..."
find Assets -name "*.asset" -type f 2>/dev/null | grep -iE "weapon|enemy|item|level" | head -20
echo ""
echo "Looking for balance configs..."
find Assets -name "*.json" -o -name "*Config*.cs" -o -name "*Data*.cs" 2>/dev/null | head -15
```

## 3. Balance Categories

### A. Difficulty Curve

```
       Difficulty
           ▲
           │              ╱╱╱
           │           ╱╱╱
           │        ╱╱╱    ← Gradually increasing
           │     ╱╱╱
           │  ╱╱╱
           │╱╱╱
           └──────────────────▶ Time/Level

Target: 40% failure rate = engaging
```

| Phase | Levels | Player State | Design Goal |
|-------|--------|--------------|-------------|
| Tutorial | 1-5 | Learning | Near-zero failure |
| Early | 6-15 | Building confidence | 20% failure |
| Mid | 16-30 | Challenge | 40% failure |
| Late | 31-50 | Mastery test | 50% failure |
| Endgame | 50+ | Prestige | Variable |

### B. Economy Balance

```
Income Sources          Sinks (Spending)
─────────────────       ─────────────────
Mission rewards    →    Equipment upgrades
Daily login        →    Consumables
Achievements       →    Cosmetics
Premium currency   →    Time skips
```

| Metric | Healthy Range |
|--------|---------------|
| Session earnings | 5-15% of next upgrade |
| Time to meaningful purchase | 2-3 sessions |
| Premium to free ratio | 3:1 value |

### C. Progression Pacing

| Milestone | Expected Time | Player Feeling |
|-----------|---------------|----------------|
| First unlock | 5 minutes | "I can progress!" |
| First meaningful choice | 30 minutes | "My build matters" |
| First major achievement | 2 hours | "I accomplished something" |
| Endgame glimpse | 5 hours | "There's more to see" |

### D. Retention Hooks

| Hook | Frequency | Purpose |
|------|-----------|---------|
| Daily rewards | 24h | Return daily |
| Weekly challenges | 7d | Longer engagement |
| Season pass | 90d | Long-term commitment |
| Limited events | Varies | FOMO + excitement |

## 4. Analysis Checklist

The agent evaluates:

```markdown
### Difficulty
- [ ] Tutorial is skip-able for veterans
- [ ] Difficulty options available
- [ ] Failure doesn't feel punishing
- [ ] Challenge scales with skill

### Economy
- [ ] No pay-to-win (PvP unaffected by purchases)
- [ ] Free players can access all content (eventually)
- [ ] Premium feels valuable, not required
- [ ] No predatory mechanics (loot boxes to minors)

### Progression
- [ ] Always something to work toward
- [ ] Multiple progression paths
- [ ] Resets/prestiges are rewarding
- [ ] New players can catch up

### Retention
- [ ] First session hooks player
- [ ] Clear reason to return tomorrow
- [ ] Social features encourage play
- [ ] Content updates keep it fresh
```

## 5. Generate Balance Report

// turbo
```bash
cat > game-balance-report.md << 'EOF'
# Game Balance Review

Generated: $(date '+%Y-%m-%d')

## Executive Summary
(1-2 sentence overall assessment)

## Difficulty Curve
### Current State
(Agent analysis)

### Issues
-

### Recommendations
-

## Economy
### Current State
(Agent analysis)

### Issues
-

### Recommendations
-

## Progression
### Current State
(Agent analysis)

### Issues
-

### Recommendations
-

## Retention
### Current State
(Agent analysis)

### Issues
-

### Recommendations
-

## Priority Actions
1. (Highest impact)
2.
3.

## Metrics to Track
-
EOF

echo "✅ Balance report created: game-balance-report.md"
```

## 6. Balance Simulation

For numerical balance, the agent can simulate:

```csharp
// Example: Calculate time-to-max-level
public void SimulateProgression()
{
    int level = 1;
    int xp = 0;
    int sessions = 0;

    while (level < maxLevel)
    {
        xp += averageXPPerSession;
        sessions++;

        while (xp >= XPToNextLevel(level))
        {
            xp -= XPToNextLevel(level);
            level++;
        }
    }

    Debug.Log($"Sessions to max level: {sessions}");
    Debug.Log($"Hours (30min sessions): {sessions * 0.5f}");
}
```

## Example Commands

- "Review difficulty balance for our survival game"
- "Analyze if our premium currency is fairly priced"
- "Check player retention mechanics"
- "Balance weapon damage across all tiers"
- "Is our progression too slow for casual players?"