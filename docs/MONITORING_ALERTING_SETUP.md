# Monitoring & Alerting Setup
**For:** .agents Framework Multi-Agent Systems  
**Components:** Security modules + performance monitoring + alerting  
**Metrics:** Real-time dashboards + alerts

---

## Architecture Overview

```
┌─────────────────┐
│  Agent1-48      │
│  (Running)      │
└────────┬────────┘
         │ Emits metrics
         ▼
┌─────────────────────────────────┐
│  Monitoring Collector           │
│ - File operations tracker       │
│ - Process execution tracker     │
│ - Circuit breaker status        │
│ - Integrity check results       │
└────────┬────────────────────────┘
         │ Push metrics every 60s
         ▼
┌─────────────────────────────────┐
│  Metrics Store (Prometheus)     │
│ - Time-series data              │
│ - Retention: 30 days            │
└────────┬────────────────────────┘
         │
     ┌───┴───────────────────┬────────────────┐
     │                       │                │
     ▼                       ▼                ▼
┌─────────────┐    ┌──────────────┐   ┌──────────────┐
│  Dashboard  │    │  Alerting    │   │  Log Stream  │
│ (Grafana)   │    │  (AlertMgr)  │   │  (ELK/JSON)  │
└─────────────┘    └──────────────┘   └──────────────┘
                          │
                          ▼
                   ┌──────────────┐
                   │  Slack/Email │
                   └──────────────┘
```

---

## Metrics Collection Points

### 1. File Operations Metrics

**Source:** SafeFileOperations wrapper  
**Frequency:** Every operation

```python
# In SafeFileOperations.SafeWriteFile():
metrics.file_operations_attempted.inc()
metrics.file_operations_success.inc()
metrics.file_operations_blocked.labels(reason="forbidden_path").inc()
```

**Metrics Exposed:**
```
file_operations_attempted{agent="agent1"}       42
file_operations_success{agent="agent1"}        42
file_operations_blocked{agent="agent1", reason="forbidden_path"}  0
file_operations_blocked{agent="agent1", reason="forbidden_file"}  0
file_operations_errors{agent="agent1"}          0
```

### 2. Process Execution Metrics

**Source:** SafeProcessExecution wrapper  
**Frequency:** Every subprocess call

```python
# In SafeProcessExecution.ExecuteSafely():
metrics.process_execution_attempted.inc(executable="git")
metrics.process_execution_success.inc(executable="git")
metrics.process_execution_blocked.labels(reason="shell_metachar").inc()
metrics.process_execution_timeout.inc()
```

**Metrics Exposed:**
```
process_execution_attempted{executable="git"}         8
process_execution_success{executable="git"}           8
process_execution_blocked{executable="git", reason="dangerous_char"}  0
process_execution_timeout{executable="git"}           0
```

### 3. Circuit Breaker Metrics

**Source:** MCP Router (mcp_circuit_breaker.py)  
**Frequency:** Every message + every 60s status dump

```python
# In route_mcp_message():
metrics.mcp_messages_routed{sender="agent1", receiver="agent2"}.inc()
metrics.mcp_errors_recorded{sender="agent1", receiver="agent2"}.inc()

# In get_circuit_breaker().get_status():
metrics.circuit_breaker_open_circuits.set(count)
metrics.circuit_breaker_at_risk_pairs.set(count)
```

**Metrics Exposed:**
```
mcp_messages_routed{sender="agent1", receiver="agent2"}  1245
mcp_errors_recorded{sender="agent1", receiver="agent2"}  3
circuit_breaker_open_circuits                             0
circuit_breaker_at_risk_pairs                            12
```

### 4. Asset Integrity Metrics

**Source:** SafeAssetOperations.ValidateProjectIntegrity()  
**Frequency:** Every startup + hourly check

```python
# In ValidateProjectIntegrity():
if valid:
    metrics.asset_integrity_check_passed.inc()
else:
    metrics.asset_integrity_check_failed.inc()
    metrics.critical_alert("ProjectVersion.txt corrupted")
```

**Metrics Exposed:**
```
asset_integrity_check_passed   5
asset_integrity_check_failed   0
project_version_txt_exists    true
```

