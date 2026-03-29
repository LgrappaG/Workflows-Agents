---
name: audio-streaming-audio
description: Stream audio for large files and memory-constrained platforms
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Memory optimization, large audio files, streaming music
avoid: Streaming artifacts, buffering issues, memory waste
mandates: Implement smooth buffering, test on target platform, validate transitions
response: Configure streaming, test buffering, validate playback
---
# Audio Streaming Audio

Stream audio for large files and memory-constrained platforms

## Risk Level
**MEDIUM**

## Core Rules
- Implement smooth buffering
- test on target platform
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure streaming
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Memory optimization
- large audio files

## What NOT to Do
- Streaming artifacts
- buffering issues
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
