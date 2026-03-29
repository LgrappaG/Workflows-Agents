---
name: timeline-camera-transitions
description: Implement smooth camera transitions between timeline keyframes
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Camera work, cinematic framing, scene transitions
avoid: Jarring cuts, interpolation issues, clipping problems
mandates: Use smooth interpolation, validate camera paths, test on target hardware
response: Create camera transitions, configure interpolation, validate smoothness
---
# Timeline Camera Transitions

Implement smooth camera transitions between timeline keyframes

## Risk Level
**MEDIUM**

## Core Rules
- Use smooth interpolation
- validate camera paths
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create camera transitions
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Camera work
- cinematic framing

## What NOT to Do
- Jarring cuts
- interpolation issues
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
