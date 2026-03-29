# .agents Community Marketplace Governance

**Version**: 1.0.0
**Effective Date**: 2026-03-30
**Last Updated**: 2026-03-30

---

## 1. Core Principles

The .agents marketplace operates on **trust, transparency, and quality**.

- **Trust First**: Community members earn reputation through consistent contribution
- **Transparent Moderation**: All enforcement decisions logged and appealable
- **Quality Over Quantity**: Skill quality and maintenance matter more than volume
- **Sustainability**: Revenue sharing ensures long-term contributor engagement
- **Safety by Default**: Security and privacy non-negotiable

---

## 2. Contributor Tiers

### Tier 1: Anonymous (Entry)
**Requirements**: Email verified
**Privileges**:
- Submit up to 3 skills per month
- View published marketplace
- Participate in discussions

**Restrictions**:
- No access to revenue sharing
- Skills require higher scrutiny in review
- Rate-limited to prevent spam

**Path to Tier 2**: Publish 1 skill, >50 downloads, 4+ rating

---

### Tier 2: Verified (Active)
**Requirements**:
- Email verified
- GitHub/portfolio demonstrated
- At least 1 published skill
- Passed baseline security review

**Privileges**:
- Unlimited skill submissions
- Eligible for revenue sharing
- Access to analytics dashboard
- Priority support

**Maintenance**:
- Must publish or update skill every 6 months
- Download count threshold: >100/month average

**Path to Tier 3**: 3+ published skills, >500 aggregate downloads, 4.5+ rating

---

### Tier 3: Trusted (Sustained)
**Requirements**:
- 3+ published, actively maintained skills
- >500 aggregate downloads
- 4.5+ average rating
- 12+ months contributor history
- Passed enhanced security audit

**Privileges**:
- Access to beta features
- Enhanced analytics (real-time)
- Community voting on governance changes
- Priority for marketplace promotion

**Maintenance Requirements**:
- At least 1 skill per 12 months
- Respond to issues within 7 days
- Maintain 4.0+ average rating

**Path to Tier 4**: Lead ecosystem contribution, mentor others, 2+ years history

---

### Tier 3: Maintainer (Leadership)
**Requirements**:
- 18+ months sustained contribution
- Led ecosystem initiatives
- Mentored 3+ contributors to Tier 2+
- Community voting approval (75% threshold)

**Privileges**:
- Moderation rights (review Tier 1 submissions)
- Vote on governance changes
- Featured placement in marketplace
- Enhanced revenue share (120% baseline)

**Responsibilities**:
- Review 5+ submissions per month
- Mentor 2+ junior contributors
- Participate in monthly governance calls
- Enforce community standards

---

## 3. Submission & Review Process

### Step 1: Submission
**Requirements**:
- Skill naming convention: `category-skill-name`
- README with usage examples
- At least 5-line description
- License specified (MIT/Apache/GPL/proprietary)
- No hardcoded secrets or API keys

**Automated Checks**:
- ✅ OWASP Top 10 scanning (XSS, SQL injection, etc.)
- ✅ Dependency vulnerability check
- ✅ License compatibility check
- ✅ Code format validation
- ✅ Malware scanning

**Duration**: <1 hour

---

### Step 2: Manual Review (Tier 1 Only)
**Trigger**: All Tier 1 submissions or high-risk skills
**Reviewer**: Tier 3+ maintainer
**Timeline**: 5 business days

**Checklist**:
- [ ] Documentation quality (clear, actionable)
- [ ] Risk level assessment (low/medium/high)
- [ ] No hostile dependencies (typosquatting, etc.)
- [ ] Mandates are clear and testable
- [ ] Response patterns are complete

**Outcomes**:
- ✅ **Approved**: Publish immediately
- 🟡 **Changes Requested**: 5 days to address, then re-review
- ❌ **Rejected**: Clear reasoning provided, appeals available

---

### Step 3: Publication
**Actions**:
- Add to marketplace index
- Create skill landing page
- Notify relevant communities
- Begin analytics tracking

---

## 4. Content Moderation

### Violation Categories

| Category | Severity | Examples | Action |
|----------|----------|----------|--------|
| **Safety** | Critical | Malware, hardcoded secrets, exploits | Immediate removal + tier downgrade |
| **License** | High | AGPL without disclosure, GPL violations | Removal + 30-day ban |
| **Quality** | Medium | Undocumented, broken, abandoned | Archive + warning |
| **Community** | Medium | Harassment, spam, off-topic | Tier downgrade + training |
| **Copyright** | High | DMCA-eligible content, stolen code | Removal + legal review |

### Appeal Process

1. **Notification**: Clear reasoning within 24 hours
2. **Appeal Window**: 30 days to submit appeal
3. **Triage**: Violation category review
4. **Hearing**: Async discussion with community moderators
5. **Decision**: Binding within 14 days

**Escalation**: Critical rejections get human arbitration (2+ maintainers)

---

