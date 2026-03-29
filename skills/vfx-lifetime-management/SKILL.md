---
name: vfx-lifetime-management
description: Manage particle lifetimes for efficient memory usage
risk: low
source: workspace
date_added: '2026-03-21'
usage: Memory efficiency, particle cleanup, lifecycle management
avoid: Memory leaks, orphaned particles, excessive memory
mandates: Clean up properly, manage lifecycle, monitor memory
response: Configure lifetime, implement cleanup, test memory
---
# Vfx Lifetime Management

Manage particle lifetimes for efficient memory usage

## Risk Level
**LOW**

## Core Rules
- Clean up properly
- manage lifecycle
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure lifetime
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Memory efficiency
- particle cleanup

## What NOT to Do
- Memory leaks
- orphaned particles
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
