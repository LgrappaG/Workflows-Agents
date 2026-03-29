---
name: networking-server-authority
description: Implement server-authoritative gameplay for security and integrity
risk: high
source: workspace
date_added: '2026-03-21'
usage: Secure gameplay, anti-cheat, authoritative state management
avoid: Server overload, action lag, validation failures
mandates: Validate all actions server-side, implement rate limiting, handle errors
response: Implement server authority, validate actions, test integrity
---
# Networking Server Authority

Implement server-authoritative gameplay for security and integrity

## Risk Level
**HIGH**

## Core Rules
- Validate all actions server-side
- implement rate limiting
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement server authority
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Secure gameplay
- anti-cheat

## What NOT to Do
- Server overload
- action lag
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
