---
name: configuration-profile-management
description: Manage multiple configuration profiles for different scenarios
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Development, staging, production configs, profile switching
avoid: Profile conflicts, incomplete overrides, hard-to-debug profile merging
mandates: Support profile inheritance, validate profile completeness, handle profile conflicts
response: Design profile hierarchy, implement merging logic, validate completeness, document profile structure
---

# Configuration Profile Management

Manage multiple configuration profiles for different scenarios

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
- Development
- Development workflows

## What NOT to Do
- Profile conflicts
- Incomplete testing
- Deploy without validation
