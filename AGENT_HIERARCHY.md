# Agent Hierarchy: 48-Agent Organizational Structure for Game Development

**Framework**: .agents
**Version**: 1.0
**Date**: 2026-03-21
**Purpose**: Define organizational structure for solo developers building games with AI agent specialization

---

## Executive Summary

The 48-Agent Hierarchy is a specialized organizational model designed to support solo game developers leveraging the .agents framework. It provides structured guidance for when to invoke specific agent specialists, how they collaborate, and their integration with the 512+ skill system.

This hierarchy is inspired by professional game studios but optimized for solo development, with agents functioning as specialized AI consultants rather than traditional team members.

---

## Hierarchy Overview

```
┌─────────────────────────────────────────────┐
│      CREATIVE DIRECTOR (1 Agent)            │ ← Tier 1: Executive
├─────────────────────────────────────────────┤
│ Tech Lead │ Production Lead │ Quality Lead  │ ← Tier 2: Department Heads (3)
├─────────────────────────────────────────────┤
│        Tier 3: 44 Specialist Agents         │
│  • Core Development (8)                     │
│  • Graphics & Visuals (8)                   │
│  • Audio & Narrative (5)                    │
│  • AI & Gameplay (6)                        │
│  • Tools & Pipeline (6)                     │
│  • Testing & Quality (4)                    │
│  • Content & Design (7)                     │
└─────────────────────────────────────────────┘

TOTAL: 48 Agents
```

---

## TIER 1: EXECUTIVE LEADERSHIP (1 Agent)

### 1. Creative Director
- **Role**: Vision keeper, story overseer, creative decision maker
- **Specialization**: Game design, narrative direction, artistic vision
- **Responsibilities**:
  - Define game vision and core mechanics
  - Guide narrative and story development
  - Approve major design decisions
  - Maintain creative consistency
  - Set quality standards and artistic direction

- **When to Call**:
  - Need overall game direction or vision review
  - Major narrative or story decisions required
  - Design philosophy or artistic direction needed
  - Game concept validation or pivots required
  - Cross-discipline approval or sign-off needed

- **Skills Used**: advanced-architecture-patterns, game-design-specialist, narrative-design, vision-documentation

---

## TIER 2: DEPARTMENT HEADS (3 Agents)

### 2. Tech Lead
- **Role**: Architecture guardian, performance optimizer, systems designer
- **Specialization**: Technical architecture, performance, systems design
- **Responsibilities**:
  - Define technical architecture
  - Optimize performance and efficiency
  - Manage technology selections
  - Mentor other technical agents
  - Ensure scalability and maintainability

- **When to Call**:
  - Need architecture design or review
  - Performance optimization required
  - Technology selection or evaluation
  - System design consultation
  - Cross-system integration planning

- **Reporting To**: Creative Director
- **Manages**: Core Development, Tools & Pipeline, AI & Gameplay specialists
- **Skills Used**: advanced-architecture-patterns, performance-profiling-cross-engine, cross-engine-architecture, engine-agnostic-patterns

---

### 3. Production Lead
- **Role**: Timeline keeper, scope manager, dependency tracker
- **Specialization**: Project management, scheduling, scope control
- **Responsibilities**:
  - Create and manage project timeline
  - Control scope and feature prioritization
  - Track dependencies and blockers
  - Monitor progress and milestones
  - Manage risk and contingency planning

- **When to Call**:
  - Need project timeline or schedule
  - Scope management or prioritization
  - Dependency or blocker identification
  - Milestone planning or tracking
  - Risk assessment or contingency planning

- **Reporting To**: Creative Director
- **Manages**: Content & Design, Testing & Quality specialists
- **Skills Used**: project-timeline-management, scope-management, dependency-tracking, risk-assessment

---

### 4. Quality Lead
- **Role**: Quality gatekeeper, testing advocate, standards enforcer
- **Specialization**: Testing, quality assurance, standards compliance
- **Responsibilities**:
  - Define quality standards and metrics
  - Establish testing protocols
  - Monitor bug tracking and resolution
  - Maintain code and asset standards
  - Enforce best practices across teams

- **When to Call**:
  - Need quality standards or metrics
  - Testing strategy or protocol
  - Bug prioritization or triage
  - Quality verification or gate approval
  - Standards compliance review

- **Reporting To**: Creative Director
- **Manages**: Testing & Quality, Graphics & Visuals specialists
- **Skills Used**: automated-testing-framework, validation-framework, performance-profiling-cross-engine, compatibility-testing

---

## TIER 3: SPECIALISTS BY DOMAIN (44 Agents)

---

## CORE DEVELOPMENT SPECIALISTS (8 Agents)

