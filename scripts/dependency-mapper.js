#!/usr/bin/env node

/**
 * Dependency Mapper for .agents Framework
 * Maps skill dependencies and detects circular references
 * Builds skill prerequisite chains
 */

const fs = require('fs');
const path = require('path');

class DependencyMapper {
  constructor(agentsDir = '.agents') {
    this.agentsDir = agentsDir;
    this.skills = {};
    this.dependencies = {};
    this.circularDeps = [];
    this.orphanedSkills = [];
  }

  map() {
    console.log('🔗 Building skill dependency map...\n');

    this.loadAllSkills();
    this.extractDependencies();
    this.detectCircularDependencies();
    this.report();
  }

  loadAllSkills() {
    console.log('Loading all skills...');

    const skillsDir = path.join(this.agentsDir, 'skills');
    fs.readdirSync(skillsDir).forEach(skillDir => {
      this.skills[skillDir] = {
        name: skillDir,
        prerequisites: [],
        dependents: [],
        level: 0
      };
      this.dependencies[skillDir] = [];
    });

    console.log(`  ✓ Loaded ${Object.keys(this.skills).length} skills`);
  }

  extractDependencies() {
    console.log('Extracting dependencies from workflows...');

    const workflowsDir = path.join(this.agentsDir, 'workflows');

    fs.readdirSync(workflowsDir).filter(f => f.endsWith('.md')).forEach(workflow => {
      const content = fs.readFileSync(path.join(workflowsDir, workflow), 'utf8');

      // Extract YAML frontmatter
      const match = content.match(/^---\n([\s\S]*?)\n---/);
      if (!match) return;

      const frontmatter = match[1];

      // Parse skills arrays
      ['required', 'recommended', 'optional'].forEach(type => {
        const pattern = new RegExp(`${type}:\\s*\\[(.*?)\\]`, 's');
        const arrayMatch = frontmatter.match(pattern);
        if (arrayMatch) {
          const skills = arrayMatch[1]
            .split(',')
            .map(s => s.trim().replace(/['"`]/g, ''))
            .filter(s => s);

          // Build dependency graph (skills in 'required' are prerequisites for 'recommended')
          if (type === 'required' && skills.length > 0) {
            const firstSkill = skills[0];
            if (this.skills[firstSkill]) {
              skills.slice(1).forEach(skillId => {
                if (this.skills[skillId]) {
                  this.dependencies[skillId].push(firstSkill);
                  this.skills[skillId].prerequisites.push(firstSkill);
                  this.skills[firstSkill].dependents.push(skillId);
                }
              });
            }
          }
        }
      });
    });

    console.log('  ✓ Dependencies extracted');
  }

  detectCircularDependencies() {
    console.log('Detecting circular dependencies...');

    const visited = new Set();
    const stack = new Set();

    const hasCycle = (skillId, stack, visited) => {
      visited.add(skillId);
      stack.add(skillId);

      (this.dependencies[skillId] || []).forEach(dep => {
        if (!visited.has(dep)) {
          if (hasCycle(dep, stack, visited)) {
            return true;
          }
        } else if (stack.has(dep)) {
          this.circularDeps.push({ from: skillId, to: dep });
          return true;
        }
      });

      stack.delete(skillId);
      return false;
    };

    Object.keys(this.skills).forEach(skillId => {
      if (!visited.has(skillId)) {
        hasCycle(skillId, new Set(), visited);
      }
    });

    console.log(`  ✓ Circular dependency check complete (${this.circularDeps.length} found)`);

    // Identify orphaned skills
    this.orphanedSkills = Object.values(this.skills)
      .filter(s => s.prerequisites.length === 0 && s.dependents.length === 0)
      .map(s => s.name);

    console.log(`  ✓ Identified ${this.orphanedSkills.length} orphaned skills`);
  }

  report() {
    console.log('\n' + '='.repeat(60));
    console.log('DEPENDENCY MAP REPORT');
    console.log('='.repeat(60) + '\n');

    // Circular dependencies
    if (this.circularDeps.length > 0) {
      console.log(`❌ CIRCULAR DEPENDENCIES (${this.circularDeps.length})`);
      this.circularDeps.forEach(dep => {
        console.log(`├── ${dep.from} ← → ${dep.to}`);
      });
      console.log('\n');
    } else {
      console.log('✅ No circular dependencies detected\n');
    }

    // Dependency chains
    console.log('TOP 10 DEPENDENCY CHAINS (by depth)');
    const chains = this.findDependencyChains();
    chains
      .sort((a, b) => b.chain.length - a.chain.length)
      .slice(0, 10)
      .forEach((item, idx) => {
        const chain = item.chain.join(' → ');
        console.log(`├── ${(idx + 1)}. ${chain} (depth: ${item.chain.length})`);
      });
    console.log('\n');

    // Skills with most dependencies
    console.log('TOP 10 MOST DEPENDED-ON SKILLS');
    Object.values(this.skills)
      .sort((a, b) => b.dependents.length - a.dependents.length)
      .slice(0, 10)
      .forEach((skill, idx) => {
        console.log(`├── ${(idx + 1).toString().padStart(2)}. ${skill.name.padEnd(35)} depended on by ${skill.dependents.length} skills`);
      });
    console.log('\n');

    // Orphaned skills
    if (this.orphanedSkills.length > 0) {
      console.log(`⚠️ ORPHANED SKILLS (${this.orphanedSkills.length}} - no workflow dependencies)`);
      this.orphanedSkills.slice(0, 15).forEach(skill => {
        console.log(`├── ${skill}`);
      });
      if (this.orphanedSkills.length > 15) {
        console.log(`└── ... and ${this.orphanedSkills.length - 15} more`);
      }
      console.log('\n');
    } else {
      console.log('✅ No orphaned skills\n');
    }

    console.log('✅ Dependency mapping complete!');
  }

  findDependencyChains() {
    const chains = [];

    const buildChain = (skillId, chain = []) => {
      const updated = [...chain, skillId];
      if (updated.length > 1) {
        chains.push({ chain: updated });
      }
      (this.dependencies[skillId] || []).forEach(dep => {
        if (!updated.includes(dep)) { // Prevent cycles
          buildChain(dep, updated);
        }
      });
    };

    Object.keys(this.skills).forEach(skillId => {
      buildChain(skillId);
    });

    return chains;
  }
}

// Run mapper
const mapper = new DependencyMapper();
mapper.map();
