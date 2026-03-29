---
name: animation-constraint-rigging
description: Implement constraints for rigging setup and skeletal control
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Rigging control, skeletal constraints, procedural positioning
avoid: Constraint conflicts, joint locking, deformation errors
mandates: Validate constraint chains, test deformation, handle edge cases
response: Configure constraints, test rigging, validate deformation
---
# Animation Constraint Rigging

Implement constraints for rigging setup and skeletal control

## Risk Level
**MEDIUM**

## Core Rules
- Validate constraint chains
- test deformation
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure constraints
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Rigging control
- skeletal constraints

## What NOT to Do
- Constraint conflicts
- joint locking
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
