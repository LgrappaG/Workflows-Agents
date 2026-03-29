---
name: networking-connection-management
description: Manage network connections with reconnection and timeout handling
risk: high
source: workspace
date_added: '2026-03-21'
usage: Connection reliability, error recovery, network stability
avoid: Connection drops, lost sessions, unrecoverable states
mandates: Implement reconnection, handle timeouts, validate recovery
response: Implement connection manager, test reconnection, validate stability
---
# Networking Connection Management

Manage network connections with reconnection and timeout handling

## Risk Level
**HIGH**

## Core Rules
- Implement reconnection
- handle timeouts
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement connection manager
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Connection reliability
- error recovery

## What NOT to Do
- Connection drops
- lost sessions
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
