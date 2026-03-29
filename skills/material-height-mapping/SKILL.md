---
name: material-height-mapping
description: Use heightmaps to simulate surface elevation and parallax effects
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Parallax effects, surface displacement, visual depth
avoid: Extreme height values, misaligned with normal maps
mandates: Grayscale format, range 0-1, couple with normal map generation
response: Generate height maps, configure parallax offset, validate visual consistency
---
# Material Height Mapping

Use heightmaps to simulate surface elevation and parallax effects

## Risk Level
**MEDIUM**

## Core Rules
- Grayscale format
- range 0-1
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Generate height maps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Parallax effects
- surface displacement

## What NOT to Do
- Extreme height values
- misaligned with normal maps
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
