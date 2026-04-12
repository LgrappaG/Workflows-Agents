# Incident Response Playbook - Phase 1 Security
**For:** .agents Framework Production Deployments  
**Owner:** On-Call Security Engineer  
**Updated:** 2026-04-12

---

## Incident Classification

| Severity | Response Time | Escalation | Example |
|----------|---|---|---|
| **CRITICAL** | <5 min | Page immediately | Project corrupted, circuit breaker cascading |
| **HIGH** | <15 min | Alert team | Shell injection attempt, path escape |
| **MEDIUM** | <1 hour | Create ticket | High block rate, performance degradation |
| **LOW** | <24 hours | Log & monitor | Single operation slow, 1 at-risk pair |

---

## CRITICAL: Project Corruption

### Symptoms
```
Alert: "🚨 CRITICAL: Asset Integrity Check Failed"
OR
Agent abruptly stops with: "Project corrupted - ABORT"
OR
Dashboard shows: ProjectVersion.txt missing
```

### Timeline

**T+0 (Alert Fires)**
```
1. Acknowledge alert in Slack
   ✅ Post: "Incident acknowledged by @{your-name}"

2. Verify the issue (< 30 sec)
   Check 1: Dashboard → Asset Integrity = RED ❌
   Check 2: ls -l ProjectSettings/ProjectVersion.txt
   Check 3: tail logs/agent1.log | grep SECURITY
```

**T+1 min (Stop Damage)**
```
1. Immediately stop Agent1
   pkill -9 -f "Agent1"

2. Brief team
   Slack: "Agent1 STOPPED - ProjectVersion.txt corrupted"
   
3. Do NOT restart or debug yet
   Do NOT attempt to "fix" the file manually
```

**T+5 min (Investigate)**
```
1. Collect evidence
   tail -500 logs/agent1.log > incident_Agent1.log
   tail -500 logs/orchestrator.log > incident_orchestrator.log
   zip incident_$(date +%s).zip incident_*.log

2. Understand the timeline
   grep "ProjectVersion.txt" logs/agent*.log | sort
   What operation touched this file?

3. Check if backup exists
   ls -la .git/  # Version control backup?
   find /backup -name "ProjectVersion.txt" -mtime -1
```

**T+15 min (Recovery Decision)**

**Option A: Use Version Control (Preferred)**
```bash
# If .git exists, recover from last commit
cd ProjectSettings
git checkout ProjectVersion.txt

# Verify
cat ProjectVersion.txt

# Restart Agent1
./Agent1.exe

# Check: Alert should clear
```

**Option B: Use Filesystem Backup (Fallback)**
```bash
# If backup exists
cp /backup/ProjectSettings/ProjectVersion.txt \
   ProjectSettings/ProjectVersion.txt

# Verify integrity
ValidateProjectIntegrity()  # Should return true

# Restart Agent1
```

**Option C: Restore from S3 Snapshot (Ultimate Fallback)**
```bash
# If nothing else works
aws s3 cp s3://gamma4jarvis-backup/ProjectVersion.txt.2026041200 \
         ProjectSettings/ProjectVersion.txt

# Verify and restart
```

**T+30 min (Verification)**
```
1. Start Agent1 with monitoring
   ./Agent1.exe --with-monitoring
   
2. Check logs
   tail -f logs/agent1.log
   Should see: "✅ Security initialization successful"
   
3. Check dashboard
   Asset Integrity = ✅ GREEN
   Agent1 Status = ✅ RUNNING
   
4. If OK, move to post-incident
   If NOT OK, escalate to security architect
```

---

## CRITICAL: Circuit Breaker Cascading

### Symptoms
```
Alert: "🚨 CRITICAL: Multiple Circuit Breaker Trips Detected"
Dashboard shows: 5+ open circuits, 50+ at-risk pairs
```

### Cascade Definition
```
"Cascading" = Multiple agent pairs (>5) entering circuit failure 
             within 5 minutes
```

### Timeline

**T+0 (Detect)**
```
1. Dashboard shows: circuit_breaker_open_circuits = 5+
2. Within Slack: Pin cascade incident
   title: "🚨 CASCADING CIRCUIT FAILURE"
   details: Shows which pairs are failing
```

