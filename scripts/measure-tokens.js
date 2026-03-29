#!/usr/bin/env node

/**
 * Token Counter & Benchmark Tool for .agents Framework
 * 
 * Usage:
 *   node measure-tokens.js measure [file]    - Count tokens in a file
 *   node measure-tokens.js compare before after - Compare two files
 *   node measure-tokens.js benchmark - Run full benchmark suite
 */

const fs = require('fs');
const path = require('path');

// Approximate token counter (based on Claude tokenizer rules)
// 1 token ≈ 4 characters on average (varies by language)
function estimateTokens(text) {
  // Remove markdown formatting
  const cleaned = text
    .replace(/#+\s/g, '')
    .replace(/\*\*/g, '')
    .replace(/\[.*?\]\(.*?\)/g, '')
    .replace(/```[\s\S]*?```/g, '')
    .trim();

  // Rough token estimation: ~4 chars per token
  const charCount = cleaned.length;
  const wordCount = cleaned.split(/\s+/).length;
  
  // More accurate: use word count with multiplier
  // Average: 1.3 tokens per word (varies)
  const estimatedTokens = Math.ceil(wordCount * 1.3);
  
  return {
    characters: charCount,
    words: wordCount,
    estimated_tokens: estimatedTokens
  };
}

function formatNumber(num) {
  return new Intl.NumberFormat('en-US').format(num);
}

function calculateSavings(before, after) {
  const savedTokens = before - after;
  const percentage = ((savedTokens / before) * 100).toFixed(1);
  return {
    saved_tokens: savedTokens,
    percentage: percentage,
    ratio: `${before} → ${after}` 
  };
}

// Command: measure [file]
function measure(filePath) {
  if (!fs.existsSync(filePath)) {
    console.error(`❌ File not found: ${filePath}`);
    process.exit(1);
  }

  const content = fs.readFileSync(filePath, 'utf8');
  const stats = estimateTokens(content);

  console.log(`\n📊 Token Measurement: ${path.basename(filePath)}`);
  console.log(`   Characters: ${formatNumber(stats.characters)}`);
  console.log(`   Words: ${formatNumber(stats.words)}`);
  console.log(`   Estimated Tokens: ${formatNumber(stats.estimated_tokens)}`);
}

// Command: compare before after
function compare(beforePath, afterPath) {
  if (!fs.existsSync(beforePath) || !fs.existsSync(afterPath)) {
    console.error(`❌ File not found`);
    process.exit(1);
  }

  const beforeContent = fs.readFileSync(beforePath, 'utf8');
  const afterContent = fs.readFileSync(afterPath, 'utf8');

  const beforeStats = estimateTokens(beforeContent);
  const afterStats = estimateTokens(afterContent);
  const savings = calculateSavings(beforeStats.estimated_tokens, afterStats.estimated_tokens);

  console.log(`\n📊 Token Comparison`);
  console.log(`   Before: ${formatNumber(beforeStats.estimated_tokens)} tokens (${formatNumber(beforeStats.characters)} chars)`);
  console.log(`   After:  ${formatNumber(afterStats.estimated_tokens)} tokens (${formatNumber(afterStats.characters)} chars)`);
  console.log(`\n   ✅ Savings: ${formatNumber(savings.saved_tokens)} tokens (-${savings.percentage}%)`);
}

// Command: benchmark - Full suite
function benchmark() {
  const projectRoot = path.join(__dirname, '..');
  const skillsDir = path.join(projectRoot, 'skills');

  if (!fs.existsSync(skillsDir)) {
    console.error(`❌ Skills directory not found: ${skillsDir}`);
    process.exit(1);
  }

  const skills = fs.readdirSync(skillsDir)
    .filter(f => fs.statSync(path.join(skillsDir, f)).isDirectory());

  console.log(`\n🔍 Benchmarking ${skills.length} skills...`);

  let totalTokens = 0;
  const skillStats = [];

  for (const skill of skills) {
    const skillPath = path.join(skillsDir, skill, 'SKILL.md');
    if (fs.existsSync(skillPath)) {
      const content = fs.readFileSync(skillPath, 'utf8');
      const stats = estimateTokens(content);
      totalTokens += stats.estimated_tokens;
      skillStats.push({
        name: skill,
        tokens: stats.estimated_tokens,
        chars: stats.characters
      });
    }
  }

  // Sort by tokens descending
  skillStats.sort((a, b) => b.tokens - a.tokens);

  console.log(`\n📈 Per-Skill Breakdown (Top 10):`);
  console.log(`   ${'Skill Name'.padEnd(35)} ${'Tokens'.padStart(10)} ${'Chars'.padStart(10)}`);
  console.log(`   ${'-'.repeat(55)}`);
  skillStats.slice(0, 10).forEach(s => {
    console.log(`   ${s.name.padEnd(35)} ${formatNumber(s.tokens).padStart(10)} ${formatNumber(s.chars).padStart(10)}`);
  });

  console.log(`\n📊 Summary:`);
  console.log(`   Total Skills: ${skills.length}`);
  console.log(`   Total Tokens (all skills): ${formatNumber(totalTokens)}`);
  console.log(`   Average per Skill: ${Math.round(totalTokens / skills.length)} tokens`);
  console.log(`   Largest Skill: ${skillStats[0].name} (${formatNumber(skillStats[0].tokens)} tokens)`);
  console.log(`   Smallest Skill: ${skillStats[skillStats.length - 1].name} (${formatNumber(skillStats[skillStats.length - 1].tokens)} tokens)`);

  // Estimate with compression
  const estimatedCompression = 0.45; // 45% reduction
  const compressedTokens = Math.round(totalTokens * (1 - estimatedCompression));
  const savedTokens = totalTokens - compressedTokens;

  console.log(`\n🎯 With Compression (45% estimated):`);
  console.log(`   Compressed Total: ${formatNumber(compressedTokens)} tokens`);
  console.log(`   Potential Savings: ${formatNumber(savedTokens)} tokens (-${estimatedCompression * 100}%)`);
}

// Main
const command = process.argv[2];
const arg1 = process.argv[3];
const arg2 = process.argv[4];

switch (command) {
  case 'measure':
    if (!arg1) {
      console.error('Usage: measure-tokens.js measure <file>');
      process.exit(1);
    }
    measure(arg1);
    break;

  case 'compare':
    if (!arg1 || !arg2) {
      console.error('Usage: measure-tokens.js compare <before> <after>');
      process.exit(1);
    }
    compare(arg1, arg2);
    break;

  case 'benchmark':
    benchmark();
    break;

  default:
    console.log(`
🔧 Token Measurement Tool for .agents Framework

Usage:
  node measure-tokens.js measure <file>    - Count tokens in a file
  node measure-tokens.js compare <b> <a>   - Compare two files
  node measure-tokens.js benchmark         - Run full benchmark suite

Examples:
  node measure-tokens.js measure skills/csharp-master/SKILL.md
  node measure-tokens.js compare before.md after.md
  node measure-tokens.js benchmark
    `);
}
