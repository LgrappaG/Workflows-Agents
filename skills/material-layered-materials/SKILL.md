---
name: material-layered-materials
description: Combine multiple material layers for complex surfaces
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Multi-layer surfaces, weathering effects, complex materials
avoid: Excessive layering, performance degradation, layer conflicts
mandates: Use layer blending, manage complexity, profile GPU cost, validate appearance
response: Stack material layers, configure blending, validate visual result
---
# Material Layered Materials

Combine multiple material layers for complex surfaces

## Risk Level
**MEDIUM**

## Core Rules
- Use layer blending
- manage complexity
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Stack material layers
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Multi-layer surfaces
- weathering effects

## What NOT to Do
- Excessive layering
- performance degradation
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
