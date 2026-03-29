# Utility Scripts Documentation

Helper scripts for .agents project analysis, validation, and optimization.

## Overview

Utility scripts automate metric calculation, validation, and report generation. All scripts are JavaScript-based and run with Node.js.

## Available Scripts

### 1. `measure-tokens.js` - Token Counting & Efficiency Analysis
**Purpose:** Calculate token count and compression ratios for skills

**Metrics Calculated:**
- Raw character count → estimated tokens (4 chars ≈ 1 token)
- YAML frontmatter tokens (9 fields)
- Markdown body tokens
- Total compression ratio vs raw markdown
- Per-skill efficiency scores

**Usage:**
```bash
node scripts/measure-tokens.js                    # Analyze all skills
node scripts/measure-tokens.js [skill-directory]  # Single skill analysis
```

**Output:**
- Token efficiency report (CSV format)
- Compression statistics (30-56% range target)
- Outliers (too large or too small)
- Framework-level metrics

**Example Output:**
```
Skill: animation-blending
Raw estimate: 450 tokens
Compressed: 270 tokens
Ratio: 60% compression
Category: Optimal
```

**Target:** All skills 40-60% compression (600-1200 bytes)

---

### 2. `schema-validator.js` - YAML Schema Validation
**Purpose:** Validate SKILL.md YAML against schema

**Validates:**
- YAML 1.1 syntax correctness
- Required 9 fields present
- Field data types (string fields required)
- Frontmatter delimiters (--- ... ---)
- Markdown structure consistency
- No duplicate keys

**Usage:**
```bash
node scripts/schema-validator.js                   # Validate all
node scripts/schema-validator.js [skill-name]     # Single skill
node scripts/schema-validator.js --strict         # Strict mode
```

**Output:**
- Schema compliance report
- Errors and warnings per skill
- Suggested fixes
- Summary statistics

**Exit Codes:**
- 0 = All valid
- 1 = Warnings found
- 2 = Critical errors

---

### 3. `validate-compression.js` - Compression Ratio Analysis
**Purpose:** Ensure skills meet token efficiency targets

**Checks:**
- File size within bounds (600-1200 bytes)
- Phase 5 enriched skills (<1500 bytes)
- Compression ratio 40-60%
- No redundant whitespace
- Abbreviation consistency

**Usage:**
```bash
node scripts/validate-compression.js
node scripts/validate-compression.js --phase 5   # Phase 5 limits
node scripts/validate-compression.js --report    # Detailed report
```

**Output:**
- Skills below target (<40% compression): List
- Skills above target: List with suggestions
- Phase 5 enriched breakdown
- Optimization recommendations

**Targets by Phase:**
- Phase 1-4: 40-60% compression, 600-1200 bytes
- Phase 5: 40-50% compression, <1500 bytes (enriched)

---

### 4. `coverage-analyzer.js` - Domain & Category Coverage
**Purpose:** Analyze skill distribution across domains and categories

**Metrics:**
- Skills per domain (approx 30-50 per domain)
- Gaps in domain coverage
- Risk level distribution (target: 40% low, 40% medium, 20% high)
- Naming pattern consistency
- Missing or redundant skills

**Usage:**
```bash
node scripts/coverage-analyzer.js
node scripts/coverage-analyzer.js --domains           # Domain breakdown
node scripts/coverage-analyzer.js --risk-distribution # Risk metrics
node scripts/coverage-analyzer.js --gaps              # Coverage gaps
```

**Output:**
- Domain statistics table
- Risk distribution visualization
- Coverage gap analysis
- Recommendations for balance

**Example Output:**
```
Domain: animation (42 skills)
Risk: 18 low (43%), 20 medium (48%), 4 high (9%)
Status: Balanced within domain

Domain: ui (35 skills)
Risk: 14 low (40%), 14 medium (40%), 7 high (20%)
Status: Well-balanced
```

---

### 5. `benchmark-aggregator.js` - Performance Metrics Aggregation
**Purpose:** Combine benchmark results from CI/CD runs

**Collects:**
- Build time benchmarks
- Skill validation timing
- Token efficiency metrics
- Compression ratio trends
- Historical performance data

**Usage:**
```bash
node scripts/benchmark-aggregator.js
node scripts/benchmark-aggregator.js --generate-report   # HTML report
node scripts/benchmark-aggregator.js --compare [v1] [v2] # Version compare
```

**Output:**
- Aggregated benchmark statistics
- Trend analysis (improving/degrading)
- Performance graphs (if HTML output)
- Historical comparison data

---

### 6. `dependency-mapper.js` - Skill Dependency Analysis
**Purpose:** Map skill prerequisites and workflows that use skills

**Generates:**
- Dependency graph (which skills referenced by workflows)
- Prerequisite chains
- Circular dependency detection
- Skills with no workflows using them
- Workflow completion graphs

