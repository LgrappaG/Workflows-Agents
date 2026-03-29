---
name: audio-platform-specific-codecs
description: Handle platform-specific audio codec requirements and limitations
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Platform support, codec compatibility, cross-platform audio
avoid: Codec mismatches, incompatibility issues, quality loss
mandates: Support target platform codecs, test on all platforms, validate quality
response: Configure platform codecs, test on platforms, validate compatibility
---
# Audio Platform Specific Codecs

Handle platform-specific audio codec requirements and limitations

## Risk Level
**MEDIUM**

## Core Rules
- Support target platform codecs
- test on all platforms
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure platform codecs
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Platform support
- codec compatibility

## What NOT to Do
- Codec mismatches
- incompatibility issues
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