### 5. Unity Architect
- **Title**: Senior Engine Architect - Unity
- **Specialization**: Unity engine architecture, project structure, framework design
- **Primary Skills**: unity-project-setup, advanced-architecture-patterns, assembly-optimization, unity-version-management
- **When to Call**:
  - Unity project setup or architecture design
  - Complex Unity systems design
  - Engine version migration planning
  - Unity-specific architecture patterns
  - Build pipeline or project structure

- **Collaboration**: Works with Tech Lead, C# Master, Blueprint Designer
- **Risk Level**: Medium

---

### 6. C# Master
- **Title**: Advanced C# Developer
- **Specialization**: Advanced C# programming, performance optimization, memory management
- **Primary Skills**: csharp-advanced-patterns, advanced-memory-profiling, advanced-il-emit, garbage-collection-optimization
- **When to Call**:
  - Need advanced C# architecture or patterns
  - Performance optimization in C# code
  - Memory management or GC tuning
  - IL emit or reflection-based solutions
  - Complex C# system design

- **Collaboration**: Works with Unity Architect, Performance Tester
- **Risk Level**: Medium

---

### 7. Blueprint Designer
- **Title**: Visual Systems Designer
- **Specialization**: Visual scripting, blueprint systems, node-based programming
- **Primary Skills**: blueprint-design-patterns, visual-scripting-optimization, node-graph-systems, blueprint-performance-tuning
- **When to Call**:
  - Need blueprint or visual scripting system
  - Complex node-graph design
  - Performance optimization for visual scripts
  - Blueprint architecture or patterns
  - Rapid prototyping with visual systems

- **Collaboration**: Works with Unity Architect, Gameplay Programmer
- **Risk Level**: Low

---

### 8. Gameplay Programmer
- **Title**: Core Gameplay Systems Developer
- **Specialization**: Game mechanics, gameplay systems, input handling
- **Primary Skills**: gameplay-loop-implementation, input-system-setup, game-state-management, player-controller-implementation
- **When to Call**:
  - Core gameplay system implementation
  - Game mechanics programming
  - Player input handling or controller setup
  - Game state management
  - Gameplay loop optimization

- **Collaboration**: Works with Game Design Specialist, Physics Programmer
- **Risk Level**: Medium

---

### 9. VR/XR Specialist
- **Title**: Virtual Reality Developer
- **Specialization**: VR/XR platform integration, immersive systems, spatial computing
- **Primary Skills**: vr-controller-setup, vr-locomotion-systems, vr-optimization, xr-interaction-design
- **When to Call**:
  - VR/XR platform integration
  - Immersive interaction design
  - VR performance optimization
  - Motion sickness mitigation
  - Spatial computing challenges

- **Collaboration**: Works with Mobile Expert, Platform Specialist
- **Risk Level**: High

---

### 10. Mobile Expert
- **Title**: Mobile Platform Specialist
- **Specialization**: Mobile game development, platform optimization, touch input
- **Primary Skills**: mobile-performance-optimization, touch-input-systems, mobile-battery-management, platform-specific-optimization
- **When to Call**:
  - Mobile platform development
  - Touch input or gesture systems
  - Mobile performance optimization
  - Battery and memory management
  - Mobile-specific feature integration

- **Collaboration**: Works with Platform Specialist, VR/XR Specialist
- **Risk Level**: Medium

---

### 11. Platform Specialist
- **Title**: Multi-Platform Architect
- **Specialization**: Cross-platform development, platform abstraction, deployment
- **Primary Skills**: platform-abstraction-layers, cross-platform-deployment, platform-specific-features, compatibility-testing
- **When to Call**:
  - Multi-platform architecture or design
  - Platform-specific feature integration
  - Build and deployment across platforms
  - Platform compatibility issues
  - Cross-platform abstraction layers

- **Collaboration**: Works with Mobile Expert, DevOps Engineer
- **Risk Level**: Medium

---

### 12. Scripting Master
- **Title**: Scripting Systems Engineer
- **Specialization**: Scripting languages, custom script engines, automation
- **Primary Skills**: custom-scripting-engine, lua-integration, scripting-optimization, script-serialization
- **When to Call**:
  - Custom scripting engine development
  - Scripting language integration (Lua, etc.)
  - Script automation systems
  - Complex scripting architecture
  - Script performance optimization

- **Collaboration**: Works with Gameplay Programmer, Tools Programmer
- **Risk Level**: Medium

---

## GRAPHICS & VISUALS SPECIALISTS (8 Agents)

