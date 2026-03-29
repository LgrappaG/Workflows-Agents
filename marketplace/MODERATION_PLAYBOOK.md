# 🛡️ MODERATION PLAYBOOK

**Purpose:** Clear guidelines for reviewers and maintainers handling submissions, violations, and appeals.

---

## REVIEWER ROLES

### Tier 3+ Maintainers

**Responsibilities:**
- Review 5+ Tier 1 submissions per month
- Provide constructive feedback within 5 days
- Document reasoning for all decisions
- Participate in appeal hearings
- Attend monthly governance meetings

**Tools:**
- GitHub review interface
- Slack channel: #moderation-team
- Decision tracker: reviews.agents.dev

**Training:**
- Onboarding: 2-hour review process walkthrough
- Refresher: Monthly (30 min updates)
- Escalation: Clear criteria for hard cases

---

## SUBMISSION REVIEW CHECKLIST

### Pre-Review (Automated)

```
□ OWASP scan passed
□ No hardcoded secrets detected
□ Dependencies scanned (no typos, CVEs)
□ License compatible
□ Malware scan clear
□ File format valid
□ Size within limits (<500MB)
```

### Manual Review (Tier 1 Only, <5 min typical)

```
DOCUMENTATION QUALITY:
  □ README with clear usage examples
  □ Purpose stated in first 1-2 sentences
  □ Installation instructions provided
  □ Troubleshooting section included
  □ API/integration examples shown

RISK ASSESSMENT:
  □ Risk level clearly marked (low/med/high)
  □ Rationale for risk level documented
  □ Security implications addressed
  □ Fallback behavior specified
  □ Performance expectations set

CODE QUALITY:
  □ No obvious bugs
  □ Error handling present
  □ Test coverage evident
  □ Dependencies current
  □ Follows .agents conventions

MANDATES CLARITY:
  □ All mandates can be tested
  □ Measurable success criteria defined
  □ Platform-specific notes included
  □ Data privacy addressed
  □ Compatibility noted

RESPONSE PATTERNS:
  □ Implementation example provided
  □ Expected inputs/outputs shown
  □ Edge cases documented
  □ Best practices included
  □ Common pitfalls warned

DECISION:
  □ Approved (all boxes checked)
  □ Changes Requested (2-3 items need work)
  □ Rejected (5+ items need major revision)
```

---

## VIOLATION RESPONSE PLAYBOOK

### Critical Violations (Malware, Hardcoded Secrets)

**Timeline:** Immediate

1. **Detection (0 minutes)**
   - Automated scan flags: IMMEDIATE QUARANTINE
   - Manual report: Verify within 15 minutes

2. **Removal (15 minutes)**
   - Take skill offline
   - Backup evidence
   - Notify contributor

3. **Investigation (1 hour)**
   - Analyze scope of issue
   - Check for affected dependencies
   - Document findings

4. **Notification (2 hours)**
   ```
   Subject: CRITICAL SECURITY: Skill Removed

   Your skill [name] has been removed immediately due to:
   [Specific violation with evidence]

   Timeline for appeal: 30 days
   Contact: appeals@agents.dev

   Note: Users affected by your skill have been notified.
   ```

5. **Appeal Process** (30 days)
   - Only if contributor disputes finding
   - Goes to arbitration panel (not standard review)
   - Decision: Permanent removal likely

### High Violations (License, Copyright, Exploit Code)

**Timeline:** 24 hours decision, 5 days appeal window

1. **Investigation (2 hours)**
   - Verify violation claim
   - Gather evidence links
   - Document rationale

2. **Decision Notification (4 hours)**
   ```
   Subject: Skill Removed: [violation type]

   Your skill [name] has been removed due to:
   [Clear explanation with evidence]

   Action taken: Removal + 30-day submission ban
   Appeal deadline: 30 days
   Appeal process: appeals@agents.dev
   ```

3. **Appeal Handling** (30 days)
   - Contributor submits evidence
   - Panel reviews (3 members)
   - Decision within 14 days

### Medium Violations (Quality, Community)

**Timeline:** 7 days decision, warning first

1. **Warning Notification**
   ```
   Subject: Community Standards Alert

   Your skill [name] needs improvement:
   [Specific issues]

   Action: Move to "unmaintained" shelf for 30 days
   Update required by: [date + 30 days]
   Appeal: Not applicable (warning stage)
   ```

2. **30-Day Grace Period**
   - Still visible/downloadable
   - Marked as "Needs Maintenance"
   - User count frozen

3. **Compliance Deadline**
   - If fixed: Restored immediately
   - If not fixed: Archived (read-only)
   - Tier downgrade: -1 tier (capped at Tier 1)

