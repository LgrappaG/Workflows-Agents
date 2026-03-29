#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const projectRoot = path.join(__dirname, '..');
const outputPath = path.join(projectRoot, 'reports', 'benchmarks', 'suite-results.json');

const jobs = [
  {
    name: 'token-benchmark',
    cmd: 'node',
    args: ['scripts/measure-tokens.js', 'benchmark']
  },
  {
    name: 'compression-validation',
    cmd: 'node',
    args: ['scripts/validate-compression.js']
  },
  {
    name: 'coverage-analysis',
    cmd: 'node',
    args: ['scripts/coverage-analyzer.js']
  }
];

const result = {
  timestamp: new Date().toISOString(),
  jobs: []
};

for (const job of jobs) {
  const started = Date.now();
  const proc = spawnSync(job.cmd, job.args, {
    cwd: projectRoot,
    encoding: 'utf8'
  });

  result.jobs.push({
    name: job.name,
    duration_ms: Date.now() - started,
    exit_code: proc.status,
    stdout_tail: (proc.stdout || '').split('\n').slice(-20).join('\n'),
    stderr_tail: (proc.stderr || '').split('\n').slice(-20).join('\n')
  });
}

result.failed = result.jobs.filter((j) => j.exit_code !== 0).length;

fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, JSON.stringify(result, null, 2), 'utf8');

console.log(`[benchmark-suite] jobs=${result.jobs.length} failed=${result.failed}`);
console.log('[benchmark-suite] report=reports/benchmarks/suite-results.json');
