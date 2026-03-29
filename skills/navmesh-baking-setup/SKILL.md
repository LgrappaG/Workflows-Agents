---
name: navmesh-baking-setup
description: Configure and bake navigation mesh for pathfinding
risk: low
source: workspace
date_added: '2026-03-21'
usage: Pathfinding setup, AI movement, navigation configuration
avoid: Incomplete baking, unreachable areas, incorrect settings
mandates: Validate bake results, test pathfinding, check coverage
response: Configure baking parameters, bake mesh, validate results
---
# Navmesh Baking Setup

Configure and bake navigation mesh for pathfinding

## Risk Level
**LOW**

## Core Rules
- Validate bake results
- test pathfinding
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Configure baking parameters
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Pathfinding setup
- AI movement

## What NOT to Do
- Incomplete baking
- unreachable areas
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
