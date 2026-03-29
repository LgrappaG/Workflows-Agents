---
name: security-data-encryption-at-rest
description: Encrypt data at rest for protection
risk: high
source: workspace
date_added: '2026-03-24'
usage: Player PII protection in production database, payment processor integration data storage, user analytics dataset anonymization, backup data protection at rest, GDPR compliance data minimization
avoid: Encryption without key rotation plan, storing encryption keys alongside encrypted data, weak ciphers (AES-128, outdated algorithms), 100% decryption in memory (stream decrypt instead), encryption with single key (no HSM)
mandates: Encrypt all PII using AES-256-GCM; rotate encryption keys annually; verify decryption success rate >99.99%; audit key access monthly; achieve zero unencrypted PII in databases
response: 'Design encryption schema: identify PII fields (name, email, IP, player_id for analytics);, Implement key management system: generate primary + backup keys; store keys in, Execute annual key rotation: generate new key; re-encrypt all data with new, 1% minimum); delete old key after 30-day rollback window; document rotation in'
---

# Security Data Encryption At Rest

Encrypt data at rest for protection

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
- Data security
- Development workflows

## What NOT to Do
- Weak encryption
- Incomplete testing
- Deploy without validation
