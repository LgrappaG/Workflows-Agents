---
name: gesture-recognition-engine
description: Recognize complex gestures from touch or motion input
risk: high
source: workspace
date_added: '2026-03-24'
usage: Mobile UI swipe-to-delete, VR hand tracking circular grab gestures, accessibility single-finger shortcut strokes, artistic sketch-based UI for menu navigation, whiteboard app shape recognition
avoid: Position-dependent gesture templates requiring retraining on screen size change, single-stroke-only patterns missing multi-stroke user behaviors, gesture recognition during accelerometer motion (walking) causing false positives, no confidence thresholding accepting random noise as gesture, gesture library bloat without pruning redundant patterns
mandates: Gesture accuracy >95% on known patterns, false-positive rate <2%, support 15+ gesture types, recognition latency <100ms per stroke, gesture library versioning with checksum validation
response: 'Normalize touch input strokes to scale/rotation-invariant features: angle sequence (turning angles), curvature, Load gesture classifier (template matching with dynamic time warping, or HMM, or, Score incoming stroke against known gestures using classifier, accepting matches above 0, 85 confidence threshold and rejecting low-confidence ambiguous strokes'
---

# Gesture Recognition Engine

Recognize complex gestures from touch or motion input

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
- Gesture support
- Development workflows

## What NOT to Do
- False positives
- Incomplete testing
- Deploy without validation
