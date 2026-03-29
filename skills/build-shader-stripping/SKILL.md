---
name: build-shader-stripping
description: Strip unused shaders and variants from build to reduce size
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Build size reduction, performance optimization, build time acceleration
avoid: Removing used shaders, incorrect variant detection, stripping platform-required shaders
mandates: Analyze shader usage, validate variant selection, test on target platforms
response: Analyze shader dependencies, strip unused variants, measure size reduction, validate platform compatibility
---

# Build Shader Stripping

Strip unused shaders and variants from build to reduce size

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
- Build size reduction
- Development workflows

## What NOT to Do
- Removing used shaders
- Incomplete testing
- Deploy without validation
