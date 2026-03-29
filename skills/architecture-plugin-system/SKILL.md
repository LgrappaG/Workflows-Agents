---
name: architecture-plugin-system
description: Build extensible plugin system for third-party extensions
risk: high
source: workspace
date_added: '2026-03-24'
usage: Plugin architecture, extensibility, custom extensions
avoid: Plugin conflicts, API versioning issues, security vulnerabilities from plugins
mandates: Implement plugin discovery, validate plugin compatibility, sandbox plugin execution
response: Design plugin interface, implement discovery mechanism, add compatibility validation, sandbox execution
---

# Architecture Plugin System

Build extensible plugin system for third-party extensions

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
- Plugin architecture
- Development workflows

## What NOT to Do
- Plugin conflicts
- Incomplete testing
- Deploy without validation
