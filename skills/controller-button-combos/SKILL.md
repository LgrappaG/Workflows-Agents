---
name: controller-button-combos
description: Support button combination detection and mapping
risk: low
source: workspace
date_added: '2026-03-24'
usage: Fighting game frame-perfect combo windows, MOBA ability cast sequences, action game attack chains (kick→punch→special), accessibility shortcut layers via button chording, rhythm game hit sequences
avoid: Overlapping combo patterns without priority ordering causing ambiguous matches, consuming inputs for failed combo attempts preventing single-button response, ignoring input timing windows allowing impossible combos, combo detection blocking responsiveness of individual button presses, hardcoded combo depths preventing extensibility
mandates: Detect N-button combos within 300-500ms window, <5ms combo detection latency, >95% accuracy on intentional player combos, <2% false-positive rate, support 2-6 button depth combos
response: Maintain rolling input buffer (circular queue, 20-entry capacity) with precise timestamps, button, Match incoming input stream against combo patterns using trie-based state machine with, Apply spatial constraints (only process combos from single controller, not crossed inputs), Consume matched combo inputs from buffer and fire combo action event, leaving
---

# Controller Button Combos

Support button combination detection and mapping

## Risk Level
**LOW**

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
- Combo actions
- Development workflows

## What NOT to Do
- Combo whiffing
- Incomplete testing
- Deploy without validation
