---
name: build-caching-strategy
description: Implement intelligent caching for incremental builds
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Build acceleration, resource efficiency, cache invalidation patterns
avoid: Stale cache corruption, incomplete cache invalidation, cache pollution
mandates: Implement versioning, validate cache coherence, handle cache invalidation
response: Design cache structure, implement versioning strategy, add cache invalidation logic, test coherence
---

# Build Caching Strategy

Implement intelligent caching for incremental builds

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
- Build acceleration
- Development workflows

## What NOT to Do
- Stale cache corruption
- Incomplete testing
- Deploy without validation
