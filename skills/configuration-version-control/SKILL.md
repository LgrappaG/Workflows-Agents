---
name: configuration-version-control
description: Version configuration files and manage migrations
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Config versioning, migration management, rollback capability
avoid: Unversioned changes, broken migrations, lost configuration history
mandates: Track config versions, implement migration framework, validate backwards compatibility
response: Version config schema, implement migration system, validate upgrade path, test rollback
---

# Configuration Version Control

Version configuration files and manage migrations

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
- Config versioning
- Development workflows

## What NOT to Do
- Unversioned changes
- Incomplete testing
- Deploy without validation
