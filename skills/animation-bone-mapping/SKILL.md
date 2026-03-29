---
name: animation-bone-mapping
description: Map bones between different skeletons for animation compatibility
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Cross-skeleton compatibility, animation reuse, character variety
avoid: Mapping errors, bone mismatches, animation failures
mandates: Validate bone hierarchies, test mapping accuracy, document mappings
response: Create bone mapping, test compatibility, validate results
---
# Animation Bone Mapping

Map bones between different skeletons for animation compatibility

## Risk Level
**MEDIUM**

## Core Rules
- Validate bone hierarchies
- test mapping accuracy
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create bone mapping
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Cross-skeleton compatibility
- animation reuse

## What NOT to Do
- Mapping errors
- bone mismatches
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
