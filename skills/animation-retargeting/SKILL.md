---
name: animation-retargeting
description: Retarget animations between different skeleton structures
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Character variety, animation reuse, cross-character compatibility
avoid: Bone mapping errors, scale mismatches, joint failures
mandates: Validate bone hierarchies, test retargeting accuracy, handle edge cases
response: Configure bone mapping, test retargeting, validate results
---
# Animation Retargeting

Retarget animations between different skeleton structures

## Risk Level
**MEDIUM**

## Core Rules
- Validate bone hierarchies
- test retargeting accuracy
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure bone mapping
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Character variety
- animation reuse

## What NOT to Do
- Bone mapping errors
- scale mismatches
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
