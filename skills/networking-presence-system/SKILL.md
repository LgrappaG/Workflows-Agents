---
name: networking-presence-system
description: Track and broadcast player presence and availability status
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Player status, friend systems, matchmaking support
avoid: Status sync failures, false presence, privacy issues
mandates: Implement reliable sync, protect privacy, validate status accuracy
response: Implement presence tracking, test status sync, validate accuracy
---
# Networking Presence System

Track and broadcast player presence and availability status

## Risk Level
**MEDIUM**

## Core Rules
- Implement reliable sync
- protect privacy
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement presence tracking
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Player status
- friend systems

## What NOT to Do
- Status sync failures
- false presence
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
