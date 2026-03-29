---
name: debug-hot-reload
description: Implement hot reload for rapid iteration and debugging
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Rapid iteration, live debugging, fast development
avoid: Reload failures, state corruption, data loss
mandates: Ensure reload reliability, preserve state, validate integrity
response: Implement hot reload, test reliability, validate state
---
# Debug Hot Reload

Implement hot reload for rapid iteration and debugging

## Risk Level
**MEDIUM**

## Core Rules
- Ensure reload reliability
- preserve state
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement hot reload
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Rapid iteration
- live debugging

## What NOT to Do
- Reload failures
- state corruption
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
