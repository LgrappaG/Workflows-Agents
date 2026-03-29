---
name: networking-client-authority
description: Implement client-authoritative gameplay for reduced latency
risk: high
source: workspace
date_added: '2026-03-21'
usage: Low-latency gameplay, client control, gameplay responsiveness
avoid: Cheating exploitation, state inconsistency, desynchronization
mandates: Validate client actions, implement anti-cheat, handle conflicts
response: Implement client authority, validate actions, test anti-cheat
---
# Networking Client Authority

Implement client-authoritative gameplay for reduced latency

## Risk Level
**HIGH**

## Core Rules
- Validate client actions
- implement anti-cheat
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement client authority
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Low-latency gameplay
- client control

## What NOT to Do
- Cheating exploitation
- state inconsistency
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
