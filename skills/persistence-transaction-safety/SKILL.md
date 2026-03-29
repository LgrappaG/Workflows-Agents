---
name: persistence-transaction-safety
description: Implement ACID transaction guarantees for reliable saves
risk: high
source: workspace
date_added: '2026-03-24'
usage: Save reliability, corruption prevention, crash recovery
avoid: Partial writes on crash, lost updates, inconsistent state after failure
mandates: Implement atomic writes, validate state consistency, handle crash recovery
response: Implement transaction framework, write atomically, add crash recovery, validate consistency
---

# Persistence Transaction Safety

Implement ACID transaction guarantees for reliable saves

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
- Save reliability
- Development workflows

## What NOT to Do
- Partial writes on crash
- Incomplete testing
- Deploy without validation
