---
name: advanced-il-emit
description: Use IL emit for low-level code generation
risk: high
source: workspace
date_added: '2026-03-21'
usage: Performance optimization, code generation, dynamic methods
avoid: IL errors, stack corruption, platform incompatibility
mandates: Validate IL, test thoroughly, handle edge cases
response: Generate IL, validate bytecode, test execution
---
# Advanced Il Emit

Use IL emit for low-level code generation

## Risk Level
**HIGH**

## Core Rules
- Validate IL
- test thoroughly
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Generate IL
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Performance optimization
- code generation

## What NOT to Do
- IL errors
- stack corruption
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
