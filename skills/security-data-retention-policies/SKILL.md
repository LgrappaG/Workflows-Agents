---
name: security-data-retention-policies
description: Implement data retention policies
risk: high
source: workspace
date_added: '2026-03-24'
usage: Analytics data retention after GDPR requirement expiry, payment transaction archive for tax compliance, player support tickets deletion after 2-year hold, backup dataset rotation, compliance audit data cleanup
avoid: Indefinite data retention without business justification, manual deletion processes (missing records), retention policy without enforcement mechanism, orphaned data after main record deletion, policy updates without version tracking
mandates: Define retention schedule for each data class (analytics=90d, transactions=7yr, support=2yr); auto-delete expired data monthly; verify 100% compliance via audit; achieve zero data older than policy
response: 'Classify all data types by retention requirement: map to regulatory requirements (GDPR, Implement auto-deletion pipeline: create scheduled job (monthly, UTC 02:00) that queries for, Verify retention compliance: query all tables for records older than policy maximum;, Audit retention policy enforcement: track deletion job success rate (target >99'
---

# Security Data Retention Policies

Implement data retention policies

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
- Data minimization
- Development workflows

## What NOT to Do
- Retaining data too long
- Incomplete testing
- Deploy without validation
