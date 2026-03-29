---
name: material-blending-modes
description: Apply appropriate blend modes for material composition
risk: low
source: workspace
date_added: '2026-03-21'
usage: Material composition, visual effects, transparency handling
avoid: Incorrect blend mode selection, visual artifacts
mandates: Understand blend mode effects, validate visual result, test on target hardware
response: Select blend mode, test appearance, adjust for desired effect
---
# Material Blending Modes

Apply appropriate blend modes for material composition

## Risk Level
**LOW**

## Core Rules
- Understand blend mode effects
- validate visual result
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Select blend mode
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Material composition
- visual effects

## What NOT to Do
- Incorrect blend mode selection
- visual artifacts
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
