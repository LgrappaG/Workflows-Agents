---
name: debug-missing-reference-cleaner
description: Identify and remove missing script references from scenes and prefabs
risk: low
source: workspace
date_added: '2026-03-24'
usage: Reference cleanup, scene debugging, prefab maintenance, asset integrity
avoid: Deleting valid components, removing non-script references, incomplete scans
mandates: Scan references, remove safely, verify integrity, test thoroughly
response: Scan for missing references, analyze results, safely remove broken links, verify scene
---

# Debug Missing Reference Cleaner

Identify and remove missing script references from scenes and prefabs

## Risk Level
**LOW**

## Core Rules
- Scan comprehensively
- Verify removals
- Preserve scene integrity

## Response Pattern

1. Scan for missing references
2. Analyze detected references
3. Safely remove broken links
4. Verify integrity

## Usage
- Reference cleanup
- Scene debugging
- Prefab maintenance

## What NOT to Do
- Delete valid components
- Remove non-script references
- Deploy without testing
