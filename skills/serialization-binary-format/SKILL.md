---
name: serialization-binary-format
description: Implement binary serialization for efficient save files
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Performance optimization, file size reduction, save system foundation
avoid: Format brittleness, endianness issues, backwards incompatibility
mandates: Support format versioning, validate binary integrity, test cross-platform compatibility
response: Design binary format, implement serialization encoder, add versioning, test portability
---

# Serialization Binary Format

Implement binary serialization for efficient save files

## Risk Level
**MEDIUM**

## Core Rules
- Implement properly
- Test thoroughly
- Validate results

## Response Pattern

1. Design appropriate approach
2. Implement solution
3. Test edge cases
4. Validate quality

## Usage Contexts
- Performance optimization
- Development workflows

## What NOT to Do
- Format brittleness
- Incomplete testing
- Deploy without validation
