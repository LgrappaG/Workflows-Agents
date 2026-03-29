---
name: timeline-data-persistence
description: Persist and load timeline state for save/load functionality
risk: medium
source: workspace
date_added: '2026-03-21'
usage: Save systems, state management, data persistence
avoid: Data corruption, state inconsistency, loading errors
mandates: Validate saved data, test loading, handle version compatibility
response: Implement save/load system, test data integrity, validate restoration
---
# Timeline Data Persistence

Persist and load timeline state for save/load functionality

## Risk Level
**MEDIUM**

## Core Rules
- Validate saved data
- test loading
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement save/load system
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Save systems
- state management

## What NOT to Do
- Data corruption
- state inconsistency
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
