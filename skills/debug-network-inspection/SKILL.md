---
name: debug-network-inspection
description: Capture and analyze 100% of network traffic with protocol classification
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Network protocol debugging for multiplayer gameplay desynchronization, bandwidth optimization analysis before mobile release, latency detection in production builds with live telemetry, multi-client communication verification for deterministic systems
avoid: Interception overhead blocking realtime traffic causing frame drops, ring buffer overflow dropping older packets when inspection backlog builds, timestamp drift >1ms across distributed clients breaking latency correlation, false positive latency spikes from measurement backlog vs. actual network delay, incomplete message capture due to fragmentation not being reassembled
mandates: Capture 100% of network traffic with <2% CPU overhead, track message latency with <10ms accuracy via timestamp correlation, inspect ≥10,000 buffered messages without data loss, auto-classify protocol versions.
response: Install network interception at transport layer (socket layer for TCP/UDP, or QUIC, Decode protocol headers to extract routing metadata (message type, sequence number, timestamp),, Correlate message pairs (request-response, publish-subscribe) by tagging with session ID and sequence, Generate latency histogram on-demand (p50, p95, p99) and identify outliers >100ms for
---

# Network Inspection

Capture and analyze network traffic with real-time protocol classification and latency analysis.

## Risk Level
**MEDIUM**

## Core Rules
- Capture 100% of network traffic
- Track message latency with <10ms accuracy
- Inspect buffered messages without data loss
- Auto-classify protocol versions

## Response Pattern

1. Install transport-layer interception
2. Decode protocol headers and metadata
3. Correlate message pairs with timestamps
4. Generate latency histograms on-demand

## Usage
- Network protocol debugging for multiplayer
- Bandwidth optimization analysis
- Latency detection in production builds
- Multi-client communication verification

## What NOT to Do
- Blocking realtime traffic
- Ring buffer overflow dropping packets
- Timestamp drift across clients
- Incomplete message capture
- Network bottleneck creation

