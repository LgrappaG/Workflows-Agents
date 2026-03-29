---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - ai-debugging-tools
  - ui-performance-optimization
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - material-visual-debugging
  - networking-guild-system
  - physics-fluid-dynamics
  - physics-constraint-optimization
  - physics-joint-constraints
  - networking-performance-monitoring
  - physics-chain-dynamics
  - physics-hair-dynamics
  - physics-performance-metrics
  - physics-performance-profiling
  - physics-terrain-deformation
  - ui-context-menus
  - ui-keyboard-shortcuts
  - ui-panel-layout
  - ui-prefab-variants
  - ui-two-way-binding
  - build-system-optimization
  - csharp-builder-pattern
  - custom-workflow-builder
  - debug-build-diagnostic
  - engine-migration-guide
  - networking-server-maintenance
  - networking-server-security
  - terrain-performance-tuning
  - terrain-physics-colliders
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
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
  - debug-performance-profiler
  - performance-dashboard
  - physics-buoyancy
  - physics-force-fields
  - physics-solver-configuration
  - physics-vehicle-wheels
  - ai-environmental-awareness
  - ai-learning-adaptation
  - csharp-chain-of-responsibility
  - csharp-performance-optimization
  - networking-analytics-tracking
  - networking-antiCheat-detection
  - networking-connection-management
  - networking-leaderboard
  - networking-lobby-system
  - networking-packet-loss-handling
  recommended:
  - networking-replay-system
  - networking-server-authority
  - physics-collision-callbacks
  - physics-debug-visualization
  - physics-destruction-system
  - physics-rope-simulation
  - physics-spring-dynamics
  - physics-time-scaling
  - physics-trigger-volumes
  - physics-vehicle-setup
  - terrain-cave-systems
  - terrain-path-carving
  - terrain-shape-tools
  - terrain-water-integration
  - timeline-performance-profiling
  - advanced-performance-tuning
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - animation-performance-profiling
  - audio-ducking-sidechains
  - audio-performance-profiling
  - automated-testing-framework
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - debug-performance-metrics
  - debug-physics-debugger
  - godot-physics-system
  - material-mipmap-chains
  - material-performance-profiling
  - material-physics-interactions
  - networking-account-recovery
  - networking-achievement-tracking
  - networking-auction-system
  - networking-authentication
  - networking-ban-system
  - networking-bandwidth-optimization
  - networking-battle-pass
  - networking-chat-system
  - networking-client-authority
  - networking-cloud-saves
  - networking-cross-progression
  - networking-encryption
  - networking-friend-system
  - networking-interpolation
  - networking-lag-compensation
  - networking-matchmaking
  - networking-message-ordering
  - networking-ngo-setup
  - networking-player-persistence
  - networking-player-spawning
  - networking-prediction-reconciliation
  - networking-presence-system
  - networking-pvp-ranking
  - networking-region-selection
  - networking-reward-distribution
  - networking-rollback-resimulation
  - networking-rpc-system
  - networking-server-load-balancing
  - networking-server-replication
  - networking-spectator-mode
  - networking-state-synchronization
  - networking-statistics-synchronization
  - networking-trading-system
  - performance-profiling-cross-engine
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-continuous-collision
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-friction-models
  - physics-inertia-calculation
  optional:
  - physics-layer-masking
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-particle-collisions
  - physics-ragdoll-physics
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
skill_density: 166.0
estimated_skills_needed: 166
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Technical Debt Audit

Identify and track technical debt: obsolete code, version mismatches, TODO comments, architectural issues.

## Prerequisites

- Code analysis tools (optional)
- 1 week for audit

// turbo-all

## Phase 1: Find TODO/FIXME Comments

```bash
# Search entire project
grep -r "TODO\|FIXME\|HACK\|XXX" Assets/ --include="*.cs" > debt.txt

# Count by type
grep -c "TODO" debt.txt
grep -c "FIXME" debt.txt
grep -c "HACK" debt.txt
```

## Phase 2: Detect Unused Code

```bash
# Tools: ReSharper, Rider, or CodeClimate
# Identify: Dead code, unused methods, unreferenced scripts
# Risk: Increases maintenance burden
```

## Phase 3: Version & Dependency Mismatches

```plaintext
Check:
- Unity version documented vs actual
- Package versions locked or floating?
- Third-party SDKs outdated?
- Breaking changes not handled?
```

## Phase 4: Architectural Tech Debt

```markdown
Red flags:
- Monolithic scripts >500 lines
- God objects with 20+ public fields
- Hardcoded values instead of configuration
- Missing error handling
- No logging/validation
```

## Phase 5: Create Debt Backlog

```markdown
Prioritize:
1. CRITICAL: Blocks new features or causes crashes
2. HIGH: Performance impact or security risks
3. MEDIUM: Increases development friction
4. LOW: Nice-to-has, cosmetic improvements

Example:
- [CRITICAL] NetworkManager crashes on disconnect
- [HIGH] Physics queries called every frame (performance)
- [MEDIUM] UIController needs refactoring (1000 lines)
- [LOW] Remove Debug.Logs before release
```

## Verification

- [ ] All TODO/FIXME comments cataloged
- [ ] Debt backlog prioritized
- [ ] Critical items assigned to sprints
- [ ] 20% of velocity reserved for debt reduction

## Related Topics

- See `/project-health-check` for ongoing monitoring
- Refer to `/code-review-swarm` for prevention strategies