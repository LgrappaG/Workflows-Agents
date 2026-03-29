---
name: debug-remote-profiling
description: Profile performance on remote devices
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Performance optimization in deployed mobile builds, multi-device profiling farm for memory leak detection, networked gameplay bottleneck identification (physics/render sync), remote VR device profiling without emulator tethering
avoid: Profiler overhead exceeding game thread time budget causing stuttering, uncompressed metric streaming consuming >5% of network bandwidth, synchronous query blocks during frame rendering, missing frame context headers causing timestamp desynchronization, profiler connection drop losing historical data without persistence
mandates: Maintain profiling overhead <5% of frame budget (e.g., <0.83ms at 60fps), capture remote frame metrics with <50ms transmission latency, achieve >90% CPU/GPU measurement accuracy, support ≥3 concurrent profiler connections.
response: Initialize profiler on target with configurable sampling budget (1%, 5%, 10%), allocating, Stream aggregated metrics (frame time, draw calls, memory delta) through binary protocol, Collect CPU sampler data via frame markers (BeginSample/EndSample), GPU counters via query, On request, trigger garbage collection analysis to measure pause duration, heap fragmentation,
---

# Debug Remote Profiling

Profile performance on remote devices

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
- Remote profiling
- Development workflows

## What NOT to Do
- Profiling overhead
- Incomplete testing
- Deploy without validation
