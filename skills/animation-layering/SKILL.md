---
name: animation-layering
description: Implement animation layer stacking for complex behaviors
risk: low
source: workspace
date_added: '2026-03-21'
usage: Additive animations, gesture layering, effect stacking
avoid: Layer conflicts, weight overflow, performance degradation
mandates: Manage layer ordering, validate weights, monitor performance
response: Create layer structure, configure weights, validate blend
---
# Animation Layering

Implement animation layer stacking for complex behaviors

## Risk Level
**LOW**

## Core Rules
- Manage layer ordering
- validate weights
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create layer structure
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Additive animations
- gesture layering

## What NOT to Do
- Layer conflicts
- weight overflow
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
