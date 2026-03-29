---
name: networking-message-ordering
description: Ensure messages are processed in correct order despite network delays
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Action ordering, consistent gameplay, state integrity
avoid: Out-of-order execution, state corruption, unexpected behavior
mandates: Implement sequence numbering, validate ordering, handle duplicates
response: Implement ordering system, test message sequence, validate consistency
---
# Networking Message Ordering

Ensure messages are processed in correct order despite network delays

## Risk Level
**MEDIUM**

## Core Rules
- Implement sequence numbering
- validate ordering
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement ordering system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Action ordering
- consistent gameplay

## What NOT to Do
- Out-of-order execution
- state corruption
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
