# Validation Hooks System: 8-Gate Quality Framework for .agents

**Framework**: .agents
**Version**: 1.0
**Date**: 2026-03-21
**Purpose**: Establish comprehensive quality gates for skill development and workflow management

---

## Executive Summary

The Validation Hooks System provides an 8-gate quality framework for maintaining excellence in the .agents framework. This system ensures that all skills, workflows, and documentation meet production standards before integration into the framework.

**Key Metrics**:
- 8 validation gates covering all aspects of quality
- 100% enforcement of standards
- Automated testing where possible
- Clear pass/fail criteria
- Integration with CI/CD pipeline

---

## System Architecture

```
┌─────────────────────────────────────────────┐
│  Pre-Commit Hook (pre-commit-skills.py)     │ ← Gate 1-2
├─────────────────────────────────────────────┤
│  Skill Validation Hook (validate-skill.py)  │ ← Gate 3-8
├─────────────────────────────────────────────┤
│  Workflow Validation (pre-commit-workflows) │ ← Gate 1-3
├─────────────────────────────────────────────┤
│  Documentation Hook (validate-docs.py)      │ ← Continuous
├─────────────────────────────────────────────┤
│  Commit Message Hook (pre-commit-message)   │ ← Gate 5
├─────────────────────────────────────────────┤
│  CI/CD Pipeline Integration                 │ ← Aggregation
└─────────────────────────────────────────────┘
```

---

## THE 8 VALIDATION GATES

### GATE 1: YAML Frontmatter Validation

**Purpose**: Ensure all required metadata is present and correctly formatted

**Checked Fields**:
- `name`: Skill name following pattern `{domain}-{specialty}`
- `description`: Concise description (< 100 characters)
- `risk`: One of [low, medium, high]
- `source`: Should be "workspace"
- `date_added`: Valid date format (YYYY-MM-DD)
- `usage`: Comma-separated usage contexts
- `avoid`: Comma-separated anti-patterns
- `mandates`: Comma-separated requirements
- `response`: Comma-separated response actions

**Pass Criteria**:
- All 9 fields present
- No empty values
- Valid formats for all fields
- Dates are valid ISO 8601 format

**Fail Criteria**:
- Missing any required field
- Empty or whitespace-only values
- Invalid format (e.g., invalid date)
- Invalid risk level

**Implementation**: `pre-commit-skills.py` - Gate 1

---

### GATE 2: Skill Naming Convention

**Purpose**: Ensure consistent and meaningful skill naming

**Naming Pattern**: `{domain}-{specialty}`

**Valid Domains**:
- animation, audio, ai, behavior, blueprint, build, ci-cd
- clustering, collision, component, compute, computer-vision
- console, constraint, cross-engine, custom, data, debug, decision
- deployment, dialogue, distribution, dynamic, edge, ensemble
- engine, feature, federated, fine-tuning, garbage-collection
- godot, graphics, gpu, hierarchy, hyperparameter, il, inference
- input, inspector, interpolation, ik, joint, language, layer
- level, lighting, localization, math, memory, mesh, ml, mobile
- model, motion, motor, movement, multiplayer, navigation, nlp
- node, networking, normalization, object, optimization, particle
- performance, physics, pipeline, plugin, pooling, prediction
- procedural, profiler, profiling, projection, property, rag, ray
- reflection, reinforcement, rendering, resource, response, rigging
- runtime, scripting, security, sensor, serialization, shader
- socket, sound, spatial, specialized, state, streaming, string
- structure, synchronization, system, task, telemetry, temporal
- terrain, testing, texture, thread, tile, time, tool, trace
- transfer, transform, transition, ui, unreal, validation, vfx
- vr, world, xr, and custom game-specific domains

**Naming Rules**:
- Lowercase only
- Hyphens separate domain and specialty (no underscores)
- Specialty is descriptive (e.g., "pbr-setup" not "pbr")
- No redundant domain naming (e.g., "animation-animator" should be "animation-master")

**Pass Criteria**:
- Follows `{domain}-{specialty}` pattern
- Valid domain from approved list
- Descriptive specialty name
- No redundancy

