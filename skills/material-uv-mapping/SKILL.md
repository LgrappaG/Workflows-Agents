---
name: material-uv-mapping
description: Create and manage UV coordinates for texture application
risk: low
source: workspace
date_added: '2026-03-21'
usage: Texture projection, material application, asset preparation
avoid: UV overlaps, mirroring without purpose, poor seam placement
mandates: Minimize overlaps, optimize for memory, maintain 0-1 space, plan layouts
response: Generate UV maps, optimize layout, validate texture application
---
# Material Uv Mapping

Create and manage UV coordinates for texture application

## Risk Level
**LOW**

## Core Rules
- Minimize overlaps
- optimize for memory
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Generate UV maps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Texture projection
- material application

## What NOT to Do
- UV overlaps
- mirroring without purpose
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
