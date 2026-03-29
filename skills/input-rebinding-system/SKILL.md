---
name: input-rebinding-system
description: Enable player input rebinding for customizable controls
risk: medium
source: workspace
date_added: '2026-03-24'
usage: FPS weapon wheel remapping, fighting game button layouts, accessibility motor control remapping, esports tournament standardized configs, VR teleport gesture binding
avoid: Double-binding same key to multiple actions without priority, losing rebinds on engine crash or power loss, allowing rebinding of critical OS/engine inputs (Alt+F4), race conditions in multithreaded input processing, loading stale rebind cache after hotplug device change
mandates: Detect rebinding conflicts in <5ms, validate against 50+ reserved system keys, support unlimited custom keybinds, persist with JSON schema versioning, zero data loss on crash
response: Parse input events into rebindable action sets indexed by action ID with, Validate rebind requests against reserved system keys (OS shortcuts) and existing bindings, Persist remapped controls to structured storage with version migration, checksum validation, and, Broadcast rebind events to all input consumers with delta payload for immediate
---

# Input Rebinding System

Enable player input rebinding for customizable controls

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
- Player customization
- Development workflows

## What NOT to Do
- Conflicting bindings
- Incomplete testing
- Deploy without validation
