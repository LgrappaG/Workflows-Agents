# INTEGRATION_GUIDE.md - How to Use .agents Framework Features

**Version**: 9.0.1
**Date**: 2026-03-21
**Purpose**: Comprehensive guide to integrating and using all .agents framework features

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Core Systems](#core-systems)
3. [Using Skills](#using-skills)
4. [Running Workflows](#running-workflows)
5. [Agent Assignment](#agent-assignment)
6. [Validation & Quality](#validation--quality)
7. [Advanced Integration](#advanced-integration)
8. [API Reference](#api-reference)
9. [Common Patterns](#common-patterns)
10. [Best Practices](#best-practices)

---

## Quick Start

### 1. Initialize Your Project

```bash
# Run the project initialization workflow
agents init my-game-project --template unity-3d

# This will:
# - Create project structure
# - Initialize git repository
# - Set up hooks and validation
# - Configure development environment
```

### 2. Explore Available Skills

```bash
# List all 512 skills
agents skills list

# Filter by domain
agents skills list --domain physics
agents skills list --domain ui --search "animation"

# View skill details
agents skill info physics-joint-constraints
```

### 3. Create Your First Workflow

```bash
# List available workflows
agents workflow list

# View workflow details
agents workflow info unity-3d-setup

# Run a workflow interactively
agents workflow run unity-3d-setup
```

### 4. Get Expert Guidance

```bash
# Invoke a specific agent for consultation
agents agent invoke "Unity Architect" --task "setup-3d-project"

# Get recommendations from hierarchy
agents agent recommend --for "performance optimization"

# List all agents
agents agent list --hierarchy
```

---

## Core Systems

### System 1: Skill System (512 Skills)

**What**: Discrete, reusable units of expertise
**Who**: Every skill is mapped to agent specialists
**How**: Skills are organized in 4 phases by domain and complexity

#### Skill Structure

```
Skill Name: physics-joint-constraints
├─ Description: Configure joint constraints for realistic physics
├─ Domain: physics
├─ Complexity: medium
├─ Risk Level: low
├─ Prerequisite Skills: [physics-setup, rigidbody-basics]
├─ Usage Contexts: VR, physics-heavy games, ragdoll systems
├─ Mandates: [Test on target platforms, Validate performance impact]
└─ Response: [Configure constraints, Validate through testing, Optimize if needed]
```

#### Using Skills

```python
# Python API
from agents import SkillSystem

skills = SkillSystem()

# Get skill
skill = skills.get('physics-joint-constraints')

# Check prerequisites
prereqs = skill.get_prerequisites()

# Get skill difficulty
difficulty = skill.get_complexity()  # Returns 1-10

# Find related skills
related = skills.find_related('physics-joint-constraints')

# Validate skill application
is_applicable = skills.validate_for_context('vr-physics')
```

### System 2: Workflow System (63 Workflows)

**What**: Sequences of steps for specific development tasks
**Who**: Each workflow is guided by a primary agent
**How**: Workflows chain 3-5 core skills into actionable procedures

#### Workflow Structure

```yaml
version: 9.0.1
category: Performance
agent: Profiling Specialist
difficulty: intermediate
estimated_time: 2-3 hours

skills:
  required: [5 core skills]
  recommended: [10 additional skills]

validation_gates: 7
complexity_score: 8.3
skill_density: 0.87
integration_level: 0.92
```

#### Running Workflows

```bash
# Interactive workflow execution
agents workflow run shader-optimization-guide

# Workflow with parameters
agents workflow run unity-3d-setup \
  --target-platform webgl \
  --use-urp \
  --enable-vr-support

# Dry-run (preview steps without executing)
agents workflow run shader-optimization-guide --dry-run

# Generate workflow report
agents workflow analyze unity-performance-audit
```

### System 3: Agent Hierarchy (48 Agents)

**What**: Specialized AI consultants for different roles
**Who**: 48 agents organized in 4 tiers
**How**: Each agent has specific expertise and workflow assignments

#### Agent Hierarchy Tiers

```
Tier 1: Executive (1 Agent)
└─ Creative Director
   Approves major decisions, sets vision

Tier 2: Department Heads (3 Agents)
├─ Tech Lead
│  Architecture, performance, technology decisions
├─ Production Lead
│  Timeline, scope, risk management
└─ Quality Lead
   Testing, standards, compliance

Tier 3: Specialists (44 Agents)
├─ Core Development (8)
├─ Graphics & Visuals (8)
├─ Audio & Narrative (5)
├─ AI & Gameplay (6)
├─ Tools & Pipeline (6)
├─ Testing & Quality (5)
└─ Content & Design (7)
```

#### Working with Agents

```bash
# Get agent specialization
agents agent info "Unity Architect"

# Get agent recommendations
agents agent recommend \
  --agent "Tech Lead" \
  --problem "performance bottleneck"

# List agents by specialization
agents agent list --specialization "graphics"

# Get workflow assignments for agent
agents agent workflows "Profiling Specialist"

# Create agent consultation request
agents agent consult "Security Specialist" \
  --issue "encryption setup" \
  --priority high
```

### System 4: Validation System (8 Gates)

**What**: Automated quality assurance for skills and workflows
**Who**: Used by QA system and pre-commit hooks
**How**: Each gate checks specific quality criteria

#### The 8 Validation Gates

| Gate | Checks | Automation |
|------|--------|-----------|
| Gate 1 | YAML Frontmatter | Auto-checked |
| Gate 2 | Naming Conventions | Auto-enforced |
| Gate 3 | Description Quality | Token analysis |
| Gate 4 | Risk Appropriateness | Pattern matching |
| Gate 5 | Mandate Clarity | Specificity scoring |
| Gate 6 | Response Actionability | Step validation |
| Gate 7 | Token Efficiency | Size analysis |
| Gate 8 | Cross-Skill Consistency | Dependency checking |

#### Using Validation

```bash
# Validate a skill
agents validate skill physics-joint-constraints

# Validate a workflow
agents validate workflow unity-3d-setup

# Run comprehensive validation
agents validate all --full-report

# Run QA pipeline (Python)
python3 qa_polish_phase4.py

# Check git pre-commit hooks
./hooks/pre-commit-skills.py
```

---

## Using Skills

### Skill Discovery

```bash
# Find skills by domain
agents skills list --domain animation
agents skills list --domain networking

# Find skills by complexity
agents skills list --min-complexity 7 --max-complexity 10

# Find skills by risk level
agents skills list --risk high
agents skills list --risk low

# Full-text search
agents skills search "particle system"
agents skills search "optimization"

# Find prerequisites for a skill
agents skill prerequisites physics-ragdoll-physics

# Find dependents (skills that require this one)
agents skill dependents ui-button-events
```

### Skill Application

```python
# Check if a skill applies to your context
from agents import SkillSystem, Context

context = Context(
    platform='mobile',
    engine='unity',
    target_audience='vr',
    performance_critical=True
)

skills = SkillSystem()
applicable = skills.filter_by_context(context)

# Get skills for a specific task
audio_setup = skills.get_for_task('audio-system-setup')

# Get progression path
beginner_to_advanced = skills.get_progression_path(
    starting_skill='ui-button-events',
    target_complexity=9
)
```

### Skill Combination

```bash
# Get recommended skill combinations
agents skills combine --for "multiplayer-setup"

# Get skill chain for progression
agents skills chain \
  --start material-pbr-setup \
  --end advanced-shader-optimization

# Analyze skill dependencies
agents skills graph --export-graphml dependencies.graphml
```

---

## Running Workflows

### Basic Workflow Execution

```bash
# List all workflows
agents workflow list

# View workflow details
agents workflow info unity-3d-setup

# Run workflow step-by-step
agents workflow run unity-3d-setup --interactive

# Auto-run workflow (non-interactive)
agents workflow run unity-3d-setup --batch
```

### Workflow Customization

```bash
# Run with custom parameters
agents workflow run mobile-optimization-audit \
  --target-platform android \
  --memory-limit 2gb \
  --profiling-detail comprehensive

# Skip certain steps
agents workflow run unity-performance-audit \
  --skip "generate-report"

# Only run specific steps
agents workflow run unity-3d-setup \
  --only "install-dependencies,configure-project"
```

### Workflow Analysis

```bash
# Analyze workflow dependencies
agents workflow analyze unity-3d-setup

# Generate workflow report
agents workflow report unity-performance-audit --format pdf

# Compare workflows
agents workflow compare unity-2d-setup unity-3d-setup

# Show workflow metrics
agents workflow metrics code-review-swarm
```

---

## Agent Assignment

### Working with Assigned Agents

Each workflow has a primary and secondary agent assignment:

```bash
# Get primary agent for workflow
agents workflow agent unity-3d-setup
# Returns: "Unity Architect"

# Get secondary agents
agents workflow secondary-agents code-review-swarm
# Returns: ["Code Reviewer", "Csharp Master", ...]

# Consult assigned agent
agents agent consult "Unity Architect" \
  --workflow unity-3d-setup \
  --question "best practices for project structure"
```

### Custom Agent Assignment

```bash
# Reassign agent to workflow
agents workflow assign code-review-swarm \
  --agent "Tech Lead" \
  --mode primary

# Get recommendation for agent
agents agent recommend \
  --for "performance-critical-task" \
  --show-alternatives

# Create team for workflow
agents workflow team build \
  --workflow shader-optimization-guide \
  --primary "Graphics Specialist" \
  --secondary ["Shader Optimizer", "Performance Profiler"]
```

---

## Validation & Quality

### Pre-Commit Validation

```bash
# Automatically run on git commit
git add my-skill.md
git commit -m "Add new shader optimization skill"
# Runs: pre-commit-skills.py (validates frontmatter, naming)

# Manual pre-commit check
./hooks/pre-commit-skills.py

# Check workflow validation
./hooks/pre-commit-workflows.py

# Check commit message format
./hooks/pre-commit-message.py
```

### Quality Scoring

```bash
# Check quality score for skill
agents validate skill my-skill --score

# Check quality score for workflow
agents validate workflow my-workflow --score

# Get detailed quality breakdown
agents validate all --detailed --score

# Export quality metrics
agents metrics export quality --format json
```

### Comprehensive QA

```bash
# Run full QA pipeline
python3 qa_polish_phase4.py

# Generate QA report
agents qa run --full --report QA_REPORT.md

# Analyze framework health
agents qa health-check

# Benchmark framework performance
agents qa benchmark --iterations 100
```

---

## Advanced Integration

### Phase 3 Integration Fields

All 63 workflows include advanced integration tracking:

```yaml
# Example: Advanced integration fields in workflow
validation_gates: 7          # Number of quality gates triggered
complexity_score: 8.3        # Task complexity 1-10
skill_density: 0.87          # Normalized skill requirement
integration_level: 0.92      # Workflow interconnection
agent_hierarchy:
  primary: "Profiling Specialist"
  secondary: ["Tech Lead", "Performance Optimizer"]
skill_prerequisites:
  - unity-project-setup
  - profiling-basics
  - performance-analysis
cross_workflow_dependencies:
  - depends_on: "unity-3d-setup"
  - enables: ["shader-optimization-guide", "memory-profiler-advanced"]
```

### Skill Prerequisite Mapping

```python
from agents import SkillGraph

graph = SkillGraph()

# Get skill prerequisites
prereqs = graph.get_prerequisites('physics-ragdoll-physics')
# Returns: [physics-setup, rigidbody-basics, animation-setup]

# Get recommended learning path
path = graph.get_learning_path(
    target_skill='reinforcement-learning',
    current_level='intermediate'
)

# Check if skills are compatible
compatible = graph.are_compatible(
    ['networking-setup', 'encryption-advanced'],
    context={'platform': 'mobile'}
)
```

### Cross-Workflow Dependencies

```bash
# Show workflow dependency graph
agents workflow deps --graph

# Find workflows that depend on workflow
agents workflow dependents unity-3d-setup

# Find workflows required before workflow
agents workflow prerequisites shader-optimization-guide

# Generate dependency report
agents workflow graph export \
  --format png \
  --include-metrics
```

---

## API Reference

### Command Line Interface

```bash
# Skill Management
agents skills list
agents skills search <query>
agents skill info <skill-name>
agents skill prerequisites <skill-name>
agents skills combine --for <task>

# Workflow Management
agents workflow list
agents workflow info <workflow-name>
agents workflow run <workflow-name> [options]
agents workflow analyze <workflow-name>

# Agent Management
agents agent list [--hierarchy]
agents agent info <agent-name>
agents agent recommend --for <task>
agents agent consult <agent-name> --issue <issue>

# Validation
agents validate skill <skill-name> [--score]
agents validate workflow <workflow-name> [--score]
agents validate all [--full-report]

# Metrics & Analysis
agents metrics export <metric-type> --format <format>
agents qa run [--full] [--report <filename>]
agents qa health-check
```

### Python API

```python
from agents import (
    SkillSystem,
    WorkflowSystem,
    AgentHierarchy,
    ValidationSystem,
    SkillGraph
)

# Initialize systems
skills = SkillSystem()
workflows = WorkflowSystem()
agents = AgentHierarchy()
validator = ValidationSystem()
graph = SkillGraph()

# Get skill
skill = skills.get('physics-joint-constraints')

# Get workflow
workflow = workflows.get('unity-3d-setup')

# Get agent
agent = agents.get('Tech Lead')

# Validate
results = validator.validate(skill)

# Query graph
prereqs = graph.get_prerequisites('reinforcement-learning')
```

---

## Common Patterns

### Pattern 1: Project Setup

```bash
# Initialize project
agents workflow run vibe-project-init

# Set up 3D graphics
agents workflow run unity-3d-setup --use-hdrp

# Configure physics
agents skill apply physics-setup
agents skill apply physics-joint-constraints

# Set up performance monitoring
agents workflow run unity-performance-audit --baseline
```

### Pattern 2: Performance Optimization

```bash
# Profile current performance
agents workflow run unity-profile-audit

# Identify bottlenecks
agents skill apply debug-performance-profiler

# Optimize graphics
agents workflow run shader-optimization-guide

# Optimize memory
agents workflow run memory-profiler-advanced

# Verify improvements
agents workflow run unity-performance-audit --compare
```

### Pattern 3: Multiplayer Implementation

```bash
# Set up networking
agents workflow run multiplayer-setup

# Configure backend
agents workflow run backend-setup

# Implement matchmaking
agents skill apply networking-matchmaking

# Add chat system
agents skill apply networking-chat-system

# Test network performance
agents skill apply networking-performance-monitoring
```

### Pattern 4: Mobile Deployment

```bash
# Set up mobile project
agents workflow run android-specific-setup

# Optimize for mobile
agents workflow run mobile-optimization-audit

# Test on devices
agents workflow run compatibility-testing

# Build and deploy
agents workflow run build-android-deployment
```

---

## Best Practices

### 1. Skill Application

- **Read the entire skill** before applying
- **Check prerequisites** for learning path
- **Validate context** (platform, engine, audience)
- **Test in isolation** before integrating
- **Document integration** for future reference

### 2. Workflow Execution

- **Review all steps** in interactive mode first
- **Backup project** before running optimization workflows
- **Run dry-run** for destructive operations
- **Follow estimated time** for planning
- **Document results** and metrics

### 3. Agent Consultation

- **Be specific** about your problem
- **Provide context** (platform, target, constraints)
- **Ask for alternatives** and trade-offs
- **Request documentation** for decisions made
- **Follow recommendations** with verification

### 4. Validation

- **Run validation** before committing
- **Address all errors** (0 tolerance)
- **Review warnings** and consider addressing
- **Use quality scores** to track improvements
- **Automate validation** with git hooks

### 5. Integration

- **Map dependencies** for your workflows
- **Plan skill progression** for team members
- **Track metrics** for each phase
- **Document decisions** in ADRs
- **Review quality** regularly

---

## Troubleshooting Integration

### Issue: Skill Not Found

```bash
# Check if skill exists
agents skills search <partial-name>

# List skills in domain
agents skills list --domain <domain>

# Check skill spelling
agents skill info <skill-name> --strict
```

### Issue: Workflow Fails

```bash
# Run in interactive mode to debug
agents workflow run <workflow> --interactive

# Check prerequisites
agents workflow prerequisites <workflow>

# View detailed error
agents workflow run <workflow> --debug --verbose

# Run individual steps
agents skill apply <required-skill>
```

### Issue: Validation Errors

```bash
# Get validation details
agents validate all --full-report

# Check specific gate
agents validate skill <skill> --gate 5

# Run QA with debug output
python3 qa_polish_phase4.py --debug
```

---

## Resources

- **Complete Reference**: See FRAMEWORK_COMPLETE.md
- **Troubleshooting**: See TROUBLESHOOTING.md
- **Validation Details**: See VALIDATION_HOOKS.md
- **QA Results**: See QA_FINAL_REPORT.md
- **Agent Roles**: See AGENT_HIERARCHY.md

---

**For further assistance, consult the relevant agent specialist through the hierarchy.**
