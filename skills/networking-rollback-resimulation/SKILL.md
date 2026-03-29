---
name: networking-rollback-resimulation
description: Implement rollback netcode for fighting game-style latency compensation
risk: high
source: workspace
date_added: '2026-03-21'
usage: Low-latency gameplay, fighting games, competitive play
avoid: Inconsistent rollback, visual glitches, state divergence
mandates: Validate rollback accuracy, test consistency, handle edge cases
response: Implement rollback system, test consistency, validate visuals
---
# Networking Rollback Resimulation

Implement rollback netcode for fighting game-style latency compensation

## Risk Level
**HIGH**

## Core Rules
- Validate rollback accuracy
- test consistency
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement rollback system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Low-latency gameplay
- fighting games

## What NOT to Do
- Inconsistent rollback
- visual glitches
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
