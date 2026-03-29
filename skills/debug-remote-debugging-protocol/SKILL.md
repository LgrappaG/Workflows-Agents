---
name: debug-remote-debugging-protocol
description: Implement remote debugging protocol for networked dev tools
risk: high
source: workspace
date_added: '2026-03-24'
usage: Cross-device debugger attachment, CI/CD cloud build remote debugging, multi-developer simultaneous breakpoint sessions, embedded device debugging via network tunnel
avoid: Protocol version mismatch causing hard disconnect without fallback, synchronous blocking calls without timeout (max 5s), uncompressed JSON flooding network with >1MB/s, breakpoint state becoming orphaned after code hot-reload, connection pooling exhaustion from abandoned sessions
mandates: Maintain protocol version compatibility with fallback negotiation, achieve <100ms command latency, support ≥2 simultaneous debugger clients, preserve breakpoint state across network interruptions.
response: Execute handshake negotiation to validate protocol version compatibility and establish baseline feature, Configure transport layer with message compression (zlib) to reduce bandwidth overhead to, Implement bidirectional heartbeat every 5s with exponential backoff retry (1s, 2s, 4s,, Validate breakpoint consistency by comparing checksums after each code reload to detect
---

# Debug Remote Debugging Protocol

Implement remote debugging protocol for networked dev tools

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
- Remote debugging
- Development workflows

## What NOT to Do
- Protocol versioning issues
- Incomplete testing
- Deploy without validation
