---
name: serialization-custom-types
description: Enable serialization of custom user-defined types
risk: medium
source: workspace
date_added: '2026-03-24'
usage: User struct serialization, game data persistence, flexibility
avoid: Recursive serialization issues, circular reference handling, type resolution failures
mandates: Support composite types, detect cycles, provide clear type registration
response: Design custom type system, implement cycle detection, add type registry, test composition
---

# Serialization Custom Types

Enable serialization of custom user-defined types

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
- User struct serialization
- Development workflows

## What NOT to Do
- Recursive serialization issues
- Incomplete testing
- Deploy without validation
