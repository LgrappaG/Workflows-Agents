---
name: injection-context-isolation
description: Isolate dependency contexts for thread safety and test isolation
risk: high
source: workspace
date_added: '2026-03-24'
usage: Multi-threaded safety, test isolation, context management
avoid: Context pollution across threads, test interference, resource leaks
mandates: Implement thread-local contexts, validate isolation, prevent cross-context leaks
response: Design context isolation, use thread-local storage, validate boundaries, test concurrency
---

# Injection Context Isolation

Isolate dependency contexts for thread safety and test isolation

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
- Multi-threaded safety
- Development workflows

## What NOT to Do
- Context pollution across threads
- Incomplete testing
- Deploy without validation