**T+2 min (Assess)**
```
1. Is it a single bug in one agent?
   Check logs: Which agent appears in MOST failures?
   
   If ONE agent keeps appearing (e.g., Agent12):
   → Likely: Bug in Agent12's code
   → Fix: Update Agent12, restart
   
2. Is it a network/orchestration issue?
   Check net latency, API response times
   
   If network degraded:
   → Fix: Check GitHub API status
   → Fix: Check network connectivity
   → Fix: Increase timeout values

3. Is it data corruption spreading?
   Check: Do error messages suggest data issue?
   
   If corruption suspected:
   → Go to "CRITICAL: Project Corruption" playbook
```

**T+5 min (Action)**

**If Single Agent Issue:**
```bashdraft
1. Identify culprit (e.g., Agent12)
   grep "circuit.*Agent12" logs/*.log | head -20

2. Stop the agent
   pkill -f Agent12

3. Check Agent12.cs for recent changes
   git diff HEAD~1 scripts/Agent12.cs
   
4. Fix the bug (likely: infinite retry loop)

5. Redeploy
   dotnet build
   ./Agent12.exe

6. Verify circuits recover
   wait 60 sec
   Dashboard should show circuit_breaker_open_circuits = 0
```

**If Network Issue:**
```bash
1. Check GitHub API status
   curl https://api.github.com/status

2. Check local network
   ping 8.8.8.8  # Internet connectivity
   ping github.com

3. Increase timeout temporarily
   In SafeProcessExecution, increase DEFAULT_TIMEOUT_MS
   Test, measure, adjust

4. Restart affected agents
```

**If Data Corruption:**
```bash
# Follow "CRITICAL: Project Corruption" playbook
# Likely root cause, not just symptom
```

**T+15 min (Recovery)**
```
1. Manual circuit resets (if all checks passed)
   python3 -c "from mcp_circuit_breaker import get_circuit_breaker
   cb = get_circuit_breaker()
   cb.reset_circuit('Agent12', 'Agent15')  # etc"

2. Monitor recovery
   Expect: circuit_breaker_open_circuits → 0

3. Monitor error rates
   Expect: mcp_errors_recorded → stable drop
```

---

## HIGH: Shell Injection Attempt

### Symptoms
```
Alert: "🚨 HIGH: Shell Injection Attack Blocked"
Log: "[SECURITY] Hard boundary violation: Dangerous character '|' in argument"
```

### Timeline

**T+0 (Detect & Block)**
```
✅ Good news: Attack was BLOCKED by SafeProcessExecution!

1. Check alert
   Which agent attempted the injection?
   What dangerous character was blocked?
   
   Example alert detail:
   Agent: Agent8
   Command: git clone || rm -rf /
   Blocked: || (pipe operator)
```

**T+15 sec (Investigate)**
```
1. Is this a legitimate false positive?
   Cases where legitimate code has shell chars:
   - Complex git commands with pipes for piping outputs
   - Python scripts with multiline commands
   - PowerShell arrays with parentheses
   
   If legitimate: May need to refactor code
   If attack: Bug in Agent8, investigate code

2. Review Agent8.cs
   grep -n "git\|shell\|execute" scripts/Agent8.cs
   Look for: Is agent concatenating user input?

3. Check if repeated
   grep "Shell Injection" logs/*.log | grep Agent8
   Is this a pattern or one-off?
```

**T+5 min (Decision)**

**If False Positive (Legitimate Use Case):**
```
1. Understand the requirement
   Why does Agent8 need shell operators?
   Is there a non-shell way to do this?

2. Refactor to avoid shell
   Instead of: "git clone foo | xargs git clone foo2"
   Do: Two separate calls
   
3. Update agent code
   Test thoroughly
   Re-deploy

4. Update SafeProcessExecution if needed ONLY if:
   - You have strong business justification
   - Security architect approves
   - Updated tests pass
```

**If Attack (Bug in Agent8):**
```
1. Stop Agent8
   pkill -f Agent8

2. Code review
   What part of Agent8 triggers this?
   Is it user input? Config file? API response?
   Is input validation missing?

3. Fix the bug
   Add validation before passing to ExecuteSafely()
   Example: validate_command_args(args)

4. Test fix locally
   python tests/test_phase1_validation.py  # Must: 14/14 PASS

5. Re-deploy Agent8
```

