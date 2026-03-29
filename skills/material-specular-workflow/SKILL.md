---
name: material-specular-workflow
description: Use specular color maps instead of metallic for non-PBR workflows
risk: low
source: workspace
date_added: '2026-03-21'
usage: Legacy materials, specific workflows, custom rendering
avoid: Mixing with metallic workflow, incorrect specular values
mandates: Keep specular 0-1 range, test under various lighting, document workflow
response: Apply specular maps, configure values, validate appearance
---
# Material Specular Workflow

Use specular color maps instead of metallic for non-PBR workflows

## Risk Level
**LOW**

## Core Rules
- Keep specular 0-1 range
- test under various lighting
- Test thoroughly before deploying

## Response Pattern

### When Using This Skill
1. Apply specular maps
2. Validate the implementation
3. Test edge cases and error conditions
4. Ensure performance meets requirements

## Usage Contexts
- Legacy materials
- specific workflows

## What NOT to Do
- Mixing with metallic workflow
- incorrect specular values
- Deploy without testing

## Key Requirements
- Understand the use cases before application
- Follow the documented response pattern
- Validate results in the target environment
- Monitor for performance impact

## Further Learning
Review related skills and documentation for deeper understanding of related systems and best practices.
