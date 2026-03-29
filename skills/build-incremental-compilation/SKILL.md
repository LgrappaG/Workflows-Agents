---
name: build-incremental-compilation
description: Speed up iteration through delta compilation, rebuilding only changed dependencies
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Quick iteration loops, hot-reload during development, rapid test cycles, minimize developer wait between builds
avoid: Full rebuilds on minor edits, ignoring dependency graphs, skipping modification timestamp tracking, rebuilding unchanged dependencies
mandates: Track file modification times per asset, build dependency graph, calculate delta compile set, reduce rebuild overhead to <100ms
response: Profile baseline rebuild time, implement incremental tracking with modification cache, validate delta-only compilation, measure rebuild speedup
---

# Build Incremental Compilation

Implement incremental compilation to speed up iteration cycles

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
- Build optimization
- Development workflows

## What NOT to Do
- Full rebuilds on minor changes
- Incomplete testing
- Deploy without validation
