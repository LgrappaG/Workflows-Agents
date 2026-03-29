---
name: vfx-gpu-instancing
description: Implement GPU instancing for efficient particle and effect rendering
risk: low
source: workspace
date_added: '2026-03-21'
usage: Batching optimization, particle efficiency, draw call reduction
avoid: Draw call overhead, batching failures, memory issues
mandates: Implement proper batching, validate efficiency, profile draws
response: Configure instancing, validate batching, test efficiency
---
# Vfx Gpu Instancing

Implement GPU instancing for efficient particle and effect rendering

## Risk Level
**LOW**

## Core Rules
- Implement proper batching
- validate efficiency
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure instancing
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Batching optimization
- particle efficiency

## What NOT to Do
- Draw call overhead
- batching failures
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