**Usage:**
```bash
node scripts/dependency-mapper.js
node scripts/dependency-mapper.js --graph       # ASCII dependency graph
node scripts/dependency-mapper.js [skill-name]  # Single skill deps
node scripts/dependency-mapper.js --orphaned    # Skills with no workflows
```

**Output:**
- Dependency matrix (skills × workflows)
- Missing prerequisites list
- Orphaned skills
- Workflow dependency order

**Example Output:**
```
Skill: animation-blending
Workflows using: 3 (animation-pipeline, vr-controller-setup, ui-animation)
Prerequisites: animation-state-machine, unity-2d-expert
Prerequisite chain depth: 2
Status: Well-integrated
```

---

### 7. `generate-html-report.js` - Report Generation
**Purpose:** Generate comprehensive HTML reports for framework analysis

**Generates:**
- Skill inventory (all 587 skills with metadata)
- Workflow dependency diagrams
- Domain coverage charts
- Risk distribution visualizations
- Token efficiency graphs
- Validation coverage reports

**Usage:**
```bash
node scripts/generate-html-report.js                      # Full report
node scripts/generate-html-report.js --skills-only        # Skill inventory
node scripts/generate-html-report.js --workflows-only     # Workflow diagrams
node scripts/generate-html-report.js --output [path]      # Custom path
```

**Output:**
- `reports/skills-inventory.html` - All 587 skills with search
- `reports/workflow-diagram.html` - Interactive dependency graphs
- `reports/coverage-analysis.html` - Domain coverage charts
- `reports/framework-overview.html` - Comprehensive report

**Features:**
- Interactive drill-down
- Search/filter by domain, risk level, date added
- Sorting by skill name, size, compression
- Chart export (PNG/SVG)

---

## Automation Notes

### Pre-validation Pipeline (Git Pre-commit)

The scripts work together in pre-commit workflow:

```
1. schema-validator.js (YAML syntax)
   ↓
2. validate-compression.js (token efficiency)
   ↓
3. coverage-analyzer.js (warning if gaps detected)
   ↓
4. measure-tokens.js (optional detailed metrics)
   ↓
Commit allowed if: valid YAML + within compression targets
```

### CI/CD Integration

Scripts run in GitHub Actions:
- Every push: schema-validator.js + validate-compression.js
- Nightly: coverage-analyzer.js + benchmark-aggregator.js
- Weekly: generate-html-report.js (HTML reports)
- Monthly: dependency-mapper.js (orphaned skill check)

---

## Performance Characteristics

| Script | Execution Time | Input | Output |
|--------|---|--------|--------|
| measure-tokens.js | 5-15s | All 587 skills | CSV report |
| schema-validator.js | 8-20s | All YAML files | Validation errors |
| validate-compression.js | 3-10s | All skills | Compression matrix |
| coverage-analyzer.js | 2-5s | Skill names | Domain statistics |
| benchmark-aggregator.js | 10-30s | Benchmark files | Aggregated metrics |
| dependency-mapper.js | 15-45s | Skills + workflows | Dependency graph |
| generate-html-report.js | 30-60s | Full project | HTML files (5+ MB) |

**Total validation time:** <2 minutes for all scripts

---

## Common Usage Patterns

### Daily Development

```bash
# Before committing
node scripts/schema-validator.js [new-skill]
node scripts/validate-compression.js --report

# Quick check
node scripts/measure-tokens.js
```

### Weekly Review

```bash
# Coverage analysis
node scripts/coverage-analyzer.js

# Find orphaned skills
node scripts/dependency-mapper.js --orphaned
```

### Release Preparation

```bash
# Full validation
node scripts/schema-validator.js
node scripts/validate-compression.js
node scripts/coverage-analyzer.js

# Generate reports
node scripts/generate-html-report.js
node scripts/benchmark-aggregator.js --generate-report
```

---

## Integration with .agents Framework

These scripts support:
- ✅ 587 total skills validation
- ✅ 63 workflows dependency checking
- ✅ 50+ approved domains analysis
- ✅ 8-gate validation system
- ✅ Phase 5 enrichment (1500-byte limit)
- ✅ Token efficiency targets (40-60% compression)

**Framework Status:**
- Automation Coverage: 100%
- Validation Automation: Complete
- Reporting Automation: Complete
- Dependency Analysis: Complete

---

## Troubleshooting

### Node.js Not Found
```bash
# Install Node.js
# Windows: Download from nodejs.org
# macOS: brew install node
# Linux: apt-get install nodejs npm
```

### Script Permissions
```bash
# Ensure scripts are executable
chmod +x scripts/*.js

# Run with explicit node
node scripts/measure-tokens.js
```

### Memory Issues on Large Projects
```bash
# Increase Node memory limit
node --max-old-space-size=4096 scripts/generate-html-report.js
```

---

## Support & Documentation

For detailed documentation on each script:
- See inline comments in each script file
- Run scripts with `--help` flag
- Check CONTRIBUTING.md for framework guidelines

