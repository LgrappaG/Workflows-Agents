---
name: networking-player-persistence
description: Persist player data across sessions for long-term progression
risk: high
source: workspace
date_added: '2026-03-21'
usage: Player progression, data persistence, long-term gameplay
avoid: Data loss, corruption, cheating exploitation
mandates: Implement secure storage, validate integrity, test persistence
response: Design persistence system, implement storage, test data integrity
---
# Networking Player Persistence

Persist player data across sessions for long-term progression

## Risk Level
**HIGH**

## Core Rules
- Implement secure storage
- validate integrity
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Design persistence system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Player progression
- data persistence

## What NOT to Do
- Data loss
- corruption
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
