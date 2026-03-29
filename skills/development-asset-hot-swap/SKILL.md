---
name: development-asset-hot-swap
description: Replace game assets at runtime without scene reload or visual artifacts
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Texture artist iteration on material visuals during gameplay, mesh optimization testing (LOD variants), material authoring with live feedback, prefab variant testing without rebuild, runtime shader variant switching
avoid: Material references breaking after swap due to descriptor handle reuse, dangling pointers causing GPU validation errors on next draw call, visual artifacts from partial updates (old texture on new mesh LOD), VRAM exhaustion from orphaned assets not being freed, race conditions if asset swap races with active render job
mandates: Support ≥50 concurrent asset replacements in single operation, maintain material bindings across 95% of mesh instances without rebind, achieve <300ms hot-swap latency, guarantee zero visual glitches from partial updates.
response: 'Invalidate GPU renderer cache for all objects using target asset (texture/mesh), clearing, Load new asset via async import with progress callback, deserializing GPU resources, Rebind material/mesh to all affected instances in single batch operation, updating vertex, Verify GPU memory state post-swap: check descriptor validity, confirm texture/mesh handles are'
---

# Asset Hot-Swap

Replace game assets at runtime without scene reload or visual artifacts using GPU cache invalidation.

## Risk Level
**MEDIUM**

## Core Rules
- Support >=50 concurrent asset replacements
- Maintain material bindings across 95% of mesh instances
- Achieve <300ms hot-swap latency
- Guarantee zero visual glitches

## Response Pattern

1. Invalidate GPU renderer cache
2. Load new asset via async import
3. Rebind material/mesh in batch operation
4. Verify GPU memory state post-swap

## Usage
- Texture artist iteration during gameplay
- Mesh optimization testing (LOD variants)
- Material authoring with live feedback
- Prefab variant testing without rebuild
- Shader variant switching at runtime

## What NOT to Do
- Material references breaking after swap
- Dangling pointers from descriptor reuse
- Visual artifacts from partial updates
- VRAM exhaustion from orphaned assets
- Race conditions with active render jobs

