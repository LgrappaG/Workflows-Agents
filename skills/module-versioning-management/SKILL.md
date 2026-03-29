---
name: module-versioning-management
description: Manage module versioning and compatibility across versions
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Version compatibility, breaking change management, upgrade paths
avoid: Breaking changes without migration, version conflicts, orphaned code
mandates: Implement version tracking, support compatibility layers, validate upgrade paths
response: Track module versions, create compatibility layers, validate upgrade path, manage deprecation
---

# Module Versioning Management

Manage module versioning and compatibility across versions

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
- Version compatibility
- Development workflows

## What NOT to Do
- Breaking changes without migration
- Incomplete testing
- Deploy without validation
