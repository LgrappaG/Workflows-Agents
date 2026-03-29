---
name: telemetry-real-time-alerts
description: Generate real-time alerts for critical metrics
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Live ops crisis response (CMS went down, users stuck in tutorial), revenue drop alerts (monetization >=20% below forecast), deployment rollback triggers (crash rate spike post-release), resource exhaustion (server CPU>95% for >5min)
avoid: Alerting on every single metric fluctuation without thresholds causing alert fatigue, ignoring baseline drift causing alerts to trigger forever on new normal, missing cooldown causing double-alert noise, using real-time data without smoothing amplifying noise-induced false triggers
mandates: Alert latency <10s from anomaly detection to on-call notification, false positive rate <5%, threshold drift detection, cooldown enforcement (min 5min between identical alerts)
response: Ingest metric streams into alerting engine; define threshold rules (e, g, , crash_rate>0, 5%, fps_p95<15, ccu_drop>20% in 5min window) with severity tiers (critical/warning/info)
---

# Telemetry Real Time Alerts

Generate real-time alerts for critical metrics

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
- Incident alerts
- Development workflows

## What NOT to Do
- Alert fatigue
- Incomplete testing
- Deploy without validation
