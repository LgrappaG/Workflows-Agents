---
version: 9.0.0
category: Git & CI/CD
agent: DevOps Engineer
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - ui-performance-optimization
  - ui-accessibility
  - ui-keyboard-shortcuts
  - networking-guild-system
  - ui-focus-navigation
  - build-system-optimization
  - networking-performance-monitoring
  - ui-context-menus
  - ui-dynamic-styling
  - ui-hierarchy-panel
  - ui-panel-layout
  - ui-prefab-variants
  - ui-two-way-binding
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - networking-ngo-setup
  - physics-fluid-dynamics
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-event-handlers
  - ui-form-submission
  - ui-grid-layout
  - ui-input-validation
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - debug-performance-charts
  - networking-lobby-system
  - ai-debugging-tools
  - animation-performance-profiling
  - audio-performance-profiling
  - ci-cd-pipeline-setup
  - debug-performance-profiler
  - godot-animation-setup
  - machine-learning-setup
  - navmesh-baking-setup
  - networking-leaderboard
  - performance-dashboard
  - physics-performance-metrics
  recommended:
  - physics-performance-profiling
  - timeline-performance-profiling
  - advanced-performance-tuning
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - automated-testing-framework
  - compatibility-testing
  - csharp-performance-optimization
  - data-pipeline-setup
  - debug-performance-metrics
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-performance-profiling
  - material-specular-workflow
  - material-translucency-setup
  - material-visual-debugging
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
  - networking-server-authority
  - networking-server-load-balancing
  optional:
  - networking-server-maintenance
  - networking-server-replication
  - networking-server-security
  - networking-spectator-mode
  - networking-state-synchronization
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- response-patterns-actionability
- mandates-clarity
primary_agent: tech-lead
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 15.88
estimated_skills_needed: 127
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Changelog Generator Workflow

Automatically generate a formatted changelog from your git commit history.

## 1. Specify the Range

Tell the agent what commits to include:
- "Generate changelog for the last release"
- "Changelog from v1.0.0 to v1.1.0"
- "Changelog for commits since last week"
- "Full changelog from the beginning"

## 2. Gather Commit History (Agent Action)

// turbo
```bash
# Get commit history with conventional commit parsing
git log --pretty=format:"%h|%s|%an|%ad" --date=short > .temp_commits.txt
echo "Commits gathered."
```

## 3. Categorize Changes

The agent parses commits using Conventional Commits patterns:

| Prefix | Category | Emoji |
|--------|----------|-------|
| `feat:` | Added | ✨ |
| `fix:` | Fixed | 🐛 |
| `perf:` | Performance | ⚡ |
| `refactor:` | Changed | ♻️ |
| `docs:` | Documentation | 📝 |
| `test:` | Tests | ✅ |
| `build:` / `ci:` | Build | 🔧 |
| `BREAKING CHANGE` | Breaking | 💥 |
| Other | Other | 📦 |

---

## 4. Generate Changelog

// turbo
```bash
# Create or update CHANGELOG.md
cat > CHANGELOG.md << 'CHANGELOG_HEADER'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

CHANGELOG_HEADER

echo "CHANGELOG.md header created. Agent will now populate entries."
```

## 5. Changelog Entry Format

The agent generates entries in this format:

```markdown
## [1.1.0] - 2026-03-20

### 💥 Breaking Changes
- Removed deprecated `OldAPI.Initialize()` method

### ✨ Added
- New VR hand tracking gesture system (#123)
- Accessibility comfort vignette option

### 🐛 Fixed
- Fixed null reference in PlayerController on scene reload
- Resolved Quest 3 passthrough flickering

### ⚡ Performance
- Reduced GC allocations in Update loop by 40%
- Optimized mesh batching for complex scenes

### ♻️ Changed
- Refactored NetworkManager to use dependency injection
- Updated XR Interaction Toolkit to 3.0.1

### 📝 Documentation
- Added architecture decision records (ADRs)
- Updated README with Quest build instructions
```

---

## 6. Version Bump Suggestion

Based on changes, the agent suggests the next version:

| Change Type | Version Bump |
|-------------|--------------|
| Breaking changes | Major (1.0.0 → 2.0.0) |
| New features | Minor (1.0.0 → 1.1.0) |
| Bug fixes only | Patch (1.0.0 → 1.0.1) |

---

## 7. Optional: Update package.json / AssemblyInfo

If requested, update version numbers:

```bash
# For Unity package.json
jq '.version = "1.1.0"' package.json > temp.json && mv temp.json package.json

# For AssemblyInfo.cs
sed -i 's/AssemblyVersion("[^"]*")/AssemblyVersion("1.1.0")/' Properties/AssemblyInfo.cs
```

---

## 8. Cleanup

// turbo
```bash
rm -f .temp_commits.txt
echo "Changelog generation complete!"
```

---

## Configuration Options

Tell the agent your preferences:

| Option | Example |
|--------|---------|
| Format | "Use Keep a Changelog format" (default) |
| Emoji | "No emojis please" / "Use emojis" (default) |
| Grouping | "Group by date" / "Group by type" (default) |
| Links | "Link to GitHub issues" / "No links" |
| Authors | "Include commit authors" / "Omit authors" (default) |

---

## Example Commands

- "Generate changelog for v0.9.0 to v1.0.0"
- "Create a changelog entry for today's commits"
- "Update CHANGELOG.md with all commits since the last tag"
- "Generate release notes for GitHub release"