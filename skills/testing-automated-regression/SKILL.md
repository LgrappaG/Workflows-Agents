---
name: testing-automated-regression
description: Automate regression testing to catch regressions early
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Daily CI/CD validation, pre-release gate verification, engine upgrade validation, platform port certification, critical hotfix deployment
avoid: Ignoring flaky tests (leads to 'cry wolf'), non-deterministic test order execution, insufficient test isolation, missing platform-specific coverage, tests running >30min without parallelization
mandates: Maintain 95%+ test pass rate. Execute full regression suite <15min. Detect 100% of critical bug regressions. Flakiness rate <3%. Cover all platform-specific code paths.
response: Establish baseline regression suite by instrumenting all critical gameplay systems (player controller,, Configure CI/CD pipeline to run regression tests on every commit with platform, Implement flaky test detector that runs each test 5x in isolation; quarantine, Document regression coverage report monthly showing pass rate %, affected systems, and
---

# Testing Automated Regression

Automate regression testing to catch regressions early

## Risk Level
**MEDIUM**

## Core Rules
- Implement properly
- Test thoroughly
- Validate results

## Response Pattern

1. Design appropriate approach
2. Implement solution
3. Test edge cases
4. Validate quality

## Usage Contexts
- Regression prevention
- Development workflows

## What NOT to Do
- Flaky tests
- Incomplete testing
- Deploy without validation
