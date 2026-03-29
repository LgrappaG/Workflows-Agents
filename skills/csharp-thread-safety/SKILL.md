---
name: csharp-thread-safety
description: Ensure thread safety in concurrent systems
risk: high
source: workspace
date_added: '2026-03-21'
usage: Thread safety, concurrent access, data protection
avoid: Race conditions, data corruption, inconsistent state
mandates: Synchronize properly, use thread-safe collections, test thoroughly
response: Implement thread safety, test concurrency, validate consistency
---
# Csharp Thread Safety

Ensure thread safety in concurrent systems

## Risk Level
**HIGH**

## Core Rules
- Synchronize properly
- use thread-safe collections
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Implement thread safety
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Thread safety
- concurrent access

## What NOT to Do
- Race conditions
- data corruption
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
