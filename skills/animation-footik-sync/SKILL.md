---
name: animation-footik-sync
description: Synchronize foot IK with ground terrain and animation curves
risk: high
source: workspace
date_added: '2026-03-21'
usage: Terrain adaptation, footstep synchronization, natural movement
avoid: Foot sliding, IK jitter, terrain clipping
mandates: Implement raycast grounding, validate curve alignment, profile performance
response: Configure terrain detection, sync curves, test on varied terrain
---
# Animation Footik Sync

Synchronize foot IK with ground terrain and animation curves

## Risk Level
**HIGH**

## Core Rules
- Implement raycast grounding
- validate curve alignment
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure terrain detection
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Terrain adaptation
- footstep synchronization

## What NOT to Do
- Foot sliding
- IK jitter
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
