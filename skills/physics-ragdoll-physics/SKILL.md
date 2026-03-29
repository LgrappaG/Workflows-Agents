---
name: physics-ragdoll-physics
description: Implement ragdoll physics for lifelike character death/injury animations
risk: high
source: workspace
date_added: '2026-03-21'
usage: Character death, physics-based animation, impact response
avoid: Jerky ragdolls, penetration, unrealistic collapse
mandates: Tune joint constraints, validate collisions, test behavior
response: Configure ragdoll setup, test animations, validate physics
---
# Physics Ragdoll Physics

Implement ragdoll physics for lifelike character death/injury animations

## Risk Level
**HIGH**

## Core Rules
- Tune joint constraints
- validate collisions
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure ragdoll setup
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Character death
- physics-based animation

## What NOT to Do
- Jerky ragdolls
- penetration
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
