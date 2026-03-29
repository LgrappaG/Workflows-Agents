---
name: development-live-collaboration-sessions
description: Persistent multi-user editor sessions with deterministic conflict resolution
risk: high
source: workspace
date_added: '2026-03-24'
usage: Co-op multiplayer level design with 3-5 simultaneous artists, distributed game jam scenarios, mentoring sessions with live code/scene sharing, remote pair programming on gameplay systems with async updates
avoid: Session desynchronization under high edit frequency from missing message delivery, dropped edits during network hiccup causing silent data loss, competing changes creating invalid game state (orphaned references, type mismatch), session state growing unbounded in memory without periodic cleanup, edit conflicts not resolved deterministically causing different clients to diverge
mandates: Maintain ≥5 concurrent editor connections, achieve 99%+ state consistency across all clients, persist session data across ≥30 minute sessions, resolve competing edits in <1s with deterministic outcome.
response: 'Initialize session state synchronization channel with per-user subscription to entity change streams, Detect competing writes via operational transformation: assign unique client ID to each, Implement automatic conflict resolution: prioritize edits by (timestamp, client_id) tuple for deterministic, Periodically checkpoint session state (every 5 min or 100 edits) to enable'
---

# Live Collaboration Sessions

Persistent multi-user editor sessions with operational transformation, deterministic conflict resolution, and crash recovery.

## Risk Level
**HIGH**

## Core Rules
- Maintain >=5 concurrent editor connections
- Achieve 99%+ state consistency across clients
- Persist session data across >=30 minute sessions
- Resolve competing edits in <1s deterministically

## Response Pattern

1. Initialize session sync with subscription channels
2. Detect competing writes via OT with Lamport timestamps
3. Apply automatic conflict resolution deterministically
4. Checkpoint session state periodically for recovery

## Usage
- Co-op multiplayer level design (3-5 artists)
- Distributed game jam scenarios
- Mentoring sessions with live code/scene sharing
- Remote pair programming on gameplay systems

## What NOT to Do
- Session desynchronization under high frequency
- Dropped edits during network hiccup
- Competing changes creating invalid game state
- Unbounded session state memory growth
- Non-deterministic conflict resolution

