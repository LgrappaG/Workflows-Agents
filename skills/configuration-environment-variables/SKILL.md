---
name: configuration-environment-variables
description: Manage environment-specific configuration using environment variables
risk: low
source: workspace
date_added: '2026-03-24'
usage: Environment setup, deployment configuration, externalized settings
avoid: Hardcoded values, unvalidated input, production secrets in code
mandates: Implement safe variable loading, validate types and ranges, handle missing values
response: Define environment variable schema, implement safe loading, add validation, document required variables
---

# Configuration Environment Variables

Manage environment-specific configuration using environment variables

## Risk Level
**LOW**

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
- Environment setup
- Development workflows

## What NOT to Do
- Hardcoded values
- Incomplete testing
- Deploy without validation
