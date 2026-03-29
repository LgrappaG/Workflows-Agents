# Troubleshooting Guide

## Common Issues & Solutions

### Build Issues

**"Unity Build fails with 'IL2CPP error'"**
→ 1) Clear Library folder (`rm -rf Library`)
→ 2) Reimport assets (`Assets → Reimport All`)
→ 3) Rebuild project

**"APK too large (>150MB)"**
→ Use `/build-size-optimization` workflow
→ Key fixes: Enable compression, strip managed code, remove unused assets

**"iOS build rejected: 'Inadequate Encryption'"**
→ Add to Info.plist: `NSLocalNetworkUsageDescription` (Bonjour)
→ Or: Use TLS 1.2+ only

---

### Performance Issues

**"Game FPS drops to 30 after 10 mins play"**
→ Profile: `Window → Profiler`
→ Check: GC.Alloc (garbage), Memory(leaks), Physics time
→ Use: `@profiling-specialist` skill

**"Mobile device overheats, causes throttling"**
→ Reduce quality: Disable shadows, cut draw calls
→ Implement: Dynamic quality scaling based on temp
→ Profile: Check GPU time, thermal monitoring

**"Multiplayer game lags with 20 players"**
→ Use: `/load-testing-setup` to identify breaking point
→ Solutions: Reduce network update rate, implement spatial culling, shard server

---

### Mobile-Specific

**"Android app crashes immediately on old devices"**
→ Check MinAPI setting (should be 28+)
→ Use: `@mobile-expert` for device-specific debugging
→ Test on: Galaxy A12 (low-end), Galaxy A52 (mid-range)

**"iOS handles notches weird on some models"**
→ Use: `Screen.safeArea` for UI placement
→ Test on: iPhone 12 mini, iPhone 14 Pro Max

---

### Network/Backend

**"Players lose data randomly"**
→ Issue: Likely no authoritative server validation
→ Fix: Implement server-side verification for all player actions
→ Use: `@backend-specialist` for architecture review

**"Database queries timeout"**
→ Profile: Check slow query log
→ Likely: N+1 queries or missing indexes
→ Solution: Add indexes on queried fields, use JOIN instead of loop

---

### Localization

**"Japanese text displays as boxes/squares"**
→ Check: CJK font configured, font atlas size 4096x4096+
→ Verify: TextMesh Pro settings include CJK fallback

**"Text overflows UI in German/Spanish"**
→ German +35% longer than English
→ Use: Flexible layout groups, enable text wrapping, increase container width

---

### Accessibility

**"Colorblind players say they can't distinguish health from enemies"**
→ Add icon + symbol, not just color
→ Test: use ColorOracle simulator (free)

**"Deaf players miss audio alerts"**
→ Add visual feedback: Screen flash, on-screen icon
→ Implement: Haptic feedback on vibration-capable devices

---

## When to Use Each Skill

| Problem | Skill |
|---------|-------|
| Performance lag | `@profiling-specialist` |
| iOS/Android issues | `@mobile-expert` |
| Game balance complaints | `@game-design-specialist` |
| Server crashes | `@backend-specialist` |
| Accessibility concerns | `@accessibility-expert` |
| Deployment issues | `@devops-engineer` |
| Security vulnerabilities | `@security-specialist` |

## Getting More Help

- `/troubleshooting-guide` - This guide
- `/project-health-check` - Run diagnostics
- `/technical-debt-audit` - Find architectural issues
- Community: GitHub Issues, Discord

---

Last updated: 2026-03-19