---

## Dashboard Configuration (Grafana)

### Dashboard 1: Security Overview

```
Row 1: Real-Time Status
┌─────────────────────────────────────┐
│ File Operations   │ Process Exec   │
│ 42 success / 0 blocked              │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│ Circuit Breaker   │ Integrity Check │
│ 0 open / 12 at-risk                 │
└─────────────────────────────────────┘

Row 2: Hourly Trends (Last 24 hours)
┌──────────────────────────────────────┐
│ File Operations Success Rate (%)      │ 100.0% ✅
│ Process Execution Success Rate (%)    │ 100.0% ✅
│ Circuit Breaker Trips                 │ 0      ✅
│ Integrity Check Failures              │ 0      ✅
└──────────────────────────────────────┘

Row 3: By Agent (Last 4 hours)
┌─────────────┬──────────┬─────────┬──────────┐
│ Agent       │ File Ops │ Proc Ex │ Circuit  │
├─────────────┼──────────┼─────────┼──────────┤
│ Agent1      │ 42/0     │ 8/0     │ 0 open   │
│ Agent2      │ 38/0     │ 6/0     │ 0 open   │
│ Agent3      │ 35/0     │ 7/0     │ 0 open   │
│ Agent4      │ - (pending) -      │ - (pending) -      │
└─────────────┴──────────┴─────────┴──────────┘
```

### Dashboard 2: Security Threats

```
Row 1: Attempted Attacks
┌──────────────────────────────┐
│ Shell Injection Attempts: 0  │
│ Path Escape Attempts:     0  │
│ Forbidden Access:         0  │
│ Asset Corruption:         0  │
└──────────────────────────────┘

Row 2: Attack Timeline
[Graph showing attack attempts over time]
(Should be flat at zero)

Row 3: Top Alert Causes
┌──────────────────────────────┐
│ 1. (No incidents)             │
│ 2. (No incidents)             │
│ 3. (No incidents)             │
└──────────────────────────────┘
```

### Dashboard 3: Performance Impact

```
Row 1: Resource Usage
┌─────────────────────────────┐
│ Memory (Agent1):   245 MB    │
│ CPU (Agent1):       8.2%     │
│ Disk I/O:           12 MB/s  │
└─────────────────────────────┘

Row 2: Overhead Analysis
┌─────────────────────────────┐
│ File Ops Latency:    2.3 ms  │
│ Process Exec Latency: 1.8 ms │
│ Total Overhead:      1.2%    │
└─────────────────────────────┘

Row 3: Performance Trends
[Graph] Memory usage over 24h
[Graph] CPU usage over 24h
```

---

## Alert Rules (AlertManager)

### CRITICAL Alerts (Immediate Action)

```yaml
alert: IntegrityCheckFailed
  condition: asset_integrity_check_failed > 0
  for: 1m
  action: CRITICAL - PROJECT CORRUPTED
  severity: page (immediate)
  notification: slack #security-alerts, email

alert: CircuitBreakerOpen
  condition: circuit_breaker_open_circuits > 0
  for: 5m
  action: HIGH - AGENT COMMUNICATION LOOP DETECTED
  severity: page
  notification: slack #security-alerts

alert: ShellInjectionAttempt
  condition: process_execution_blocked{reason="dangerous_char"} > 0
  for: 1m
  action: HIGH - SHELL INJECTION BLOCKED
  severity: alert
  notification: slack #security-alerts

alert: PathEscapeAttempt
  condition: file_operations_blocked{reason="forbidden_path"} > 0
  for: 1m
  action: HIGH - PATH ESCAPE ATTEMPT BLOCKED
  severity: alert
  notification: slack #security-alerts
```

### WARNING Alerts (Investigate)

```yaml
alert: HighBlockedOperations
  condition: file_operations_blocked > 10 in 5m
  for: 5m
  action: WARNING - Multiple blocked file operations
  severity: warning
  notification: slack #security-monitoring

alert: ProcessExecutionErrors
  condition: process_execution_errors > 3 in 5m
  for: 5m
  action: WARNING - Process execution errors
  severity: warning
  notification: slack #security-monitoring

alert: CircuitBreakerAtRisk
  condition: circuit_breaker_at_risk_pairs > 20
  for: 10m
  action: WARNING - Many agent pairs at risk
  severity: warning
  notification: slack #security-monitoring
```

