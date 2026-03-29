---
name: terrain-splat-mapping
description: Apply layered textures using splat mapping techniques
risk: low
source: workspace
date_added: '2026-03-21'
usage: Multi-texture blending, terrain variety, visual complexity
avoid: Visible seams, poor blending, texture stretching
mandates: Use proper UV mapping, blend layers smoothly, validate appearance
response: Set up splat mapping, blend layers, validate appearance
---
# Terrain Splat Mapping

Apply layered textures using splat mapping techniques

## Risk Level
**LOW**

## Core Rules
- Use proper UV mapping
- blend layers smoothly
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Set up splat mapping
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Multi-texture blending
- terrain variety

## What NOT to Do
- Visible seams
- poor blending
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