### 13. Graphics Programmer
- **Title**: Rendering Systems Engineer
- **Specialization**: Rendering architecture, graphics pipeline, rendering optimization
- **Primary Skills**: graphics-urp-setup, graphics-hdrp-setup, graphics-postprocessing, rendering-optimization
- **When to Call**:
  - Graphics pipeline design or optimization
  - Rendering architecture decisions
  - Graphics API selection or migration
  - Complex rendering systems
  - Graphics performance issues

- **Collaboration**: Works with Quality Lead, Shader Specialist
- **Risk Level**: High

---

### 14. Shader Specialist
- **Title**: Shader Programming Expert
- **Specialization**: Shader development, GPU programming, visual effects shaders
- **Primary Skills**: shader-graph-advanced, shader-optimization, compute-shaders, material-pbr-setup
- **When to Call**:
  - Custom shader development
  - GPU programming or compute shaders
  - Shader performance optimization
  - Complex visual effects shaders
  - Material system design

- **Collaboration**: Works with Graphics Programmer, VFX Artist
- **Risk Level**: High

---

### 15. VFX Artist
- **Title**: Visual Effects Specialist
- **Specialization**: Particle systems, visual effects, dynamic visuals
- **Primary Skills**: vfx-particle-systems, vfx-burst-optimization, vfx-gpu-instancing, particle-optimization
- **When to Call**:
  - Particle system or VFX design
  - Complex visual effects
  - VFX performance optimization
  - GPU-accelerated effects
  - Dynamic visual system design

- **Collaboration**: Works with Shader Specialist, Particle Master
- **Risk Level**: Medium

---

### 16. Particle Master
- **Title**: Particle System Optimization Expert
- **Specialization**: Particle systems, emission patterns, performance optimization
- **Primary Skills**: particle-optimization, particle-pooling, particle-sorting, gpu-instancing-optimization
- **When to Call**:
  - Particle system optimization
  - Large-scale particle effects
  - Particle pooling or caching
  - Memory-efficient particle handling
  - Particle system architecture

- **Collaboration**: Works with VFX Artist, Graphics Programmer
- **Risk Level**: Medium

---

### 17. Animation Master
- **Title**: Character Animation Systems Designer
- **Specialization**: Animation systems, character animation, blend trees
- **Primary Skills**: animation-state-machine, animation-blend-trees, animation-humanoid-setup, animation-optimization
- **When to Call**:
  - Animation system design or architecture
  - Complex animation state machines
  - Humanoid animation setup
  - Animation performance optimization
  - Animation pipeline design

- **Collaboration**: Works with Rigging Specialist, Modeling Specialist
- **Risk Level**: Medium

---

### 18. Rigging Specialist
- **Title**: Character Rigging Expert
- **Specialization**: Character rigging, skeleton setup, bone structure
- **Primary Skills**: rigging-humanoid-setup, constraint-rigging, bone-mapping, ik-setup
- **When to Call**:
  - Character rigging or skeleton setup
  - Complex rigging systems
  - IK/FK rig setup
  - Bone mapping or retargeting
  - Rigging optimization

- **Collaboration**: Works with Animation Master, Modeling Specialist
- **Risk Level**: Medium

---

### 19. Modeling Specialist
- **Title**: 3D Character Modeler
- **Specialization**: 3D modeling, character modeling, mesh optimization
- **Primary Skills**: character-modeling-optimization, mesh-optimization, uv-layout-optimization, polygon-optimization
- **When to Call**:
  - 3D character or asset modeling
  - Mesh optimization or LOD setup
  - UV layout or texel density optimization
  - Model performance issues
  - Asset pipeline integration

- **Collaboration**: Works with Rigging Specialist, Lighting Designer
- **Risk Level**: Low

---

### 20. Lighting Designer
- **Title**: Environmental Lighting Expert
- **Specialization**: Lighting design, light baking, dynamic lighting
- **Primary Skills**: lighting-optimization, light-baking, dynamic-lighting, environmental-lighting
- **When to Call**:
  - Lighting design or optimization
  - Light baking or indirect lighting
  - Dynamic lighting systems
  - Lighting performance issues
  - Environmental lighting setup

- **Collaboration**: Works with Modeling Specialist, Graphics Programmer
- **Risk Level**: Medium

---

## AUDIO & NARRATIVE SPECIALISTS (5 Agents)

### 21. Audio Programmer
- **Title**: Audio Systems Engineer
- **Specialization**: Audio systems, sound engine, spatial audio
- **Primary Skills**: audio-system-setup, spatial-audio-implementation, audio-optimization, audio-streaming
- **When to Call**:
  - Audio system architecture or design
  - Spatial audio implementation
  - Complex audio systems
  - Audio performance optimization
  - Audio engine integration

- **Collaboration**: Works with Sound Designer, Composer
- **Risk Level**: Medium

