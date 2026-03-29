---
name: telemetry-crash-reporting
description: Capture and report crash dumps for debugging
risk: high
source: workspace
date_added: '2026-03-24'
usage: Production crash hotfix prioritization (prioritize top 10 crashes causing 90% impact), regression detection (new crash spike post-release), platform-specific crash trends (iOS vs Android malloc failures), performance profiling via hot-path crashes
avoid: Uploading crashes with stripped binaries preventing symbol resolution, omitting register map for native crashes causing incomplete stack traces, deduping only via top frame causing false grouping, queuing crashes indefinitely without disk bounds causing storage bloat
mandates: Stack trace symbol resolution >=95%, crash delivery >=99%, crash dedup ratio >=80%, collection time <30s, offline queuing with disk persistence
response: 'Intercept UncaughtExceptionHandler/Signal handlers; capture full stack trace, register map (if native), app, Upload crash report to backend with version + register map; trigger symbol, Deduplicate crashes via deterministic hash of top 3 stack frames + exception, Validate resolution: log false-positive symbolication (e'
---

# Telemetry Crash Reporting

Capture and report crash dumps for debugging

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
- Crash analysis
- Development workflows

## What NOT to Do
- Privacy violations
- Incomplete testing
- Deploy without validation
