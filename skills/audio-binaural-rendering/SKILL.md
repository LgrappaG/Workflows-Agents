---
name: audio-binaural-rendering
description: Implement binaural audio rendering for head-tracking VR/AR
risk: high
source: workspace
date_added: '2026-03-21'
usage: VR/AR audio, head tracking, immersive 3D audio
avoid: Head tracking sync issues, audio pops, quality degradation
mandates: Sync to head tracking, validate HRTF, test immersion
response: Implement binaural system, integrate head tracking, test immersion
---
# Audio Binaural Rendering

Implement binaural audio rendering for head-tracking VR/AR

## Risk Level
**HIGH**

## Core Rules
- Sync to head tracking
- validate HRTF
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement binaural system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- VR/AR audio
- head tracking

## What NOT to Do
- Head tracking sync issues
- audio pops
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
