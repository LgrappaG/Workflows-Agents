---
version: 9.0.0
category: Core Development
agent: Unity Architect
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - networking-server-maintenance
  - ai-debugging-tools
  - ai-learning-adaptation
  - ai-perception-system
  - material-metallic-workflow
  - material-mipmap-chains
  - terrain-normal-generation
  - terrain-water-integration
  - ui-text-binding
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-squad-tactics
  - ai-threat-assessment
  - animation-constraint-rigging
  - audio-ducking-sidechains
  - automated-testing-framework
  - build-system-optimization
  - cinemachine-aim-assist
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - csharp-builder-pattern
  - csharp-chain-of-responsibility
  - debug-build-diagnostic
  - engine-migration-guide
  - material-disney-workflow
  - material-specular-workflow
  - networking-guild-system
  - physics-chain-dynamics
  - physics-constraint-optimization
  - physics-fluid-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
  recommended:
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-heightmap-import
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-noise-functions
  - terrain-path-carving
  - terrain-performance-tuning
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-wind-zones
  - timeline-camera-transitions
  - training-datasets
  - ui-accessibility
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-context-menus
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-dynamic-styling
  - ui-event-handlers
  - ui-focus-navigation
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  optional:
  - ui-input-validation
  - ui-keyboard-shortcuts
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: unity-architect
secondary_agents:
- production-lead
complexity_score: 10
skill_density: 23.5
estimated_skills_needed: 94
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# Unity Documentation Generator Workflow

This workflow automatically generates standard XML document comments for your Unity C# classes, methods, and properties using the `code-documentation-doc-generate` skill from the awesome-skills repository. Having well-documented code is essential for maintainability and IDE tooling support.

## 1. Select the Target Files

Identify which C# scripts require documentation updates. You can target specific files or entire directories.

**Example Instruction for the Agent:**
"Please run the docs generator on the `Assets/Scripts/Managers` directory."

## 2. Generate XML Comments

The AI Agent will analyze the selected code and produce standard XML comments (`/// <summary>`) for every public and protected member.

If methods contain complex reasoning, it will also provide `/// <remarks>` tags explaining the 'why' behind the logic.

// turbo
## 3. Verify Changes

Once the agent completes generating the XML comments, review the changes using `git diff`.

```bash
git diff --stat
```

**Next Steps:**
- Check for accuracy in the generated summaries.
- If everything looks correct, you are ready to commit the changes.

## 4. Commit Documentation Updates

You can ask the agent to commit the newly added documentation.

**Example Instruction for the Agent:**
"Commit the new XML documentation with the message 'docs: Added XML summaries to Manager scripts'."