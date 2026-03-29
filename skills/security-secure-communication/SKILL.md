---
name: security-secure-communication
description: Implement secure communication channels
risk: high
source: workspace
date_added: '2026-03-24'
usage: Player login data protection, payment processing API encryption, OAuth token transmission security, analytics data collection privacy, cross-region server communication
avoid: Self-signed certificates in production, TLS versions below 1.3, missing certificate pinning for sensitive APIs, expired certificates (>0 days past expiry allowed), certificate validation bypasses (insecure flag true)
mandates: Enforce TLS 1.3+ for all data in transit; certificate pinning for critical APIs; validate 100% of certificates (expiry, issuer, domain); monitor certificate renewal 30 days before expiry
response: 'Establish TLS infrastructure: configure web servers with TLS 1, 3 (minimum); disable TLS 1, 0/1, 1/1'
---

# Security Secure Communication

Implement secure communication channels

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
- Network security
- Development workflows

## What NOT to Do
- Man-in-the-middle attacks
- Incomplete testing
- Deploy without validation