**T+15 min (Follow-up)**
```
1. Monitor for repeats
   grep "Shell Injection" logs/*.log | tail -10
   Should show: Zero more attempts

2. If repeated from other agents
   Escalate to security training
   Likely systemic issue with how agents construct commands

3. Update AGENT_QUICK_START_GUIDE.md
   Add example preventing this mistake
```

---

## HIGH: Path Escape Attempt

### Symptoms
```
Alert: "🚨 HIGH: Path Escape Attempt - Forbidden Access Blocked"
Log: "[SECURITY] Hard boundary violation: Access to ProjectSettings forbidden"
```

### Timeline

**T+0 (Verify Block)**
```
✅ Attack blocked by SafeFileOperations!

Check dashboard:
file_operations_blocked{reason="forbidden_path"} = 1

Verify: Agent did NOT write to ProjectSettings/
Actually check: ls -la ProjectSettings/
```

**T+10 min (Investigate)**
```
1. Which agent? Which path?
   grep "forbidden_path" logs/agent*.log
   
   Example finding:
   [Agent5] Attempted write to: ProjectSettings/ProjectVersion.txt
   [Agent5] BLOCKED: Hard boundary violation

2. Why would Agent5 need ProjectSettings/?
   Legitimate reasons: None (should be read-only)
   Suspicious reasons: Bug in path construction

3. Review Agent5 code
   grep -B2 -A2 "ProjectSettings" scripts/Agent5.cs
   Check: Is path hardcoded or constructed from input?
```

**T+15 min (Action)**

**If Bug (Path Misconstruction):**
```bash
1. Identify root cause
   Why is Agent5 trying to write to ProjectSettings/?
   - Relative path (..) escape?
   - Symbolic link dereference?
   - Config file pointing to wrong location?

2. Fix the bug
   Use SafeFileOperations.SafeWriteFile() with full path
   Do NOT construct paths from user input

3. Test
   Verify agent cannot escape to ProjectSettings/

4. Re-deploy
```

**If Suspicious (Possible Compromise):**
```bash
1. Check git history
   git log --oneline scripts/Agent5.cs | head -5
   Who made recent changes?

2. Code review recent changes
   git show HEAD:scripts/Agent5.cs
   Is there suspicious new code?

3. Consider rolling back to known-good
   git checkout HEAD~1 scripts/Agent5.cs

4. Isolate and debug
   Stop Agent5, run in test environment

5. Escalate if needed
```

---

## MEDIUM: High Block Rate

### Symptoms
```
Alert: "⚠️  MEDIUM: High File Operation Block Rate (>10 blocks/5min)"
Or:    "⚠️  MEDIUM: High Process Execution Failures (>3 failures/5min)"
```

### Timeline

**T+0 to T+30 min (Investigate)**
```
1. Dashboard shows
   Recent 5 minutes:
   file_operations_blocked = 15
   process_execution_blocked = 2
   
2. Is this an attack?
   Look at block reasons:
   - "forbidden_path" = Path escape attempt
   - "dangerous_char" = Shell injection attempt
   - Other = Config/bug issue
   
3. Is this a config issue?
   Check if any agent changed config recently
   grep "config" git log --oneline | head -5

4. Is this a bug?
   All from same agent? → Agent bug
   Across many agents? → Systemic issue
```

**T+30 min (Decision)**

**If Attack Pattern:**
```
1. Identify attack vector
   Examples:
   - Multiple agents all trying forbidden_path → coordinated
   - Single agent trying many times → brute force

2. Block or restrict
   Consider: Disable the agent temporarily
   Or: Rate limit that agent

3. Investigate source
   Where is the attack coming from?
   Is an agent compromised?

4. Escalate if needed
```

**If Bug Pattern:**
```
1. Identify common theme
   Are all blocks for same path?
   Are all failed commands similar?

2. Fix root cause
   Update agent code / config

3. Test thoroughly before re-deploy

4. Monitor for recurrence
```

---

## LOW: At-Risk Pairs

### Symptoms
```
Dashboard shows: circuit_breaker_at_risk_pairs > 20
Alert: "Circuit breaker tracking 25+ at-risk agent pairs"
```

