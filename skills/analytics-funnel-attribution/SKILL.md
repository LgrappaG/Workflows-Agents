---
name: analytics-funnel-attribution
description: "Track acquisition and retention funnels for skill usage and workflow completion"
risk: medium
source: .agents-phase6
date_added: 2026-03-29
usage: "Use when implementing Phase 6 scale, interoperability, and analytics initiatives"
avoid: "Do not deploy without compatibility checks, rollback strategy, and measurable SLOs"
mandates:
  - define measurable success criteria and failure budgets
  - include platform-specific acceptance gates
  - include data privacy and governance checks
response: assess baseline, design minimal implementation, validate measurable targets, document rollback plan
---

# analytics-funnel-attribution

## Overview

Track user acquisition, engagement, and retention funnels for game features—measuring skill adoption, workflow completion, and feature impact on business metrics. This skill enables data-driven iteration on framework quality and community engagement.

## Key Capabilities

### 1. Funnel Tracking
- **Event Stream**: Track skill usage, workflow starts/completions, feature interactions
- **Session Management**: Identify user cohorts and session lifecycles
- **Retention Curves**: Measure D1, D7, D30 retention for features
- **Convertion Tracking**: Skill discovery → adoption → maintenance pipeline
- **Churn Analysis**: Identify users at risk and feature abandonment patterns

### 2. Attribution Modeling
- **Multi-Touch Attribution**: Credit skill exposure across multiple touchpoints
- **First/Last-Click Models**: Simple and complex attribution for causal inference
- **Cohort Analysis**: Compare feature adoption across user segments
- **A/B Testing Framework**: Controlled experiments on skill variants
- **Incrementality Testing**: Measure true impact vs. correlation

### 3. Analytics Infrastructure
- **Event Validation**: Schema validation, deduplication, late arrival handling
- **Real-time Dashboards**: Live funnel metrics with <5min latency
- **Batch Processing**: Daily/weekly cohort analysis and retention calculations
- **Data Privacy**: GDPR compliance with anonymization and consent tracking
- **Sampling**: Efficient large-scale processing via intelligent sampling

### 4. Insights & Reporting
- **Automated Alerts**: Anomaly detection on key metrics (drop >20%)
- **Cohort Insights**: Generation of insights via statistical testing
- **Custom Reports**: Self-service dashboards for different stakeholder needs
- **Export APIs**: CSV/JSON export for external analysis
- **Predictive Models**: Churn prediction, lifetime value estimation

## Implementation Pattern

```csharp
// Pseudo-code: Event tracking and funnel analysis
namespace SkillAnalytics {
    public class SkillEventTracker {
        public void TrackSkillDiscovery(string skillId, string userId, string source) {
            var evt = new Event {
                EventType = "skill_discovered",
                SkillId = skillId,
                UserId = userId,
                Source = source,
                Timestamp = DateTime.UtcNow
            };
            EventStore.Log(evt);
        }

        public void TrackSkillAdoption(string skillId, string userId, string workflowId) {
            EventStore.Log(new Event {
                EventType = "skill_adopted",
                SkillId = skillId,
                UserId = userId,
                WorkflowId = workflowId,
                Timestamp = DateTime.UtcNow
            });
        }

        public async Task<FunnelMetrics> ComputeFunnel(
            string skillId,
            TimeSpan period,
            CancellationToken ct = default)
        {
            var discovered = await EventStore.Count(
                eventType: "skill_discovered",
                skillId: skillId,
                period: period
            );

            var adopted = await EventStore.Count(
                eventType: "skill_adopted",
                skillId: skillId,
                period: period
            );

            var completed = await EventStore.Count(
                eventType: "workflow_completed",
                skillId: skillId,
                period: period
            );

            return new FunnelMetrics {
                Discovered = discovered,
                Adopted = adopted,
                AdoptionRate = (double)adopted / discovered,
                Completed = completed,
                CompletionRate = (double)completed / adopted
            };
        }
    }
}
```

## Mandates

- **Consent-First**: Track only GDPR-compliant events with explicit user consent
- **Privacy by Design**: No PII in event stream, anonymized user IDs
- **Accuracy Thresholds**: Metrics must be 99%+ accurate for decision-making
- **Latency Targets**: Real-time dashboards update within 5 minutes
- **Retention Policy**: Raw events deleted after 90 days, aggregates kept for 2 years

## Best Practices

1. **Event Schema First**: Design events before implementation, validate strictly
2. **Track Behaviors, Not Identities**: Focus on what users do, not who they are
3. **Correlation ≠ Causation**: Use proper statistical testing for causal claims
4. **Sample Judiciously**: Balance accuracy with cost through intelligent sampling
5. **Iterate on Metrics**: Review and refine KPIs quarterly based on learnings

## Key Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Skill Discovery → Adoption | >30% | <20% |
| Workflow Completion Rate | >80% | <60% |
| Feature Retention (D7) | >50% | <30% |
| Event Processing Latency | <1min | >5min |
| Data Freshness | <5min | >15min |

## Resources

- [Event Schema Design Guide](docs/event-schema.md)
- [Attribution Model Comparison](docs/attribution-models.md)
- [GDPR Compliance Checklist](docs/gdpr-checklist.md)
- Example: `examples/funnel-dashboard-config.json`
