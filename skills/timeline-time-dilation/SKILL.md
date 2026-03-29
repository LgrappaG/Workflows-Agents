---
name: timeline-time-dilation
description: Implement time scaling and dilation within timeline playback
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Slow-motion effects, bullet time, gameplay integration
avoid: Physics desynchronization, audio artifacts, performance issues
mandates: Synchronize physics systems, handle audio carefully, profile impact
response: Configure time dilation, test physics sync, validate audio
---
# Timeline Time Dilation

Implement time scaling and dilation within timeline playback

## Risk Level
**MEDIUM**

## Core Rules
- Synchronize physics systems
- handle audio carefully
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure time dilation
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Slow-motion effects
- bullet time

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
