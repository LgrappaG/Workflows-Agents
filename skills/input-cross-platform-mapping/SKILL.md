---
name: input-cross-platform-mapping
description: Map input across different platforms uniformly
risk: high
source: workspace
date_added: '2026-03-24'
usage: Cross-platform multiplayer latency parity, console port optimization, VR/desktop hybrid locomotion, mobile controller support, esports tournament standardization
avoid: Platform-specific code in gameplay logic instead of input layer, mixing input APIs in same frame causing jitter, ignoring platform capability drift (driver updates), hardcoded button layouts instead of using platform-neutral action bindings, assuming all platforms report axes in same coordinate system
mandates: Maintain <50ms input latency across Desktop/Mobile/Console/VR, normalize gamepad axes to ±1.0 range with ±0.01 precision, 100% API coverage (XInput/DirectInput/HID/Touch), platform fallback chains tested on 8+ device types
response: 'Abstract platform-specific APIs (Windows XInput/DirectInput, Linux evdev, macOS IOKit, mobile Touch/GameController, VR, Normalize all input events to canonical enum space: gamepad sticks (X/Y ∈, Implement platform detection with automatic cascading fallback (try XInput → DirectInput →, Profile input latency per platform at startup using event timestamp delta analysis'
---

# Input Cross Platform Mapping

Map input across different platforms uniformly

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
- Cross-platform support
- Development workflows

## What NOT to Do
- Platform-specific bugs
- Incomplete testing
- Deploy without validation
