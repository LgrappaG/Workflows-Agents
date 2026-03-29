---
name: privacy-data-deletion
description: Implement right-to-be-forgotten data deletion
risk: high
source: workspace
date_added: '2026-03-24'
usage: User exercises GDPR Article 17 right-to-be-forgotten, player account termination with data purge, compliance audit verification, responding to CCPA deletion requests
avoid: Soft-deletes (mark as deleted but retain data), incomplete cascade deletion (orphaned records in linked tables), backup retention beyond deletion date, deletion without immutable audit trail
mandates: Delete all PII within 30 days of user request; verify deletion from production DB, backups (3 copies minimum), and cache layers; confirm zero trace via automated audit report
response: 'Parse deletion request to identify all user identifiers (UUID, email, account_id) across, Execute cascading delete operations: player profiles → achievement records → transaction history, Verify deletion by running SELECT queries across 3+ backup systems; generate cryptographic, Publish deletion confirmation email with manifest hash within 24 hours; alert legal'
---

# Privacy Data Deletion

Implement right-to-be-forgotten data deletion

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
- GDPR compliance
- Development workflows

## What NOT to Do
- Incomplete deletion
- Incomplete testing
- Deploy without validation
