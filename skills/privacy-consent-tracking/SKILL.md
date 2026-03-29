---
name: privacy-consent-tracking
description: Track and manage player consent for data usage
risk: high
source: workspace
date_added: '2026-03-24'
usage: GDPR consent management for EU players, CCPA opt-in for CA users, consent form versioning after privacy policy updates, user consent audit during regulatory inspections
avoid: Pre-ticked consent boxes, implied consent without explicit action, consent versioning without tracking, bulk consent revocation without individual audit, consent records deletion during retention period
mandates: Capture explicit consent (checkbox + timestamp) for each data processing purpose; version consent forms (v1.2.3); enable revocation within 48 hours; maintain consent audit for 7 years minimum
response: "Store consent records with: user_id, purpose_code (e.g., 'analytics', 'marketing', 'profiling'), consent_version, timestamp_utc, ip_address, user_agent; implement database constraints requiring consent audit trail. Implement dual-submission pattern: frontend captures explicit opt-in with unique nonce; backend validates"
---

# Privacy Consent Tracking

Track and manage player consent for data usage

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
- Consent management
- Development workflows

## What NOT to Do
- Invalid consent records
- Incomplete testing
- Deploy without validation
