---
name: metrics-custom-dashboards
description: Create custom dashboards for analytics visualization
risk: low
source: workspace
date_added: '2026-03-24'
usage: Live ops war room displays (DAU, revenue, crash rate, server health), post-match analysis (player scores, ability usage heatmaps), event campaign tracking (offer redemption, A/B lift %), automated KPI scorecards
avoid: Running un-indexed queries on raw events causing 30s+ latency, rendering all 100 widgets immediately causing browser freeze, caching dashboard without TTL causing stale data, storing widget definitions in unversioned schema breaking older dashboards, serving different viewers identical data instead of filtering by permissions
mandates: Query response latency <2s, widget render time <500ms, support >=50 concurrent viewers, cache hit rate >=80%, version-aware schema enforcement
response: 'Design dashboard schema: {dashboard_id, widgets:[{query_id, chart_type, refresh_interval_sec}]}; store widget queries in parameterized, g, , @region, @date_range) supporting 20+ common metrics, Execute queries against pre-aggregated fact tables (not raw events); apply query cache'
---

# Metrics Custom Dashboards

Create custom dashboards for analytics visualization

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
- Data visualization
- Development workflows

## What NOT to Do
- Cluttered dashboards
- Incomplete testing
- Deploy without validation
