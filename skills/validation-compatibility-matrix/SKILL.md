---
name: validation-compatibility-matrix
description: Validate build compatibility across platform matrix
risk: low
source: workspace
date_added: '2026-03-24'
usage: Platform certification (Steam, Console, VR), live service hardware tier assignment, player device support validation, shader compilation bottleneck detection, driver compatibility regression tracking, minimum spec justification
avoid: Testing only developer hardware (confirmation bias), insufficient test duration per config (<5min per run), ignoring driver version variance, not testing edge cases (max settings + low VRAM), skipping thermals/power consumption measurement
mandates: Test 5+ OS × 4+ GPU × 3+ RAM configs. Generate visual compatibility report. Coverage >95% user config combinations. Identify 100% of incompatible combinations before launch.
response: 'Build compatibility test matrix with axes: OS (Win10/Win11/Mac/Linux), GPU (RTX 3060/2060/Intel UHD/AMD, Automate hardware provisioning using CI matrix strategy; rent time on cloud GPU, Capture per-config metrics: success/fail, average FPS, shader compilation time, driver crash rate;, Publish pre-launch compatibility guarantee document listing supported configs (green [OK]), partially-supported with'
---

# Validation Compatibility Matrix

Validate build compatibility across platform matrix

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
- Platform compatibility
- Development workflows

## What NOT to Do
- Platform-specific bugs missed
- Incomplete testing
- Deploy without validation
