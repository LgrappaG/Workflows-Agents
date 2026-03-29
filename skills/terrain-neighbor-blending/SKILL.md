---
name: terrain-neighbor-blending
description: Blend terrain across chunk boundaries for seamless appearance
risk: low
source: workspace
date_added: '2026-03-21'
usage: Terrain streaming, seamless blending, chunk management
avoid: Visible seams, incorrect blending, z-fighting
mandates: Implement smooth blending, validate transitions, test appearance
response: Configure blending, test chunk transitions, validate seamlessness
---
# Terrain Neighbor Blending

Blend terrain across chunk boundaries for seamless appearance

## Risk Level
**LOW**

## Core Rules
- Implement smooth blending
- validate transitions
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure blending
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Terrain streaming
- seamless blending

## What NOT to Do
- Visible seams
- incorrect blending
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
