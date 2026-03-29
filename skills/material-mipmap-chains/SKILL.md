---
name: material-mipmap-chains
description: Generate and manage mipmap chains for texture filtering
risk: low
source: workspace
date_added: '2026-03-21'
usage: Performance optimization, filtering quality, memory management
avoid: Missing mipmaps, incorrect generation, memory waste
mandates: Generate complete chains, use proper filtering, validate appearance
response: Generate mipmaps, configure filtering, validate distant appearance
---
# Material Mipmap Chains

Generate and manage mipmap chains for texture filtering

## Risk Level
**LOW**

## Core Rules
- Generate complete chains
- use proper filtering
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Generate mipmaps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Performance optimization
- filtering quality

## What NOT to Do
- Missing mipmaps
- incorrect generation
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
