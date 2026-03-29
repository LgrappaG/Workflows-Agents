---
name: material-refraction
description: Implement light bending through transparent materials
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Glass, water, transparent surfaces, optical effects
avoid: Incorrect IOR values, performance issues, screen-space artifacts
mandates: Use physically accurate IOR values, handle edge cases, profile performance
response: Set refraction index, configure distortion, validate optical accuracy
---
# Material Refraction

Implement light bending through transparent materials

## Risk Level
**MEDIUM**

## Core Rules
- Use physically accurate IOR values
- handle edge cases
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Set refraction index
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Glass
- water

## What NOT to Do
- Incorrect IOR values
- performance issues
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
