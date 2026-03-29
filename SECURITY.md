# Security Policy

## Supported Versions

| Version | Supported          |
|---------|-------------------|
| 9.0.x   | ✅ Yes            |
| 8.2.x   | ✅ Security fixes  |
| 8.1.x   | ❌ No             |
| < 8.0   | ❌ No             |

## Reporting a Vulnerability

**Please do NOT open public GitHub issues for security vulnerabilities.**

Instead, use GitHub's private vulnerability reporting:

### Option 1: GitHub Security Advisory (Recommended)

1. Go to the repository's Security tab
2. Click "Report a vulnerability"
3. Fill out the form with details
4. Submit privately

**Link**: https://github.com/LgrappaG/Workflows-Agents/security/advisories

### Option 2: Email

Email security concerns to: `[security@example.com]`

**Include:**
- Description of the vulnerability
- Steps to reproduce (specific commands or scenarios)
- Potential impact (what could an attacker do?)
- Suggested fix (if available)
- Your contact information

### What Constitutes a Vulnerability?

We care about reports involving:

- **Code Injection**: Unsanitized inputs in skill definitions or workflows
- **XSS/Script Injection**: Malicious code execution in documentation
- **Dependency Vulnerabilities**: Compromised or outdated packages
- **Information Disclosure**: Accidental exposure of sensitive data
- **Authentication/Authorization flaws**: Improper access controls
- **Validation Bypass**: Circumventing safety checks

We do NOT classify these as vulnerabilities:

- ⚠️ Social engineering or phishing attempts
- ⚠️ Physical security issues
- ⚠️ Feature requests disguised as bugs
- ⚠️ Third-party service issues (e.g., GitHub, npm)

## Vulnerability Response Timeline

| Stage | Timeline |
|-------|----------|
| **Initial Response** | Within 24 hours |
| **Investigation** | Within 5 business days |
| **Patch Release** | Within 14 days (critical) or next regular release |
| **Public Disclosure** | After patch is released or 90 days, whichever is sooner |

## Disclosure Policy

1. **Acknowledgment**: We'll confirm receipt of your report
2. **Investigation**: We'll verify and assess the issue
3. **Coordination**: We'll discuss timeline and fix with you
4. **Patch**: We'll develop and test a fix
5. **Release**: We'll release a patch update (or minor version)
6. **Public Notice**: We'll publish a security advisory with credit to the reporter (unless you prefer anonymity)

## Security Best Practices for Contributors

When contributing skills and workflows, please ensure:

### Input Validation

```python
# ❌ Bad - allows arbitrary input
username = user_input

# ✅ Good - validates input
if not isinstance(username, str) or len(username) > 255:
    raise ValueError("Invalid username")
```

### Avoid Hardcoding Secrets

```yaml
# ❌ Bad
api_key: "sk-1234567890abcdef"

# ✅ Good - reference environment variables
api_key: ${OPENAI_API_KEY}
```

### Sanitize External Data

```python
# If processing Unity project files:
import os
if os.path.isabs(path):  # Prevent directory traversal
    raise ValueError("Path must be relative")
```

### OWASP Top 10 Awareness

Review these common vulnerabilities in game dev contexts:

1. **Injection**: SQL, command, template injection
2. **Broken Authentication**: Weak credential handling
3. **Exposed Data**: Unencrypted sensitive information
4. **Broken Access Control**: Bypass authorization checks
5. **Configuration Issues**: Default credentials, verbose errors
6. **Vulnerable Dependencies**: Outdated packages
7. **Authentication Failure**: Poor session management
8. **Data Integrity Issues**: Malicious file uploads
9. **Insufficient Logging**: No audit trails
10. **SSRF**: Server-side request forgery

## Security Audit Schedule

- **Monthly**: Dependency scanning with `npm audit` and `pip audit`
- **Quarterly**: Manual code review by security-focused contributors
- **Yearly**: Third-party security assessment (if resources allow)

## Dependencies

We keep dependencies minimal and regularly updated:

```bash
# Check for vulnerabilities
npm audit
pip audit

# Update safely
npm update
pip install --upgrade -r requirements.txt
```

## Compliance

.agents respects:
- **GDPR**: No personal data collection
- **OWASP Top 10**: Security best practices
- **CWE**: Common Weakness Enumeration standards
- **CVE**: Tracking known vulnerabilities

## Questions?

For security questions (non-vulnerability):
- Open a GitHub Discussion in the Security category
- Email: `security@example.com`

---

**Thank you for helping keep .agents secure! 🔒**