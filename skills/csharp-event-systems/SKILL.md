---
name: csharp-event-systems
description: Implement event-driven systems for decoupled communication
risk: low
source: workspace
date_added: '2026-03-21'
usage: Event handling, decoupled communication, reactive systems
avoid: Memory leaks, event storms, dangling references
mandates: Unsubscribe properly, manage subscriptions, test cleanup
response: Implement events, manage subscriptions, test lifecycle
---
# Csharp Event Systems

Implement event-driven systems for decoupled communication

## Risk Level
**LOW**

## Core Rules
- Unsubscribe properly
- manage subscriptions
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement events
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Event handling
- decoupled communication

## What NOT to Do
- Memory leaks
- event storms
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
