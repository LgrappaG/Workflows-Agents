---
name: debug-gc-profiling
description: Profile garbage collection for memory optimization
risk: low
source: workspace
date_added: '2026-03-21'
usage: GC analysis, memory optimization, allocation tuning
avoid: Inaccurate profiling, missed opportunities, poor diagnosis
mandates: Profile accurately, analyze GC, optimize allocations
response: Profile GC, analyze behavior, optimize patterns
---
# Debug Gc Profiling

Profile garbage collection for memory optimization

## Risk Level
**LOW**

## Core Rules
- Profile accurately
- analyze GC
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Profile GC
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- GC analysis
- memory optimization

## What NOT to Do
- Inaccurate profiling
- missed opportunities
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
