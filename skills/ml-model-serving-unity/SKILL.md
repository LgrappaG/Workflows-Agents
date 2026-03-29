---
name: ml-model-serving-unity
description: "Serve on-device and remote ML models for gameplay inference with fallback paths"
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

# ml-model-serving-unity

## Overview

Deploy machine learning models for real-time gameplay inference (behavior prediction, player skill detection, content recommendation) with on-device and cloud fallback paths. This skill bridges ML model lifecycle and game runtime requirements.

## Key Capabilities

### 1. Model Loading & Inference
- **Framework Support**: ONNX Runtime, TensorFlow Lite, ML.NET, PyTorch Mobile
- **Quantization Support**: FP32/FP16, INT8, dynamic quantization for mobile
- **Batch Inference**: Multi-sample processing for narrative branching
- **GPU Acceleration**: Optional GPU compute for large models (if available)
- **Async Execution**: Non-blocking inference with cancellation support

### 2. On-Device Serving
- **Bundled Models**: Include lightweight models in build (50-500MB typical)
- **Asset Loading**: Stream models from disk with memory mapping
- **Warmup Paths**: Pre-load models during loading screens
- **Memory Constraints**: Adaptive loading based on available RAM

### 3. Remote Cloud Serving
- **Provider Integration**: AWS SageMaker, Google Vertex AI, Azure ML, custom endpoints
- **Request Batching**: Aggregate client requests for batch inference efficiency
- **Latency Budgeting**: Async inference with client-side queueing
- **Fallback Chains**: Primary (cloud) → secondary (fallback on-device) → default (rule-based)

### 4. Observability & Validation
- **Inference Latency Tracking**: Per-model timing and throughput metrics
- **Input/Output Validation**: Schema checking and anomaly detection on predictions
- **Model Versioning**: A/B testing across model versions in production
- **Confidence Scoring**: Output confidence intervals for risk-aware decisions

## Implementation Pattern

```csharp
// Pseudo-code: Multi-provider model orchestration
class GameplayInference : MonoBehaviour {
    public async Task<PlayerSkillPrediction> PredictPlayerSkill(
        PlayerGameplayData data,
        CancellationToken ct = default)
    {
        // 1. Prepare feature vector
        var features = FeatureExtractor.Extract(data);

        // 2. Try cloud inference with timeout
        try {
            var cloudResult = await RemoteModelClient.InferAsync(
                model: "player-skill-v2",
                input: features,
                timeout: TimeSpan.FromSeconds(3),
                cancellationToken: ct
            );
            if (cloudResult.Confidence > 0.8) {
                return cloudResult;
            }
        } catch (TimeoutException) {
            // Cloud timeout, proceed to fallback
        }

        // 3. Fallback to on-device ONNX model
        var onDeviceResult = await LocalOnnxRuntime.InferAsync(
            modelPath: "Models/player-skill-lite.onnx",
            input: features,
            cancellationToken: ct
        );

        // 4. If both fail, use rule-based heuristic
        if (onDeviceResult == null) {
            return RuleBasedSkillPredictor.Predict(data);
        }

        // 5. Record metrics
        await MetricsCollector.RecordInference(
            modelVersion: "v2",
            latency: sw.ElapsedMilliseconds,
            source: "onDevice"
        );

        return onDeviceResult;
    }
}
```

## Mandates

- **Dual-Path Validation**: Test on-device AND cloud paths independently
- **Baseline Metrics**: Establish accuracy/latency baselines before deployment
- **Graceful Degradation**: Every ML path must have a procedural fallback
- **Model Card Documentation**: Version, training data, fairness metrics per model
- **Privacy Compliance**: No raw player data logged, only aggregated inference stats

## Best Practices

1. **Quantize First**: Ship quantized models to minimize bundle size
2. **Batch When Possible**: Accumulate inference requests for efficiency
3. **Version Aggressively**: Tag models with production deployment dates
4. **Monitor Drift**: Track prediction distribution changes over time
5. **Test Fallbacks**: Ensure rule-based fallback produces acceptable results

## Performance Targets

| Metric | Target | Hard Limit |
|--------|--------|-----------|
| On-device inference | <100ms | <500ms |
| Cloud inference | <1s | <3s |
| Model load time | <5s | <15s |
| Fallback latency | <50ms | <100ms |
| Model bundle size | <200MB | <500MB |

## Resources

- [ONNX Runtime Integration Guide](docs/onnx-integration.md)
- [Model Quantization Workflow](docs/quantization.md)
- [Cloud Provider Setup](docs/cloud-providers.md)
- Example: `examples/behavior-prediction-model.onnx`
