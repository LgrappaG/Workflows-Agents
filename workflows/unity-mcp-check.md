---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - networking-guild-system
  - physics-fluid-dynamics
  - build-system-optimization
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - networking-ngo-setup
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-physics-colliders
  - ui-accessibility
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
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-two-way-binding
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - networking-friend-system
  - networking-message-ordering
  - terrain-cave-systems
  - terrain-shape-tools
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-debugging-tools
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
  recommended:
  - audio-ducking-sidechains
  - audio-mixer-setup
  - automated-testing-framework
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - compatibility-testing
  - csharp-async-await
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - debug-physics-debugger
  - godot-animation-setup
  - godot-physics-system
  - godot-setup
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
  - graphics-render-queue
  - graphics-screen-space-reflections
  - graphics-shader-compiler
  - graphics-shadow-optimization
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - material-pbr-setup
  - material-physics-interactions
  - material-specular-workflow
  - material-translucency-setup
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
  - networking-interpolation
  - networking-lag-compensation
  - networking-leaderboard
  - networking-lobby-system
  - networking-matchmaking
  - networking-packet-loss-handling
  - networking-performance-monitoring
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
  - networking-server-replication
  - networking-server-security
  - networking-spectator-mode
  - networking-state-synchronization
  - networking-statistics-synchronization
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- response-patterns-actionability
- mandates-clarity
primary_agent: unity-architect
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 53.67
estimated_skills_needed: 161
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity MCP Connection Check

Verify that Antigravity can directly control your Unity Editor.

## 1. Check Scene Info (Agent Action)

The agent attempts to retrieve information about the active scene.

// turbo
```bash
# This is a conceptual representation; the agent will use mcp_mcp-unity_get_scene_info
```

## 2. Verify Capabilities

The agent checks if it can:
- [ ] List GameObjects in hierarchy
- [ ] Read Console Logs
- [ ] Detect the active Render Pipeline (URP/Built-in)

## 3. Results

If successful:
- 🟢 **Connected**: All direct editor tools are available.
- 🟡 **Partial**: Connected, but some features (like URP-specific tools) may be limited.

If unsuccessful:
- 🔴 **Disconnected**: Ensure the `mcp-unity` server is running and configured in `mcp_config.json`.