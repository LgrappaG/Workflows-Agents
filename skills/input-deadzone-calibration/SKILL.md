---
name: input-deadzone-calibration
description: Configure deadzone calibration for controller sticks
risk: low
source: workspace
date_added: '2026-03-24'
usage: Long gaming sessions with controller aging, older wireless controllers with drift, mobile accelerometer drift compensation, VR touch controller variance, competitive play requiring precision aiming
avoid: Fixed circular deadzones ignoring stick manufacturing variance, single global calibration applied to all device models, ignoring hardware-specific drift patterns, corrupting calibration data with unvalidated user input, recalibrating too frequently causing instability
mandates: Deadzone range 0-30% stick travel with ±1% accuracy, per-device calibration indexed by hardware UUID, detect stick drift >5% variance in <2ms, persist calibration profiles with integrity hash
response: 'Capture raw stick values across full range (0° to 360°, 16+ samples, Compute radial deadzone ellipse via principal component analysis fitted to actual stick, Store calibration profiles keyed by gamepad vendor/product ID with device rotation normalization, Apply adaptive deadzone at input read time: clamp raw values against calibration'
---

# Input Deadzone Calibration

Configure deadzone calibration for controller sticks

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
- Controller calibration
- Development workflows

## What NOT to Do
- Incorrect calibration
- Incomplete testing
- Deploy without validation
