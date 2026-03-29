#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { listSkills, parseFrontmatter } = require('./lib/skill-metadata');

const projectRoot = path.join(__dirname, '..');
const reportPath = path.join(projectRoot, 'reports', 'analytics', 'enrichment-report.json');

const MODE = process.argv.includes('--apply') ? 'apply' : 'dry-run';
const LIMIT_ARG = process.argv.find((arg) => arg.startsWith('--limit='));
const LIMIT = LIMIT_ARG ? Number(LIMIT_ARG.split('=')[1]) : Infinity;

function enrichMandates(domain) {
  return [
    `- define at least 1 measurable ${domain} target (latency, fps, memory, or pass-rate)`,
    '- include one platform-specific acceptance criterion',
    '- include one failure-mode guardrail with explicit fallback behavior'
  ];
}

function enrichResponse(domain) {
  return `assess ${domain} baseline with metrics, apply minimal viable change, verify against measurable threshold, document rollback strategy`;
}

function needsEnrichment(frontmatter) {
  const mandates = String(frontmatter.mandates || '').toLowerCase();
  const response = String(frontmatter.response || '').toLowerCase();
  const genericTerms = ['best practices', 'optimize as needed', 'improve quality'];
  const hasGeneric = genericTerms.some((term) => mandates.includes(term) || response.includes(term));
  const hasWeakMandates = mandates.split(',').length < 2 && !mandates.includes('-');
  return hasGeneric || hasWeakMandates;
}

function patchFrontmatter(raw, frontmatter, domain) {
  const mandatesBlock = enrichMandates(domain).join('\n');
  const responseLine = enrichResponse(domain);

  const patchedMandates = /\nmandates:\s*[\s\S]*?(?=\n[a-z_]+:|\n---)/i.test(raw)
    ? raw.replace(/\nmandates:\s*[\s\S]*?(?=\n[a-z_]+:|\n---)/i, `\nmandates:\n${mandatesBlock}`)
    : raw.replace(/\n---\n/, `\nmandates:\n${mandatesBlock}\n---\n`);

  const patchedResponse = /\nresponse:\s*.*$/m.test(patchedMandates)
    ? patchedMandates.replace(/\nresponse:\s*.*$/m, `\nresponse: ${responseLine}`)
    : patchedMandates.replace(/\n---\n/, `\nresponse: ${responseLine}\n---\n`);

  return patchedResponse;
}

function run() {
  const skills = listSkills(projectRoot);
  const report = {
    timestamp: new Date().toISOString(),
    mode: MODE,
    scanned: skills.length,
    candidates: 0,
    changed: 0,
    files: []
  };

  let changedCount = 0;
  for (const skill of skills) {
    if (changedCount >= LIMIT) {
      break;
    }

    const content = fs.readFileSync(skill.path, 'utf8');
    const frontmatter = parseFrontmatter(content);
    if (!needsEnrichment(frontmatter)) {
      continue;
    }

    report.candidates += 1;
    const next = patchFrontmatter(content, frontmatter, skill.domain);

    if (MODE === 'apply' && next !== content) {
      fs.writeFileSync(skill.path, next, 'utf8');
      changedCount += 1;
      report.changed += 1;
      report.files.push(skill.id);
    }
  }

  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf8');

  console.log(`[enrich-skills] mode=${MODE} scanned=${report.scanned} candidates=${report.candidates} changed=${report.changed}`);
  console.log(`[enrich-skills] report=${path.relative(projectRoot, reportPath).replace(/\\/g, '/')}`);
}

run();