---

### 22. Sound Designer
- **Title**: Audio Content Specialist
- **Specialization**: Sound design, audio content, SFX creation
- **Primary Skills**: sound-design-workflow, audio-asset-creation, audio-mixing, sound-implementation
- **When to Call**:
  - Sound design or audio content decisions
  - SFX or audio asset pipeline
  - Audio content organization
  - Sound design workflow setup
  - Audio asset integration

- **Collaboration**: Works with Audio Programmer, Composer
- **Risk Level**: Low

---

### 23. Composer
- **Title**: Music Systems Designer
- **Specialization**: Music composition, dynamic music, scoring
- **Primary Skills**: dynamic-music-system, music-composition-integration, adaptive-music, music-streaming
- **When to Call**:
  - Music composition or dynamic music systems
  - Adaptive music implementation
  - Music scoring or composition guidance
  - Musical system design
  - Music asset pipeline

- **Collaboration**: Works with Audio Programmer, Sound Designer, Dialogue System Specialist
- **Risk Level**: Low

---

### 24. Dialogue System Specialist
- **Title**: Dialogue & Narrative Systems Engineer
- **Specialization**: Dialogue systems, branching narratives, dialogue UI
- **Primary Skills**: dialogue-system-setup, branching-narrative-design, dialogue-ui-implementation, dialogue-localization
- **When to Call**:
  - Dialogue system architecture or design
  - Branching narrative implementation
  - Dialogue UI or UX design
  - Dialogue state management
  - Dialogue localization setup

- **Collaboration**: Works with Narrative Designer, Composer
- **Risk Level**: Medium

---

### 25. Narrative Designer
- **Title**: Story & Narrative Lead
- **Specialization**: Story writing, narrative design, lore documentation
- **Primary Skills**: narrative-design, dialogue-writing, story-architecture, lore-documentation
- **When to Call**:
  - Story or narrative design guidance
  - Dialogue writing or refinement
  - Narrative structure or branching
  - Lore consistency or documentation
  - Story-game integration

- **Collaboration**: Works with Dialogue System Specialist, Creative Director
- **Risk Level**: Low

---

## AI & GAMEPLAY SPECIALISTS (6 Agents)

### 26. AI Programmer
- **Title**: Artificial Intelligence Systems Engineer
- **Specialization**: AI architecture, decision systems, behavioral AI
- **Primary Skills**: ai-behavior-switching, ai-learning-adaptation, decision-trees, reinforcement-learning
- **When to Call**:
  - AI system architecture or design
  - Complex AI behavior implementation
  - AI decision-making systems
  - AI performance optimization
  - Learning or adaptive AI systems

- **Collaboration**: Works with Behavior Specialist, Physics Programmer
- **Risk Level**: High

---

### 27. Behavior Specialist
- **Title**: NPC Behavior Systems Expert
- **Specialization**: NPC behaviors, behavior trees, action systems
- **Primary Skills**: behavior-tree-implementation, npc-scheduling, ai-state-management, behavior-balancing
- **When to Call**:
  - NPC behavior system design
  - Behavior tree architecture
  - Complex NPC behaviors
  - Behavior balancing or optimization
  - Behavior state management

- **Collaboration**: Works with AI Programmer, Gameplay Balancer
- **Risk Level**: Medium

---

### 28. Physics Programmer
- **Title**: Physics Systems Engineer
- **Specialization**: Physics simulation, collision systems, physical interactions
- **Primary Skills**: physics-setup-advanced, physics-optimization, collision-detection-optimization, ragdoll-setup
- **When to Call**:
  - Physics system architecture or design
  - Complex physics simulation
  - Physics performance optimization
  - Collision detection issues
  - Ragdoll or character physics

- **Collaboration**: Works with Gameplay Programmer, AI Programmer
- **Risk Level**: High

---

### 29. Networking Specialist
- **Title**: Multiplayer & Networking Engineer
- **Specialization**: Network architecture, multiplayer systems, synchronization
- **Primary Skills**: networking-architecture-design, multiplayer-synchronization, network-optimization, lag-compensation
- **When to Call**:
  - Multiplayer game architecture
  - Network synchronization design
  - Network performance issues
  - Lag compensation or prediction
  - Multiplayer system integration

- **Collaboration**: Works with Gameplay Programmer, Platform Specialist
- **Risk Level**: High

---

### 30. Game Design Specialist
- **Title**: Mechanics & Balance Designer
- **Specialization**: Game mechanics, balance design, gameplay loops
- **Primary Skills**: game-design-specialist, balancing-systems, difficulty-curve-design, progression-systems
- **When to Call**:
  - Game mechanic design or iteration
  - Gameplay balance or tuning
  - Difficulty curve design
  - Progression system design
  - Gameplay loop optimization

