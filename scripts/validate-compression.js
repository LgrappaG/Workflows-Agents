#!/usr/bin/env node

/**
 * Compression Validator for .agents Framework
 * Validates that SKILL.md files follow compression guidelines
 * 
 * Usage:
 *   node validate-compression.js           - Validate all skills
 *   node validate-compression.js <skill>   - Validate specific skill
 */

const fs = require('fs');
const path = require('path');

const RULES = {
  description_max_chars: 200,
  code_snippet_max_lines: 20,
  nested_depth_max: 3,
  warnings: {
    verbose_section: 500, // chars
    long_bullet: 150,     // chars per bullet
  }
};

function parseYAML(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;

  const yaml = match[1];
  const result = {};

  yaml.split('\n').forEach(line => {
    const [key, value] = line.split(':').map(s => s.trim());
    if (key && value) {
      result[key] = value.replace(/^['"]|['"]$/g, '');
    }
  });

  return result;
}

function validateSkill(skillPath) {
  if (!fs.existsSync(skillPath)) {
    return { valid: false, errors: [`File not found: ${skillPath}`], warnings: [] };
  }

  const content = fs.readFileSync(skillPath, 'utf8');
  const errors = [];
  const warnings = [];

  // Parse YAML frontmatter
  const yaml = parseYAML(content);
  const hasYaml = Boolean(yaml);
  if (!yaml) {
    warnings.push('YAML frontmatter not detected; running content-only compression checks');
  }

  // Rule 1: Description length
  const description = hasYaml ? (yaml.description || '') : '';
  if (description.length > RULES.description_max_chars) {
    warnings.push(
      `Description too long: ${description.length}/${RULES.description_max_chars} chars. ` +
      `Suggestion: Use 1-liner + detailed content in resources/`
    );
  }

  // Rule 2: Check for verbose sections
  const sections = content.split('\n## ');
  sections.forEach((section, idx) => {
    const lines = section.split('\n');
    if (lines.length > 50) {
      warnings.push(
        `Section ${idx + 1} is verbose (${lines.length} lines). ` +
        `Consider moving to resources/ directory.`
      );
    }
  });

  // Rule 3: Check code snippets
  const codeBlocks = content.match(/```[\s\S]*?```/g) || [];
  codeBlocks.forEach((block, idx) => {
    const lines = block.split('\n').length;
    if (lines > RULES.code_snippet_max_lines) {
      warnings.push(
        `Code block ${idx + 1} is long: ${lines} lines (max: ${RULES.code_snippet_max_lines}). ` +
        `Suggestion: Show first 20 lines + reference full file.`
      );
    }
  });

  // Rule 4: Check for nested depth
  const nestedPatterns = content.match(/^#{4,}/gm) || [];
  if (nestedPatterns.length > 0) {
    warnings.push(
      `Found ${nestedPatterns.length} level-4+ headings. ` +
      `Max recommended: level 3. Flatten structure.`
    );
  }

  // Rule 5: Check for long bullets
  const bullets = content.match(/^\s*[-*]\s+.+$/gm) || [];
  bullets.forEach((bullet, idx) => {
    const text = bullet.replace(/^\s*[-*]\s+/, '');
    if (text.length > RULES.warnings.long_bullet) {
      warnings.push(
        `Bullet ${idx + 1} too verbose: ${text.length} chars. ` +
        `Keep bullets concise.`
      );
    }
  });

  return {
    valid: errors.length === 0,
    errors,
    warnings,
    info: {
      name: hasYaml ? yaml.name : path.basename(path.dirname(skillPath)),
      description_chars: description.length,
      sections: sections.length - 1,
      code_blocks: codeBlocks.length,
      file_lines: content.split('\n').length
    }
  };
}

function formatResult(skillName, result) {
  const status = result.valid ? '✅' : '❌';
  
  console.log(`\n${status} ${skillName}`);
  
  if (result.errors.length > 0) {
    console.log(`   ERRORS:`);
    result.errors.forEach(err => console.log(`     • ${err}`));
  }

  if (result.warnings.length > 0) {
    console.log(`   WARNINGS (${result.warnings.length}):`);
    result.warnings.forEach(warn => console.log(`     ⚠️  ${warn}`));
  }

  if (result.info) {
    console.log(`   INFO:`);
    console.log(`     • Description: ${result.info.description_chars}/${RULES.description_max_chars} chars`);
    console.log(`     • Sections: ${result.info.sections}`);
    console.log(`     • Code blocks: ${result.info.code_blocks}`);
    console.log(`     • Lines: ${result.info.file_lines}`);
  }
}

function validateAll() {
  const projectRoot = path.join(__dirname, '..');
  const skillsDir = path.join(projectRoot, 'skills');

  if (!fs.existsSync(skillsDir)) {
    console.error(`❌ Skills directory not found: ${skillsDir}`);
    process.exit(1);
  }

  const skills = fs.readdirSync(skillsDir)
    .filter(f => fs.statSync(path.join(skillsDir, f)).isDirectory());

  console.log(`\n🔍 Validating ${skills.length} skills against compression rules...\n`);

  let validCount = 0;
  let warningCount = 0;
  let errorCount = 0;
  const results = [];

  for (const skill of skills) {
    const skillPath = path.join(skillsDir, skill, 'SKILL.md');
    const result = validateSkill(skillPath);
    
    formatResult(skill, result);
    
    if (result.valid) validCount++;
    if (result.errors.length > 0) errorCount++;
    if (result.warnings.length > 0) warningCount++;

    results.push({ skill, result });
  }

  // Summary
  console.log(`\n${'='.repeat(60)}`);
  console.log(`📊 Summary:`);
  console.log(`   Valid: ${validCount}/${skills.length}`);
  console.log(`   Warnings: ${warningCount}`);
  console.log(`   Errors: ${errorCount}`);

  if (errorCount === 0 && warningCount === 0) {
    console.log(`\n   ✅ All skills pass validation!`);
  } else if (errorCount === 0) {
    console.log(`\n   ⚠️  All skills are valid, but ${warningCount} have optimization suggestions.`);
  } else {
    console.log(`\n   ❌ ${errorCount} skill(s) have errors. See above for details.`);
  }

  process.exit(errorCount > 0 ? 1 : 0);
}

function validateSpecific(skillName) {
  const projectRoot = path.join(__dirname, '..');
  const skillPath = path.join(projectRoot, 'skills', skillName, 'SKILL.md');
  
  const result = validateSkill(skillPath);
  formatResult(skillName, result);

  process.exit(result.valid ? 0 : 1);
}

// Main
const skillArg = process.argv[2];

if (skillArg) {
  validateSpecific(skillArg);
} else {
  validateAll();
}
