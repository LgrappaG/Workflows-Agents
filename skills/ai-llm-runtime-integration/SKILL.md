---
name: ai-llm-runtime-integration
description: "Integrate runtime LLM orchestration for NPC and mission generation with guardrails"
risk: high
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

# ai-llm-runtime-integration

## Overview

Orchestrate large language models at runtime for dynamic NPC dialogue, mission generation, and world-building while maintaining safety guardrails and performance budgets. This skill enables production-grade LLM integration in game engines with fallback strategies and measurable SLOs.

## Key Capabilities

### 1. LLM Service Integration
- **Remote APIs**: OpenAI, Anthropic, Meta, Azure OpenAI with fallback chaining
- **On-Device Models**: ONNX Runtime, TensorFlow Lite for offline capability
- **Streaming Responses**: Token-by-token dialogue generation for real-time character interaction
- **Batch Processing**: Async mission generation with configurable QoS tiers

### 2. Safety & Guardrails
- **Content Filtering**: NSFW, violence, PII detection at ingestion and output
- **Token Budget Enforcement**: Hard limits on API spend per session/world
- **Latency Budgets**: Fail-open gracefully when responses exceed SLO (fallback to procedural)
- **Rate Limiting**: Per-player, per-NPC throttling with queue management
- **Jailbreak Detection**: Prompt injection mitigation via semantic anomaly scoring

### 3. Mission & Dialogue Generation
- **Context Awareness**: World state, player history, NPC personality injection
- **Deterministic Seeding**: Reproduce missions for testing/replay with fixed seeds
- **Branching Narratives**: Dynamic mission trees based on player choices
- **Localization**: Multi-language generation with style preservation

### 4. Performance & Observability
- **Response Caching**: LRU cache for repeated generation patterns
- **Latency Tracing**: End-to-end timing from request to gameplay integration
- **Usage Analytics**: Token counts, API costs, fallback rates per feature
- **A/B Testing**: Variant generation for NPC dialogue quality measurement

## Implementation Pattern

```csharp
// Pseudo-code: High-level orchestration
class NPCDialogueGenerator : MonoBehaviour {
    public async Task<DialogueNode> GenerateResponse(
        NPCContext context,
        PlayerInput input,
        CancellationToken ct = default)
    {
        // 1. Load player history + world state
        var memoryContext = await LoadPlayerMemory(context.PlayerId);

        // 2. Build prompt with safety constraints
        var prompt = BuildPrompt(context, memoryContext, input);

        // 3. Orchestrate across providers with fallback
        var response = await LlmOrchestrator.GenerateWithFallback(
            prompt: prompt,
            maxTokens: context.TokenBudget,
            timeout: TimeSpan.FromSeconds(5),
            providers: new[] { "primary", "fallback", "procedural" }
        );

        // 4. Validate & cache result
        if (!await ValidateContent(response)) {
            response = await GenerateFallbackDialogue(context);
        }

        // 5. Record analytics
        await RecordUsage(context, response);

        return ParseDialogueNode(response);
    }
}
```

## Mandates

- **Measurable SLOs**: Define latency, cost, and fallback rate budgets upfront
- **Safety Gates**: Content filter + jailbreak detection must run on all responses
- **Platform Validation**: Test on target hardware with real network conditions
- **Privacy Compliance**: No PII in logs, GDPR-compliant caching strategies
- **Rollback Plan**: Graceful degradation to procedural generation under load

## Best Practices

1. **Budget First**: Set hard token/cost limits per play session
2. **Fallback Early**: Always have deterministic procedural generation as backup
3. **Cache Aggressively**: Reuse generated content for common scenarios
4. **Test Jailbreaks**: Red-team your prompts before production
5. **Monitor Drift**: Track changes in model output quality over time

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| API downtime | Implement 3+ provider fallback chain + offline models |
| Jailbreak attacks | Semantic anomaly detection + rate limiting by player |
| Token overspend | Per-session budget with hard cutoff |
| Inappropriate output | Content filter + human review queue for edge cases |
| Latency spikes | SLO-aware timeout + procedural fallback |

## Resources

- [LLM Integration Best Practices](docs/llm-integration.md)
- [Safety Guardrails Checklist](docs/safety-checklist.yml)
- [Cost Optimization Strategies](docs/cost-optimization.md)
- Example: `examples/npc-dialogue-generator.cs`
