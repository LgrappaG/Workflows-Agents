---
name: persistence-hot-reload-systems
description: Enable rapid iteration with hot-reload of saved game state
risk: high
source: workspace
date_added: '2026-03-24'
usage: Development iteration, testing workflows, rapid prototyping
avoid: Stale references, memory leaks from reloads, state corruption
mandates: Implement safe resource cleanup, validate state after reload, prevent reference issues
response: Design hot-reload system, implement state refresh, add memory cleanup, test state validity
---

# Persistence Hot Reload Systems

Enable rapid iteration with hot-reload of saved game state

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
- Development iteration
- Development workflows

## What NOT to Do
- Stale references
- Incomplete testing
- Deploy without validation
