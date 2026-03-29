---
name: physics-object-pooling
description: Implement physics object pooling for efficient rigid body management
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Performance optimization, memory efficiency, particle physics
avoid: Pool exhaustion, memory leaks, physics starvation
mandates: Pre-allocate pools appropriately, monitor usage, implement fallback
response: Create physics pool, configure size, test under load
---
# Physics Object Pooling

Implement physics object pooling for efficient rigid body management

## Risk Level
**MEDIUM**

## Core Rules
- Pre-allocate pools appropriately
- monitor usage
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create physics pool
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Performance optimization
- memory efficiency

## What NOT to Do
- Pool exhaustion
- memory leaks
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
