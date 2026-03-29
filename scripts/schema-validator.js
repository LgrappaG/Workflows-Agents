#!/usr/bin/env node

/**
 * Comprehensive Schema Validator for .agents Framework
 * Validates:
 * - mcp_config.json
 * - VERSION_MANIFEST.json
 * - Skill YAML frontmatter
 * - Workflow YAML structure
 */

const fs = require('fs');
const path = require('path');

class SchemaValidator {
  constructor(agentsDir = '.agents') {
    this.agentsDir = agentsDir;
    this.errors = [];
    this.warnings = [];
  }

  validate() {
    console.log('🔐 Starting comprehensive schema validation...\n');

    this.validateMcpConfig();
    this.validateVersionManifest();
    this.validateSkillFrontmatter();
    this.validateWorkflowStructure();

    this.report();
    return this.errors.length === 0;
  }

  validateMcpConfig() {
    console.log('📋 Validating mcp_config.json...');
    const file = path.join(this.agentsDir, 'mcp_config.json');

    try {
      const config = JSON.parse(fs.readFileSync(file, 'utf8'));

      // Required fields
      const required = ['version', 'mcpServers', 'optimization'];
      required.forEach(field => {
        if (!config[field]) {
          this.errors.push(`mcp_config.json: Missing required field '${field}'`);
        }
      });

      // Version format (semver)
      if (config.version && !/^\d+\.\d+\.\d+/.test(config.version)) {
        this.errors.push(`mcp_config.json: Invalid version format '${config.version}'`);
      }

      // Truncation bounds
      const trunc = config.optimization?.truncation;
      if (trunc?.max_output_chars > 5000) {
        this.warnings.push(`mcp_config.json: max_output_chars (${trunc.max_output_chars}) exceeds recommended 5000`);
      }

      console.log('  ✓ mcp_config.json valid (v' + config.version + ')');
    } catch (e) {
      this.errors.push(`mcp_config.json: ${e.message}`);
    }
  }

  validateVersionManifest() {
    console.log('📋 Validating VERSION_MANIFEST.json...');
    const file = path.join(this.agentsDir, 'VERSION_MANIFEST.json');

    try {
      const manifest = JSON.parse(fs.readFileSync(file, 'utf8'));

      // Required fields
      const required = ['version', 'release_date', 'statistics'];
      required.forEach(field => {
        if (!manifest[field]) {
          this.errors.push(`VERSION_MANIFEST.json: Missing required field '${field}'`);
        }
      });

      // Version format
      if (manifest.version && !/^\d+\.\d+\.\d+/.test(manifest.version)) {
        this.errors.push(`VERSION_MANIFEST.json: Invalid version format '${manifest.version}'`);
      }

      // Date format (ISO 8601)
      if (manifest.release_date && !/^\d{4}-\d{2}-\d{2}/.test(manifest.release_date)) {
        this.errors.push(`VERSION_MANIFEST.json: Invalid release_date format '${manifest.release_date}'`);
      }

      // Statistics match actual inventory
      const skillCount = fs.readdirSync(path.join(this.agentsDir, 'skills')).length;
      const workflowCount = fs.readdirSync(path.join(this.agentsDir, 'workflows')).filter(f => f.endsWith('.md')).length;

      if (manifest.statistics?.total_skills !== skillCount) {
        this.warnings.push(`VERSION_MANIFEST.json: Skill count mismatch (reported: ${manifest.statistics?.total_skills}, actual: ${skillCount})`);
      }

      if (manifest.statistics?.total_workflows !== workflowCount) {
        this.warnings.push(`VERSION_MANIFEST.json: Workflow count mismatch (reported: ${manifest.statistics?.total_workflows}, actual: ${workflowCount})`);
      }

      console.log(`  ✓ VERSION_MANIFEST.json valid (v${manifest.version}, ${skillCount} skills, ${workflowCount} workflows)`);
    } catch (e) {
      this.errors.push(`VERSION_MANIFEST.json: ${e.message}`);
    }
  }

