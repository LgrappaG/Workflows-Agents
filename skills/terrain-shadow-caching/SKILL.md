---
name: terrain-shadow-caching
description: Cache terrain shadows for improved performance
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Shadow optimization, performance improvement, visual quality
avoid: Stale shadows, incorrect caching, performance regression
mandates: Invalidate cache on terrain changes, validate results, profile impact
response: Configure shadow caching, validate appearance, test performance
---
# Terrain Shadow Caching

Cache terrain shadows for improved performance

## Risk Level
**MEDIUM**

## Core Rules
- Invalidate cache on terrain changes
- validate results
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure shadow caching
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Shadow optimization
- performance improvement

## What NOT to Do
- Stale shadows
- incorrect caching
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
