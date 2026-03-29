---
name: graphics-temporal-antialiasing
description: Implement temporal antialiasing for smooth edge rendering
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Edge quality, motion smoothing, reduced aliasing
avoid: Ghosting, temporal artifacts, motion blur
mandates: Tune TAA parameters, validate visual quality, test motion
response: Configure TAA, tune parameters, test on motion
---
# Graphics Temporal Antialiasing

Implement temporal antialiasing for smooth edge rendering

## Risk Level
**MEDIUM**

## Core Rules
- Tune TAA parameters
- validate visual quality
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure TAA
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Edge quality
- motion smoothing

## What NOT to Do
- Ghosting
- temporal artifacts
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
