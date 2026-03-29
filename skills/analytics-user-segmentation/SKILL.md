---
name: analytics-user-segmentation
description: Segment players into cohorts for analysis
risk: low
source: workspace
date_added: '2026-03-24'
usage: Whale vs casual player segmentation, region-based content delivery, retention cohort analysis (churned after day 3), VIP user targeting for offers
avoid: Computing segments on every single event causing cascading latency, using stale event data (>5min old) inflating segment size estimates, ignoring consent flags including non-opted users, hard-coding segment logic without versioning causing AB test data corruption
mandates: Segment accuracy >=95%, cohort refresh latency <5min from event, max 1000 concurrent named segments, consent-verified membership only
response: Define segments with SQL-like conditions (e, g, , revenue>100 AND retention_day_7>=0, 6) stored in Segment Registry, versioning each definition for audit trails
---

# Analytics User Segmentation

Segment players into cohorts for analysis

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
- Cohort analysis
- Development workflows

## What NOT to Do
- Arbitrary segmentation
- Incomplete testing
- Deploy without validation
