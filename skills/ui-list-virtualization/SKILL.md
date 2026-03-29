---
name: ui-list-virtualization
description: Optimize large list rendering through virtualization
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Performance optimization, large lists, memory efficiency
avoid: Rendering all items, memory waste, performance degradation
mandates: Implement recycling, validate scrolling, profile performance
response: Implement virtualization, configure recycling, test scrolling
---
# Ui List Virtualization

Optimize large list rendering through virtualization

## Risk Level
**MEDIUM**

## Core Rules
- Implement recycling
- validate scrolling
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement virtualization
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Performance optimization
- large lists

## What NOT to Do
- Rendering all items
- memory waste
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
