---
name: cross-engine-portability-layer
description: "Design portability layer to share gameplay logic across Unity, Godot, and Unreal"
risk: medium
source: .agents-phase6
date_added: 2026-03-29
usage: "Use when implementing Phase 6 scale, interoperability, and analytics initiatives"
avoid: "Do not deploy without compatibility checks, rollback strategy, and measurable SLOs"
mandates:
  - define measurable success criteria and failure budgets
  - include platform-specific acceptance gates
  - include data privacy and governance checks
response: assess baseline, design minimal implementation, validate measurable targets, document rollback plan
---

# cross-engine-portability-layer

## Overview

Design and implement an abstraction layer that decouples game logic from engine-specific APIs, enabling seamless skill and workflow portability across Unity, Godot, and Unreal. This skill defines the technical foundation for true multi-engine game development.

## Key Capabilities

### 1. Abstraction Layer Architecture
- **Engine Abstraction**: Unified API for rendering, physics, input, audio across engines
- **Interface Definitions**: Core interfaces (IGameObject, ITransform, IPhysicsBody, IRenderer)
- **Adapter Pattern**: Engine-specific implementations hiding platform details
- **Plugin Architecture**: Hot-swap engine components for testing and migration

### 2. Gameplay Logic Portability
- **Core Game Loop**: Engine-agnostic update/render cycles
- **Event System**: Unified event dispatching across all engines
- **Serialization**: Asset and world state serialization with engine-agnostic format
- **Script Bindings**: C# as common language with scripting language bridges

### 3. Asset Pipeline
- **Format Neutrality**: GLTF/FBX for models, standard audio formats, platform-agnostic shaders
- **Import Workflows**: Automated conversion & optimization per engine
- **Dependency Tracking**: Asset ownership and cross-references validated
- **Version Management**: Asset versioning with backward compatibility layers

### 4. Platform Layer
- **Input Abstraction**: Unified input API for keyboard, gamepad, touch, VR
- **Graphics Abstraction**: Shader compilation for each engine
- **Audio Abstraction**: Spatial audio, mixing, platform-specific codecs
- **Storage Abstraction**: Save game serialization, network persistence

## Mandates

- **Zero Engine Lock-in**: Core gameplay logic uses ONLY abstraction interfaces
- **Platform Parity**: Feature set equivalent across all three engines
- **Compatibility Matrix**: Document which features work on which engines
- **Migration Paths**: Automated tools for porting existing single-engine projects
- **Performance Budgets**: Define acceptable overhead for abstraction layer (<5% typical)

## Best Practices

1. **Lean Abstraction**: Only abstract what's truly needed, not everything
2. **Test on All Engines**: CI/CD must validate on Unity, Godot, Unreal in parallel
3. **Profile Overhead**: Measure abstraction layer performance regularly
4. **Design for Extensibility**: Allow custom engine implementations per feature
5. **Document Engine Quirks**: Keep wiki of engine-specific limitations

## Compatibility Matrix

| Feature | Unity | Godot | Unreal | Status |
|---------|-------|-------|--------|--------|
| 3D Rendering | ✅ | ✅ | ✅ | Stable |
| Physics | ✅ | ✅ | ✅ | Stable |
| Input | ✅ | ✅ | 🟡 | In Progress |
| Audio | ✅ | ✅ | 🟡 | Testing |
| Networking | 🟡 | 🟡 | ❌ | Planned |
| VR | ✅ | 🟡 | ✅ | Mixed |

## Resources

- [Abstraction Layer Design Document](docs/portability-architecture.md)
- [Engine Adapter Implementation Guide](docs/adapters.md)
- [Asset Pipeline Specification](docs/asset-pipeline.md)
