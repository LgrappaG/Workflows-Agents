#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const projectRoot = path.join(__dirname, '..');
const watchTargets = ['skills', 'workflows'];
const reportPath = path.join(projectRoot, 'reports', 'analytics', 'live-validation.json');

function runValidation(label) {
  const runs = [
    {
      name: 'skills-fast',
      cmd: 'python',
      args: ['hooks/pre-commit-skills.py']
    },
    {
      name: 'workflows',
      cmd: 'python',
      args: ['hooks/pre-commit-workflows.py']
    }
  ];

  const result = {
    timestamp: new Date().toISOString(),
    trigger: label,
    runs: []
  };

  for (const run of runs) {
    const started = Date.now();
    const proc = spawnSync(run.cmd, run.args, {
      cwd: projectRoot,
      encoding: 'utf8'
    });

    result.runs.push({
      name: run.name,
      exit_code: proc.status,
      duration_ms: Date.now() - started,
      stdout_tail: (proc.stdout || '').split('\n').slice(-20).join('\n'),
      stderr_tail: (proc.stderr || '').split('\n').slice(-20).join('\n')
    });
  }

  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.writeFileSync(reportPath, JSON.stringify(result, null, 2), 'utf8');

  const failed = result.runs.filter((r) => r.exit_code !== 0).length;
  console.log(`[validation-watch] trigger=${label} failed=${failed} report=reports/analytics/live-validation.json`);
}

let debounceTimer = null;
function scheduleValidation(reason) {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => runValidation(reason), 700);
}

function start() {
  runValidation('startup');

  for (const target of watchTargets) {
    const abs = path.join(projectRoot, target);
    if (!fs.existsSync(abs)) {
      continue;
    }

    fs.watch(abs, { recursive: true }, (eventType, filename) => {
      if (!filename) {
        return;
      }
      if (!filename.endsWith('.md')) {
        return;
      }
      scheduleValidation(`${eventType}:${target}/${filename.replace(/\\/g, '/')}`);
    });

    console.log(`[validation-watch] watching ${target}`);
  }
}

start();
