#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const projectRoot = path.join(__dirname, '..');
const skillsRoot = path.join(projectRoot, 'skills');

const phase6Seeds = [
  {
    id: 'ai-llm-runtime-integration',
    description: 'Integrate runtime LLM orchestration for NPC and mission generation with guardrails',
    risk: 'high'
  },
  {
    id: 'ml-model-serving-unity',
    description: 'Serve on-device and remote ML models for gameplay inference with fallback paths',
    risk: 'high'
  },
  {
    id: 'cross-engine-portability-layer',
    description: 'Design portability layer to share gameplay logic across Unity, Godot, and Unreal',
    risk: 'medium'
  },
  {
    id: 'community-marketplace-governance',
    description: 'Define trust, moderation, and lifecycle governance for community skill marketplace',
    risk: 'medium'
  },
  {
    id: 'analytics-funnel-attribution',
    description: 'Track acquisition and retention funnels for skill usage and workflow completion',
    risk: 'medium'
  },
  {
    id: 'benchmark-regression-gates',
    description: 'Define regression gates that fail CI when benchmark drift crosses thresholds',
    risk: 'high'
  }
];

function skillTemplate(seed) {
  const date = new Date().toISOString().slice(0, 10);
  return `---
name: ${seed.id}
description: "${seed.description}"
risk: ${seed.risk}
source: .agents-phase6
date_added: ${date}
usage: "Use when implementing Phase 6 scale, interoperability, and analytics initiatives"
avoid: "Do not deploy without compatibility checks, rollback strategy, and measurable SLOs"
mandates:
  - define measurable success criteria and failure budgets
  - include platform-specific acceptance gates
  - include data privacy and governance checks
response: assess baseline, design minimal implementation, validate measurable targets, document rollback plan
---

# ${seed.id}

Phase 6 seed skill scaffold.
`;
}

function run() {
  let created = 0;

  for (const seed of phase6Seeds) {
    const dir = path.join(skillsRoot, seed.id);
    const file = path.join(dir, 'SKILL.md');

    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    if (!fs.existsSync(file)) {
      fs.writeFileSync(file, skillTemplate(seed), 'utf8');
      created += 1;
    }
  }

  console.log(`[phase6-bootstrap] seeds=${phase6Seeds.length} created=${created}`);
}

run();
