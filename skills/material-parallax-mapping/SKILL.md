---
name: material-parallax-mapping
description: Create depth illusion through view-dependent surface offset
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Surface depth illusion, high-quality materials, visual enhancement
avoid: Excessive parallax offset, silhouette distortion, performance issues
mandates: Use height maps, limit offset, test from multiple angles, profile GPU cost
response: Enable parallax effect, configure height scale, validate visual quality
---
# Material Parallax Mapping

Create depth illusion through view-dependent surface offset

## Risk Level
**MEDIUM**

## Core Rules
- Use height maps
- limit offset
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Enable parallax effect
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Surface depth illusion
- high-quality materials

## What NOT to Do
- Excessive parallax offset
- silhouette distortion
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
