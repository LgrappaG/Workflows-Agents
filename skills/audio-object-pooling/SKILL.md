---
name: audio-object-pooling
description: Implement audio source pooling for efficient sound effect management
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Performance optimization, memory management, sound effect efficiency
avoid: Object pool exhaustion, memory leaks, audio starvation
mandates: Pre-allocate pools, monitor pool usage, implement fallback behavior
response: Create audio pool, configure pool size, test under load
---
# Audio Object Pooling

Implement audio source pooling for efficient sound effect management

## Risk Level
**MEDIUM**

## Core Rules
- Pre-allocate pools
- monitor pool usage
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create audio pool
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Performance optimization
- memory management

## What NOT to Do
- Object pool exhaustion
- memory leaks
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
