---
version: 9.0.0
category: Code Quality
agent: Code Reviewer
difficulty: intermediate
estimated_time: 1-3 hours
skills:
  required:
  - networking-server-security
  - networking-guild-system
  - networking-server-maintenance
  - networking-server-authority
  - networking-analytics-tracking
  - networking-encryption
  - networking-authentication
  - networking-bandwidth-optimization
  - networking-cloud-saves
  - networking-lag-compensation
  - networking-performance-monitoring
  - networking-player-persistence
  - networking-prediction-reconciliation
  - networking-replay-system
  - networking-server-replication
  - networking-state-synchronization
  - networking-trading-system
  - networking-account-recovery
  - networking-achievement-tracking
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-ban-system
  - networking-battle-pass
  - networking-chat-system
  - networking-client-authority
  - networking-connection-management
  - networking-cross-progression
  - networking-friend-system
  - networking-interpolation
  - networking-leaderboard
  - networking-lobby-system
  - networking-matchmaking
  - networking-message-ordering
  - networking-ngo-setup
  - networking-packet-loss-handling
  - networking-player-spawning
  - networking-presence-system
  - networking-pvp-ranking
  - networking-region-selection
  - networking-reward-distribution
  - networking-rollback-resimulation
  - networking-rpc-system
  - networking-server-load-balancing
  - networking-spectator-mode
  - networking-statistics-synchronization
  - automated-testing-framework
  - ai-debugging-tools
  - compatibility-testing
  - custom-workflow-builder
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-physics-colliders
  - csharp-chain-of-responsibility
  - terrain-normal-generation
  - ui-dynamic-styling
  - ui-input-validation
  - ui-text-binding
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-perception-system
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  recommended:
  - audio-ducking-sidechains
  - build-system-optimization
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-builder-pattern
  - debug-build-diagnostic
  - engine-migration-guide
  - material-mipmap-chains
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-event-handlers
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-panel-layout
  - ui-performance-optimization
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-theme-switching
  optional:
  - ui-tooltips
  - ui-touch-input
  - ui-transition-timing
  - ui-two-way-binding
  - ui-visual-feedback
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: code-reviewer
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 21.0
estimated_skills_needed: 147
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Security Audit Workflow

Comprehensive security review using `@security-specialist`.

## 1. Define Audit Scope

Tell the agent what to audit:
- "Full security audit of my multiplayer game"
- "Check for cheating vulnerabilities"
- "Review data storage security"
- "Audit network communication"

## 2. Security Categories

### A. Client-Side Security

| Check | Risk | Status |
|-------|------|--------|
| No hardcoded secrets | Critical | |
| Input validation | Critical | |
| Memory protection | High | |
| Anti-tampering | High | |
| Secure storage | High | |

### B. Network Security

| Check | Risk | Status |
|-------|------|--------|
| Encrypted transport (TLS/DTLS) | Critical | |
| Server-authoritative game state | Critical | |
| Rate limiting | High | |
| Replay attack prevention | High | |
| Session management | High | |

### C. Anti-Cheat

| Check | Risk | Status |
|-------|------|--------|
| Server validates all actions | Critical | |
| Position/speed validation | High | |
| Damage calculation server-side | Critical | |
| Resource/currency server-controlled | Critical | |
| Impossible action detection | High | |

### D. Data Protection

| Check | Risk | Status |
|-------|------|--------|
| PII handling (GDPR) | Critical | |
| Save data encryption | High | |
| Analytics privacy | Medium | |
| Third-party SDK audit | Medium | |

## 3. Automated Security Scan

// turbo
```bash
echo "=== Security Scan ==="
echo ""
echo "Checking for hardcoded secrets..."
grep -rn "password\|secret\|apikey\|api_key\|token" --include="*.cs" Assets/ 2>/dev/null | grep -v "//.*password" | head -20
echo ""
echo "Checking for insecure storage..."
grep -rn "PlayerPrefs.SetString" --include="*.cs" Assets/ 2>/dev/null | head -10
echo ""
echo "Checking for direct SQL..."
grep -rn "SELECT\|INSERT\|UPDATE\|DELETE" --include="*.cs" Assets/ 2>/dev/null | head -10
echo ""
echo "Checking network code..."
grep -rn "\[ServerRpc\]\|\[ClientRpc\]" --include="*.cs" Assets/ 2>/dev/null | head -20
```

