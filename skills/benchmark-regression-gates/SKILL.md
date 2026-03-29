---
name: benchmark-regression-gates
description: "Define regression gates that fail CI when benchmark drift crosses thresholds"
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

# benchmark-regression-gates

## Overview

Define quantitative performance gates in CI/CD that automatically fail builds when key metrics regress—ensuring framework performance doesn't degrade as it scales. This skill makes performance a first-class requirement alongside functionality.

## Key Capabilities

### 1. Benchmark Definition
- **Metric Types**: Token compression, skill load time, memory usage, validation throughput
- **Baseline Management**: Establish baselines per branch/commit/release
- **Threshold Tiers**: Soft (warning), hard (fail), critical (immediate rollback)
- **Device Coverage**: Test on reference hardware (MacBook Pro 2023, RTX 4070, etc.)
- **Regression Detection**: Statistical significance testing with 95% confidence

### 2. CI/CD Integration
- **Automated Execution**: Run benchmarks on every PR to main
- **Build Artifacts**: Store historical benchmark data for trend analysis
- **Parallel Testing**: Execute benchmarks across multiple environments simultaneously
- **Cached Baselines**: Git-tracked baseline files for deterministic comparisons
- **PR Comments**: Inline benchmark reports showing delta vs. baseline

### 3. Performance Monitoring
- **Real-Time Alerts**: Slack/email on regressions during development
- **Historical Trends**: Dashboard showing performance evolution over time
- **Profiling Data**: Collect flame graphs and memory dumps for investigation
- **Cost Analysis**: Token spend and API costs tracked per feature
- **Correlation Analysis**: Link regressions to specific commits/authors

### 4. Remediation Workflow
- **Bisect Support**: Automated binary search to find regressing commit
- **Performance Lab**: Dedicated environment for deep profiling and optimization
- **Rollback Automation**: Automatic revert on critical regressions (with approval)
- **Optimization Tips**: Suggest common fixes based on regression type
- **Communication**: Notify relevant maintainers and track resolution time

## Gate Thresholds

```yaml
gates:
  token_compression:
    metric: "average_tokens_per_skill"
    baseline: 498  # tokens
    warning: "102%"  # 508 tokens
    failure: "105%"  # 523 tokens
    critical: "110%"  # 548 tokens

  skill_load_time:
    metric: "p99_skill_load_ms"
    baseline: 45  # milliseconds
    warning: "110%"  # 50ms
    failure: "120%"  # 54ms
    critical: "150%"  # 68ms

  validation_throughput:
    metric: "validations_per_second"
    baseline: 820  # skills/sec
    warning: "90%"  # 738/sec
    failure: "85%"  # 697/sec
    critical: "80%"  # 656/sec

  memory_footprint:
    metric: "peak_memory_mb"
    baseline: 256  # MB
    warning: "110%"  # 282 MB
    failure: "120%"  # 307 MB
    critical: "150%"  # 384 MB
```

## Implementation Pattern

```csharp
// Pseudo-code: Gate enforcement in CI
namespace BenchmarkGates {
    public class RegressionGateValidator {
        public async Task<GateResult> ValidateMetrics(
            string metric,
            float currentValue,
            GateThresholds thresholds,
            CancellationToken ct = default)
        {
            var baseline = await BaselineStore.Get(metric);
            var percentChange = (currentValue / baseline - 1) * 100;

            var result = new GateResult {
                Metric = metric,
                Baseline = baseline,
                Current = currentValue,
                PercentChange = percentChange,
                Status = DetermineStatus(percentChange, thresholds)
            };

            if (result.Status == GateStatus.Critical) {
                await NotifyMaintainers(result);
                await AttemptAutoRevert(thresholds.CommitSha);
            } else if (result.Status == GateStatus.Failure) {
                throw new RegressionGateException(result);
            }

            return result;
        }

        private GateStatus DetermineStatus(
            float percentChange,
            GateThresholds thresholds)
        {
            if (percentChange >= thresholds.Critical) return GateStatus.Critical;
            if (percentChange >= thresholds.Failure) return GateStatus.Failure;
            if (percentChange >= thresholds.Warning) return GateStatus.Warning;
            return GateStatus.Pass;
        }
    }
}
```

## Mandates

- **Deterministic Baselines**: Baselines tracked in git, reviewable in PRs
- **Noisy Metric Handling**: Use median/p99 instead of averages for flaky benchmarks
- **Historical Context**: Preserve baseline history for trend analysis (100+ releases)
- **Override Policy**: Manual overrides require code review + maintainer approval
- **Public Transparency**: All benchmark results publicly visible in PR comments

## Best Practices

1. **Start Conservative**: Thresholds should accommodate 1-2% natural variation initially
2. **Profile Before Optimizing**: Use flame graphs, not guesses, for tuning
3. **Test on Target Hardware**: Benchmark on real devices, not just CI VMs
4. **Document Regressions**: Link to investigation issues, not just violations
5. **Celebrate Improvements**: Highlight positive regressions as wins

## Sample Gate Report

```
═══════════════════════════════════════════════════════════════
  BENCHMARK REGRESSION GATES - PR #512
═══════════════════════════════════════════════════════════════

✅ token_compression:      498 → 502 (+0.8%)        [PASS]
✅ skill_load_time:        45ms → 44ms (-2.2%)      [PASS]
⚠️  validation_throughput: 820 → 798 (-2.7%)        [WARNING]
✅ memory_footprint:       256 → 257 MB (+0.4%)     [PASS]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  DECISION: ✅ APPROVED (1 warning acceptable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Resources

- [Benchmark Configuration Reference](docs/benchmark-config.md)
- [Gate Threshold Tuning Guide](docs/threshold-tuning.md)
- [Regression Investigation Playbook](docs/investigation-guide.md)
- [Performance Lab Setup Guide](docs/perf-lab-setup.md)
