---
name: compliance-gdpr-requirements
description: Ensure GDPR compliance in data handling
risk: high
source: workspace
date_added: '2026-03-24'
usage: EU game launch compliance checklist, migrating legacy games to GDPR, responding to privacy auditor findings, establishing legal basis documentation for data transfers
avoid: Processing data without documented legal basis, collecting data beyond stated purpose (scope creep), retaining PII longer than necessary, omitting Article 17 implementation, unsigned or outdated DPAs with vendors
mandates: 'Implement Article 5 (lawfulness + transparency + minimization), Article 6 (legal basis verification: 0=rejected, 1+ basis required), Article 17 (right to erasure); achieve 100% compliance within 90 days'
response: 'Map all data processing operations to GDPR Article 6 legal bases (consent,, Enforce data minimization at collection point: whitelist only necessary fields per purpose;, Implement Article 17 deletion handler: process erasure requests within 30-day SLA; query, Prepare Data Processing Agreement (DPA) with all third-party vendors; add contractual clause'
---

# Compliance Gdpr Requirements

Ensure GDPR compliance in data handling

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
- Legal compliance
- Development workflows

## What NOT to Do
- Compliance violations
- Incomplete testing
- Deploy without validation