- **Collaboration**: Works with Creative Director, Gameplay Balancer
- **Risk Level**: Low

---

### 31. Gameplay Balancer
- **Title**: Metrics & Balance Analyst
- **Specialization**: Game balance, metrics analysis, data-driven balance
- **Primary Skills**: balancing-systems, game-metrics-tracking, data-driven-balance, progression-tuning
- **When to Call**:
  - Game balance analysis or tuning
  - Metrics tracking or interpretation
  - Data-driven balance decisions
  - Progression curve analysis
  - Economy or reward system balancing

- **Collaboration**: Works with Game Design Specialist, Behavior Specialist
- **Risk Level**: Medium

---

## TOOLS & PIPELINE SPECIALISTS (6 Agents)

### 32. DevOps Engineer
- **Title**: Build & Deployment Systems Engineer
- **Specialization**: Build systems, deployment automation, CI/CD
- **Primary Skills**: ci-cd-pipeline-setup, build-system-optimization, deployment-automation, version-management
- **When to Call**:
  - CI/CD pipeline setup or configuration
  - Build system optimization
  - Deployment automation
  - Version control or release management
  - Build and deployment issues

- **Collaboration**: Works with Tech Lead, Build System Specialist
- **Risk Level**: High

---

### 33. Build System Specialist
- **Title**: Build Optimization Expert
- **Specialization**: Build optimization, compilation speedup, asset pipeline
- **Primary Skills**: build-system-optimization, asset-pipeline-setup, compilation-acceleration, asset-processing
- **When to Call**:
  - Build system design or optimization
  - Compilation speed issues
  - Asset processing or pipeline
  - Build performance analysis
  - Build architecture redesign

- **Collaboration**: Works with DevOps Engineer, Asset Pipeline Expert
- **Risk Level**: Medium

---

### 34. Asset Pipeline Expert
- **Title**: Asset Management Systems Designer
- **Specialization**: Asset pipelines, asset organization, asset versioning
- **Primary Skills**: asset-pipeline-setup, asset-management-system, version-control-integration, asset-tagging-system
- **When to Call**:
  - Asset pipeline design or setup
  - Asset organization or structure
  - Asset versioning or management
  - Asset dependency tracking
  - Asset workflow optimization

- **Collaboration**: Works with Build System Specialist, Editor Extension Specialist
- **Risk Level**: Medium

---

### 35. CI/CD Specialist
- **Title**: Continuous Integration & Deployment Expert
- **Specialization**: CI/CD automation, testing pipelines, deployment strategies
- **Primary Skills**: ci-cd-pipeline-setup, automated-testing-framework, deployment-verification, pipeline-monitoring
- **When to Call**:
  - CI/CD pipeline configuration
  - Automated testing integration
  - Deployment strategy or verification
  - Pipeline monitoring or debugging
  - Test automation setup

- **Collaboration**: Works with DevOps Engineer, QA Lead
- **Risk Level**: High

---

### 36. Tools Programmer
- **Title**: Development Tools Engineer
- **Specialization**: Custom tools, editor tools, workflow automation
- **Primary Skills**: editor-extension-development, custom-workflow-builder, plugin-architecture, tool-optimization
- **When to Call**:
  - Custom tool development
  - Editor extension or plugin creation
  - Workflow automation or optimization
  - Tool architecture or design
  - Development environment setup

- **Collaboration**: Works with Editor Extension Specialist, Scripting Master
- **Risk Level**: Medium

---

### 37. Editor Extension Specialist
- **Title**: Editor & Tool Extensibility Expert
- **Specialization**: Editor tools, tool extensibility, custom inspectors
- **Primary Skills**: editor-extension-development, custom-inspector-tools, profiler-extensions, console-extensions
- **When to Call**:
  - Editor extension development
  - Custom inspector tool creation
  - Editor workflow optimization
  - Profiler or debug tool extensions
  - Development tool enhancement

- **Collaboration**: Works with Tools Programmer, Asset Pipeline Expert
- **Risk Level**: Low

---

## TESTING & QUALITY SPECIALISTS (5 Agents)

### 38. QA Lead
- **Title**: Quality Assurance Manager
- **Specialization**: QA strategy, testing planning, bug management
- **Primary Skills**: automated-testing-framework, testing-strategy-design, bug-triage, qa-process-setup
- **When to Call**:
  - QA strategy or testing planning
  - Bug triage or prioritization
  - QA process design or improvement
  - Testing scope or coverage
  - Quality gates or approval

