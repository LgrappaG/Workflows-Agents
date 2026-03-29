#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { listSkills } = require('./lib/skill-metadata');

const projectRoot = path.join(__dirname, '..');
const usageDir = path.join(projectRoot, 'reports', 'usage');
const outputPath = path.join(projectRoot, 'reports', 'analytics', 'dashboard.json');

function readUsageEvents() {
  if (!fs.existsSync(usageDir)) {
    return [];
  }

  const events = [];
  for (const fileName of fs.readdirSync(usageDir)) {
    if (!fileName.endsWith('.json')) {
      continue;
    }
    const abs = path.join(usageDir, fileName);
    try {
      const payload = JSON.parse(fs.readFileSync(abs, 'utf8'));
      if (Array.isArray(payload)) {
        events.push(...payload);
      } else {
        events.push(payload);
      }
    } catch (_err) {
      // skip malformed files
    }
  }
  return events;
}

function groupBy(array, fn) {
  return array.reduce((acc, item) => {
    const key = fn(item);
    acc[key] = (acc[key] || 0) + 1;
    return acc;
  }, {});
}

function run() {
  const skills = listSkills(projectRoot);
  const events = readUsageEvents();

  const dashboard = {
    generated_at: new Date().toISOString(),
    total_skills: skills.length,
    total_usage_events: events.length,
    skills_by_domain: groupBy(skills, (s) => s.domain),
    skills_by_risk: groupBy(skills, (s) => s.risk),
    usage_by_type: groupBy(events, (e) => e.type || 'unknown'),
    top_used_skills: Object.entries(groupBy(events, (e) => e.skill || 'unknown'))
      .sort((a, b) => b[1] - a[1])
      .slice(0, 20)
      .map(([skill, count]) => ({ skill, count }))
  };

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, JSON.stringify(dashboard, null, 2), 'utf8');

  console.log(`[analytics-dashboard] events=${dashboard.total_usage_events}`);
  console.log('[analytics-dashboard] report=reports/analytics/dashboard.json');
}

run();
