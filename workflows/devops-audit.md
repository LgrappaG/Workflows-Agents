---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - custom-workflow-builder
  - ci-cd-pipeline-setup
  - graphics-hdrp-setup
  - ui-performance-optimization
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-specular-workflow
  - godot-animation-setup
  - data-pipeline-setup
  - networking-ngo-setup
  - ai-debugging-tools
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - godot-setup
  - machine-learning-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - physics-vehicle-setup
  - terrain-performance-tuning
  - build-system-optimization
  - debug-renderer-debugging
  - networking-performance-monitoring
  - ui-event-handlers
  - csharp-performance-optimization
  - debug-performance-charts
  - debug-script-debugging
  - debug-shader-debugging
  - timeline-performance-profiling
  - ui-anchor-positioning
  - ui-context-menus
  - ui-dynamic-styling
  - ui-keyboard-shortcuts
  - ui-transition-timing
  - advanced-performance-tuning
  - animation-performance-profiling
  - audio-performance-profiling
  - csharp-builder-pattern
  - debug-build-diagnostic
  - debug-performance-metrics
  - debug-performance-profiler
  - engine-migration-guide
  - material-performance-profiling
  - material-visual-debugging
  - networking-guild-system
  - performance-dashboard
  - performance-profiling-cross-engine
  - physics-fluid-dynamics
  - physics-performance-metrics
  - physics-performance-profiling
  - ui-accessibility
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  recommended:
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-two-way-binding
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - automated-testing-framework
  - graphics-shadow-optimization
  - animation-constraint-rigging
  - cinemachine-virtual-camera
  - graphics-shader-compiler
  - material-mipmap-chains
  - physics-constraint-optimization
  - terrain-wind-zones
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - compatibility-testing
  - csharp-async-await
  - csharp-chain-of-responsibility
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
  - graphics-sorting-layers
  - graphics-temporal-antialiasing
  - networking-server-maintenance
  - networking-server-security
  - physics-chain-dynamics
  - physics-hair-dynamics
  optional:
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- response-patterns-actionability
- mandates-clarity
primary_agent: code-reviewer
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 23.17
estimated_skills_needed: 139
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# DevOps Audit Workflow

Audit and improve your DevOps infrastructure using `@devops-engineer`.

## 1. Current State Assessment

// turbo
```bash
echo "=== DevOps Audit ==="
echo ""
echo "Git Configuration:"
git remote -v 2>/dev/null || echo "Not a git repository"
echo ""
echo "CI/CD Files:"
ls -la .github/workflows/*.yml 2>/dev/null || echo "No GitHub Actions found"
ls -la .gitlab-ci.yml 2>/dev/null || echo "No GitLab CI found"
ls -la azure-pipelines.yml 2>/dev/null || echo "No Azure Pipelines found"
echo ""
echo "Build Scripts:"
ls -la *.sh build.* 2>/dev/null || echo "No build scripts found"
```

## 2. Audit Categories

### A. Version Control

| Check | Status |
|-------|--------|
| Git repository initialized | |
| .gitignore properly configured | |
| Branch protection rules | |
| Commit message convention | |
| Git LFS for large assets | |

### B. CI/CD Pipeline

| Check | Status |
|-------|--------|
| Automated builds on push | |
| Test runner integrated | |
| Build notifications | |
| Artifact storage | |
| Deployment automation | |

### C. Build Configuration

| Check | Status |
|-------|--------|
| Unity version locked | |
| Build targets defined | |
| Debug vs Release configs | |
| Signing configured | |
| Version numbering automated | |

### D. Environment Management

| Check | Status |
|-------|--------|
| Dev/Staging/Prod environments | |
| Secrets management | |
| Environment variables | |
| Configuration per environment | |

## 3. GitHub Actions Template

If no CI/CD exists, the agent generates:

// turbo
```bash
mkdir -p .github/workflows

cat > .github/workflows/unity-build.yml << 'EOF'
name: Unity Build

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true

      - uses: game-ci/unity-builder@v4
        env:
          UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
        with:
          targetPlatform: Android
          androidAppBundle: true

      - uses: actions/upload-artifact@v4
        with:
          name: Build-Android
          path: build/Android

  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: game-ci/unity-test-runner@v4
        env:
          UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
        with:
          testMode: editmode
EOF

echo "✅ GitHub Actions workflow created"
```

## 4. Unity Build Script

// turbo
```bash
cat > build.sh << 'EOF'
#!/bin/bash
set -e

UNITY_PATH="${UNITY_PATH:-/Applications/Unity/Hub/Editor/2022.3.0f1/Unity.app/Contents/MacOS/Unity}"
PROJECT_PATH="$(pwd)"
BUILD_PATH="$PROJECT_PATH/Builds"

# Parse arguments
TARGET="${1:-Android}"
CONFIG="${2:-Release}"

echo "Building $TARGET ($CONFIG)..."

$UNITY_PATH \
  -batchmode \
  -nographics \
  -projectPath "$PROJECT_PATH" \
  -executeMethod BuildScript.Build \
  -buildTarget "$TARGET" \
  -buildConfig "$CONFIG" \
  -logFile "$BUILD_PATH/build.log" \
  -quit

echo "Build complete: $BUILD_PATH"
EOF

chmod +x build.sh
echo "✅ Build script created: build.sh"
```

## 5. Common Issues

### 🔴 Critical
- [ ] No CI/CD pipeline
- [ ] Secrets in repository
- [ ] No automated testing
- [ ] Manual deployments only

### 🟡 Important
- [ ] No branch protection
- [ ] Missing code review process
- [ ] No artifact versioning
- [ ] Build times too long

### 🔵 Minor
- [ ] No build status badges
- [ ] Missing documentation
- [ ] No performance benchmarks
- [ ] Manual changelog

## 6. Generate Audit Report

// turbo
```bash
cat > devops-audit-report.md << 'EOF'
# DevOps Audit Report

Generated: $(date '+%Y-%m-%d')

## Current State

### Version Control
- Repository:
- Branches:
- Protection:

### CI/CD
- Platform:
- Pipelines:
- Coverage:

### Build Process
- Automation:
- Targets:
- Time:

## Recommendations

### Immediate (This Week)
1.

### Short-term (This Month)
1.

### Long-term (This Quarter)
1.

## Action Items
- [ ]
EOF

echo "✅ Audit report created: devops-audit-report.md"
```

## Example Commands

- "Audit our CI/CD setup"
- "Set up GitHub Actions for Unity builds"
- "Create automated Quest deployment"
- "Review our build pipeline for improvements"