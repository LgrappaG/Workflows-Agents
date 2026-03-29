---
name: material-translucency-setup
description: Implement semi-transparent materials with light transmission
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Glass, foliage, transparent effects, light transmission
avoid: Extreme transparency, Z-fighting, incorrect blend modes
mandates: Use proper blend mode, manage depth sorting, implement subsurface scattering
response: Configure transparency, set blend mode, implement light transmission
---
# Material Translucency Setup

Implement semi-transparent materials with light transmission

## Risk Level
**MEDIUM**

## Core Rules
- Use proper blend mode
- manage depth sorting
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure transparency
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Glass
- foliage

## What NOT to Do
- Extreme transparency
- Z-fighting
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