**Fail Criteria**:
- Doesn't match pattern
- Invalid domain
- Single-word name
- Ambiguous or unclear specialty

**Implementation**: `pre-commit-skills.py` - Gate 2

---

### GATE 3: Description Quality & Optimization

**Purpose**: Ensure descriptions are concise, clear, and optimized for token efficiency

**Requirements**:
- Length: 50-100 characters (optimal around 75)
- Must be action-oriented (verb-first)
- Must clearly describe the skill's purpose
- No filler words (the, and, etc. in opening)

**Examples**:
- ✓ "Configure physically-based rendering materials with proper workflow"
- ✗ "This skill is about configuring materials..." (too wordy, slow start)
- ✓ "Master particle system design for complex visual effects"
- ✗ "Particle systems are important..." (not action-oriented)

**Pass Criteria**:
- 50-100 characters
- Starts with verb or action word
- No filler or redundancy
- Clearly describes purpose

**Fail Criteria**:
- < 50 or > 100 characters
- Doesn't start with action
- Contains filler words
- Unclear purpose

**Implementation**: `validate-skill.py` - Gate 3

---

### GATE 4: Risk Level Appropriateness

**Purpose**: Ensure risk levels are correctly assigned and consistent

**Risk Definitions**:

**LOW RISK**:
- Simple, isolated functionality
- Well-established patterns
- Limited failure impact
- Example: "material-pbr-setup" (standard workflow)

**MEDIUM RISK**:
- Moderate complexity
- Some integration required
- Moderate failure impact
- Example: "physics-setup-advanced" (complex but bounded)

**HIGH RISK**:
- Complex systems integration
- Potential widespread impact
- Requires careful validation
- Example: "reinforcement-learning" (high complexity, validation needed)

**Consistency Rules**:
- Related skills have consistent risk levels
- Higher complexity = higher risk (generally)
- Integration complexity considered
- Validation requirements factored in

**Pass Criteria**:
- Risk level matches complexity
- Consistent with related skills
- Appropriate for typical use case

**Fail Criteria**:
- Risk level doesn't match complexity
- Inconsistent with related skills
- No justification for unusual risk

**Implementation**: `validate-skill.py` - Gate 4

---

### GATE 5: Mandates Clarity & Specificity

**Purpose**: Ensure mandates are actionable and specific

**Mandate Requirements**:
- Must be specific and measurable
- Must be directly actionable
- Should start with imperative verbs
- Minimum 3 mandates per skill

**Valid Mandates**:
- ✓ "Validate model accuracy with cross-validation"
- ✓ "Test on all target platforms before deployment"
- ✓ "Profile memory usage and optimize allocations"

**Invalid Mandates**:
- ✗ "Be careful" (not specific)
- ✗ "Test well" (not measurable)
- ✗ "Don't make mistakes" (not actionable)

**Mandate Categories**:
- Validation mandates (test, verify, validate)
- Performance mandates (profile, optimize, benchmark)
- Quality mandates (document, review, check)
- Compatibility mandates (test on platforms, ensure compatibility)

**Pass Criteria**:
- All mandates are specific
- Each is actionable
- Minimum 3 mandates
- Clear success criteria

**Fail Criteria**:
- Vague or unclear mandates
- Not directly actionable
- < 3 mandates
- No way to verify completion

**Implementation**: `validate-skill.py` - Gate 5

---

### GATE 6: Response Patterns Actionability

**Purpose**: Ensure response patterns are specific and achievable

**Response Pattern Requirements**:
- Must describe concrete steps
- Must be achievable in typical use
- Should have 3-4 distinct steps
- Each step must be observable/measurable

**Valid Response Pattern**:
```
Configure system, implement features, test functionality, validate results
```

**Invalid Response Patterns**:
```
Do the right thing
Handle all cases properly
Make it work
```

**Response Steps**:
1. Configuration or setup
2. Implementation or execution
3. Testing or validation
4. Verification or measurement

**Pass Criteria**:
- 3-4 concrete steps
- Each step is specific
- Steps are observable
- Logically sequenced

**Fail Criteria**:
- Vague or unclear steps
- < 3 or > 4 steps
- Steps not independently observable
- Illogical sequence

**Implementation**: `validate-skill.py` - Gate 6

