---
name: material-normal-mapping
description: Create surface detail using normal maps without increasing geometry
risk: low
source: workspace
date_added: '2026-03-21'
usage: Surface detail, performance optimization, visual complexity
avoid: Incorrect tangent space, swapped channels, low-quality normals
mandates: Use DirectX or OpenGL format consistently, proper UV mapping, test orientation
response: Import normal maps, verify tangent space, adjust strength, validate detail
---
# Material Normal Mapping

Create surface detail using normal maps without increasing geometry

## Risk Level
**LOW**

## Core Rules
- Use DirectX or OpenGL format consistently
- proper UV mapping
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Import normal maps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Surface detail
- performance optimization

## What NOT to Do
- Incorrect tangent space
- swapped channels
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
