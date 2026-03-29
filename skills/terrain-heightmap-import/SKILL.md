---
name: terrain-heightmap-import
description: Import and configure heightmaps for terrain generation
risk: low
source: workspace
date_added: '2026-03-21'
usage: Terrain creation, landscape import, height configuration
avoid: Incorrect scale, inverted heights, misaligned coordinates
mandates: Validate heightmap format, check dimensions, test visual result
response: Import heightmap, configure scale, validate appearance
---
# Terrain Heightmap Import

Import and configure heightmaps for terrain generation

## Risk Level
**LOW**

## Core Rules
- Validate heightmap format
- check dimensions
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Import heightmap
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Terrain creation
- landscape import

## What NOT to Do
- Incorrect scale
- inverted heights
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
