---
name: development-live-edit-scenes
description: Multi-user scene editing with live collaboration and conflict resolution
risk: high
source: workspace
date_added: '2026-03-24'
usage: Collaborative level design with 2-4 artists simultaneous editing, runtime scene composition for dynamic worlds, prefab variant authoring with multiple designers, multi-player scenario building for gameplay testing
avoid: Simultaneous parent-child modifications creating orphaned node hierarchies, network lag inducing edit conflicts with no resolution strategy, undo/redo stack not tracking remote changes causing desynced revision history, work loss on connection drop without crash recovery, transform precision loss from excessive delta encoding/decoding cycles
mandates: Enable multi-user scene editing with automatic conflict resolution, preserve transform hierarchies across ≥100 simultaneous objects, maintain <200ms delta sync latency, support full undo/redo stack for all remote changes.
response: 'Implement optimistic locking on scene nodes: each edit acquires temporary lock, broadcasts, Encode property changes as delta patches (position delta, rotation quaternion delta) and, Validate hierarchy consistency server-side: check parent-child relationships, detect orphaned subtrees, reject reparenting, Queue competing edits by server timestamp, apply in total order, and replicate'
---

# Live Edit Scenes

Enable multi-user scene editing with automatic conflict resolution and delta synchronization.

## Risk Level
**HIGH**

## Core Rules
- Enable multi-user editing with automatic conflict resolution
- Preserve transform hierarchies across 100+ simultaneous objects
- Maintain <200ms delta sync latency
- Support full undo/redo for remote changes

## Response Pattern

1. Implement optimistic locking with grace periods
2. Encode changes as delta patches
3. Validate hierarchy consistency
4. Replicate undo/redo actions

## Usage
- Collaborative level design with 2-4 artists
- Runtime scene composition for dynamic worlds
- Prefab variant authoring with multiple designers
- Multiplayer scenario building for gameplay testing

## What NOT to Do
- Simultaneous parent-child modifications
- Network lag without conflict resolution
- Undo/redo desynchronization across clients
- Work loss on connection drop
- Excessive delta encoding/decoding

