---
name: timeline-footstep-sync
description: Synchronize footstep audio with character animations in timeline
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Audio foley, character movement, sound synchronization
avoid: Audio desynchronization, missing footsteps, audio overlapping
mandates: Match audio events to animation frames, test synchronization, validate audio
response: Create footstep events, sync with animations, test audio timing
---
# Timeline Footstep Sync

Synchronize footstep audio with character animations in timeline

## Risk Level
**MEDIUM**

## Core Rules
- Match audio events to animation frames
- test synchronization
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create footstep events
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Audio foley
- character movement

## What NOT to Do
- Audio desynchronization
- missing footsteps
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
