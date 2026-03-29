---
name: ui-focus-navigation
description: Implement focus-based navigation for keyboard and gamepad input
risk: low
source: workspace
date_added: '2026-03-21'
usage: Keyboard navigation, accessibility, input handling
avoid: Broken focus flow, unreachable elements, confusing navigation
mandates: Define focus order, handle edge cases, validate navigation
response: Set up focus system, test navigation, validate accessibility
---
# Ui Focus Navigation

Implement focus-based navigation for keyboard and gamepad input

## Risk Level
**LOW**

## Core Rules
- Define focus order
- handle edge cases
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Set up focus system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Keyboard navigation
- accessibility

## What NOT to Do
- Broken focus flow
- unreachable elements
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
