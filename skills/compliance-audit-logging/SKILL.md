---
name: compliance-audit-logging
description: Maintain comprehensive audit logs for compliance verification
risk: high
source: workspace
date_added: '2026-03-24'
usage: Post-breach forensic investigation, regulatory audit preparation, incident response timeline reconstruction, detecting unauthorized admin access, compliance certification for ISO 27001
avoid: Mutable audit logs (UPDATE/DELETE capability), unencrypted or unsigned audit entries, human-readable timestamps only (UTC epoch required), audit logs deleted during retention period, access to audit system without MFA
mandates: Log all data access events (who, what, when, where, why) in append-only format; retain audit logs 7 years minimum; achieve 99.99% integrity (zero undetected tampering); monthly tamper verification
response: 'Implement immutable audit log system: configure database with WORM (write-once-read-many) storage or, Enforce cryptographic signing: use HMAC-SHA256 or Ed25519 to sign each log entry;, Restrict audit log access: require multi-factor authentication for read access; log all, Generate monthly integrity report: hash all logs from month N; compare against'
---

# Compliance Audit Logging

Maintain comprehensive audit logs for compliance verification

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
- Compliance audits
- Development workflows

## What NOT to Do
- Incomplete logs
- Incomplete testing
- Deploy without validation
