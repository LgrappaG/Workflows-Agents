---
name: material-triplanar-mapping
description: Apply textures across multiple planes to avoid stretching on complex geometry
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Complex geometry texturing, rock/terrain surfaces, projection-free texturing
avoid: Over-blending, visible seams, high shader complexity
mandates: Use three texture projections, blend weights normalized, consider performance
response: Implement triplanar UV projection, configure blend weights, optimize shader
---
# Material Triplanar Mapping

Apply textures across multiple planes to avoid stretching on complex geometry

## Risk Level
**MEDIUM**

## Core Rules
- Use three texture projections
- blend weights normalized
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement triplanar UV projection
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Complex geometry texturing
- rock/terrain surfaces

## What NOT to Do
- Over-blending
- visible seams
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
