---
name: quality-performance-regression
description: Detect and report performance regressions in metrics
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Pre-release build certification, hotfix impact assessment, optimization validation, platform downgrade detection, third-party asset performance audit, GPU driver regression tracking
avoid: Measuring only peak performance (misses sustained load), ignoring GC pause spikes, comparing against wrong baseline (stale build), insufficient sample size (<100 frames), not accounting for platform thermal throttling
mandates: Detect 2%+ FPS regression automatically. Track frame time, memory growth, GC pauses. Baseline snapshot every release. Historical tracking 8+ builds. Fail on >5% CPU degradation.
response: 'Instrument playable sections (first 5min gameplay) with performance telemetry: capture 60fps histogram,, Establish rolling baseline using 5-build moving average; compare current frame time distribution, 01 (statistical significance), Decompose regression attribution by profiling subsystem: render time, script time, physics time,'
---

# Quality Performance Regression

Detect and report performance regressions in metrics

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
- Performance tracking
- Development workflows

## What NOT to Do
- False positives from environmental variance
- Incomplete testing
- Deploy without validation
