---
name: animation-streaming
description: Implement streaming for large animation data sets
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Large-scale animation, memory efficiency, streaming playback
avoid: Buffer underruns, streaming artifacts, memory bloat
mandates: Implement robust buffering, validate streaming, monitor memory
response: Implement streaming system, test buffering, validate performance
---
# Animation Streaming

Implement streaming for large animation data sets

## Risk Level
**MEDIUM**

## Core Rules
- Implement robust buffering
- validate streaming
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement streaming system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Large-scale animation
- memory efficiency

## What NOT to Do
- Buffer underruns
- streaming artifacts
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
