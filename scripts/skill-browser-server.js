#!/usr/bin/env node

const http = require('http');
const path = require('path');
const { listSkills, toRelativeProjectPath } = require('./lib/skill-metadata');

const projectRoot = path.join(__dirname, '..');
const port = Number(process.env.SKILL_BROWSER_PORT || 4173);

function filterSkills(skills, query) {
  const q = (query.q || '').toLowerCase().trim();
  const domain = (query.domain || '').toLowerCase().trim();
  const risk = (query.risk || '').toLowerCase().trim();

  return skills.filter((skill) => {
    if (domain && skill.domain.toLowerCase() !== domain) {
      return false;
    }
    if (risk && skill.risk.toLowerCase() !== risk) {
      return false;
    }
    if (!q) {
      return true;
    }

    const bag = [skill.id, skill.name, skill.description, skill.usage, skill.domain]
      .join(' ')
      .toLowerCase();

    return bag.includes(q);
  });
}

function htmlPage() {
  return `<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>.agents Skill Browser</title>
  <style>
    :root { --bg: #f2efe8; --ink: #19242b; --card: #fffdf7; --accent: #0f7b6c; --line: #d8d2c6; }
    body { margin: 0; font-family: "Segoe UI", Tahoma, sans-serif; color: var(--ink); background: radial-gradient(circle at 10% 0%, #fff9e8, var(--bg)); }
    .wrap { max-width: 1100px; margin: 0 auto; padding: 24px; }
    .title { font-size: 28px; margin: 0 0 14px; letter-spacing: 0.2px; }
    .controls { display: grid; grid-template-columns: 1.5fr 1fr 1fr auto; gap: 10px; margin-bottom: 14px; }
    input, select, button { border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; font-size: 14px; }
    button { cursor: pointer; background: var(--accent); color: #fff; border-color: transparent; }
    .meta { font-size: 13px; opacity: 0.8; margin-bottom: 10px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }
    .card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px; }
    .id { font-size: 14px; font-weight: 600; margin-bottom: 6px; }
    .muted { font-size: 12px; opacity: 0.8; margin-bottom: 8px; }
    .desc { font-size: 13px; min-height: 52px; }
    .path { font-family: Consolas, monospace; font-size: 11px; opacity: 0.8; margin-top: 10px; word-break: break-all; }
    @media (max-width: 760px) { .controls { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <div class="wrap">
    <h1 class="title">.agents Skill Browser</h1>
    <div class="controls">
      <input id="q" placeholder="search skill, description, usage" />
      <select id="domain"><option value="">all domains</option></select>
      <select id="risk"><option value="">all risk levels</option><option>low</option><option>medium</option><option>high</option></select>
      <button id="run">search</button>
    </div>
    <div class="meta" id="meta"></div>
    <div class="grid" id="grid"></div>
  </div>
  <script>
    async function getJson(url) { const r = await fetch(url); return r.json(); }
    async function seedDomains() {
      const data = await getJson('/api/domains');
      const select = document.getElementById('domain');
      data.domains.forEach((d) => {
        const o = document.createElement('option');
        o.value = d;
        o.textContent = d;
        select.appendChild(o);
      });
    }
    async function search() {
      const q = document.getElementById('q').value;
      const domain = document.getElementById('domain').value;
      const risk = document.getElementById('risk').value;
      const params = new URLSearchParams({ q, domain, risk });
      const data = await getJson('/api/skills?' + params.toString());

      const grid = document.getElementById('grid');
      grid.innerHTML = '';
      document.getElementById('meta').textContent = data.count + ' skills';

      data.skills.forEach((s) => {
        const el = document.createElement('article');
        el.className = 'card';
        el.innerHTML = '<div class="id">' + s.id + '</div>' +
          '<div class="muted">domain: ' + s.domain + ' | risk: ' + s.risk + ' | ' + s.bytes + ' bytes</div>' +
          '<div class="desc">' + (s.description || 'no description') + '</div>' +
          '<div class="path">' + s.relative_path + '</div>';
        grid.appendChild(el);
      });
    }
    document.getElementById('run').addEventListener('click', search);
    document.getElementById('q').addEventListener('keydown', (e) => { if (e.key === 'Enter') search(); });
    seedDomains().then(search);
  </script>
</body>
</html>`;
}

function json(res, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(200, {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(body)
  });
  res.end(body);
}

function parseQuery(urlObj) {
  const query = {};
  urlObj.searchParams.forEach((value, key) => {
    query[key] = value;
  });
  return query;
}

const server = http.createServer((req, res) => {
  const urlObj = new URL(req.url, `http://localhost:${port}`);

  if (urlObj.pathname === '/') {
    const page = htmlPage();
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(page);
    return;
  }

  if (urlObj.pathname === '/api/skills') {
    const allSkills = listSkills(projectRoot).map((s) => ({
      ...s,
      relative_path: toRelativeProjectPath(projectRoot, s.path)
    }));
    const query = parseQuery(urlObj);
    const filtered = filterSkills(allSkills, query);
    json(res, { count: filtered.length, skills: filtered });
    return;
  }

  if (urlObj.pathname === '/api/domains') {
    const domains = [...new Set(listSkills(projectRoot).map((s) => s.domain))].sort();
    json(res, { count: domains.length, domains });
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(port, () => {
  console.log(`[skill-browser] running at http://localhost:${port}`);
});
