---
name: terrain-streaming
description: Implement terrain streaming for infinite or very large worlds
risk: high
source: workspace
date_added: '2026-03-21'
usage: Large worlds, memory optimization, open-world design
avoid: Visible loading, memory spikes, streaming stalls
mandates: Implement smooth loading, manage memory carefully, test extensively
response: Set up streaming system, test transitions, monitor memory
---
# Terrain Streaming

Implement terrain streaming for infinite or very large worlds

## Risk Level
**HIGH**

## Core Rules
- Implement smooth loading
- manage memory carefully
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Set up streaming system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Large worlds
- memory optimization

## What NOT to Do
- Visible loading
- memory spikes
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
