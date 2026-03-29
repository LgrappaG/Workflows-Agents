#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    return {};
  }

  const lines = match[1].split('\n');
  const result = {};

  for (const line of lines) {
    const idx = line.indexOf(':');
    if (idx <= 0) {
      continue;
    }
    const key = line.slice(0, idx).trim();
    let value = line.slice(idx + 1).trim();
    value = value.replace(/^['\"]|['\"]$/g, '');
    result[key] = value;
  }

  return result;
}

function getSkillsRoot(projectRoot = path.join(__dirname, '..', '..')) {
  return path.join(projectRoot, 'skills');
}

function listSkills(projectRoot = path.join(__dirname, '..', '..')) {
  const skillsRoot = getSkillsRoot(projectRoot);
  if (!fs.existsSync(skillsRoot)) {
    return [];
  }

  return fs
    .readdirSync(skillsRoot)
    .filter((entry) => fs.statSync(path.join(skillsRoot, entry)).isDirectory())
    .map((skillName) => {
      const filePath = path.join(skillsRoot, skillName, 'SKILL.md');
      if (!fs.existsSync(filePath)) {
        return null;
      }

      const content = fs.readFileSync(filePath, 'utf8');
      const frontmatter = parseFrontmatter(content);

      return {
        id: skillName,
        path: filePath,
        domain: skillName.split('-')[0] || 'misc',
        name: frontmatter.name || skillName,
        description: frontmatter.description || '',
        risk: frontmatter.risk || 'unknown',
        usage: frontmatter.usage || '',
        date_added: frontmatter.date_added || '',
        bytes: Buffer.byteLength(content, 'utf8')
      };
    })
    .filter(Boolean);
}

function toRelativeProjectPath(projectRoot, filePath) {
  return path.relative(projectRoot, filePath).replace(/\\/g, '/');
}

module.exports = {
  parseFrontmatter,
  listSkills,
  getSkillsRoot,
  toRelativeProjectPath
};
