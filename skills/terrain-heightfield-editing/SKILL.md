---
name: terrain-heightfield-editing
description: Edit terrain heightfields using sculpting tools
risk: low
source: workspace
date_added: '2026-03-21'
usage: Terrain sculpting, landscape creation, manual editing
avoid: Accidental destructive edits, unsaved changes, poor workflow
mandates: Implement undo/redo, save frequently, validate changes
response: Sculpt terrain, apply edits, validate appearance
---
# Terrain Heightfield Editing

Edit terrain heightfields using sculpting tools

## Risk Level
**LOW**

## Core Rules
- Implement undo/redo
- save frequently
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Sculpt terrain
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Terrain sculpting
- landscape creation

## What NOT to Do
- Accidental destructive edits
- unsaved changes
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
