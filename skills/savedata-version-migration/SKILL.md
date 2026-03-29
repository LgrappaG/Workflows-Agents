---
name: savedata-version-migration
description: Migrate save data across save format versions
risk: high
source: workspace
date_added: '2026-03-24'
usage: Version compatibility, breaking change management, player save preservation
avoid: Save corruption, lost player data, irreversible migrations
mandates: Support multi-version migration, validate data integrity, provide rollback
response: Design migration framework, implement version handlers, add validation, test edge cases
---

# Savedata Version Migration

Migrate save data across save format versions

## Risk Level
**HIGH**

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
- Save corruption
- Incomplete testing
- Deploy without validation
