---
name: quality-metrics-collection
description: Collect and aggregate quality metrics from test runs
risk: low
source: workspace
date_added: '2026-03-24'
usage: Live service monitoring, player health assessment, version stability tracking, crash analysis causation, content performance A/B testing, server load forecasting, hardware device capability profiling
avoid: Collecting metrics too frequently (network/battery drain), unbounded storage (disk bloat), ignoring platform differences (iOS vs Android variance >30%), transmitting PII accidentally, not timestamping metrics in UTC
mandates: Capture 40+ metrics automatically. Data retention 90 days. Correlation analysis on 10+ metric pairs. Latency <100ms per metric push. Anomaly detection >95% precision.
response: Design metrics schema covering gameplay (completion rate, death frequency, session duration), performance, Implement client-side telemetry collector using ring buffer (5MB max per session) with, Build correlation engine that discovers relationships between metric pairs (e, g
---

# Quality Metrics Collection

Collect and aggregate quality metrics from test runs

## Risk Level
**LOW**

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
- Metrics collection
- Development workflows

## What NOT to Do
- Incomplete metric collection
- Incomplete testing
- Deploy without validation
