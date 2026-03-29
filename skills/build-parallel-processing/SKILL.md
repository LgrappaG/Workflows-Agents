---
name: build-parallel-processing
description: Parallelize build tasks to reduce total compilation time
risk: high
source: workspace
date_added: '2026-03-24'
usage: Build acceleration, developer iteration speed, CI/CD pipeline optimization
avoid: Task deadlocks, race conditions, improper synchronization, resource exhaustion
mandates: Implement safe task coordination, validate synchronization, use resource limits appropriately
response: Analyze build critical path, identify parallelizable tasks, implement coordination, measure speedup
---

# Build Parallel Processing

Parallelize build tasks to reduce total compilation time

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
- Build acceleration
- Development workflows

## What NOT to Do
- Task deadlocks
- Incomplete testing
- Deploy without validation
