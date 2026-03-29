---
name: material-subsurface-scattering
description: Simulate light scattering through semi-transparent materials
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Skin rendering, foliage, translucent materials, realism
avoid: Performance overhead, extreme scattering, unrealistic colors
mandates: Profile GPU impact, use screen-space approximation, validate appearance
response: Configure SSS parameters, apply maps, validate visual quality
---
# Material Subsurface Scattering

Simulate light scattering through semi-transparent materials

## Risk Level
**MEDIUM**

## Core Rules
- Profile GPU impact
- use screen-space approximation
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure SSS parameters
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Skin rendering
- foliage

## What NOT to Do
- Performance overhead
- extreme scattering
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
