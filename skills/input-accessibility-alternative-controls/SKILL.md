---
name: input-accessibility-alternative-controls
description: Provide accessible control schemes for diverse player needs
risk: medium
source: workspace
date_added: '2026-03-24'
usage: Disability support for motor impairment (switch control), visual impairment (screen reader + high contrast), hearing impairment (visual feedback instead of audio cues), elderly players with slower reflexes, educational accessibility (school settings)
avoid: Accessibility bolted on late causing gameplay conflicts, hiding accessibility settings in obscure menus, inaccessible remapping UI (small fonts, low contrast), assuming controller-only play excluding keyboard-only users, time-based challenges without pause allowing switch users to keep up, audio-only feedback with no visual alternative
mandates: WCAG 2.1 Level AA compliance, 100% game functions via alternative inputs (no mandatory multi-button combos), key repeat rate 0-100 keys/sec configurable, hold-to-toggle dwell time 0.2-2.0s, tested with 3+ accessibility tools
response: Expose all game actions as rebindable inputs removing mandatory combos (e, g, , allow single-key 'reload' instead of Shift+R), support switch control via hold-to-toggle, 2-2
---

# Input Accessibility Alternative Controls

Provide accessible control schemes for diverse player needs

## Risk Level
**MEDIUM**

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
- Accessibility support
- Development workflows

## What NOT to Do
- Incomplete accessibility
- Incomplete testing
- Deploy without validation
