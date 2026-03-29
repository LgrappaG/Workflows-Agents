---
name: testing-integration-test-framework
description: Build framework for multi-component integration testing
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Save/load system verification, networked gameplay scenarios, audio trigger sequences, physics-based puzzle dependencies, cross-scene state transitions, UI/input/animation chains
avoid: Over-mocking (defeats integration testing purpose), circular dependency chains not caught by tests, missing async coordination (race conditions), insufficient timeout handling, coupling tests to UI layer directly
mandates: Integrate 12+ subsystem combinations. Execution time <10min for full suite. 100% API contract verification. Coverage of 80%+ code paths. Document all integration seams.
response: Design integration test architecture using dependency injection to mock 30% of external, Implement subsystem harness that validates handshake protocols (e, g, , save system → serialization → storage backend) with timeout guards (5sec
---

# Testing Integration Test Framework

Build framework for multi-component integration testing

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
- Component interaction testing
- Development workflows

## What NOT to Do
- Test brittleness
- Incomplete testing
- Deploy without validation
