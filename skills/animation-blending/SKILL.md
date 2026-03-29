---
name: animation-blending
description: Master layered animation blending techniques for smooth transitions
risk: low
source: workspace
date_added: '2026-03-21'
usage: Multi-layer blending, smooth transitions, animation layering
avoid: Conflicting blend weights, abrupt changes, texture thrashing
mandates: Implement weight normalization, validate blend states, test transitions
response: Configure blending, set weights, validate smoothness
---
# Animation Blending

Master layered animation blending techniques for smooth transitions

## Risk Level
**LOW**

## Core Rules
- Implement weight normalization
- validate blend states
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure blending
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Multi-layer blending
- smooth transitions

## What NOT to Do
- Conflicting blend weights
- abrupt changes
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
