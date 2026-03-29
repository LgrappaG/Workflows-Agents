---
name: material-pbr-setup
description: Configure physically-based rendering materials with albedo, normal, and roughness maps
risk: low
source: workspace
date_added: '2026-03-21'
usage: Material setup, scene rendering, visual fidelity
avoid: Mixing PBR with non-PBR materials, incorrect color spaces
mandates: Use linear color space, proper texture formats, validate metallic/roughness ranges
response: Configure base material properties, apply maps, verify physical correctness
---
# Material Pbr Setup

Configure physically-based rendering materials with albedo, normal, and roughness maps

## Risk Level
**LOW**

## Core Rules
- Use linear color space
- proper texture formats
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure base material properties
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Material setup
- scene rendering

## What NOT to Do
- Mixing PBR with non-PBR materials
- incorrect color spaces
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
