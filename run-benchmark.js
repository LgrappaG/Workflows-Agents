#!/usr/bin/env node

/**
 * Direct benchmark runner
 */

const fs = require('fs');
const path = require('path');

// Approximate token counter (based on Claude tokenizer rules)
function estimateTokens(text) {
  const cleaned = text
    .replace(/#+\s/g, '')
    .replace(/\*\*/g, '')
    .replace(/\[.*?\]\(.*?\)/g, '')
    .replace(/```[\s\S]*?```/g, '')
    .trim();

  const charCount = cleaned.length;
  const wordCount = cleaned.split(/\s+/).length;
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

// Benchmark function
function benchmark() {
  const projectRoot = __dirname;
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
  console.log('\n✅ Benchmark complete!\n');
}

benchmark();
