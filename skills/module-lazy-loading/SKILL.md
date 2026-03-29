---
name: module-lazy-loading
description: Implement lazy loading of modules to reduce startup time
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Startup optimization, memory efficiency, on-demand loading
avoid: Initialization order issues, circular dependencies, failed lazy loads
mandates: Implement lazy initialization, validate load order, handle load failures
response: Design lazy load mechanism, implement initialization triggers, add error handling, test ordering
---

# Module Lazy Loading

Implement lazy loading of modules to reduce startup time

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
- Startup optimization
- Development workflows

## What NOT to Do
- Initialization order issues
- Incomplete testing
- Deploy without validation
