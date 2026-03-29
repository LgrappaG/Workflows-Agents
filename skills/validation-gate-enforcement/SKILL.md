---
name: validation-gate-enforcement
description: Enforce quality gates to block insufficient builds
risk: high
source: workspace
date_added: '2026-03-24'
usage: Pre-launch certification, hotfix deployment approval, live service patch release, console submission gate, experimental feature rollout, team milestone verification, investor demo readiness
avoid: Manual gate enforcement (human error, inconsistency), gates with no measurable criteria (subjective pass/fail), silent gate failures (no stakeholder notification), insufficient gate coverage (<5 gates), gate bypass without audit trail
mandates: Block 100% of non-compliant builds from release. Enforce 8+ gates simultaneously. Zero gate bypasses without audit trail. Automated reporting to stakeholders. Fail-secure defaults.
response: 'Define gating criteria across 8 domains: performance (FPS ≥60), stability (crash rate, 1%), compatibility (5+ configs passing), security (no auth token in logs), content, Implement gate enforcer that blocks merge→main branch if ANY gate fails; require, Configure pre-release gate sequence: Stage 1 (automated: performance, compatibility), Stage 2 (manual:'
---

# Validation Gate Enforcement

Enforce quality gates to block insufficient builds

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
- Quality assurance
- Development workflows

## What NOT to Do
- Gate bypasses
- Incomplete testing
- Deploy without validation
