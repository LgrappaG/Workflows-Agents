---
name: analytics-privacy-anonymization
description: Anonymize analytics data to protect player privacy
risk: high
source: workspace
date_added: '2026-03-24'
usage: GDPR compliance automation (automatically redact PII on event entry), consent-driven analytics (block metrics from EU users without marketing consent), right-to-be-forgotten fulfillment (revoke user's hashed ID from all fact tables), cross-border data transfer compliance (anonymize before regional transmission)
avoid: Hashing PII without salt enabling rainbow-table lookup, storing consent as blob without granularity (can't revoke 1 category), logging raw PII in audit trails (defeats anonymization), shipping raw email/IP in events, deleting consent records at GDPR request without keeping revocation proof, assuming hashing alone prevents re-identification via statistical methods
mandates: PII detection accuracy >=99%, GDPR compliance audit trail, consent tracking per user per data category, re-identification resistance >=99% via hashing + salting
response: 'Deploy PII detection: regex scan (email, phone, SSN, credit card patterns) +, Maintain consent registry: {user_id, categories: [analytics, marketing, crash_reports], granted_timestamp, revoke_timestamp}; apply consent, Hash personally identifiable fields (user_id→sha256(user_id+salt)) downstream in aggregation; salt rotates annually; log, Validate anonymization: weekly re-identification attack simulation (reverse hash lookups, statistical linkage to'
---

# Analytics Privacy Anonymization

Anonymize analytics data to protect player privacy

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
- Privacy protection
- Development workflows

## What NOT to Do
- Incomplete anonymization
- Incomplete testing
- Deploy without validation
