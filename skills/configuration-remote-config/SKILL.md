---
name: configuration-remote-config
description: Fetch configuration from remote servers at runtime
risk: high
source: workspace
date_added: '2026-03-24'
usage: Dynamic configuration, feature flags, A/B testing, server-driven features
avoid: Network failures unhandled, stale config cached, no fallback behavior, security bypass
mandates: Implement retry logic, cache with TTL, provide fallback behavior, validate config schema
response: Set up remote config endpoint, implement caching with TTL, add retry logic, configure fallbacks
---

# Configuration Remote Config

Fetch configuration from remote servers at runtime

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
- Dynamic configuration
- Development workflows

## What NOT to Do
- Network failures unhandled
- Incomplete testing
- Deploy without validation
