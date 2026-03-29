---
version: 9.0.0
category: Testing & QA
agent: QA Lead
difficulty: intermediate
estimated_time: 1-2 hours
skills:
  required:
  - custom-workflow-builder
  - automated-testing-framework
  - ui-performance-optimization
  - ui-focus-navigation
  - compatibility-testing
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - ci-cd-pipeline-setup
  - ui-accessibility
  - ui-event-handlers
  - ui-keyboard-shortcuts
  - godot-animation-setup
  - navmesh-baking-setup
  - ui-animation-states
  - ui-auto-layout
  - ui-button-events
  - ui-data-binding
  - ui-docking-windows
  - ui-drag-drop
  - ui-overflow-handling
  - ui-prefab-variants
  - ui-resize-scaling
  - ui-style-sheets
  - ui-transition-timing
  - ai-debugging-tools
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - animation-mocap-setup
  - audio-mixer-setup
  - build-system-optimization
  - csharp-builder-pattern
  - data-pipeline-setup
  - debug-build-diagnostic
  - engine-migration-guide
  - godot-setup
  - machine-learning-setup
  - material-disney-workflow
  - material-metallic-workflow
  - material-pbr-setup
  - material-specular-workflow
  - material-translucency-setup
  - networking-guild-system
  - networking-ngo-setup
  - physics-fluid-dynamics
  - physics-vehicle-setup
  - terrain-performance-tuning
  - ui-anchor-positioning
  - ui-animation-tweens
  - ui-context-menus
  - ui-dynamic-styling
  - ui-form-submission
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-input-validation
  - ui-list-repeater
  - ui-list-virtualization
  - ui-modal-dialogs
  - ui-mouse-interaction
  recommended:
  - ui-panel-layout
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-text-binding
  - ui-theme-switching
  - ui-tooltips
  - ui-touch-input
  - ui-two-way-binding
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - ai-perception-system
  - animation-constraint-rigging
  - physics-constraint-optimization
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - ai-learning-adaptation
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - csharp-async-await
  - csharp-chain-of-responsibility
  - material-mipmap-chains
  - networking-server-maintenance
  - physics-chain-dynamics
  - physics-hair-dynamics
  - physics-joint-constraints
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-blending-shaders
  - terrain-brush-settings
  - terrain-cave-systems
  - terrain-cliff-generation
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
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-shape-tools
  - terrain-sound-surfaces
  - terrain-splat-mapping
  - terrain-streaming
  - terrain-texture-painting
  optional:
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
  - terrain-water-integration
  - terrain-wind-zones
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: tech-lead
secondary_agents:
- production-lead
- quality-lead
complexity_score: 10
skill_density: 127.0
estimated_skills_needed: 127
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# UI Testing Framework & Automation

Automate UI testing to catch layout issues, button interactions, and navigation bugs early.

## Prerequisites

- UI Toolkit or uGUI
- Unity Test Framework installed
- 1 week setup

// turbo-all

## Phase 1: Install Testing Framework

```bash
Window → Package Manager → TestFramework
Install: Unity Test Framework (UTF)

Window → Package Manager → UITests
Install: UI Toolkit (built-in)
```

## Phase 2: Write UI Test Cases

```csharp
using UnityEngine.TestTools;
using UnityEngine.UI;
using NUnit.Framework;
using System.Collections;

public class UITestSuite
{
    [UnityTest]
    public IEnumerator TestPlayButtonClick() {
        // Arrange
        var playButton = GameObject.Find("PlayButton").GetComponent<Button>();

        // Act
        playButton.onClick.Invoke();
        yield return new WaitForSeconds(0.1f);

        // Assert
        var mainMenu = GameObject.Find("MainMenu");
        Assert.IsNull(mainMenu, "Main menu should close after play");
    }

    [UnityTest]
    public IEnumerator TestUIElementsRender() {
        yield return new WaitForEndOfFrame();
        var canvas = GameObject.Find("Canvas").GetComponent<Canvas>();
        Assert.IsTrue(canvas.enabled, "Canvas should be enabled");
    }
}
```

## Phase 3: Test Button Interactions

```csharp
[UnityTest]
public IEnumerator TestSettingsButtonFlow() {
    var settingsButton = GameObject.Find("SettingsButton").GetComponent<Button>();
    var settingsPanel = GameObject.Find("SettingsPanel");

    // Initially hidden
    Assert.IsFalse(settingsPanel.activeSelf);

    // Click button
    settingsButton.onClick.Invoke();
    yield return new WaitForSeconds(0.2f);

    // Now visible
    Assert.IsTrue(settingsPanel.activeSelf);

    // Click close
    var closeButton = settingsPanel.Find("CloseButton").GetComponent<Button>();
    closeButton.onClick.Invoke();
    yield return new WaitForSeconds(0.2f);

    // Hidden again
    Assert.IsFalse(settingsPanel.activeSelf);
}
```

## Phase 4: Automated Layout Testing

```csharp
[Test]
public void TestUILayoutNotOverflowing() {
    var buttons = GameObject.FindObjectsOfType<Button>();

    foreach (var button in buttons) {
        var rectTransform = button.GetComponent<RectTransform>();
        float width = rectTransform.rect.width;
        float height = rectTransform.rect.height;

        Assert.IsTrue(width > 0, $"Button {button.name} has no width!");
        Assert.IsTrue(height > 0, $"Button {button.name} has no height!");
        // Catch missing text/layout issues
    }
}
```

## Phase 5: Continuous Testing

```bash
# Run tests in CI/CD pipeline
unity -runTests -testPlatform editmode -testResults results.xml
unity -runTests -testPlatform playmode -testResults results.xml

# Results output to results.xml for CI system
```

## Verification Checklist

- [ ] All button interactions tested
- [ ] Layout validation tests passing
- [ ] Automated tests run in CI/CD
- [ ] 80%+ test coverage for UI
- [ ] No flaky tests

## Common Issues

| Issue | Solution |
|---|---|
| Tests fail intermittently | Add WaitForSeconds between interactions |
| Can't find UI element | Verify scene loaded, check Hierarchy |

## Related Topics

- See `/accessibility-audit-workflow` for UI compliance
- Refer to `/performance-audits` for UI performance