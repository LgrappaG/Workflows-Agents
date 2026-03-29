---
name: networking-cloud-saves
description: Store player saves in cloud for cross-device access
risk: high
source: workspace
date_added: '2026-03-21'
usage: Data synchronization, player convenience, cross-platform play
avoid: Save corruption, sync failures, data loss
mandates: Implement robust sync, validate integrity, handle conflicts
response: Implement cloud saves, test synchronization, validate integrity
---
# Networking Cloud Saves

Store player saves in cloud for cross-device access

## Risk Level
**HIGH**

## Core Rules
- Implement robust sync
- validate integrity
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement cloud saves
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Data synchronization
- player convenience

## What NOT to Do
- Save corruption
- sync failures
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
