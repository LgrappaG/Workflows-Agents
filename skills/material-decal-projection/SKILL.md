---
name: material-decal-projection
description: Project textures onto surfaces for dynamic material modification
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Dynamic decals, damage effects, procedural materials
avoid: Extreme decal density, performance degradation, visual clipping
mandates: Limit active decals, use efficient rendering, validate appearance
response: Project decals, configure blending, manage decal lifecycle
---
# Material Decal Projection

Project textures onto surfaces for dynamic material modification

## Risk Level
**MEDIUM**

## Core Rules
- Limit active decals
- use efficient rendering
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Project decals
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Dynamic decals
- damage effects

## What NOT to Do
- Extreme decal density
- performance degradation
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