---

## APPEAL HEARING GUIDE

### Role: Arbitration Panel Member

**Your job:** Evaluate if original decision was fair

**Time commitment:** ~2 hours per appeal (1 hour per 3 panels)

**Process:**

1. **Read Original Decision** (15 min)
   - ReviewOriginal submission
   - Review reviewer's feedback
   - Check decision reasoning

2. **Read Appeal & Evidence** (15 min)
   - Read contributor's statement
   - Check evidence links
   - Note new information

3. **Deliberation** (30 min)
   - Async discussion in Slack channel
   - 3 panelists (you + 2 others)
   - Vote format: Uphold / Overturn / Conditional

4. **Write Decision** (30 min)
   - Summary of facts
   - Analysis of arguments
   - Clear recommendation
   - Next steps if overturned

5. **Notify Contributor** (auto-sent)
   - Decision with reasoning
   - Next steps
   - Any compensation if overturned

### Vote Thresholds

| Outcome | Vote Needed |
|---------|------------|
| Uphold rejection | 2 out of 3 |
| Overturn rejection | 2 out of 3 |
| Conditional (needs changes) | Any (panelists discuss) |

---

## DECISION TEMPLATES

### Template 1: Approval Email

```
Subject: ✅ Skill Approved: [skill-name]

Hi [Contributor],

Great news! Your skill "[skill-name]" has been approved and published! 🎉

Approved by: @[reviewer]
Review time: [date]
Status: Live at marketplace.agents.dev

What's next:
• Monitor ratings and feedback
• Respond to issues within 7 days
• Maintain quality standards
• Track downloads on analytics dashboard

Revenue share begins: Immediately (Tier 2+ status)
Payment timing: Monthly for Tier 3+, quarterly for Tier 2

Questions? support@agents.dev

Happy shipping!
```

### Template 2: Changes Requested

```
Subject: 🔄 Changes Requested: [skill-name]

Hi [Contributor],

Thanks for submitting! We'd like you to address a few items before publication.

Feedback:
1. [Specific item with line references]
   Suggestion: [Concrete improvement]

2. [Specific item]
   Suggestion: [Concrete improvement]

Timeline: Please resubmit by [date + 5 days]

Next: After you update, we'll review again (typically 2-3 days)

Questions during revision? Reach out — we're here to help!
```

### Template 3: Rejection with Appeal

```
Subject: ❌ Skill Not Approved: [skill-name]

Hi [Contributor],

Thanks for your submission. We're not able to publish this skill at this time.

Primary concerns:
1. [Issue 1 with evidence]
2. [Issue 2]
3. [Issue 3]

These require significant revision beyond our 5-day window.

Next steps:
• Address issues and resubmit (new submission, not appeal)
• OR appeal this decision within 30 days (appeals@agents.dev)

Appeal process: We'll have a neutral panel review our decision.
Appeal timeline: 30 days total

Want help? Our #community-support channel has tips for improving quality.
```

---

## METRICS TO TRACK

**Reviews Team Dashboard:**

```
Weekly:
  ├─ # submissions reviewed
  ├─ Avg review time
  ├─ Approval rate
  ├─ Appeals rate
  └─ Reviewer satisfaction (self-report)

Monthly:
  ├─ Total reviews
  ├─ Decision breakdown (Approved/Changes/Rejected)
  ├─ Appeal outcomes (Upheld/Overturned)
  ├─ Content violations found
  └─ Reviewer performance outliers

Quarterly:
  ├─ Reviewer accuracy (appeals reversal rate)
  ├─ Training needs identified
  ├─ Process improvements
  └─ Community feedback on reviews
```

---

## CONFLICT OF INTEREST POLICY

Reviewers must **ABSTAIN** if:
- ✋ They authored the skill being reviewed
- ✋ They have financial interest in outcome
- ✋ They're in active dispute with contributor
- ✋ They mentor the contributor

If unsure: Ask moderator team, they'll advise.

---

## ESCALATION CRITERIA

### Auto-escalate to Panel

- Reviewer consensus unclear (split decision)
- Appeal filed on reviewer's decision
- Contributor disputes facts
- Potential conflict of interest detected
- Decision affects multiple skills

### Emergency Escalation

- Security vulnerability discovered
- Legal/IP concerns
- Contributor harassment detected
- Reviewer behavior questioned

---

## Resources for Reviewers

- **Review Template:** Copy from #review-templates channel
- **Code Patterns:** See examples in /skills directory
- **Best Practices:** Wiki at reviewers.agents.dev
- **Training:** Monthly 30-min Zoom refreshers
- **Support:** @review-moderator Slack (questions welcome)
