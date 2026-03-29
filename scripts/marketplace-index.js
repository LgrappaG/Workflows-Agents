#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const projectRoot = path.join(__dirname, '..');
const marketplaceRoot = path.join(projectRoot, 'marketplace', 'skills');
const outputPath = path.join(projectRoot, 'marketplace', 'index.json');

function readMetadata(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    return {};
  }

  const metadata = {};
  for (const line of match[1].split('\n')) {
    const idx = line.indexOf(':');
    if (idx <= 0) continue;
    metadata[line.slice(0, idx).trim()] = line.slice(idx + 1).trim().replace(/^['\"]|['\"]$/g, '');
  }
  return metadata;
}

function run() {
  if (!fs.existsSync(marketplaceRoot)) {
    fs.mkdirSync(marketplaceRoot, { recursive: true });
  }

  const entries = fs
    .readdirSync(marketplaceRoot)
    .filter((entry) => fs.statSync(path.join(marketplaceRoot, entry)).isDirectory())
    .map((id) => {
      const skillFile = path.join(marketplaceRoot, id, 'SKILL.md');
      if (!fs.existsSync(skillFile)) {
        return null;
      }
      const metadata = readMetadata(skillFile);
      return {
        id,
        name: metadata.name || id,
        description: metadata.description || '',
        risk: metadata.risk || 'unknown',
        source: metadata.source || 'community',
        updated_at: new Date(fs.statSync(skillFile).mtimeMs).toISOString()
      };
    })
    .filter(Boolean)
    .sort((a, b) => a.id.localeCompare(b.id));

  const payload = {
    generated_at: new Date().toISOString(),
    total: entries.length,
    entries
  };

  fs.writeFileSync(outputPath, JSON.stringify(payload, null, 2), 'utf8');
  console.log(`[marketplace-index] indexed=${entries.length}`);
  console.log('[marketplace-index] output=marketplace/index.json');
}

run();
