---
name: terrain-lightmap-generation
description: Generate lightmaps for terrain lighting optimization
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Lighting optimization, baked lighting, performance improvement
avoid: Low-quality lightmaps, baking errors, excessive memory
mandates: Use appropriate resolution, validate results, profile memory impact
response: Generate lightmaps, validate quality, optimize resolution
---
# Terrain Lightmap Generation

Generate lightmaps for terrain lighting optimization

## Risk Level
**MEDIUM**

## Core Rules
- Use appropriate resolution
- validate results
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Generate lightmaps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Lighting optimization
- baked lighting

## What NOT to Do
- Low-quality lightmaps
- baking errors
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