---

### GATE 7: Token Efficiency & File Size

**Purpose**: Ensure skills are optimized for token usage

**Target Metrics**:
- SKILL.md file: < 1.2 KB (< 300 tokens)
- Description: < 100 characters (< 25 tokens)
- Total skill: 500-1000 tokens
- Framework efficiency: 512+ skills in < 512K tokens

**Optimization Guidelines**:
- Remove redundant descriptions
- Use concise mandate language
- Minimize markdown formatting
- Consolidate similar concepts
- Use abbreviations where standard (e.g., "API", "UI")

**Acceptable Size Range**:
- Minimum: 600 bytes (150 tokens)
- Optimal: 900 bytes (225 tokens)
- Maximum: 1200 bytes (300 tokens)

**Pass Criteria**:
- File size < 1.2 KB
- Content token estimate < 300
- No redundancy or filler
- Efficient use of space

**Fail Criteria**:
- File size > 1.2 KB
- Token estimate > 300
- Redundant content
- Inefficient formatting

**Implementation**: `validate-skill.py` - Gate 7

---

### GATE 8: Cross-Skill Consistency

**Purpose**: Ensure consistency across all skills in the framework

**Consistency Checks**:
- YAML format consistency
- Description style consistency
- Mandate structure consistency
- Response pattern consistency
- Risk level consistency within categories
- Terminology consistency

**Category-Level Checks**:
- Related skills have consistent naming
- Related skills have appropriate risk levels
- Related skills have complementary mandates
- Related skills don't have conflicting guidance

**Framework-Level Checks**:
- No duplicate skill names or purposes
- No conflicting risk assessments
- Consistent terminology throughout
- Consistent formatting and structure

**Pass Criteria**:
- Consistent with framework standards
- Compatible with existing skills
- No conflicts with related skills
- Follows established patterns

**Fail Criteria**:
- Inconsistent formatting
- Conflicting with related skills
- Terminology mismatches
- Breaking established patterns

**Implementation**: `validate-skill.py` - Gate 8

---

## HOOK IMPLEMENTATIONS

### Hook 1: pre-commit-skills.py

**Location**: `.agents/hooks/pre-commit-skills.py`

**Purpose**: Validate all .agents skills before commit

**Triggers On**: Changes to `.agents/skills/*/SKILL.md` files

**Function**:
- Validates YAML frontmatter (Gate 1-2)
- Checks skill naming conventions
- Validates required fields
- Reports violations with line numbers

**Usage**:
```bash
python .agents/hooks/pre-commit-skills.py
```

**Output**:
```
VALIDATING: animation-blend-trees/SKILL.md
  [✓] YAML frontmatter complete
  [✓] Naming convention valid
  [✓] Required fields present

  Status: PASS
```

**On Failure**:
```
VALIDATING: invalid-skill-name/SKILL.md
  [✗] Invalid skill name format: "invalid-skill-name" (should be {domain}-{specialty})
  [✗] Missing field: "response"

  Status: FAIL - 2 errors found
```

---

### Hook 2: validate-skill.py

**Location**: `.agents/hooks/validate-skill.py`

**Purpose**: Comprehensive skill validation across all 8 gates

**Triggers On**: New or modified `.agents/skills/*/SKILL.md` files

**Function**:
- Validates all 8 gates
- Generates detailed report
- Provides specific violation details
- Suggests corrections

**Usage**:
```bash
python .agents/hooks/validate-skill.py <skill-path>
```

**Output**:
```
COMPREHENSIVE SKILL VALIDATION
==============================

Skill: animation-blend-trees
Status: PASS (8/8 gates)

Gate 1: YAML Frontmatter             [✓] PASS
Gate 2: Naming Convention            [✓] PASS
Gate 3: Description Quality          [✓] PASS (87 chars)
Gate 4: Risk Level Appropriateness   [✓] PASS (medium - correct)
Gate 5: Mandates Clarity             [✓] PASS (3 mandates)
Gate 6: Response Patterns            [✓] PASS (4 steps)
Gate 7: Token Efficiency             [✓] PASS (948 bytes)
Gate 8: Cross-Skill Consistency      [✓] PASS

Quality Score: 100%
```

