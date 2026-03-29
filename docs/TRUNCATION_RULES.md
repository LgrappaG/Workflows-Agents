# Truncation Rules for .agents Framework
# Version: 1.0
# Applies to: Skill descriptions, workflow output, response content

## Global Rules

### Content Size Limits
- **Skill description max:** 200 characters (was 300+, now compressed)
- **Workflow description max:** 150 characters
- **Code snippet max:** 20 lines (show first 20, indicate "...+N more lines")
- **Output response max:** 2000 characters (comprehensive but concise)

### Array/List Limits
- **Array display max:** 10 items
- **If > 10 items:** Show first 5 + text indicator "...and N more"
- **Nested object max:** 3 levels deep
- **Related links max:** 5 items (collapsible)

### Metadata Truncation
- **Long field values:** Collapse with "→" indicator
- **Example sections:** Show 1 example + "See resources/ for more"
- **Mandates/Guidelines:** Bullet points only, no paragraphs
- **Metadata repeated:** De-duplicate across request

---

## Skill-Specific Truncation Rules

### Type: Specialist Skills (28 total)

**Before:**
```
description: "Activate when working with C# development, Unity scripting, .NET architecture, or any task requiring deep C# expertise including performance optimization, design patterns, and Unity-specific best practices."
[54 words, 315 characters]
```

**After (Truncated):**
```
description: "Senior C# dev for Unity scripting, architecture, performance & patterns"
[12 words, 78 characters]
```

**Rule:** One-liner max. Move detailed usage to inline `usage:` and `avoid:` fields.

---

### Type: Workflow Descriptions (63 total)

**Before:**
```
title: "Debugging and Profiling Unity Performance Issues"
description: "A comprehensive workflow that guides you through identifying, 
analyzing, and resolving performance bottlenecks in Unity, including GPU 
profiling, memory analysis, and optimization strategies for mobile, VR, and 
desktop platforms."
[42 words]
```

**After (Truncated):**
```
title: "Debug Performance Issues"
description: "Profile GPU/memory bottlenecks → Optimize for mobile/VR/desktop"
[12 words]
```

**Rule:** Title max 5 words. Description = "Symptom → Resolution" format.

---

## Response Content Rules

### Rule 1: Long Output Truncation
**Trigger:** If output > 2000 characters  
**Action:** Summarize to 2000 chars max + append:
```
...

[Summary truncated. See full documentation in resources/ or docs/]
Full content: [link or reference]
```

**Example:**
```
✅ Found 47 optimization issues:
  1. GC allocations in Update() → [8 instances]
  2. Missing GetComponent() caching → [12 instances]
  3. LINQ in hot paths → [5 instances]
  ...and 22 more issues

[See detailed profiling report: docs/PROFILING_FULL.md]
```

### Rule 2: Array/List Display
**Trigger:** If array has > 10 items  
**Action:** Show first 5 + count indicator

**Example - Before:**
```
Available skills: [28 items]
- accessibility-expert
- addressables-specialist
- animator-specialist
- audio-designer
- backend-specialist
- ... [23 more]
```

**Example - After:**
```
Available skills (28 total):
  1. accessibility-expert
  2. addressables-specialist
  3. animator-specialist
  4. audio-designer
  5. backend-specialist
  
...and 23 more. Use 'agents list skills' for full list.
```

### Rule 3: Code Snippet Truncation
**Trigger:** If code block > 20 lines  
**Action:** Show first 20 + line count indicator

**Example:**
```csharp
public class PlayerController : MonoBehaviour
{
    private Rigidbody _rb;
    private InputHandler _input;
    
    private void Awake()
    {
        _rb = GetComponent<Rigidbody>();
        _input = GetComponent<InputHandler>();
    }
    
    // [+45 more lines - see resources/PlayerController.cs for full code]
}
```

### Rule 4: Nested Object Depth
**Trigger:** If nested object depth > 3 levels  
**Action:** Collapse at level 3 with indicator

**Example - Before:**
```json
{
  "skill": {
    "metadata": {
      "dependencies": {
        "optional": {
          "engine": "unity-3d"
        }
      }
    }
  }
}
```

**Example - After:**
```json
{
  "skill": {
    "metadata": {
      "dependencies": "→ [see resources/]"
    }
  }
}
```

---

## Metadata Truncation

### YAML Frontmatter Rules

