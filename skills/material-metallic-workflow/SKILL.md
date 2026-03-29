---
name: material-metallic-workflow
description: Implement metallic surface properties for realistic reflections and specularity
risk: low
source: workspace
date_added: '2026-03-21'
usage: Metal rendering, reflective surfaces, material realism
avoid: Applying metallic to non-metal surfaces, incorrect smoothness values
mandates: Metallic 0-1 range, pair with appropriate roughness, use proper cubemaps
response: Define metallic parameter, configure reflections, validate material appearance
---
# Material Metallic Workflow

Implement metallic surface properties for realistic reflections and specularity

## Risk Level
**LOW**

## Core Rules
- Metallic 0-1 range
- pair with appropriate roughness
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Define metallic parameter
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Metal rendering
- reflective surfaces

## What NOT to Do
- Applying metallic to non-metal surfaces
- incorrect smoothness values
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
