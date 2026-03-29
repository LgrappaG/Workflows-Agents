---
name: metrics-data-aggregation
description: Aggregate metrics into meaningful statistical summaries
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Revenue dashboard (daily gross, per-region breakdown), DAU/MAU trend lines, funnel conversion analysis (tutorial→level 1→purchase), cohort retention tables, A/B test result aggregation
avoid: Aggregating raw events in real-time without batching causing compute spike, storing disaggregated facts indefinitely bloating storage, using floating-point SUM causing precision loss on large revenue amounts, ignoring late-arriving events causing reconciliation failures >1%
mandates: Aggregation window <=5min, data freshness guarantee <=5min lag, compression ratio >=50% vs raw events, deterministic nil-value handling (<1% nulls impact)
response: 'Define fact tables: {timestamp_5min_bucket, dimension_keys (user_id, region, device_os), measures (event_count, revenue_sum, unique_users_hll)};, Stream raw events into windowed aggregator; apply HyperLogLog for cardinality, SUM for, Compress aggregated facts: store as Parquet with Snappy codec; apply delta-encoding on, Validate aggregation: daily reconciliation comparing raw event counts vs aggregated fact counts'
---

# Metrics Data Aggregation

Aggregate metrics into meaningful statistical summaries

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
- Data summarization
- Development workflows

## What NOT to Do
- Information loss
- Incomplete testing
- Deploy without validation
