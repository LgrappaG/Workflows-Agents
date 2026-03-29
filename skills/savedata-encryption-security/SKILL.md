---
name: savedata-encryption-security
description: Encrypt save files to protect player data and prevent tampering
risk: high
source: workspace
date_added: '2026-03-24'
usage: Data security, cheat prevention, player privacy
avoid: Weak encryption, hardcoded keys, IV reuse, padding oracle attacks
mandates: Use strong encryption, rotate keys properly, implement secure IVs, add integrity checks
response: Choose encryption algorithm, implement key management, add integrity validation, test security
---

# Savedata Encryption Security

Encrypt save files to protect player data and prevent tampering

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
