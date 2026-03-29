---
name: gesture-multitouch-gestures
description: Support multi-touch gesture recognition
risk: high
source: workspace
date_added: '2026-03-24'
usage: Mobile map pinch-zoom with simultaneous pan, VR two-hand grab-rotate interactions, accessibility two-finger tap for right-click, tablet drawing with two-finger rotation lock, photo gallery swipe with pinch zoom
avoid: Ignoring touch ID tracking causing ghost touches on finger lift, computing distances from centroid only missing asymmetric pinch, confusing pinch with scale-invariant rotation, gesture event spam (every frame) instead of delta events, requiring exact vertical/horizontal swipe angles
mandates: Detect 2-5 finger simultaneous touches with <50ms latency, pinch scale accuracy ±2%, rotation accuracy ±5°, distinguish pinch/rotate/swipe/hold reliably >98%, test on 20+ device models
response: 'Track multi-touch contact points with persistent unique IDs across frames, detecting finger, Calculate geometric properties per frame from contact points: centroid (mean position), scale, Match geometry to gesture types using discriminant functions: pinch (scale delta >threshold),, 5s)'
---

# Gesture Multitouch Gestures

Support multi-touch gesture recognition

## Risk Level
**HIGH**

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
- Multi-touch support
- Development workflows

## What NOT to Do
- Touch conflicts
- Incomplete testing
- Deploy without validation