**On Failure**:
```
COMPREHENSIVE SKILL VALIDATION
==============================

Skill: invalid-skill/SKILL.md
Status: FAIL (2/8 gates)

Gate 1: YAML Frontmatter             [✗] FAIL
  Error: Missing required field "response"

Gate 3: Description Quality          [✗] FAIL
  Error: Description too long (145 chars, max 100)
  Suggestion: "Implement animation blending for smooth transitions" (49 chars)

Quality Score: 75%
```

---

### Hook 3: pre-commit-workflows.py

**Location**: `.agents/hooks/pre-commit-workflows.py`

**Purpose**: Validate workflow definitions and skills integration

**Triggers On**: Changes to `.agents/workflows/*.yaml` files

**Function**:
- Validates workflow structure
- Checks skill references
- Validates bash commands (Unix semantics)
- Verifies MCP server integration

**Validation Checks**:
- Workflow has 4-7 steps
- All bash commands use Unix syntax
- All skill references exist
- Error handling present
- MCP servers properly configured

**Usage**:
```bash
python .agents/hooks/pre-commit-workflows.py <workflow-file>
```

---

### Hook 4: validate-docs.md

**Location**: `.agents/hooks/validate-docs.md`

**Purpose**: Continuous documentation validation

**Checks**:
- Broken internal links
- Version consistency
- Markdown formatting
- Image reference validity
- Metadata completeness

---

### Hook 5: pre-commit-message.py

**Location**: `.agents/hooks/pre-commit-message.py`

**Purpose**: Validate commit messages

**Format Required**:
```
Type: Description (SCOPE)

Valid Types: [feat, fix, docs, refactor, perf, test, chore]
Scope: Phase, Category, or specific component
```

**Examples**:
- ✓ `feat: Add phase4-ml-skills (Machine Learning)`
- ✓ `fix: Correct risk level for edge-deployment (Phase 4)`
- ✓ `docs: Update AGENT_HIERARCHY.md (Documentation)`
- ✗ `Updated some skills` (no type/scope)
- ✗ `fix: (no description)`

---

## GIT HOOK INTEGRATION

### Installation

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
set -e

# Run skill validation
python .agents/hooks/pre-commit-skills.py || exit 1

# Run comprehensive validation on new/modified skills
git diff --cached --name-only --diff-filter=A,M | grep "\.agents/skills.*SKILL.md" | while read file; do
    python .agents/hooks/validate-skill.py "$file" || exit 1
done

# Run workflow validation
python .agents/hooks/pre-commit-workflows.py || exit 1

# Success
exit 0
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

### Installation

Create `.git/hooks/commit-msg`:
```bash
#!/bin/bash

# Validate commit message format
python .agents/hooks/pre-commit-message.py "$1" || exit 1

exit 0
```

Make executable:
```bash
chmod +x .git/hooks/commit-msg
```

---

## CI/CD PIPELINE INTEGRATION

### GitHub Actions Workflow

Create `.github/workflows/validate-skills.yml`:
```yaml
name: Skill Validation

on:
  pull_request:
    paths:
      - '.agents/skills/*/SKILL.md'
      - '.agents/workflows/*.yaml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Validate Skills
        run: |
          python .agents/hooks/pre-commit-skills.py

      - name: Comprehensive Validation
        run: |
          git diff --name-only origin/main...HEAD | grep "\.agents/skills.*SKILL.md" | while read file; do
              python .agents/hooks/validate-skill.py "$file"
          done

      - name: Validate Workflows
        run: |
          python .agents/hooks/pre-commit-workflows.py

      - name: Generate Report
        if: always()
        run: |
          python .agents/hooks/generate-validation-report.py

      - name: Upload Report
        if: always()
        uses: actions/upload-artifact@v2
        with:
          name: validation-report
          path: validation-report.txt
```

---

## QUALITY THRESHOLDS & PASS/FAIL CRITERIA

### Individual Skill Thresholds