### INFO Alerts (Monitor)

```yaml
alert: DailyReport
  condition: day_completed
  for: 0m
  action: INFO - Daily security summary
  severity: info
  notification: slack #security-daily

alert: WeeklyReport
  condition: week_completed
  for: 0m
  action: INFO - Weekly security summary
  severity: info
  notification: email security@example.com
```

---

## Alert Response Procedures

### When Alert Fires: CRITICAL - PROJECT CORRUPTED

```
1. IMMEDIATE (< 1 min)
   □ Check Dashboard: Asset Integrity Check status
   □ Verify: Is ProjectVersion.txt still accessible?
   
2. IMMEDIATE (< 5 min)
   □ STOP Agent1 (pkill agent1)
   □ DO NOT continue operation
   □ Slack alert sent to #security-alerts
   
3. INVESTIGATION (< 30 min)
   □ Check logs: tail -100 logs/agent1.log | grep SECURITY
   □ Determine: What operation caused corruption?
   □ File check: ls -l ProjectSettings/ProjectVersion.txt
   
4. RECOVERY (< 1 hour)
   □ Restore from backup if available
   OR
   □ Re-clone project from repository
   OR
   □ Contact security architect immediately

5. ESCALATE
   □ Notify DevOps Lead
   □ Create incident ticket
   □ Schedule post-mortem
```

### When Alert Fires: HIGH - AGENT COMMUNICATION LOOP

```
1. IMMEDIATE (< 1 min)
   □ Check Dashboard: Which agents are looping?
   □ Identify: Agent A ↔ Agent B
   
2. INVESTIGATION (< 5 min)
   □ Check MCP logs: Grep for error pattern
   grep "Agent.*→.*Agent.*error" logs/orchestrator.log
   □ Identify: What's the error message?
   
3. DECISION (< 15 min)
   □ Is this expected? (e.g., known issue with retry limit)
   □ Is this unexpected? (e.g., data corruption, logic bug)
   
4. ACTION
   If expected:
   □ Manual reset circuit: cb.reset_circuit("AgentA", "AgentB")
   □ Continue monitoring
   
   If unexpected:
   □ Contact agent developers
   □ Review code changes
   □ Consider rolling back agent
   
5. ESCALATE if >5 circuit breaker trips in 1 hour
```

### When Alert Fires: HIGH - SHELL INJECTION BLOCKED

```
1. IMMEDIATE (< 1 min)
   □ Congratulations! The boundary worked ✅
   □ Check Dashboard: Which agent attempted injection?
   
2. INVESTIGATION (< 10 min)
   □ Extract offending command from logs:
     grep "shell_metachar" logs/agent*.log
   □ Identify: What dangerous character was blocked?
   □ Check: Is this a legitimate use case?
   
3. DECISION
   □ If legitimate: Update whitelist or refactor code
   □ If malicious: Investigate agent code for bugs
   
4. ACTION
   □ Update SafeProcessExecution if needed
   □ Re-test with test_phase1_validation.py
   □ Re-deploy with fix
```

---

## Monitoring Queries (Prometheus PromQL)

### Query 1: File Operation Success Rate (Last 24h)
```prometheus
(file_operations_success / file_operations_attempted) * 100
```
**Expected:** 100% (always successful)

### Query 2: Blocked Operations (Last 4h)
```prometheus
increase(file_operations_blocked[4h])
```
**Expected:** 0 (no blocks = no attacks)

### Query 3: Agent Pair Health (Real-time)
```prometheus
circuit_breaker_open_circuits + circuit_breaker_at_risk_pairs
```
**Expected:** <5 (most agents healthy)

### Query 4: Process Execution Success (Last 24h)
```prometheus
(process_execution_success / process_execution_attempted) * 100
```
**Expected:** >99% (maybe 1 timeout = ok)

### Query 5: Integrity Check Status (Last 7d)
```prometheus
increase(asset_integrity_check_failed[7d])
```
**Expected:** 0 (never failed)

---

