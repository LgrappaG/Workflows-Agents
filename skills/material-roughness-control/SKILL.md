---
name: material-roughness-control
description: Manage surface roughness for controlling reflection sharpness and diffusion
risk: low
source: workspace
date_added: '2026-03-21'
usage: Surface appearance, reflection control, material variation
avoid: Extreme roughness values, mismatched map resolution
mandates: Roughness 0-1 range, use high-quality maps, test under various lighting
response: Set roughness values, apply roughness maps, test reflection quality
---
# Material Roughness Control

Manage surface roughness for controlling reflection sharpness and diffusion

## Risk Level
**LOW**

## Core Rules
- Roughness 0-1 range
- use high-quality maps
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Set roughness values
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Surface appearance
- reflection control

## What NOT to Do
- Extreme roughness values
- mismatched map resolution
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