### Action
```
This is normal during heavy agent communication.
At-risk pairs = pairs that had 2/3 errors needed to break circuit

Action:
1. Monitor (no immediate action needed)
2. If not recovering after 5 min: Investigate
3. At-risk pairs should recover as agents succeed
4. If stays high 30+ min: Consider restart
```

---

## Post-Incident (All Severities)

### Immediately After Incident (Within 1 hour)

```
1. Verify system is stable
   □ All agents running
   □ No ongoing alerts
   □ Dashboard green
   
2. Collect logs
   zip incident_logs_$(date +%Y%m%d_%H%M%S).zip logs/
   
3. Notify stakeholders
   Slack: "Incident resolved - [Brief description]"
   Email: Send to security team
   
4. Begin post-mortem scheduling
```

### Post-Mortem (Within 48 hours)

```
Template:

Incident Date/Time: [when]
Detected By: [alert]
Duration: [start] to [end]
Impact: [what happened, 2-3 lines]

Root Cause: [why it happened]

Timeline:
  T+0:   [what happened]
  T+5:   [first action]
  T+15:  [investigation]
  T+30:  [resolution]
  T+45:  [verification]

Prevention:
  [ ] Code change needed
  [ ] Config change needed
  [ ] Monitoring improvement
  [ ] Documentation update
  [ ] Training needed
  [ ] Other

Follow-up Actions:
  - [ ] Action 1 (owner, due date)
  - [ ] Action 2 (owner, due date)
```

### Update Documentation

```
1. If it's a new scenario
   □ Add to this playbook
   
2. If agent had a bug
   □ Update AGENT_QUICK_START_GUIDE.md
   
3. If monitoring could be better
   □ Update MONITORING_ALERTING_SETUP.md
   
4. If process needs improvement
   □ Update PILOT_DEPLOYMENT_RUNBOOK.md
```

---

## Emergency Procedures

### Full System Rollback

**Use ONLY if:**
- Multiple cascading failures
- Cannot identify root cause within 30 min
- Worried about data corruption spreading

**Steps:**
```bash
# 1. Stop all agents
pkill -f "Agent[0-9]"

# 2. Restore from last known good snapshot
aws s3 sync s3://gamma4jarvis-backup/2026-04-12-gold/ .

# 3. Verify integrity
ValidateProjectIntegrity()  # Must return true

# 4. Start Agent 1 only
./Agent1.exe --with-monitoring

# 5. Monitor for 15 minutes
# If stable: Start Agent 2-4
# If problems: Investigate this version

# 6. Full restart only after verifying
```

### Emergency Maintenance Window

**If needed:**
```
1. Announce
   Slack: "MAINTENANCE WINDOW - All agents stopping at 2026-04-12 20:00 UTC"
   
2. Graceful shutdown (5 min)
   Signal all agents to stop
   Wait for graceful termination
   
3. Perform maintenance
   git pull (get latest)
   dotnet build (fresh compile)
   
4. Restart
   Start Agent1, verify
   Expand to others
   
5. Communicate
   Post: "Maintenance complete - System operational"
```

---

## Escalation Phone Tree

```
First Alert:
  → On-Call Security (@security-oncall on Slack)
  
High Priority (5 min):
  → DevOps Lead (page: +1-xxx-xxxx)
  
Critical (Unresponsive):
  → Security Architect (page: +1-yyy-yyyy)
  
Level 1 Escalation Failed (10 min):
  → CTO (page: +1-zzz-zzzz)
```

---

## Incident Log Template

```
Incident Report: [Incident #001]
Date: 2026-04-12
Reporter: [Name]

SEVERITY: [ ] CRITICAL [ ] HIGH [ ] MEDIUM [ ] LOW

Summary:
[1-2 sentence description]

Timeline:
[Complete timeline of events]

Root Cause:
[Why this happened]

Resolution:
[What was done to fix]

Prevention:
[What will prevent this in future]

Follow-up Tasks:
[Checklist of action items]
```

---

**Last Updated:** 2026-04-12  
**Maintained By:** Security Team  
**Review Frequency:** Quarterly or after incident  
**Next Review:** 2026-06-12
