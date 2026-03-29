---
name: configuration-platform-override
description: Override configuration based on platform or build target
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Platform-specific configs, conditional settings, build customization
avoid: Conflicting overrides, platform incompatibility, missed edge cases
mandates: Support platform detection, implement override logic, validate platform compatibility
response: Detect target platform, implement override hierarchy, apply platform configs, validate results
---

# Configuration Platform Override

Override configuration based on platform or build target

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
- Platform-specific configs
- Development workflows

## What NOT to Do
- Conflicting overrides
- Incomplete testing
- Deploy without validation
