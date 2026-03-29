---
name: testing-snapshot-comparison
description: Detect visual regressions through snapshot comparison
risk: low
source: workspace
date_added: '2026-03-24'
usage: UI regression detection, shader compilation verification, platform rendering difference validation, accessibility mode screenshot validation, localization text overflow detection, VR headset display calibration verification
avoid: Comparing non-deterministic rendering (particles, post-processing without fixed seed), pixel-perfect matching (brittleness), insufficient resolution for detecting UI text artifacts, not filtering platform-specific differences (DPI scaling), approving snapshots without commit reference
mandates: Detect pixel-delta >0.1% automatically. Track 200+ snapshots per release. Baseline update only with approval. 100% false-positive filtering. Execution <5min per test.
response: 'Capture deterministic visual snapshots at 5 key milestones (menu, gameplay, cutscene, UI, Implement image diff engine using perceptual hashing (dHash) with >95% false-positive rejection;, 1%, generate side-by-side diff heatmap highlighting changed regions >10px clusters, Create baseline approval workflow: failed snapshots trigger review task; human approves as'
---

# Testing Snapshot Comparison

Detect visual regressions through snapshot comparison

## Risk Level
**LOW**

## Core Rules
- Implement properly
- Test thoroughly
- Validate results

## Response Pattern

1. Design appropriate approach
2. Implement solution
3. Test edge cases
4. Validate quality

## Usage Contexts
- Visual regression detection
- Development workflows

## What NOT to Do
- Snapshot bloat
- Incomplete testing
- Deploy without validation
