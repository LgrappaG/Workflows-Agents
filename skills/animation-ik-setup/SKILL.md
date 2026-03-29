---
name: animation-ik-setup
description: Configure Inverse Kinematics for natural limb positioning
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Limb placement, foot alignment, procedural positioning
avoid: IK singularities, joint locking, unnatural poses
mandates: Validate IK targets, test collision avoidance, ensure smoothness
response: Set up IK chains, configure targets, test positioning
---
# Animation Ik Setup

Configure Inverse Kinematics for natural limb positioning

## Risk Level
**MEDIUM**

## Core Rules
- Validate IK targets
- test collision avoidance
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Set up IK chains
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Limb placement
- foot alignment

## What NOT to Do
- IK singularities
- joint locking
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
