---
name: telemetry-performance-monitoring
description: Monitor real-time performance metrics from running games
risk: medium
source: workspace
date_added: '2026-03-24'
usage: FPS regression detection during releases, device-specific performance baselines (low-end Android vs PS5), memory leak detection (memory climbing over session), frame-rate consistency monitoring for competitive games
avoid: Sampling every frame causing 10x metric volume, including high-variance metrics (raw frame times) without smoothing, ignoring GC pauses in frame budget, comparing cross-device metrics without device class normalization, shipping metrics without base-year calibration
mandates: Metric ingestion latency <50ms, sampling accuracy >=98% at 10% rate, frame time variance <10% drift, GC pause impact <2% of frame budget
response: Capture frame metrics (fps, frame_time_ms, gpu_ms, cpu_ms, memory_mb, gc_count) at 10% deterministic, Apply Exponential Moving Average (alpha=0, 2) to smooth outliers; compute p50, p95, p99 every 100ms window; flag, Stream sampled metrics via lightweight UDP with backup TCP fallback, compressing batch
---

# Telemetry Performance Monitoring

Monitor real-time performance metrics from running games

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
- Telemetry overhead
- Incomplete testing
- Deploy without validation