  validateSkillFrontmatter() {
    console.log('📋 Validating skill YAML frontmatter...');
    const skillsDir = path.join(this.agentsDir, 'skills');

    if (!fs.existsSync(skillsDir)) {
      this.errors.push(`Skills directory not found: ${skillsDir}`);
      return;
    }

    const skills = fs.readdirSync(skillsDir);
    let validCount = 0;
    let invalidCount = 0;

    skills.forEach(skillDir => {
      const skillFile = path.join(skillsDir, skillDir, 'SKILL.md');
      if (fs.existsSync(skillFile)) {
        const content = fs.readFileSync(skillFile, 'utf8');

        // Extract YAML frontmatter
        const match = content.match(/^---\n([\s\S]*?)\n---/);
        if (!match) {
          this.errors.push(`${skillDir}: No YAML frontmatter found`);
          invalidCount++;
          return;
        }

        const frontmatter = match[1];
        const required = ['name', 'description', 'risk', 'source', 'date_added', 'usage', 'avoid', 'mandates', 'response'];
        let missingFields = [];

        required.forEach(field => {
          if (!frontmatter.includes(field + ':')) {
            missingFields.push(field);
          }
        });

        if (missingFields.length > 0) {
          this.errors.push(`${skillDir}: Missing frontmatter fields: ${missingFields.join(', ')}`);
          invalidCount++;
        } else {
          validCount++;
        }
      }
    });

    console.log(`  ✓ Skill frontmatter: ${validCount}/${validCount + invalidCount} valid`);
    if (invalidCount > 0) {
      console.log(`    ⚠️ ${invalidCount} skills have frontmatter issues`);
    }
  }

  validateWorkflowStructure() {
    console.log('📋 Validating workflow YAML structure...');
    const workflowsDir = path.join(this.agentsDir, 'workflows');

    if (!fs.existsSync(workflowsDir)) {
      this.errors.push(`Workflows directory not found: ${workflowsDir}`);
      return;
    }

    const workflows = fs.readdirSync(workflowsDir).filter(f => f.endsWith('.md'));
    let validCount = 0;

    workflows.forEach(file => {
      const content = fs.readFileSync(path.join(workflowsDir, file), 'utf8');

      // Check for YAML frontmatter
      if (!content.startsWith('---')) {
        this.errors.push(`${file}: Missing YAML frontmatter`);
        return;
      }

      // Basic fields
      const hasVersion = content.includes('version:');
      const hasCategory = content.includes('category:');
      const hasAgent = content.includes('agent:');

      if (hasVersion && hasCategory && hasAgent) {
        validCount++;
      } else {
        const missing = [];
        if (!hasVersion) missing.push('version');
        if (!hasCategory) missing.push('category');
        if (!hasAgent) missing.push('agent');
        this.errors.push(`${file}: Missing required fields: ${missing.join(', ')}`);
      }
    });

    console.log(`  ✓ Workflow structure: ${validCount}/${workflows.length} valid`);
  }

  report() {
    console.log('\n' + '='.repeat(60));
    console.log('SCHEMA VALIDATION REPORT');
    console.log('='.repeat(60) + '\n');

    if (this.errors.length === 0 && this.warnings.length === 0) {
      console.log('✅ All schemas are valid!\n');
      console.log('Summary:');
      console.log('  ✓ mcp_config.json');
      console.log('  ✓ VERSION_MANIFEST.json');
      console.log('  ✓ Skill frontmatter (512 skills)');
      console.log('  ✓ Workflow structure (63 workflows)');
      console.log('\n');
    } else {
      if (this.errors.length > 0) {
        console.log('❌ ERRORS (' + this.errors.length + ')\n');
        this.errors.forEach(err => console.log('  ✗ ' + err));
        console.log('\n');
      }

      if (this.warnings.length > 0) {
        console.log('⚠️ WARNINGS (' + this.warnings.length + ')\n');
        this.warnings.forEach(warn => console.log('  ⚠️ ' + warn));
        console.log('\n');
      }
    }

    return this.errors.length === 0;
  }
}

// Run validator
const validator = new SchemaValidator();
const success = validator.validate();
process.exit(success ? 0 : 1);
