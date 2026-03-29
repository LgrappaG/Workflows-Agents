---
name: material-runtime-modification
description: Update materials during gameplay for visual feedback and effects
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Visual feedback, dynamic effects, gameplay integration
avoid: Inefficient updates, material duplication, performance degradation
mandates: Use material instances, batch updates, profile impact, clean up properly
response: Implement property changes, validate visual result, manage resources
---
# Material Runtime Modification

Update materials during gameplay for visual feedback and effects

## Risk Level
**MEDIUM**

## Core Rules
- Use material instances
- batch updates
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement property changes
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Visual feedback
- dynamic effects

## What NOT to Do
- Inefficient updates
- material duplication
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
