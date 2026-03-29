---
name: audio-effects-eq
description: Apply equalization to shape audio frequency response
risk: low
source: workspace
date_added: '2026-03-21'
usage: Audio shaping, frequency response control, sound design
avoid: Over-EQing, unnatural frequencies, performance issues
mandates: Use standard EQ curves, test on reference hardware, validate results
response: Create EQ curves, apply to tracks, test audio quality
---
# Audio Effects Eq

Apply equalization to shape audio frequency response

## Risk Level
**LOW**

## Core Rules
- Use standard EQ curves
- test on reference hardware
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Create EQ curves
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Audio shaping
- frequency response control

## What NOT to Do
- Over-EQing
- unnatural frequencies
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