- **Collaboration**: Works with Quality Lead, Performance Tester
- **Risk Level**: Medium

---

### 39. Performance Tester
- **Title**: Performance Analysis & Testing Expert
- **Specialization**: Performance testing, profiling, optimization verification
- **Primary Skills**: performance-profiling-cross-engine, performance-testing, bottleneck-analysis, optimization-verification
- **When to Call**:
  - Performance testing or profiling
  - Performance bottleneck identification
  - Optimization verification
  - Frame rate or memory analysis
  - Performance regression detection

- **Collaboration**: Works with QA Lead, Graphics Programmer
- **Risk Level**: Medium

---

### 40. Security Specialist
- **Title**: Security & Privacy Expert
- **Specialization**: Security design, privacy implementation, data protection
- **Primary Skills**: privacy-preservation, data-encryption, secure-coding, security-testing
- **When to Call**:
  - Security architecture or design
  - Privacy implementation or compliance
  - Security vulnerability assessment
  - Secure coding review
  - Data protection strategy

- **Collaboration**: Works with QA Lead, Platform Specialist
- **Risk Level**: High

---

### 41. Accessibility Expert
- **Title**: Accessibility & Inclusivity Specialist
- **Specialization**: Accessibility features, inclusive design, accessibility testing
- **Primary Skills**: accessibility-implementation, ui-accessibility, color-blindness-support, audio-accessibility
- **When to Call**:
  - Accessibility feature design
  - Inclusive UI/UX design
  - Accessibility testing or verification
  - Disability accommodation design
  - Accessibility compliance verification

- **Collaboration**: Works with UI/UX Designer, QA Lead
- **Risk Level**: Low

---

## CONTENT & DESIGN SPECIALISTS (7 Agents)

### 42. Level Designer
- **Title**: Level & Environment Designer
- **Specialization**: Level design, environment layout, gameplay spaces
- **Primary Skills**: level-design-theory, level-flow-design, difficulty-progression, environmental-storytelling
- **When to Call**:
  - Level design or layout
  - Gameplay space design
  - Level difficulty or flow
  - Environmental storytelling
  - Level iteration or optimization

- **Collaboration**: Works with World Builder, UI/UX Designer
- **Risk Level**: Low

---

### 43. UI/UX Designer
- **Title**: User Interface & Experience Designer
- **Specialization**: UI design, UX design, user experience
- **Primary Skills**: ui-design-principles, ux-flow-design, ui-implementation, user-feedback-integration
- **When to Call**:
  - UI design or UX decisions
  - User experience flow design
  - UI/UX implementation guidance
  - User feedback analysis or integration
  - Interface usability review

- **Collaboration**: Works with Accessibility Expert, Level Designer
- **Risk Level**: Low

---

### 44. World Builder
- **Title**: Environmental Design Specialist
- **Specialization**: World building, environment design, environmental detail
- **Primary Skills**: world-building-design, environmental-detail, location-design, world-consistency
- **When to Call**:
  - World design or environment building
  - Environmental detail design
  - Location or area design
  - World consistency or lore integration
  - Environmental storytelling

- **Collaboration**: Works with Level Designer, Concept Artist
- **Risk Level**: Low

---

### 45. Concept Artist
- **Title**: Visual Design & Concept Artist
- **Specialization**: Concept art, visual design, artistic direction
- **Primary Skills**: concept-art-creation, visual-style-guide, design-documentation, artistic-reference-creation
- **When to Call**:
  - Concept art or visual design
  - Visual style direction or guidance
  - Artistic reference creation
  - Design documentation or communication
  - Visual consistency review

- **Collaboration**: Works with World Builder, Lighting Designer
- **Risk Level**: Low

---

### 46. Documentation Specialist
- **Title**: Documentation & Communication Expert
- **Specialization**: Documentation, knowledge management, communication
- **Primary Skills**: documentation-creation, knowledge-base-setup, api-documentation, technical-writing
- **When to Call**:
  - Documentation creation or review
  - Knowledge base setup or maintenance
  - API or technical documentation
  - Process or workflow documentation
  - Communication improvement

- **Collaboration**: Works with all agents (supports documentation)
- **Risk Level**: Low

---

### 47. Quest & Systems Designer
- **Title**: Quest Design & Systems Specialist
- **Specialization**: Quest design, gameplay systems, objective design, reward systems
- **Primary Skills**: quest-design-theory, objective-design, reward-system-design, progression-systems, player-engagement
- **When to Call**:
  - Quest or objective design
  - Gameplay progression design
  - Reward system implementation
  - Player engagement and retention
  - Systems balancing and tuning
  - Narrative integration with gameplay

- **Collaboration**: Works with Game Design Specialist, Level Designer, Narrative Designer
- **Risk Level**: Low

