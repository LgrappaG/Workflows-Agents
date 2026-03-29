---
name: networking-server-load-balancing
description: Distribute server load across multiple server instances
risk: high
source: workspace
date_added: '2026-03-21'
usage: Scalability, high-player count, server management
avoid: Server overload, uneven distribution, player session loss
mandates: Implement balanced distribution, monitor loads, handle failures
response: Design load balancing, implement distribution, test scalability
---
# Networking Server Load Balancing

Distribute server load across multiple server instances

## Risk Level
**HIGH**

## Core Rules
- Implement balanced distribution
- monitor loads
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Design load balancing
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Scalability
- high-player count

## What NOT to Do
- Server overload
- uneven distribution
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
