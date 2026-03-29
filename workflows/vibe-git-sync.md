---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - networking-server-maintenance
  - custom-workflow-builder
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - ai-debugging-tools
  - ai-environmental-awareness
  - ai-learning-adaptation
  - ai-perception-system
  - networking-performance-monitoring
  - networking-prediction-reconciliation
  - networking-server-replication
  - terrain-biome-definition
  - terrain-water-integration
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - automated-testing-framework
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-chain-of-responsibility
  - material-mipmap-chains
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
  recommended:
  - networking-guild-system
  - networking-interpolation
  - networking-lag-compensation
  - networking-leaderboard
  - networking-lobby-system
  - networking-matchmaking
  - networking-message-ordering
  - networking-ngo-setup
  - networking-packet-loss-handling
  - networking-player-persistence
  - networking-player-spawning
  - networking-presence-system
  - networking-pvp-ranking
  - networking-region-selection
  - networking-replay-system
  - networking-reward-distribution
  - networking-rollback-resimulation
  - networking-rpc-system
  - networking-server-authority
  - networking-server-load-balancing
  - networking-server-security
  - networking-spectator-mode
  - networking-state-synchronization
  - networking-statistics-synchronization
  - networking-trading-system
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
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
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  optional:
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
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
complexity_score: 10
skill_density: 31.67
estimated_skills_needed: 95
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Vibe Git Sync Workflow

If `/vibe-git-push` is for pushing your flow-state work to the server, `/vibe-git-sync` is for bringing the remote server changes into your flow state without messy merge commits. 

It uses `git-advanced-workflows` knowledge from the awesome-skills repository to cleanly pull updates, perform rebases to keep a linear history, and prune dead branches, saving you mental context switching.

// turbo-all
## 1. Fetch, Prune, and Pull

The workflow automatically fetches all changes, drops tracking for deleted remote branches, and attempts a `pull --rebase` to apply your current commits on top of the latest remote changes.

```bash
echo "Fetching changes and pruning stale remote tracking branches..."
git fetch origin --prune

echo "Pulling latest changes with rebase..."
git pull --rebase origin main
```

## 2. Check for Conflicts

If the `--rebase` is successful, you are fully synced! 

If there is a conflict in your Unity YAML files (like a Scene or Prefab), the process pauses. You can then ask the AI Agent to help resolve those YAML conflicts (often by prioritizing one version or using Unity's Smart Merge tool).

## 3. Clean Local Branches

Optional cleanup step: The agent can identify local branches that have already been merged into `main` and ask if you want to delete them.

```bash
# Preview merged branches:
git branch --merged main | grep -v "\*" | grep -v "main" || echo "No merged branches to clean."
```