## 5. Maintenance & Lifecycle

### Active Maintenance (Required for All Tiers)
**Definition**:
- Respond to issues within 7 days
- Security updates within 5 days
- Minor/major updates at least every 6 months

**Consequences of Inactivity**:
- 30 days: Warning, moved to "unmaintained" shelf
- 90 days: Archived (read-only), tier downgrade
- 180 days: Deprecation notice, path to deletion after 12 months

### Deprecation Timeline
```
Day 1:    Public deprecation notice
Month 1:  Migration guide published
Month 6:  Final version tagged
Month 12: Available for deletion
```

### Reactivation Process
Contributors can reactivate archived skills:
1. Review outstanding issues
2. Update to latest platform version
3. Pass security re-audit
4. Publish migration guide
5. Set maintenance expectations

---

## 6. Revenue Sharing

### Payment Tiers

| Tier | Revenue Share | Frequency | Minimum Payout |
|------|---------------|-----------|---|
| Verified | 50% | Quarterly | $50 |
| Trusted | 65% | Monthly | $25 |
| Maintainer | 85% | Monthly | $25 |

**Revenue Sources**:
- Marketplace fees (Tier 1: 20%, licensing TBD)
- Sponsorships (equal distribution to all tiers)
- Premium support contracts (revenue-sharing pool)

### Tax Compliance
- 1099/W9 for US contributors
- Localized tax forms for international
- Automatic withholding >$600/year (US)
- Payment via Stripe/TransferWise

### Fraud Detection
- Automated flag: >200% normal download spike
- Manual review: Unusual geographic patterns
- Ban: Confirmed bot traffic, click farms

---

## 7. Dispute Resolution

### Fast Track (<$100)
- Community vote (Tier 3+)
- 7-day resolution window
- Binding decision

### Standard ($100-$10K)
- Arbitration panel (1 maintainer, 1 community, 1 neutral)
- 30-day investigation
- Written decision with reasoning

### Escalation (>$10K)
- Legal arbitration (per TOS)
- Independent arbitrator
- 60-day timeline

---

## 8. Community Governance

### Decision Making
- **Routine Decisions**: 1 maintainer approval
- **Policy Changes**: 75% community vote (Tier 3+)
- **Critical Decisions**: Unanimous maintainer council

### Calls & Meetings
- **Monthly Governance**: First Thursday, 5 PM UTC
- **Emergency Meetings**: 48-hour notice
- **Decision Log**: Public GitHub issues

### Council Formation
Maintainer council (3-7 members) elected annually:
- Nominees: Tier 3+ with 18+ month history
- Election: Community vote (Tier 2+)
- Terms: 1 year, max 3 consecutive terms

---

## 9. Special Programs

### Mentorship Program
- **Goal**: Grow Tier 2/3 community
- **Structure**: 6-month pairings
- **Incentive**: Bonus payouts (10%) for active mentors
- **Enrollment**: Open applications, selection by council

### Innovation Bounties
- **Scope**: High-impact skills, cross-engine tools, tooling
- **Budget**: 5% of monthly revenue pool
- **Application**: Quarterly open calls

### Academic Partnerships
- **Scope**: Educational skill variants, tutorials, research
- **Benefits**: Accelerated tier progression, free premium tier
- **Validation**: Partnership agreement required

---

## 10. Enforcement & Compliance

### Monitoring
- Monthly compliance audits
- Quarterly security reviews
- Annual third-party assessment

### Breach Response
1. **Detection**: Automated or reported
2. **Triage**: <24 hours for severity assessment
3. **Notification**: Within 48 hours to affected parties
4. **Remediation**: Timeline based on severity
5. **Review**: Post-incident analysis

### Documentation
- All decisions logged in GitHub issues
- Discord announcements for major changes
- CHANGELOG updates for policy revisions

---

## 11. Future Roadmap

- **Q3 2026**: Sponsorship tier, foundation model governance
- **Q4 2026**: Analytics access for Tier 2+, real-time payouts
- **Q1 2027**: Skill certification program, enterprise licensing
- **Q2 2027**: Multi-currency support, decentralized governance experiments

---

## 12. Appendices

### A. Prohibited Content
- ❌ Malware, exploit code, credential stealers
- ❌ Hardcoded API keys, database credentials
- ❌ NSFW content, harassment, hate speech
- ❌ Unlicensed copyrighted material
- ❌ Abandoned dependencies (0 updates in 2+ years)

### B. Recommended Practices
- ✅ Clear documentation with examples
- ✅ Semantic versioning
- ✅ Automated tests in CI
- ✅ Regular dependency updates
- ✅ CHANGELOG entries for changes

### C. Resources
- [Contributor Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security Checklist](../SECURITY.md)
- [Community Guidelines](./COMMUNITY.md)
- [Appeal Form Template](./APPEAL_TEMPLATE.md)

---

**Questions?** See [FAQ](./FAQ.md) or post in [Discussions](https://github.com/.agents/discussions)