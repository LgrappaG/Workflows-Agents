---
name: community-marketplace-governance
description: "Define trust, moderation, and lifecycle governance for community skill marketplace"
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

# community-marketplace-governance

## Overview

Define and implement governance frameworks for community-driven skill marketplace—including contributor trust levels, content moderation, lifecycle management, and revenue sharing. This skill ensures sustainable and safe community skill sharing at scale.

## Key Capabilities

### 1. Trust & Contributor Tiers
- **Tier System**: Anonymous → Verified → Trusted → Maintainer levels
- **Verification Process**: Email, portfolio, code review baseline for tier progression
- **Reputation Scoring**: Star ratings, download counts, maintenance history
- **Revocation Policies**: Automatic downgrade for 90+ days inactivity or policy violations
- **Community Badges**: Verified, Maintained, Endorsed, Revenue-Sharing tiers

### 2. Content Moderation
- **Automated Screening**: OWASP checks, malware scanning, dependency validation
- **Manual Review Queue**: Prioritized review for tier progression and high-impact skills
- **Appeal Process**: Transparent dispute resolution with community voting
- **Flagging System**: User-reported issues with automatic escalation rules
- **Takedown Procedures**: DMCA/legal compliance workflow with legal team integration

### 3. Lifecycle Management
- **Version Tracking**: Semantic versioning with compatibility maturity matrix
- **Deprecation Process**: 12-month notice period with migration guides
- **Archive Policy**: Skills move to read-only after 24 months inactivity
- **Reactivation**: Path for maintainers to resurrect archived skills
- **Dependency Resolution**: Transitive dependency compatibility checks

### 4. Economics & Revenue Sharing
- **Revenue Model**: Micropayment, subscription, or sponsorship tiers
- **Payout Structures**: Monthly/quarterly/yearly with programmable splits
- **Tax Compliance**: 1099/W9 forms, country-specific handling
- **Fraud Detection**: Unusual download patterns, bot prevention
- **Transparency**: Public dashboard of payouts and top contributors

## Governance Model

```
Contributor → Submission → Automated Review → Manual Review → Published
                             ↓                    ↓
                        Pass/Fail        Approved/Changes/Reject

Maintenance:
Published → Monthly Check-in → Activity Score → Tier Adjustment
                                     ↓
                        Active (Tier+1) or Deprecated (Tier-1)

Disputes:
Report → Triage → Investigation → Resolution (Appeal or Uphold)
          ↓
    Emergency: Immediate Removal
```

## Mandates

- **Transparency First**: All moderation decisions logged publicly (appeals visible)
- **Due Process**: 30-day appeal window with clear reasoning documentation
- **Security Baseline**: All published skills pass automated security gates
- **OWASP Compliance**: No SQL injection, XSS, or hardcoded credentials allowed
- **Privacy Protection**: Contributor data anonymized except for payouts
- **Accessibility**: All skills include README and basic documentation

## Best Practices

1. **Minimize False Positives**: Automated screening should allow 99% of legitimate submissions
2. **Invest in Prevention**: Community guidelines > reactive moderation
3. **Reward Maintenance**: Higher payouts for actively maintained skills
4. **Encourage Mentorship**: Pair new contributors with trusted maintainers
5. **Regular Audits**: Quarterly security and compliance reviews

## Trust Tier Progression

| Tier | Requirements | Privileges | Removal |
|------|--------------|-----------|---------|
| Anonymous | Email verified | Submit skills (limited) | Spam report |
| Verified | Portfolio + 1 published skill | Full submission | 30-day notice |
| Trusted | 3+ published, >100 downloads, 4+ rating | Revenue sharing | Appeals period |
| Maintainer | 1+ actively maintained, <30d activity | Moderation rights | Community vote |

## Resources

- [Community Guidelines](docs/community-guidelines.md)
- [Moderation Playbook](docs/moderation-playbook.md)
- [Revenue Sharing Terms](docs/revenue-terms.md)
- [Security Baseline Checklist](docs/security-checklist.csv)
