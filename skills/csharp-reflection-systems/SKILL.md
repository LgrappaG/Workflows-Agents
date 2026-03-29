---
name: csharp-reflection-systems
description: Leverage reflection for dynamic type inspection and invocation
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Dynamic features, type inspection, dynamic invocation
avoid: Performance degradation, type safety loss, maintenance complexity
mandates: Cache reflection data, profile carefully, document usage
response: Use reflection strategically, optimize caching, test thoroughly
---
# Csharp Reflection Systems

Leverage reflection for dynamic type inspection and invocation

## Risk Level
**MEDIUM**

## Core Rules
- Cache reflection data
- profile carefully
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Use reflection strategically
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Dynamic features
- type inspection

## What NOT to Do
- Performance degradation
- type safety loss
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
