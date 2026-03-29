---
name: terrain-normal-generation
description: Generate normal maps from heightfields for terrain detail
risk: low
source: workspace
date_added: '2026-03-21'
usage: Surface detail, lighting quality, visual enhancement
avoid: Incorrect normal direction, low-quality normals, format mismatches
mandates: Generate proper normals, validate direction, test appearance
response: Generate normal maps, validate appearance, apply to terrain
---
# Terrain Normal Generation

Generate normal maps from heightfields for terrain detail

## Risk Level
**LOW**

## Core Rules
- Generate proper normals
- validate direction
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Generate normal maps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Surface detail
- lighting quality

## What NOT to Do
- Incorrect normal direction
- low-quality normals
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
