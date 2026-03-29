---
name: savedata-compression-strategy
description: Compress save files for reduced storage requirements
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Storage efficiency, save size reduction, cloud save optimization
avoid: Compression overhead on small saves, CPU-intensive compression, format fragility
mandates: Select compression by size, measure overhead, validate compatibility
response: Choose compression algorithm, implement conditional compression, measure efficiency, test recovery
---

# Savedata Compression Strategy

Compress save files for reduced storage requirements

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
- Storage efficiency
- Development workflows

## What NOT to Do
- Compression overhead on small saves
- Incomplete testing
- Deploy without validation
