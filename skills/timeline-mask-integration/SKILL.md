---
name: timeline-mask-integration
description: Use animation masks with timeline for selective animation control
risk: low
source: workspace
date_added: '2026-03-21'
usage: Partial animations, layered motion, complex choreography
avoid: Mask conflicts, incomplete masking, animation artifacts
mandates: Design mask hierarchy, test all combinations, validate results
response: Create animation masks, apply to tracks, test combinations
---
# Timeline Mask Integration

Use animation masks with timeline for selective animation control

## Risk Level
**LOW**

## Core Rules
- Design mask hierarchy
- test all combinations
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create animation masks
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Partial animations
- layered motion

## What NOT to Do
- Mask conflicts
- incomplete masking
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
