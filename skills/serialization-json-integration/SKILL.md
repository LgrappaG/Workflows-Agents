---
name: serialization-json-integration
description: Support JSON serialization for human-readable saves
risk: low
source: workspace
date_added: '2026-03-24'
usage: Development debugging, human-readable saves, configuration export
avoid: JSON explosion, performance degradation on large saves, missing type info
mandates: Minimize JSON size, validate schema compliance, support type reconstruction
response: Configure JSON mappings, implement type hints, add minification, document schema
---

# Serialization Json Integration

Support JSON serialization for human-readable saves

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
- Development debugging
- Development workflows

## What NOT to Do
- JSON explosion
- Incomplete testing
- Deploy without validation
