---
name: configuration-feature-flags
description: Implement feature flags for gradual feature rollout and A/B testing
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Feature toggling, gradual rollout, A/B testing, kill switches
avoid: Permanent flag clutter, stale flags, no flag cleanup process
mandates: Implement flag evaluation, track flag lifecycle, support flag cleanup
response: Define flag system, implement evaluation engine, add lifecycle tracking, plan flag removal
---

# Configuration Feature Flags

Implement feature flags for gradual feature rollout and A/B testing

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
- Feature toggling
- Development workflows

## What NOT to Do
- Permanent flag clutter
- Incomplete testing
- Deploy without validation