## 4. Code Review Patterns

### Dangerous Patterns to Flag

```csharp
// ❌ DANGEROUS: Client reports damage
[ServerRpc]
public void DealDamageServerRpc(int damage)
{
    // Client can send any value!
    _health -= damage;
}

// ✅ SAFE: Server calculates damage
[ServerRpc]
public void AttackServerRpc(ulong targetId)
{
    int damage = CalculateDamage(OwnerClientId);
    if (ValidateTarget(targetId))
    {
        ApplyDamage(targetId, damage);
    }
}
```

```csharp
// ❌ DANGEROUS: Client sets position
[ServerRpc]
public void SetPositionServerRpc(Vector3 pos)
{
    transform.position = pos; // Teleport hack!
}

// ✅ SAFE: Server validates movement
[ServerRpc]
public void MoveServerRpc(Vector3 input)
{
    if (input.magnitude > 1f) return; // Validate
    Vector3 newPos = CalculateMovement(input);
    if (IsValidMove(transform.position, newPos))
    {
        transform.position = newPos;
    }
}
```

## 5. Vulnerability Checklist

### Client-Side
- [ ] No API keys in code
- [ ] No debug backdoors in release
- [ ] IL2CPP enabled (harder to reverse)
- [ ] Sensitive data cleared from memory
- [ ] No logging of sensitive data

### Network
- [ ] All traffic encrypted
- [ ] Server validates every RPC
- [ ] Rate limiting implemented
- [ ] Timestamps prevent replay
- [ ] Session tokens expire

### Data
- [ ] Saves encrypted
- [ ] Saves have integrity hash
- [ ] No PII stored unnecessarily
- [ ] Privacy policy exists
- [ ] Data deletion possible

### Anti-Cheat
- [ ] Movement speed validated
- [ ] Positions checked for wall clipping
- [ ] Currency server-controlled
- [ ] Impossible actions logged
- [ ] Suspicious patterns flagged

## 6. Generate Security Report

// turbo
```bash
cat > security-audit-report.md << 'EOF'
# Security Audit Report

Generated: $(date '+%Y-%m-%d')
Classification: CONFIDENTIAL

## Risk Summary

| Category | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| Client-Side | | | | |
| Network | | | | |
| Anti-Cheat | | | | |
| Data Protection | | | | |

## Critical Findings

### Finding 1: [Title]
- **Risk**: Critical
- **Location**: `file.cs:line`
- **Description**:
- **Impact**:
- **Remediation**:

## High Priority Findings

### Finding 1: [Title]
- **Risk**: High
- **Location**:
- **Description**:
- **Remediation**:

## Recommendations

### Immediate (This Sprint)
1.

### Short-term (This Month)
1.

### Long-term (This Quarter)
1.

## Compliance

- [ ] GDPR compliant
- [ ] COPPA compliant (if children users)
- [ ] Platform requirements met (Quest Store, Steam)
EOF

echo "✅ Security audit report created"
echo "⚠️  Review findings carefully before sharing"
```

## 7. Penetration Test Scenarios

| Scenario | Test | Expected Behavior |
|----------|------|------------------|
| Speed hack | Send impossible speed | Server rejects |
| Teleport | Send impossible position | Server rejects |
| Damage hack | Send high damage value | Server recalculates |
| Packet replay | Re-send old packets | Server rejects (timestamps) |
| Memory edit | Modify local health | Server corrects |
| Save edit | Modify save file | Integrity check fails |

## Example Commands

- "Run security audit on my multiplayer game"
- "Check for cheating vulnerabilities in my networked code"
- "Review data protection compliance"
- "Audit my ServerRpc implementations"