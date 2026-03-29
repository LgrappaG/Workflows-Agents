---
name: testing-stress-load-testing
description: Stress test systems under high load to identify bottlenecks
risk: high
source: workspace
date_added: '2026-03-24'
usage: Battle royale player count scaling, open-world NPC density limits, asset streaming performance, physics destruction cascades, networked server capacity planning, VR frame budget validation
avoid: Using synthetic data that doesn't match real gameplay (irrelevant results), missing network latency simulation, single-scenario testing (hides interaction bugs), insufficient sampling duration (<5min per stage), not profiling memory fragmentation separately
mandates: Sustain 60FPS at 100K+ physics objects or 2000+ networked entities. Memory <8GB headroom. Identify bottleneck within 2% accuracy. Run 4+ scenarios. Failure below 80% target = blocker.
response: 'Build scalable test scenarios using exponential load ramps: start 1K entities/frame, increment, Profile memory allocation hotspots using native profiler integration; capture heap snapshots at, Execute multi-scenario matrix combining load types (physics complexity, network tick rate, visual, Generate stress test report with regression trend (compare current vs baseline build);'
---

# Testing Stress Load Testing

Stress test systems under high load to identify bottlenecks

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
- Performance validation
- Development workflows

## What NOT to Do
- Uncontrolled resource usage
- Incomplete testing
- Deploy without validation