## Logs Retention & Archival

### Log Retention Policy

| Log Type | Retention | Archive | Notes |
|----------|-----------|---------|-------|
| Agent logs | 7 days | S3 monthly | Rotate daily |
| Security events | 30 days | S3 yearly | Critical |
| Circuit breaker | 14 days | S3 monthly | Event-driven |
| Metrics | 30 days | Prometheus native | Time-series |

### Log Locations

```
/var/log/gamma4jarvis/
├── agent1.log              # Agent output
├── agent2.log
├── ...
├── security/
│   ├── file_operations.log # SafeFileOperations events
│   ├── process_exec.log    # SafeProcessExecution events
│   ├── asset_ops.log       # SafeAssetOperations events
│   └── circuit_breaker.log # MCP circuit breaker events
└── metrics/
    ├── prometheus.log      # Metrics scrapes
    └── alerts.log          # Alert firings
```

### Log Format (JSON)

```json
{
  "timestamp": "2026-04-12T15:30:45.123Z",
  "level": "INFO|WARNING|ERROR|CRITICAL",
  "component": "SafeFileOperations",
  "agent": "Agent1",
  "event": "file_write_success|file_write_blocked",
  "details": {
    "path": "Assets/AI_Generated/output.txt",
    "reason": "allowed_path|forbidden_path",
    "duration_ms": 2.3
  }
}
```

---

## Health Check Endpoints

### Endpoint 1: Agent Health
```
GET http://localhost:9000/api/agents/{agent_id}/health

Response:
{
  "agent_id": "agent1",
  "status": "healthy|degraded|critical",
  "uptime_seconds": 7200,
  "last_security_check": "2026-04-12T15:30:00Z",
  "security_status": {
    "file_operations_blocked": 0,
    "process_execution_blocked": 0,
    "integrity_check_failed": false,
    "circuit_breaker_open": false
  }
}
```

### Endpoint 2: System Health
```
GET http://localhost:9000/api/system/health

Response:
{
  "overall_status": "healthy|warning|critical",
  "agents_healthy": 4,
  "agents_total": 4,
  "active_alerts": 0,
  "circuit_breaker_open_count": 0,
  "last_integrity_check": "2026-04-12T15:28:00Z"
}
```

### Endpoint 3: Security Metrics
```
GET http://localhost:9000/api/security/metrics

Response:
{
  "metrics": {
    "file_operations_attempted": 1245,
    "file_operations_blocked": 0,
    "process_execution_attempted": 156,
    "process_execution_blocked": 0,
    "circuit_breaker_trips": 0,
    "integrity_check_failures": 0
  },
  "trends": {
    "file_op_block_rate": 0.0,
    "process_exec_block_rate": 0.0
  }
}
```

---

## On-Call Escalation

### Escalation Chain
```
CRITICAL Alert → On-Call Security (5 min) 
              → DevOps Lead (15 min)
              → Security Architect (30 min)
              → CTO (60 min)
```

### On-Call Contact
| Role | Name | Phone | Slack | Email |
|------|------|-------|-------|-------|
| Security | [Name] | +1-xxx-xxxx | @on-call-sec | sec@... |
| DevOps | [Name] | +1-xxx-xxxx | @on-call-devops | ops@... |

---

## Setup Commands (Infrastructure)

### Deploy Prometheus Scrape Config
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'gamma4jarvis'
    static_configs:
      - targets: ['localhost:9090']
    interval: 60s
```

### Deploy AlertManager Rules
```bash
# Copy alert rules
cp alert_rules.yaml /etc/prometheus/rules/

# Reload Prometheus
curl -X POST http://localhost:9090/-/reload
```

### Deploy Grafana Dashboards
```bash
# Import dashboard JSON
curl -X POST http://localhost:3000/api/dashboards/db \
  -H "Content-Type: application/json" \
  -d @security_dashboard.json
```

---

**Monitoring Status:** ✅ Ready  
**Dashboards:** 3 (Overview, Threats, Performance)  
**Alerts:** 8 rules (CRITICAL, WARNING, INFO)  
**Tools:** Prometheus + Grafana + AlertManager  
**Update Frequency:** Every 60 seconds