---

## AGENT COLLABORATION PATTERNS

### Pattern 1: Feature Implementation Loop
```
Game Design Specialist
    ↓
Gameplay Programmer → Blueprint Designer
    ↓
AI Programmer (if AI involved)
    ↓
Graphics Programmer → Shader Specialist
    ↓
Performance Tester
    ↓
QA Lead → Bug Resolution
```

### Pattern 2: Optimization Cycle
```
Performance Tester (identify bottleneck)
    ↓
Tech Lead (evaluate approach)
    ↓
Appropriate Specialist (implement fix)
    ↓
Performance Tester (verify)
    ↓
QA Lead (regression testing)
```

### Pattern 3: Multi-Platform Launch
```
Platform Specialist (architecture)
    ↓
Mobile Expert & VR/XR Specialist (platform-specific)
    ↓
Compatibility Testing (validation)
    ↓
DevOps Engineer (deployment)
    ↓
QA Lead (final verification)
```

### Pattern 4: Asset Pipeline
```
Modeling Specialist (create)
    ↓
Asset Pipeline Expert (integrate)
    ↓
Build System Specialist (optimize)
    ↓
Performance Tester (verify)
    ↓
QA Lead (final check)
```

---

## SKILL INTEGRATION MAPPING

The 48-agent hierarchy integrates with the 512+ skill system as follows:

### Critical Skills by Tier

**Tier 1 (Creative Director)**
- Requires: 10+ meta-skills (vision, oversight, approval authority)
- Uses: advanced-architecture-patterns, game-design-specialist, narrative-design

**Tier 2 (Department Heads)**
- Each requires: 15+ core skills in their domain
- Tech Lead: advanced-architecture-patterns, performance-profiling-cross-engine, cross-engine-architecture
- Production Lead: project management, scope control, risk management skills
- Quality Lead: automated-testing-framework, validation-framework, compatibility-testing

**Tier 3 (44 Specialists)**
- Each requires: 20-30 specialized skills
- Example: Animation Master requires 25+ animation, optimization, and debugging skills
- All specialists have access to relevant problem-solving skills

### Skill Allocation Strategy

1. **Domain Skills** (primary): Each agent has 20-30 core skills in their specialization
2. **Cross-Functional Skills** (secondary): 10-15 skills for collaboration with other agents
3. **Foundation Skills** (baseline): 5 universal skills (communication, testing, debugging, documentation, version control)

---

## WORKFLOW EXAMPLES

### Example 1: Create New Character with Animation

**Sequence**:
1. **Game Design Specialist** defines character concept and mechanics
2. **Concept Artist** creates visual reference
3. **Modeling Specialist** creates base mesh
4. **Rigging Specialist** creates skeleton and rigging
5. **Animation Master** sets up animation system
6. **VFX Artist** adds effects and visual polish
7. **Quality Lead** performs integration testing
8. **QA Lead** verifies and signs off

**Timeline**: ~2 weeks
**Feedback Loops**: Between each step as needed

---

### Example 2: Multi-Platform Performance Optimization

**Sequence**:
1. **Performance Tester** profiles and identifies bottleneck
2. **Tech Lead** evaluates approach and feasibility
3. **Graphics Programmer** or **Physics Programmer** implements fix (depending on bottleneck)
4. **Platform Specialist** verifies cross-platform compatibility
5. **Mobile Expert** or **VR/XR Specialist** optimizes for their platform
6. **Performance Tester** re-profiles to verify improvement
7. **QA Lead** performs regression testing
8. **Production Lead** verifies timeline impact

**Timeline**: ~1 week
**Complexity**: High (involves multiple systems and platforms)

---

### Example 3: Gameplay Loop Implementation

**Sequence**:
1. **Creative Director** approves gameplay concept
2. **Game Design Specialist** designs mechanics and loop
3. **Gameplay Programmer** implements core loop
4. **Blueprint Designer** creates visual representations
5. **AI Programmer** adds AI interactions (if needed)
6. **Physics Programmer** adds physical interactions
7. **Gameplay Balancer** analyzes metrics and suggests tuning
8. **QA Lead** tests and verifies functionality
9. **Performance Tester** ensures performance targets met

**Timeline**: ~3 weeks
**Iteration**: Heavy (expect 3-5 feedback cycles)

---

### Example 4: Audio System Implementation

**Sequence**:
1. **Audio Programmer** designs audio architecture
2. **Sound Designer** creates or integrates audio assets
3. **Composer** integrates music system
4. **Dialogue System Specialist** integrates dialogue if needed
5. **Audio Programmer** optimizes and tests
6. **Performance Tester** profiles audio performance
7. **QA Lead** verifies quality and functionality

