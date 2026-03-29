---
name: configuration-schema-validation
description: Validate configuration against schema to catch errors early
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Config validation, error detection, type safety
avoid: Silent failures, incomplete validation, misleading error messages
mandates: Support schema definition, provide clear error messages, validate required fields
response: Define config schema, implement validator, generate error messages, test edge cases
---

# Configuration Schema Validation

Validate configuration against schema to catch errors early

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
- Config validation
- Development workflows

## What NOT to Do
- Silent failures
- Incomplete testing
- Deploy without validation