| Gate | Pass Threshold | Fail Threshold |
|------|----------------|----|
| 1: YAML Frontmatter | 100% fields present | Any missing field |
| 2: Naming Convention | Valid pattern + domain | Invalid format |
| 3: Description Quality | 50-100 chars, action-oriented | <50 or >100 chars |
| 4: Risk Level | Appropriate for complexity | Mismatched complexity |
| 5: Mandates | 3+ specific, measurable | <3 or vague mandates |
| 6: Response Patterns | 3-4 concrete steps | Vague or illogical steps |
| 7: Token Efficiency | <1.2 KB file size | >1.2 KB file size |
| 8: Consistency | Matches framework patterns | Deviates from standards |

### Framework-Level Thresholds

- **Skill Validation Pass Rate**: 100% (all skills must pass all 8 gates)
- **Documentation Coverage**: 100% (all skills must be documented)
- **Link Integrity**: 100% (no broken internal/external links)
- **Consistency**: 100% (no conflicting guidance or terminology)

### Release Gate Criteria

Before releasing a new phase:
- [ ] All skills pass all 8 gates (100%)
- [ ] Cross-skill consistency verified
- [ ] Documentation complete and accurate
- [ ] No breaking changes to existing skills
- [ ] Version consistency across all files
- [ ] Performance benchmarks met (<512K tokens for 512+ skills)
- [ ] Integration testing passed
- [ ] Quality Lead approval obtained

---

## VIOLATION REPORTING

### Report Format

```
VALIDATION VIOLATION REPORT
===========================

Date: 2026-03-21 14:32:15
Phase: 4
Validator: validate-skill.py

VIOLATIONS SUMMARY
-------------------
Total Skills Checked: 62
Passed: 61 (98.4%)
Failed: 1 (1.6%)

FAILED SKILLS
--------------
1. machine-learning-setup
   Gate 5: Mandates Clarity - FAIL
     Issue: Mandates are not specific enough
     Details: "Validate datasets" should specify validation method
     Suggestion: "Validate datasets with cross-validation and integrity checks"

   Gate 7: Token Efficiency - WARNING
     Issue: File size approaching limit (1180 bytes, max 1200)
     Suggestion: Remove redundant descriptions or consolidate related mandates

RECOMMENDATIONS
-----------------
1. Update machine-learning-setup mandates for specificity
2. Consider splitting machine-learning-setup if too complex
3. Review all ML skills for mandate clarity

STATUS: PASS WITH WARNINGS
```

### Escalation Procedures

**Warning Level**:
- File size 90-100% of limit
- Mandates could be more specific
- Description could be more concise

**Action**: Notify author, suggest improvements, track trend

**Fail Level**:
- Missing required fields
- Invalid formats
- Inconsistent with standards
- >1.2 KB file size

**Action**: Block commit/PR, require fixes, escalate if needed

---

## AUTOMATION & TOOLING

### Automated Corrections

The validation system can automatically fix:
- Date formatting (convert to ISO 8601)
- Field ordering (arrange in standard order)
- Markdown formatting (normalize)
- Naming inconsistencies (suggest corrections)

### Dashboard & Monitoring

Create validation dashboard showing:
- Overall framework quality score
- Gate-by-gate pass rates
- Trend analysis (improvement/regression)
- Category-level quality metrics
- Time to resolution for violations

### Metrics to Track

```
Quality Metrics:
- YAML Completeness: 100%
- Description Quality: 98.5% (avg 75 chars)
- Mandate Specificity: 97.2%
- Token Efficiency: 99.1% (avg 920 bytes/skill)
- Cross-Skill Consistency: 100%
- Overall Quality Score: 98.8%

Performance Metrics:
- Validation Time: 12.4s for 512 skills
- False Positive Rate: 0%
- Auto-Fix Success Rate: 87%
```

---

## TROUBLESHOOTING COMMON VIOLATIONS

### Problem: Description Too Long

**Symptoms**: Gate 3 failure - description exceeds 100 characters

**Solution**:
1. Identify key concept
2. Remove articles (the, a, an)
3. Use verbs instead of nouns
4. Abbreviate where standard

**Example**:
- ✗ "The process of implementing machine learning model training systems with proper validation" (92 chars, > 100)
- ✓ "Implement ML model training with proper validation" (50 chars, optimal)

### Problem: Vague Mandates

**Symptoms**: Gate 5 failure - mandates are not specific

