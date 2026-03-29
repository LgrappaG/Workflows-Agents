---
name: audio-spatial-3d
description: Implement 3D spatial audio with distance and directional attenuation
risk: low
source: workspace
date_added: '2026-03-21'
usage: 3D positional audio, environmental sound, immersive audio
avoid: Incorrect attenuation curves, confusing directionality, poor performance
mandates: Use realistic attenuation, test spatial accuracy, profile performance
response: Configure 3D settings, test positioning, validate audio quality
---
# Audio Spatial 3D

Implement 3D spatial audio with distance and directional attenuation

## Risk Level
**LOW**

## Core Rules
- Use realistic attenuation
- test spatial accuracy
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure 3D settings
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- 3D positional audio
- environmental sound

## What NOT to Do
- Incorrect attenuation curves
- confusing directionality
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
