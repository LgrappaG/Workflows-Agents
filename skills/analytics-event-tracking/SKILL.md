---
name: analytics-event-tracking
description: Track custom game events for player behavior analysis
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Player action tracking (quest complete, item purchased, death), engagement funnels (tutorial-to-first-kill), A/B test event collection, session-based analytics
avoid: Sending raw PII (email, IP address, device ID) in events, omitting timestamps causing retroactive ordering issues, batching indefinitely blocking offline events, ignoring network failures causing silent drops
mandates: Event delivery rate >=99%, latency <100ms per event, batch compression >=40%, zero PII in payloads, idempotency key enforcement
response: 'Configure event schema with strict field validation (event_type, user_id hash, timestamp UTC,, Implement client-side batching queue with 5s flush interval or 100-event threshold, applying, Route events to multi-region ingestion endpoints with automatic failover, logging delivery confirmations, Monitor event pipeline with 1min aggregations: ingested count, delivery rate %, latency'
---

# Analytics Event Tracking

Track custom game events for player behavior analysis

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
- Behavior tracking
- Development workflows

## What NOT to Do
- Missing events
- Incomplete testing
- Deploy without validation
