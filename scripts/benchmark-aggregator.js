#!/usr/bin/env node

/**
 * Benchmark Aggregator for .agents Framework
 * Aggregates token metrics and compression data across all skills
 */

const fs = require('fs');
const path = require('path');

class BenchmarkAggregator {
  constructor(agentsDir = '.agents') {
    this.agentsDir = agentsDir;
    this.metrics = {
      timestamp: new Date().toISOString(),
      skills: [],
      totals: {
        totalTokens: 0,
        estimatedCompressed: 0,
        savings: 0,
        avgCompressionPercent: 0
      },
      distribution: {
        byDomain: {},
        bySize: { small: 0, medium: 0, large: 0, xlarge: 0 }
      }
    };
  }

  aggregate() {
    console.log('📊 Aggregating benchmark metrics...\n');

    this.collectTokenMetrics();
    this.calculateCompressionStats();
    this.report();
    this.save();
  }

  collectTokenMetrics() {
    console.log('Collecting token metrics from all skills...');

    const skillsDir = path.join(this.agentsDir, 'skills');
    const skills = fs.readdirSync(skillsDir);

    skills.forEach(skillDir => {
      const skillFile = path.join(skillsDir, skillDir, 'SKILL.md');
      if (!fs.existsSync(skillFile)) return;

      const content = fs.readFileSync(skillFile, 'utf8');
      const tokens = Math.ceil(content.length / 4); // Rough estimate

      const domain = skillDir.split('-')[0];

      this.metrics.skills.push({
        skill: skillDir,
        domain: domain,
        tokens: tokens,
        bytes: content.length,
        estimated_compressed: Math.ceil(tokens * 0.4), // 40% compression
        compression_ratio: 0.4
      });

      this.metrics.totals.totalTokens += tokens;

      // Distribution
      if (!this.metrics.distribution.byDomain[domain]) {
        this.metrics.distribution.byDomain[domain] = {
          count: 0,
          tokens: 0,
          compressed: 0
        };
      }
      this.metrics.distribution.byDomain[domain].count++;
      this.metrics.distribution.byDomain[domain].tokens += tokens;

      // Size categories
      if (tokens < 500) {
        this.metrics.distribution.bySize.small++;
      } else if (tokens < 1000) {
        this.metrics.distribution.bySize.medium++;
      } else if (tokens < 1500) {
        this.metrics.distribution.bySize.large++;
      } else {
        this.metrics.distribution.bySize.xlarge++;
      }
    });

    console.log(`  ✓ Collected metrics for ${this.metrics.skills.length} skills`);
  }

  calculateCompressionStats() {
    console.log('Calculating compression statistics...');

    // Compression estimation (40-60% average)
    const avgCompressionPercent = 50; // 50% average
    this.metrics.totals.estimatedCompressed = Math.ceil(this.metrics.totals.totalTokens * (1 - avgCompressionPercent / 100));
    this.metrics.totals.savings = this.metrics.totals.totalTokens - this.metrics.totals.estimatedCompressed;
    this.metrics.totals.avgCompressionPercent = avgCompressionPercent;

    // Per-domain compression
    Object.entries(this.metrics.distribution.byDomain).forEach(([domain, stats]) => {
      stats.compressed = Math.ceil(stats.tokens * 0.5); // 50% avg compression
    });

    console.log('  ✓ Compression statistics calculated');
  }

  report() {
    console.log('\n' + '='.repeat(60));
    console.log('BENCHMARK AGGREGATION REPORT');
    console.log('='.repeat(60) + '\n');

    const totals = this.metrics.totals;

    console.log('OVERALL METRICS');
    console.log(`├── Total Skills: ${this.metrics.skills.length}`);
    console.log(`├── Total Tokens (uncompressed): ${totals.totalTokens.toLocaleString()}`);
    console.log(`├── Estimated after compression: ${totals.estimatedCompressed.toLocaleString()}`);
    console.log(`├── Tokens saved: ${totals.savings.toLocaleString()} (-${totals.avgCompressionPercent}%)`);
    console.log(`└── Avg tokens per skill: ${Math.round(totals.totalTokens / this.metrics.skills.length)}`);
    console.log('\n');

    // Top 15 largest skills (optimization priority)
    console.log('TOP 15 LARGEST SKILLS (token optimization priority)');
    this.metrics.skills
      .sort((a, b) => b.tokens - a.tokens)
      .slice(0, 15)
      .forEach((skill, idx) => {
        const savings = skill.tokens - skill.estimated_compressed;
        console.log(`├── ${(idx + 1).toString().padStart(2)}. ${skill.skill.padEnd(35)} ${skill.tokens} → ${skill.estimated_compressed} tokens (save ${savings})`);
      });
    console.log('\n');

    // Distribution by domain
    console.log('DISTRIBUTION BY DOMAIN');
    Object.entries(this.metrics.distribution.byDomain)
      .sort((a, b) => b[1].tokens - a[1].tokens)
      .forEach(([domain, stats]) => {
        const bar = '█'.repeat(Math.ceil(stats.count / 5));
        console.log(`├── ${domain.padEnd(20)} ${bar} ${stats.count.toString().padStart(3)} skills | ${stats.tokens.toLocaleString()} → ${stats.compressed.toLocaleString()} tokens`);
      });
    console.log('\n');

    // Size distribution
    console.log('SIZE DISTRIBUTION');
    console.log(`├── Small (<500 tokens):     ${this.metrics.distribution.bySize.small.toString().padStart(3)} skills`);
    console.log(`├── Medium (500-1000 tokens): ${this.metrics.distribution.bySize.medium.toString().padStart(3)} skills`);
    console.log(`├── Large (1000-1500 tokens): ${this.metrics.distribution.bySize.large.toString().padStart(3)} skills`);
    console.log(`└── XLarge (>1500 tokens):    ${this.metrics.distribution.bySize.xlarge.toString().padStart(3)} skills`);
    console.log('\n');

    // Compression opportunities
    const xlarge = this.metrics.skills.filter(s => s.tokens > 1500);
    if (xlarge.length > 0) {
      console.log(`⚠️ COMPRESSION OPPORTUNITIES (${xlarge.length} skills > 1500 tokens)`);
      xlarge.forEach(skill => {
        const savings = skill.tokens - skill.estimated_compressed;
        console.log(`├── ${skill.skill.padEnd(35)} ${savings} tokens to save`);
      });
      console.log('\n');
    }

    console.log('✅ Benchmark aggregation complete!');
  }

  save() {
    const reportFile = path.join(this.agentsDir, 'reports/benchmarks/aggregated-metrics.json');
    fs.mkdirSync(path.dirname(reportFile), { recursive: true });
    fs.writeFileSync(reportFile, JSON.stringify(this.metrics, null, 2));
    console.log(`📊 Report saved to ${reportFile}`);
  }
}

// Run aggregator
const aggregator = new BenchmarkAggregator();
aggregator.aggregate();
