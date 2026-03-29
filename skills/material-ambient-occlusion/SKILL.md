---
name: material-ambient-occlusion
description: Apply ambient occlusion to enhance surface detail and shadow depth
risk: low
source: workspace
date_added: '2026-03-21'
usage: Detail enhancement, shadow control, visual depth
avoid: Overusing AO, applying to entire surfaces uniformly
mandates: Use baked or real-time AO, integrate with shader, maintain performance
response: Import AO maps, configure blend modes, integrate with material stack
---
# Material Ambient Occlusion

Apply ambient occlusion to enhance surface detail and shadow depth

## Risk Level
**LOW**

## Core Rules
- Use baked or real-time AO
- integrate with shader
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Import AO maps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Detail enhancement
- shadow control

## What NOT to Do
- Overusing AO
- applying to entire surfaces uniformly
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
