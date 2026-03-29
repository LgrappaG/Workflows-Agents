#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { listSkills, toRelativeProjectPath } = require('./lib/skill-metadata');

const projectRoot = path.join(__dirname, '..');
const versionsPath = path.join(projectRoot, 'data', 'skill-versions.json');
const matrixPath = path.join(projectRoot, 'data', 'compatibility-matrix.json');

function loadJson(filePath, fallback) {
  if (!fs.existsSync(filePath)) {
    return fallback;
  }
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (_err) {
    return fallback;
  }
}

function saveJson(filePath, payload) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(payload, null, 2), 'utf8');
}

function generateIndex() {
  const now = new Date().toISOString();
  const previous = loadJson(versionsPath, { skills: {} });
  const skills = listSkills(projectRoot);

  const next = {
    updated_at: now,
    skills: {}
  };

  for (const skill of skills) {
    const existing = previous.skills[skill.id];
    const version = existing ? existing.version : '1.0.0';

    next.skills[skill.id] = {
      version,
      risk: skill.risk,
      domain: skill.domain,
      path: toRelativeProjectPath(projectRoot, skill.path),
      last_checked: now
    };
  }

  saveJson(versionsPath, next);

  const matrix = {
    updated_at: now,
    total_skills: skills.length,
    compatibility: skills.map((skill) => ({
      skill: skill.id,
      compatible_with_framework: '>=9.0.3',
      requires: [],
      breaking_since: null
    }))
  };
  saveJson(matrixPath, matrix);

  console.log(`[skill-version-manager] indexed=${skills.length}`);
}

function bumpVersion(current, type) {
  const [maj, min, pat] = current.split('.').map((n) => Number(n));
  if (type === 'major') return `${maj + 1}.0.0`;
  if (type === 'minor') return `${maj}.${min + 1}.0`;
  return `${maj}.${min}.${pat + 1}`;
}

function bump(skillId, type) {
  const db = loadJson(versionsPath, { skills: {} });
  if (!db.skills[skillId]) {
    console.error(`[skill-version-manager] unknown skill: ${skillId}`);
    process.exit(1);
  }

  const current = db.skills[skillId].version || '1.0.0';
  db.skills[skillId].version = bumpVersion(current, type || 'patch');
  db.skills[skillId].last_checked = new Date().toISOString();
  saveJson(versionsPath, db);

  console.log(`[skill-version-manager] bumped ${skillId} ${current} -> ${db.skills[skillId].version}`);
}

const cmd = process.argv[2] || 'generate';
if (cmd === 'generate') {
  generateIndex();
} else if (cmd === 'bump') {
  bump(process.argv[3], process.argv[4]);
} else {
  console.log('usage: node scripts/skill-version-manager.js [generate|bump <skillId> <patch|minor|major>]');
}