**Timeline**: ~2 weeks
**Collaboration**: Tight integration between audio specialists

---

## AGENT COMMUNICATION PROTOCOLS

### Priority Escalation
- **Level 1**: Direct agent-to-agent communication
- **Level 2**: Department head escalation (Tech Lead, Production Lead, Quality Lead)
- **Level 3**: Creative Director involvement for vision conflicts
- **Level 4**: Framework governance for major architectural changes

### Communication Channels
- **Synchronous**: Direct calls for urgent issues or decisions
- **Asynchronous**: Documented decisions for tracking and reference
- **Collaborative**: Shared sessions for complex multi-agent problems
- **Documentation**: All decisions and rationales recorded in knowledge base

### Decision Authority
- **Agents**: Authority within their domain
- **Department Heads**: Authority across their teams and cross-team decisions
- **Creative Director**: Final authority on vision, story, and creative direction
- **Quality Lead**: Authority on quality gates and release decisions

---

## METRICS & PERFORMANCE TRACKING

### Agent Performance Metrics
- **Efficiency**: Time to resolution vs. estimated time
- **Quality**: Bug rate and issue resolution quality
- **Collaboration**: Cross-team issue resolution effectiveness
- **Innovation**: New patterns and optimizations contributed

### Skill Utilization Tracking
- Tracks which skills are used most frequently
- Identifies skill gaps and training needs
- Guides framework expansion and skill additions

### Framework Health Metrics
- Total active agents and their specializations
- Skill coverage across all domains
- Integration effectiveness between agents
- Time to task completion by agent type

---

## SCALING & CUSTOMIZATION

### For Larger Teams
- **Expand Tier 3**: Add more specialists in high-demand areas
- **Create Sub-Teams**: Group related agents into specialized teams
- **Introduce Tier 4**: Junior specialists or apprentices under senior specialists
- **Specialized Leads**: Add specialized team leads (Animation Lead, Graphics Lead, etc.)

### For Smaller Solo Operations
- **Consolidate Roles**: Combine related specializations (e.g., Gameplay Programmer + AI Programmer)
- **Reduce Agents**: Focus on 15-25 most critical agents
- **Parallel Skills**: Have agents work on multiple specializations
- **Automation**: Increase automation through CI/CD and tools

### For Different Game Types
- **Action Games**: Expand Physics, AI, and Animation specialists
- **RPGs**: Expand Narrative, Dialogue, and Gameplay Balancer
- **Strategy Games**: Expand AI, Gameplay Balancer, and Tools
- **VR/XR Games**: Expand VR/XR Specialist and Platform Specialist roles

---

## ONBOARDING NEW AGENTS

### New Agent Integration Process

1. **Profile Setup**
   - Define specialization and skills
   - Assign to appropriate department
   - Set collaboration patterns

2. **Skill Acquisition**
   - Map agent to 20-30 primary skills
   - Assign 10-15 cross-functional skills
   - Establish baseline universal skills

3. **Collaboration Mapping**
   - Identify key collaborators
   - Document communication patterns
   - Set up knowledge sharing

4. **First Assignment**
   - Start with scoped, well-defined task
   - Pair with experienced agent
   - Monitor for effectiveness
   - Gather feedback and adjust

---

## FRAMEWORK INTEGRATION CHECKLIST

- [ ] All 48 agents defined with clear roles and responsibilities
- [ ] Each agent mapped to 20-30 specialized skills
- [ ] Cross-functional skills identified and documented
- [ ] Collaboration patterns established and documented
- [ ] Communication protocols defined
- [ ] Decision authority clearly delineated
- [ ] Onboarding process created and documented
- [ ] Performance metrics defined and tracked
- [ ] Scaling guidelines provided for team expansion
- [ ] Agent communication templates created

---

## CONCLUSION

The 48-Agent Hierarchy provides a comprehensive organizational structure for solo developers and teams leveraging the .agents framework with 512+ skills. By organizing agents into specialized tiers with clear responsibilities, collaboration patterns, and skill integration, this hierarchy enables:

- **Scalability**: From solo development to larger teams
- **Specialization**: Deep expertise in each domain
- **Collaboration**: Efficient cross-team cooperation
- **Quality**: High standards through specialized oversight
- **Efficiency**: Right specialist for each task
- **Learning**: Clear paths for skill development and specialization

This hierarchy works in conjunction with the .agents skill system, providing both the "who" (agents) and "what" (skills) dimensions of AI-assisted game development.

---

**Document Version**: 1.0
**Last Updated**: 2026-03-21
**Framework Version**: .agents 1.0 (512+ skills)
