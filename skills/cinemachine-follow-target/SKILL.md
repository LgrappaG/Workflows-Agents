---
name: cinemachine-follow-target
description: Implement target following behavior for cameras
risk: low
source: workspace
date_added: '2026-03-21'
usage: Player following, target tracking, dynamic framing
avoid: Lag issues, lost targets, poor framing
mandates: Handle target loss, tune damping, validate framing
response: Configure follow behavior, tune parameters, test tracking
---
# Cinemachine Follow Target

Implement target following behavior for cameras

## Risk Level
**LOW**

## Core Rules
- Handle target loss
- tune damping
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure follow behavior
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Player following
- target tracking

## What NOT to Do
- Lag issues
- lost targets
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