**Solution**:
1. Add measurement criteria
2. Specify tools or methods
3. Set clear success criteria

**Example**:
- ✗ "Validate models" (vague)
- ✓ "Cross-validate models with stratified K-fold and measure accuracy/precision/recall" (specific)

### Problem: Inconsistent Risk Level

**Symptoms**: Gate 4 failure - risk level doesn't match complexity

**Solution**:
1. Review related skills
2. Assess system integration impact
3. Consider validation requirements
4. Adjust risk level accordingly

### Problem: File Size Exceeds Limit

**Symptoms**: Gate 7 failure - skill.md > 1.2 KB

**Solution**:
1. Remove redundancy between fields
2. Consolidate similar mandates
3. Abbreviate where appropriate
4. Consider splitting into two skills

---

## EXTENDING THE VALIDATION SYSTEM

### Adding Custom Gates

1. Define gate logic and criteria
2. Implement validation function
3. Add to validation pipeline
4. Document in this guide
5. Update quality threshold table
6. Test thoroughly

### Custom Gate Template

```python
def validate_gate_n(skill: dict) -> tuple[bool, str]:
    """
    Validate Gate N: [Description]

    Args:
        skill: Parsed skill dictionary

    Returns:
        (pass: bool, message: str)
    """
    # Validation logic here

    if passes:
        return True, "Gate N: PASS"
    else:
        return False, f"Gate N: FAIL - {reason}"
```

---

## COMPLIANCE & CERTIFICATION

### Skill Certification Levels

**Tier 1: Validated** (Passes all 8 gates)
- Approved for immediate use
- Included in releases
- Full quality assurance

**Tier 2: Provisional** (Passes 7/8 gates with minor issues)
- Can be used with caveats
- Must be resolved before release
- Tracked for resolution

**Tier 3: Experimental** (Passes <7 gates)
- Not approved for use
- Requires significant work
- Must not be committed

### Certification Badge

```
[✓ VALIDATED] Framework: .agents
    Skill: animation-blend-trees
    Date: 2026-03-21
    Version: 1.0
    Quality: 100% (8/8 gates)
```

---

## VERSION CONTROL & HISTORY

### Validation History Tracking

Track validation results over time:
- Version history of each skill
- Violation trends
- Quality improvements/regressions
- Author-level metrics

### Rollback Procedures

If violations found after release:
1. Identify affected skills
2. Assess impact
3. Plan correction
4. Test thoroughly
5. Release patch
6. Document incident

---

## CONCLUSION

The Validation Hooks System provides comprehensive quality gates ensuring the .agents framework maintains the highest standards. With 8 validation gates, automated enforcement, CI/CD integration, and clear reporting, this system enables:

- **Quality Assurance**: Consistent, high-quality skills
- **Automation**: Reduced manual review burden
- **Scalability**: Handles 512+ skills efficiently
- **Compliance**: Maintains framework integrity
- **Improvement**: Tracks and trends quality metrics
- **Developer Experience**: Clear guidance and feedback

By implementing these validation hooks, the framework ensures sustainable growth while maintaining quality standards across all 512+ skills.

---

**Document Version**: 1.0
**Last Updated**: 2026-03-21
**Framework Version**: .agents 1.0 (512+ skills)

---

## Quick Reference

| Component | File | Purpose | Trigger |
|-----------|------|---------|---------|
| Pre-Commit Skills | `.agents/hooks/pre-commit-skills.py` | YAML & naming validation | Git pre-commit |
| Comprehensive Validation | `.agents/hooks/validate-skill.py` | All 8 gates | Manual/CI-CD |
| Workflow Validation | `.agents/hooks/pre-commit-workflows.py` | Workflow checks | Git pre-commit |
| Documentation Validation | `.agents/hooks/validate-docs.py` | Link/format checks | CI-CD |
| Commit Message Validation | `.agents/hooks/pre-commit-message.py` | Message format | Git commit-msg |
| CI/CD Integration | `.github/workflows/validate-skills.yml` | Automated validation | GitHub Actions |
| Reporting | `.agents/hooks/generate-validation-report.py` | Quality reporting | Manual/CI-CD |
