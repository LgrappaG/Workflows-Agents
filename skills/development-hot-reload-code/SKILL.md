---
name: development-hot-reload-code
description: Enable hot-reload of code changes during gameplay
risk: high
source: workspace
date_added: '2026-03-24'
usage: Gameplay iteration with physics-heavy scenes, shader constant tweaking without scene reset, game logic debugging in active multiplayer test, UI event handler modification during runtime testing
avoid: State loss when component fields change signature (missing field deserialize crash), memory leaks from unreleased old IL method handles, reload operation blocking game thread causing frame drop >50ms, conflicting patches applied if two compilations race, type change breaking serialization format expectations
mandates: Preserve ≥95% of application state on reload, maintain runtime scene object integrity across 500+ entities, achieve <500ms reload time, guarantee zero conflicting edits with pending async saves.
response: Snapshot current application state (scene graph, entity component data, active timers) into, Route reload signal through compile-on-demand service with parallel shader compilation to minimize, Apply IL patch manager to running assembly, updating method bodies in-place while, Restore previous state incrementally, validating type signatures match and invoking reset callbacks
---

# Development Hot Reload Code

Enable hot-reload of code changes during gameplay

## Risk Level
**HIGH**

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
- Live iteration
- Development workflows

## What NOT to Do
- State loss on reload
- Incomplete testing
- Deploy without validation