**Default (include these):**
```yaml
---
name: skill-name
description: One-liner
risk: low|medium|high
source: workspace|anthropic|community
date_added: 'YYYY-MM-DD'
---
```

**Optional (truncate/collapse):**
```yaml
usage: Brief comma-separated triggers
avoid: Brief comma-separated anti-patterns
depends_on: [related-skills]  # only if > 0
see_also: [related-docs]      # only if > 0
version: 7.0.3                # auto-managed
updated: '2026-03-21'         # auto-managed
```

**Rule:** If field empty or generic, omit entirely.

---

## Response Format Rules

### Rule: Always Include
1. ✅ Immediate actionable answer (first 2 sentences)
2. ✅ Key points (bullets, max 5)
3. ✅ Next steps or related resources

### Rule: Conditionally Include
4. ❓ Detailed examples (only if < 20 lines)
5. ❓ Full error traces (summarize + reference)
6. ❓ Architecture diagrams (link to resources/)

### Rule: Omit (Link Instead)
7. ❌ Verbose explanations > 500 chars
8. ❌ Full API documentation (link to Unity Docs)
9. ❌ Multi-page tutorials (link to resources/)

**Format Indicator:** Use "→" to show collapsed content
```
"→ [See detailed guide: docs/ARCHITECTURE.md]"
```

---

## Implementation Checklist

### Phase 1: Apply to Existing Skills
- [ ] Review all 28 SKILL.md files
- [ ] Apply 1-liner compression to descriptions
- [ ] Extract verbose content to `resources/` subdirectories
- [ ] Update `mcp_config.json` with rules

### Phase 2: Build Tooling
- [ ] Script: `scripts/validate-compression.js`
  - Checks description length < 200 chars
  - Warns if code snippets > 20 lines
  - Validates truncation indicators
- [ ] Script: `scripts/measure-tokens.js`
  - Counts tokens before/after optimization
  - Reports savings percentage
  - Identifies high-impact optimizations

### Phase 3: Documentation
- [ ] Skill authors guide (use compressed format)
- [ ] LLM system prompt updates
- [ ] Backward compatibility notes

### Phase 4: Monitoring
- [ ] Track token usage over time
- [ ] Gather feedback from users
- [ ] Adjust rules based on real-world data

---

## Configuration

Add to `.agents/mcp_config.json`:

```json
{
  "version": "7.0.3",
  "truncation": {
    "enabled": true,
    "rules_file": "docs/TRUNCATION_RULES.md",
    "max_output_chars": 2000,
    "max_array_items": 10,
    "max_code_lines": 20,
    "max_nested_depth": 3,
    "collapse_indicator": "→",
    "cache_ttl_seconds": 3600
  }
}
```

---

## Testing & Validation

### Before Deployment
```bash
# Measure token reduction
agents measure-tokens before after

# Validate all skills comply
agents validate-compression

# Test with actual LLM
agents test-truncation --agent=claude
```

### Expected Results
- Skill definitions: -40% to -60% tokens
- Response content: -20% to -30% tokens
- Overall framework: -30% to -50% tokens
- **Zero functionality loss**

---

## Appendix: Compression Examples

### Example 1: C# Master Skill

**Before:** 254 tokens
```markdown
# C# Master
You are a **Senior C# Developer**...
[long description]

## Use this skill when
- Writing C# code
- Designing architecture
- Resolving bugs
- Optimizing performance
- Implementing systems

## Core Mandates
### 1. Modern C# Standards
- Use C# 10+ features
- XML documentation
[continues...]
```

**After:** 78 tokens (-69%)
```markdown
---
name: csharp-master
description: Senior C# dev for Unity, architecture, GC optimization & patterns
usage: C# coding, refactoring, SOLID, performance tuning
avoid: Non-C# tasks, game design
mandates: C# 10+, SOLID, no GetComponent in Update, object pooling
---

See resources/CSHARP_MANDATES.md for details.
```

### Example 2: Workflow Description

**Before:** 45 words
```
A comprehensive workflow that guides you through identifying, analyzing, and 
resolving performance bottlenecks in Unity, including GPU profiling, memory 
analysis, and optimization strategies for mobile, VR, and desktop platforms.
```

**After:** 11 words (-76%)
```
Profile GPU/memory → Optimize for mobile/VR/desktop
```

---

## Questions?

See: `docs/TOKEN_OPTIMIZATION.md` (comprehensive guide)  
Issues: Create GitHub issue with `token-optimization` tag
