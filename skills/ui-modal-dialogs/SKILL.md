---
name: ui-modal-dialogs
description: Create and manage modal dialog windows
risk: low
source: workspace
date_added: '2026-03-21'
usage: User confirmation, data input, focused interaction
avoid: Multiple modals, focus loss, incomplete dismissal
mandates: Implement focus management, handle dismissal, validate stacking
response: Create modal dialog, manage focus, implement dismissal
---
# Ui Modal Dialogs

Create and manage modal dialog windows

## Risk Level
**LOW**

## Core Rules
- Implement focus management
- handle dismissal
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create modal dialog
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- User confirmation
- data input

## What NOT to Do
- Multiple modals
- focus loss
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
