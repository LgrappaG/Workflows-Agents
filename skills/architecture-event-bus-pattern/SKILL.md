---
name: architecture-event-bus-pattern
description: Implement event bus for decoupled inter-module communication
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Decoupled messaging, event-driven architecture, reduced coupling
avoid: Event handler leaks, circular event chains, performance degradation
mandates: Implement subscription lifecycle, detect circular events, monitor performance
response: Design event bus, implement pub-sub mechanism, add listener cleanup, optimize dispatch
---

# Architecture Event Bus Pattern

Implement event bus for decoupled inter-module communication

## Risk Level
**MEDIUM**

## Core Rules
- Implement properly
- Test thoroughly
- Validate results

## Response Pattern

1. Design appropriate approach
2. Implement solution
3. Test edge cases
4. Validate quality

## Usage Contexts
- Decoupled messaging
- Development workflows

## What NOT to Do
- Event handler leaks
- Incomplete testing
- Deploy without validation
