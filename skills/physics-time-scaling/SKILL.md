---
name: physics-time-scaling
description: Implement time scaling for slow-motion and fast-motion physics
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Slow motion effects, time dilation, gameplay mechanics
avoid: Physics desynchronization, audio artifacts, extreme instability
mandates: Maintain physics stability, test edge cases, validate behavior
response: Configure time scaling, test physics stability, validate effects
---
# Physics Time Scaling

Implement time scaling for slow-motion and fast-motion physics

## Risk Level
**MEDIUM**

## Core Rules
- Maintain physics stability
- test edge cases
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure time scaling
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Slow motion effects
- time dilation

## What NOT to Do
- Physics desynchronization
- audio artifacts
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
