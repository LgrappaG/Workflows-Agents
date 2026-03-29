---
name: input-analog-curve-shaping
description: Shape analog input curves for feel optimization
risk: medium
source: workspace
date_added: '2026-03-24'
usage: FPS aiming sensitivity tuning per player skill, racing game acceleration curves matching car feel, VR locomotion comfort curves, accessibility slow-motion input for fine targeting, mobile swipe response curves
avoid: Runtime curve computation per input event destroying latency budget, curve functions breaking monotonicity causing input reversal, unlimited curve complexity overwhelming preview responsiveness, applying curves after movement calculations destroying feel, curve mismatch between platforms
mandates: Support 6+ curve types (linear/quadratic/cubic/exponential/bezier/custom), apply curves in <1ms per-axis using LUT, curve adjustment UI with 60fps live preview, persist per-player preferences with 10+ preset curves
response: 'Implement parametric curve functions with presets: quadratic (sensitivity 0, 5-2, 0), cubic (acceleration ramping), exponential (rapid response), piecewise linear (custom threshold), and, Author custom curves via visual Bezier control-point editor with normalized 0-1 input/output'
---

# Input Analog Curve Shaping

Shape analog input curves for feel optimization

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
- Feel tuning
- Development workflows

## What NOT to Do
- Non-intuitive curves
- Incomplete testing
- Deploy without validation
