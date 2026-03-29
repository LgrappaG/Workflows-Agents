---
name: debug-heap-snapshot
description: Capture heap snapshots for memory analysis
risk: low
source: workspace
date_added: '2026-03-21'
usage: Memory debugging, leak detection, allocation analysis
avoid: Inaccurate snapshots, missed allocations, poor analysis
mandates: Capture accurately, analyze allocations, identify leaks
response: Capture heap snapshot, analyze allocations, identify leaks
---
# Debug Heap Snapshot

Capture heap snapshots for memory analysis

## Risk Level
**LOW**

## Core Rules
- Capture accurately
- analyze allocations
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Capture heap snapshot
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Memory debugging
- leak detection

## What NOT to Do
- Inaccurate snapshots
- missed allocations
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
