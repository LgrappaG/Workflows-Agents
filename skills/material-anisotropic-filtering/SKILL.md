---
name: material-anisotropic-filtering
description: Improve texture filtering quality on angled surfaces
risk: low
source: workspace
date_added: '2026-03-21'
usage: Visual quality enhancement, distant surface improvement, filtering
avoid: Excessive anisotropy, performance degradation, quality overkill
mandates: Balance quality with performance, profile impact, test on hardware
response: Enable anisotropic filtering, configure level, validate quality
---
# Material Anisotropic Filtering

Improve texture filtering quality on angled surfaces

## Risk Level
**LOW**

## Core Rules
- Balance quality with performance
- profile impact
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Enable anisotropic filtering
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Visual quality enhancement
- distant surface improvement

## What NOT to Do
- Excessive anisotropy
- performance degradation
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
