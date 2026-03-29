---
name: controller-haptic-feedback
description: Configure haptic feedback for controllers
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Impact feedback on weapon hits/collisions, door lock haptic confirmation, VR controller bullet chambering buzz, mobile phone vibration alerts, accessibility tactile cues for UI navigation, racing wheel torque feedback
avoid: Submitting unbatched haptic requests every frame causing driver stutter, overlapping contradictory haptic patterns (hit while existing rumble active), haptic stutter from driver lag due to command flooding, no per-device fallback causing crashes on unsupported hardware, haptic intensity clipping on weak motors
mandates: Haptic latency <20ms from trigger to motor activation, support 8+ intensity levels (0-255), per-motor control on dual-motor gamepads, haptic queue overhead <2% frame time, test on 15+ device models
response: 'Queue haptic commands with intensity (0-1), duration (ms), pattern type (sine/square/decay), and, Route haptic requests through abstraction layer supporting motor types: standard rumble (left/right, Batch haptic updates into single frame submission to hardware driver, limiting command, Implement haptic fallback chains (test adaptive triggers → rumble → phone vibration'
---

# Controller Haptic Feedback

Configure haptic feedback for controllers

## Risk Level
**MEDIUM**

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
- Haptic support
- Development workflows

## What NOT to Do
- Excessive vibration
- Incomplete testing
- Deploy without validation
