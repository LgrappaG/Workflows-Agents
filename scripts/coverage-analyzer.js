#!/usr/bin/env node

/**
 * Skill Coverage Analyzer for .agents Framework
 * Analyzes which skills are used in which workflows
 * Identifies under-utilized and over-utilized skills
 */

const fs = require('fs');
const path = require('path');

class CoverageAnalyzer {
  constructor(agentsDir = path.join(__dirname, '..')) {
    this.agentsDir = agentsDir;
    this.skillUsage = {};
    this.workflowCount = 0;
  }

  analyze() {
    console.log('📊 Starting skill coverage analysis...\n');

    this.buildSkillUsageMap();
    this.report();
  }

  buildSkillUsageMap() {
    console.log('Scanning workflows for skill references...');

    const skillsDir = path.join(this.agentsDir, 'skills');
    const workflowsDir = path.join(this.agentsDir, 'workflows');

    // Initialize all skills with 0 usage
    fs.readdirSync(skillsDir).forEach(skillDir => {
      this.skillUsage[skillDir] = {
        skill: skillDir,
        usageCount: 0,
        workflows: [],
        category: skillDir.split('-')[0]
      };
    });

    // Check each workflow for skill references
    fs.readdirSync(workflowsDir).filter(f => f.endsWith('.md')).forEach(workflow => {
      this.workflowCount++;
      const content = fs.readFileSync(path.join(workflowsDir, workflow), 'utf8');

      // Extract YAML frontmatter
      const match = content.match(/^---\n([\s\S]*?)\n---/);
      if (!match) return;

      const frontmatter = match[1];

      // Parse skills arrays (required, recommended, optional)
      const skillArrays = ['required', 'recommended', 'optional'];
      skillArrays.forEach(type => {
        const pattern = new RegExp(`${type}:\\s*\\[(.*?)\\]`, 's');
        const arrayMatch = frontmatter.match(pattern);
        if (arrayMatch) {
          const skills = arrayMatch[1]
            .split(',')
            .map(s => s.trim().replace(/['"`]/g, ''))
            .filter(s => s);

          skills.forEach(skillId => {
            if (this.skillUsage[skillId]) {
              this.skillUsage[skillId].usageCount++;
              this.skillUsage[skillId].workflows.push({
                workflow: workflow.replace('.md', ''),
                type: type
              });
            }
          });
        }
      });
    });
  }

  report() {
    console.log('\n' + '='.repeat(60));
    console.log('SKILL COVERAGE ANALYSIS REPORT');
    console.log('='.repeat(60) + '\n');

    // Sort by usage
    const skills = Object.values(this.skillUsage).sort((a, b) => b.usageCount - a.usageCount);

    // Statistics
    const totalSkills = skills.length;
    const usedSkills = skills.filter(s => s.usageCount > 0).length;
    const unusedSkills = totalSkills - usedSkills;

    console.log('OVERVIEW');
    console.log(`├── Total Skills: ${totalSkills}`);
    console.log(`├── Total Workflows: ${this.workflowCount}`);
    console.log(`├── Used Skills: ${usedSkills} (${Math.round(usedSkills/totalSkills*100)}%)`);
    console.log(`├── Unused Skills: ${unusedSkills} (${Math.round(unusedSkills/totalSkills*100)}%)`);
    console.log(`└── Avg Workflows per Skill: ${Math.round(usedSkills > 0 ? (this.workflowCount * 3) / usedSkills : 0)}`);
    console.log('\n');

    // Top 20 most used skills
    console.log('TOP 20 MOST USED SKILLS');
    skills
      .filter(s => s.usageCount > 0)
      .slice(0, 20)
      .forEach((skill, idx) => {
        const bar = '█'.repeat(Math.ceil(skill.usageCount / 2));
        console.log(`├── ${(idx + 1).toString().padStart(2, ' ')}. ${skill.skill.padEnd(35)} ${bar} ${skill.usageCount} workflows`);
      });
    console.log('\n');

    // Under-utilized skills (used in < 2 workflows)
    const underUtilized = skills.filter(s => s.usageCount > 0 && s.usageCount < 2);
    if (underUtilized.length > 0) {
      console.log(`⚠️ UNDER-UTILIZED SKILLS (used in <2 workflows) - ${underUtilized.length}`);
      underUtilized.slice(0, 15).forEach(skill => {
        console.log(`├── ${skill.skill.padEnd(35)} ${skill.usageCount} workflow(s)`);
      });
      if (underUtilized.length > 15) {
        console.log(`└── ... and ${underUtilized.length - 15} more`);
      }
      console.log('\n');
    }

    // Unused skills
    const unused = skills.filter(s => s.usageCount === 0);
    if (unused.length > 0) {
      console.log(`❌ UNUSED SKILLS - ${unused.length}`);
      unused.slice(0, 15).forEach(skill => {
        console.log(`├── ${skill.skill} [${skill.category}]`);
      });
      if (unused.length > 15) {
        console.log(`└── ... and ${unused.length - 15} more`);
      }
      console.log('\n');
    }

    // Domain coverage
    const byDomain = {};
    skills.forEach(skill => {
      if (!byDomain[skill.category]) {
        byDomain[skill.category] = { total: 0, used: 0, usage: 0 };
      }
      byDomain[skill.category].total++;
      if (skill.usageCount > 0) {
        byDomain[skill.category].used++;
        byDomain[skill.category].usage += skill.usageCount;
      }
    });

    console.log('DOMAIN COVERAGE');
    Object.entries(byDomain)
      .sort((a, b) => b[1].usage - a[1].usage)
      .forEach(([domain, stats]) => {
        const percentage = Math.round(stats.used / stats.total * 100);
        const bar = '█'.repeat(Math.ceil(percentage / 5));
        console.log(`├── ${domain.padEnd(20)} ${bar} ${stats.used}/${stats.total} (${percentage}%) - ${stats.usage} total uses`);
      });
    console.log('\n');

    // Save coverage report
    const report = {
      timestamp: new Date().toISOString(),
      totalSkills,
      usedSkills,
      unusedSkills,
      totalWorkflows: this.workflowCount,
      skillUsage: skills.map(s => ({
        skill: s.skill,
        usageCount: s.usageCount,
        category: s.category,
        workflows: s.workflows
      }))
    };

    const reportFile = path.join(this.agentsDir, 'reports/coverage/skill-usage-matrix.json');
    fs.mkdirSync(path.dirname(reportFile), { recursive: true });
    fs.writeFileSync(reportFile, JSON.stringify(report, null, 2));
    console.log(`✅ Coverage report saved to ${reportFile}`);
  }
}

// Run analyzer
const analyzer = new CoverageAnalyzer();
analyzer.analyze();
