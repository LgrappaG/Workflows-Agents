---
version: 9.0.0
category: Debugging & Recovery
agent: Unity Debugger
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - ai-debugging-tools
  - material-visual-debugging
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - custom-workflow-builder
  - physics-joint-constraints
  - physics-debug-visualization
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-terrain-deformation
  - terrain-physics-colliders
  - material-specular-workflow
  - ui-list-repeater
  - ui-two-way-binding
  - ai-learning-adaptation
  - build-system-optimization
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - graphics-frame-debugger
  - terrain-cave-systems
  - terrain-noise-functions
  - terrain-shape-tools
  - terrain-water-integration
  - ui-context-menus
  - ui-keyboard-shortcuts
  - ui-panel-layout
  - ui-prefab-variants
  - ui-text-binding
  - timeline-debug-visualization
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - debug-physics-debugger
  - engine-migration-guide
  - godot-physics-system
  - graphics-ambient-occlusion
  - graphics-batching-optimization
  - graphics-bloom-effect
  - graphics-culling-strategies
  - graphics-depth-of-field
  - graphics-dynamic-lighting
  - graphics-geometry-optimization
  - graphics-gpu-profiling
  - graphics-hdrp-setup
  - graphics-light-baking
  - graphics-lightmap-setup
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
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-mipmap-chains
  - material-physics-interactions
  recommended:
  - networking-guild-system
  - networking-server-maintenance
  - networking-server-security
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-collision-callbacks
  - physics-continuous-collision
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-force-fields
  - physics-friction-models
  - physics-inertia-calculation
  - physics-layer-masking
  - physics-networked-synchronization
  - physics-object-pooling
  - physics-particle-collisions
  - physics-performance-metrics
  - physics-performance-profiling
  - physics-ragdoll-physics
  - physics-rolling-resistance
  - physics-rope-simulation
  - physics-solver-configuration
  - physics-spring-dynamics
  - physics-suspension-tuning
  - physics-time-scaling
  - physics-trigger-callbacks
  - physics-trigger-volumes
  - physics-vehicle-setup
  - physics-vehicle-wheels
  - physics-water-waves
  - terrain-advanced-editing
  - terrain-biome-definition
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
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-wind-zones
  - training-datasets
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
  optional:
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
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
skill_density: 26.17
estimated_skills_needed: 157
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Error Recovery & Rollback Workflow

When things go wrong, this workflow helps you diagnose and recover safely without losing work.

## 1. Identify the Failure Type

Tell the agent what went wrong:
- "My Unity build failed mid-way"
- "Git push was rejected"
- "I have merge conflicts I can't resolve"
- "Unity project won't open anymore"
- "Package restore is broken"

## 2. Diagnosis (Agent Action)

The agent will check the current state:

### Git State Check
```bash
git status
git log --oneline -5
git stash list
```

### Unity Project State Check
```bash
ls -la Library/
ls -la Temp/
cat Packages/manifest.json
```

---

## 3. Recovery Strategies by Failure Type

### 🔴 Git Push Rejected

**Cause:** Remote has commits you don't have.

**Recovery:**
```bash
# Safe: Fetch and rebase
git fetch origin
git rebase origin/main

# If conflicts arise
git rebase --abort  # Cancel and try merge instead
git merge origin/main
```

### 🔴 Merge Conflicts

**Recovery:**
```bash
# See conflicted files
git diff --name-only --diff-filter=U

# Option 1: Keep your changes
git checkout --ours <file>

# Option 2: Keep their changes
git checkout --theirs <file>

# Option 3: Manual resolution then
git add <file>
git rebase --continue
```

### 🔴 Unity Build Failed

**Recovery Steps:**
1. Check Unity Console for the actual error
2. Clear build cache:
```bash
rm -rf Library/Bee
rm -rf Library/ScriptAssemblies
rm -rf Temp/
```
3. Reimport all:
   - Unity Editor → Assets → Reimport All

### 🔴 Unity Project Won't Open

**Recovery Steps:**
```bash
# 1. Backup current state
cp -r . ../ProjectBackup_$(date +%Y%m%d)

# 2. Delete cached data (safe to regenerate)
rm -rf Library/
rm -rf Temp/
rm -rf Logs/
rm -rf obj/

# 3. Keep these (your actual work)
# - Assets/
# - Packages/
# - ProjectSettings/

# 4. Reopen Unity — it will regenerate Library/
```

### 🔴 Package Restore Failed

**Recovery:**
```bash
# Clear package cache
rm -rf Library/PackageCache

# Reset packages lock
rm Packages/packages-lock.json

# Reopen Unity to re-resolve packages
```

### 🔴 Lost Uncommitted Work

**Check if recoverable:**
```bash
# Check stash
git stash list
git stash show -p stash@{0}

# Check reflog (last 30 days of HEAD movements)
git reflog

# Recover from reflog
git checkout <commit-hash>
```

---

## 4. Safe State Checkpoint

// turbo
After recovery, create a checkpoint:

```bash
git add -A
git stash push -m "Recovery checkpoint $(date +%Y%m%d-%H%M)"
echo "Checkpoint created. Use 'git stash pop' to restore if needed."
```

---

## 5. Prevention Tips

The agent will suggest preventive measures:

| Issue | Prevention |
|-------|------------|
| Lost work | Commit early, commit often |
| Merge conflicts | Pull before starting work, use feature branches |
| Build failures | Run builds locally before push |
| Corrupted Library | Add Library/ to .gitignore (it's regenerated) |
| Package issues | Lock package versions in manifest.json |

---

## 6. Escalation

If automated recovery fails:

1. **Document the error state** — screenshots, console logs
2. **Create a minimal repro** — smallest project that reproduces the issue
3. **Check Unity Issue Tracker** — https://issuetracker.unity3d.com
4. **Ask for help** with full context: Unity version, OS, error messages