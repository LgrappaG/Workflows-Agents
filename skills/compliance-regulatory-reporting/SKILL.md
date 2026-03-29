---
name: compliance-regulatory-reporting
description: Generate reports for regulatory compliance
risk: high
source: workspace
date_added: '2026-03-24'
usage: Game server breach disclosure protocol, payment card data breach notification (PCI-DSS), player account credential compromise response, regulatory fine appeal with documentation
avoid: Delaying breach detection or notification beyond 72-hour window, incomplete individual notification (missing mitigation steps), disclosing breach details on public channels before regulatory notification, undocumented breaches, no remediation audit trail
mandates: Report data breaches to regulators within 72 hours (GDPR Article 33); notify affected individuals within 30 days; maintain 100% accurate breach registry; document remediation for each incident
response: 'Upon breach detection, initiate incident response workflow: assign unique incident_id; categorize by, Generate regulator notification within 72-hour window: include breach scope, likely consequences, emergency, Send individual notification within 30-day SLA if breach poses high risk (unencrypted, Document remediation in immutable registry: record detection method, root cause, systems patched,'
---

# Compliance Regulatory Reporting

Generate reports for regulatory compliance

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
- Regulatory reporting
- Development workflows

## What NOT to Do
- Inaccurate reporting
- Incomplete testing
- Deploy without validation
