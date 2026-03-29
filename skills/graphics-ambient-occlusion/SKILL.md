---
name: graphics-ambient-occlusion
description: Configure ambient occlusion for contact shadow depth
risk: low
source: workspace
date_added: '2026-03-21'
usage: Visual depth, shadow contact, realistic shading
avoid: Dark corners, harsh shadows, performance degradation
mandates: Tune AO parameters, validate visual quality, monitor performance
response: Configure AO, tune parameters, test visual quality
---
# Graphics Ambient Occlusion

Configure ambient occlusion for contact shadow depth

## Risk Level
**LOW**

## Core Rules
- Tune AO parameters
- validate visual quality
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure AO
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Visual depth
- shadow contact

## What NOT to Do
- Dark corners
- harsh shadows
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
