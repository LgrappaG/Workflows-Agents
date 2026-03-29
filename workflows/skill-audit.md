---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - physics-hair-dynamics
  - ai-debugging-tools
  - custom-workflow-builder
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - physics-vehicle-setup
  - terrain-physics-colliders
  - debug-shader-debugging
  - material-mipmap-chains
  - physics-force-fields
  - physics-layer-masking
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-shape-tools
  - terrain-water-integration
  - ui-event-handlers
  - ui-input-validation
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
  - build-system-optimization
  - ci-cd-pipeline-setup
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - data-pipeline-setup
  - debug-build-diagnostic
  - debug-physics-debugger
  - debug-renderer-debugging
  - debug-script-debugging
  - engine-migration-guide
  - godot-animation-setup
  - godot-physics-system
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-physics-interactions
  - material-specular-workflow
  - material-translucency-setup
  recommended:
  - material-visual-debugging
  - navmesh-baking-setup
  - networking-guild-system
  - networking-ngo-setup
  - networking-server-maintenance
  - physics-aerodynamics
  - physics-angular-momentum
  - physics-buoyancy
  - physics-center-of-mass
  - physics-cloth-simulation
  - physics-collision-callbacks
  - physics-continuous-collision
  - physics-debug-visualization
  - physics-destruction-system
  - physics-drift-mechanics
  - physics-explosion-forces
  - physics-friction-models
  - physics-inertia-calculation
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
  - physics-vehicle-wheels
  - physics-water-waves
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
  optional:
  - terrain-wind-zones
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
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
skill_density: 32.75
estimated_skills_needed: 131
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Skill Audit Workflow

Inspired by `skill-improver` from Antigravity Awesome Skills. Scans every skill in the workspace and evaluates it against the 8-gate quality checklist. Produces a `skill-audit-results.md` report.

## 1. Discover All Skills (Agent Action)

// turbo
```bash
echo "=== Discovering Skills ==="
find .agents/skills -name "SKILL.md" -type f 2>/dev/null || echo "No skills found"
```

## 2. Audit Each Skill (Agent Action)

For each `SKILL.md` found, the agent checks:

### Quality Gates

| Gate | Check |
|------|-------|
| ✅ YAML Completeness | Has `name`, `description`, `risk`, `source`, `date_added` |
| ✅ Trigger Clarity | `description` field is specific enough to trigger correctly |
| ✅ Use When | "Use this skill when" section exists with ≥ 2 bullets |
| ✅ Do Not Use | "Do NOT use this skill when" section exists |
| ✅ Core Mandates | ≥ 2 numbered, actionable mandates (not vague) |
| ✅ Response Format | Specifies concrete output structure |
| ✅ Example Interactions | ≥ 2 real-world examples |
| ✅ Line Count | SKILL.md is under 500 lines; excess content is in `resources/` |

### Issue Severity

| Severity | Definition |
|----------|------------|
| 🔴 Critical | Missing required fields — skill may fail to load or trigger |
| 🟡 Major | Weak trigger or missing required sections — reduces effectiveness |
| 🔵 Minor | Style, optional improvements, verbosity |

## 3. Generate the Audit Report

// turbo
```bash
cat > skill-audit-results.md << 'EOF'
# Skill Audit Results

Generated: $(date '+%Y-%m-%d %H:%M')

## Skills Audited

(Agent fills in skill list here)

## Results by Skill

(Agent fills in per-skill results here)

## Summary

- 🔴 Critical Issues: (n)
- 🟡 Major Issues: (n)
- 🔵 Minor Issues: (n)
- ✅ Passing Skills: (n)

## Recommendations

(Agent provides prioritized fix suggestions)
EOF

echo "✅ Audit report template created: skill-audit-results.md"
```

## 4. Fix Issues

After reviewing `skill-audit-results.md`:

- For **Critical/Major issues**: Use `/create-skill` or direct edits to fix
- For iterative fix loops: Use the `@skill-improver` skill

**Example:**
> "Fix all 🟡 Major issues in `code-reviewer/SKILL.md` identified by the Skill Audit."