---
name: persistence-async-loading
description: Load save files asynchronously to prevent frame hitches
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Smooth gameplay, non-blocking I/O, responsive UI
avoid: Race conditions during async load, frame stalls, memory spikes
mandates: Implement async pattern, synchronize state properly, monitor memory usage
response: Implement async loader, add progress callbacks, synchronize updates, monitor heap
---

# Persistence Async Loading

Load save files asynchronously to prevent frame hitches

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
- Smooth gameplay
- Development workflows

## What NOT to Do
- Race conditions during async load
- Incomplete testing
- Deploy without validation
