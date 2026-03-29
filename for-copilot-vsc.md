---
name: MCP-FOR-UNITY Configuration for VS Code Copilot
description: Complete setup and integration guide for controlling Unity projects via MCP-FOR-UNITY directly from Copilot
---

# 🎮 MCP-FOR-UNITY for VS Code Copilot

Direct Unity project management through Copilot using the MCP-FOR-UNITY package. No intermediate bridge needed.

---

## 📋 Architecture Overview

```
┌─────────────────────────────────────────┐
│    VS Code Copilot Chat                 │
└────────────┬────────────────────────────┘
             │ MCP Protocol (HTTP)
             ↓
┌─────────────────────────────────────────┐
│    MCP-FOR-UNITY Server (localhost:8080)│
│    Runs inside Unity Editor             │
└────────────┬────────────────────────────┘
             │ IPC/Editor API
             ↓
┌─────────────────────────────────────────┐
│    Unity Editor (Running)               │
│    Modifies scenes, assets, components  │
└─────────────────────────────────────────┘
```

---

## ✅ Quick Setup (2 Steps)

### Step 1: Install MCP-FOR-UNITY Package

In your **Unity Project**, open Package Manager:
```
Window → Package Manager → Search "mcp-for-unity" → Install latest
```

Alternatively, edit `Packages/manifest.json`:
```json
{
  "dependencies": {
    "com.mcpforunity.mcp": "https://github.com/peterbrittain/mcp-for-unity.git#main"
  }
}
```

### Step 2: Enable HTTP Server in Unity

In **Unity Editor**:
```
Window → MCP for Unity → Connection → Toggle HTTP Server ON
```

You'll see the confirmation:
```
MCP-FOR-UNITY: Started local HTTP server in terminal: http://localhost:8080 ...
```

**Keep Unity running.** As long as the Editor is open, Copilot can control it.

---

## ✨ Capabilities

Once connected to MCP-FOR-UNITY, you can ask Copilot to:

✅ **Scene Management**
- Create/destroy GameObjects
- Load/save scenes
- Modify hierarchy

✅ **Component Operations**
- Add/remove components
- Update properties
- Access inspector data

✅ **Asset Management**
- Import assets
- Organize folders
- Inspect prefabs

✅ **Project Control**
- Read project settings
- Execute MCP tools
- Inspect scene state

---

## 🚀 Usage Examples

In **Copilot Chat**:

```
"Create a GameObject named Player"
"Add a Rigidbody component to the Cube"
"Change the Main Camera position to (0, 5, -10)"
"List all assets in Assets/Prefabs"
"Import the character model from Assets/Models"
"Create a red sphere at origin with physics enabled"
```

Copilot will:
1. Detect MCP-FOR-UNITY running at localhost:8080
2. Use MCP tools to execute commands
3. Modify your Unity project in real-time
4. Return confirmation

---

## 📖 Configuration Files

### mcp_config.json
Configures the MCP server connection:
```json
{
  "mcpServers": {
    "mcp-for-unity": {
      "type": "http",
      "url": "http://localhost:8080",
      "description": "MCP-FOR-UNITY HTTP Server (started automatically by Unity Editor)",
      "env": {
        "UNITY_PROJECT_PATH": "${workspaceFolder}"
      }
    }
  }
}
```

### copilot-instructions.md
Agent behavior instructions (YAML frontmatter + guidelines)

### MCP_FOR_UNITY_SETUP.md
Detailed technical setup documentation

### package.json
Project metadata (no dependencies required)

---

## 📋 Available Workflows

Type `/` in Copilot to access:

| Workflow | Purpose |
|----------|---------|
| `/unity-3d-setup` | Bootstrap new 3D project |
| `/vibe-project-init` | Initialize VR/XR project |
| `/unity-mcp-check` | Verify MCP connection status |
| `/code-review-swarm` | Deep code review (4-role) |
| `/unity-brainstorm-feature` | Feature design validation |

---

## 🧠 Available Skills

Type `@` in Copilot to access:

| Skill | Expertise |
|-------|-----------|
| `@unity-3d-expert` | 3D rendering, URP, HDRP, NavMesh, physics |
| `@csharp-master` | C# scripting, memory optimization, patterns |
| `@vr-xr-specialist` | VR/AR, XR Interaction Toolkit v3 |
| `@brainstorming` | Feature ideation, architecture validation |
| `@code-reviewer` | Production code review |

---

## 🔧 Connection Verification

In **Copilot**, run:
```
/unity-mcp-check
```

Expected output:
```
✅ MCP-FOR-UNITY connection verified
✅ Scene info accessible
✅ Ready to execute tool calls
```

---

## ❌ Troubleshooting

**"MCP-FOR-UNITY server not found"**
- Ensure Unity Editor is running and visible
- Check `Window → MCP for Unity → Connection` 
- Verify HTTP Server toggle is ON
- Check localhost:8080 is not blocked by firewall

**"Tool calls timeout"**
- Ensure Unity is not compiling (watch bottom-right)
- Disable/enable HTTP Server in Connection window
- Check Unity Console for errors

**"Package not found in Package Manager"**
- Update Package Manager to latest version
- Clear pkg-cache: `%AppData%\..\LocalLow\Unity\cache`
- Try installing from git URL directly

---

## 🎯 Advanced Usage

### Combining Skills & Workflows

1. **Design**: Use `@brainstorming` to validate feature idea
2. **Implement**: Use `@csharp-master` to write scripts
3. **Build**: Use Copilot + MCP to create scenes in real-time
4. **Review**: Use `@code-reviewer` for quality checks

### Example: Building an NPC System

```
"@brainstorming: Design an NPC system with traits and dialogue"

[Design approved]

"@csharp-master: Write NPCBrain.cs with behavior tree"

[Code written]

"Create an NPC GameObject with the NPCBrain component"

[Scene updated via MCP]

"@code-reviewer: Review the NPC implementation"

[Review report generated]
```

---

## 📁 File Structure

```
.agents/
├── copilot-instructions.md       ← Agent behavior rules
├── mcp_config.json               ← MCP server endpoint
├── MCP_FOR_UNITY_SETUP.md        ← Full setup guide
├── package.json                  ← Project metadata
├── skills/                       ← AI skills directory
│   ├── brainstorming/
│   ├── csharp-master/
│   ├── unity-3d-expert/
│   ├── vr-xr-specialist/
│   └── ...
├── workflows/                    ← Workflow templates
│   ├── unity-3d-setup.md
│   ├── vibe-project-init.md
│   └── ...
└── scripts/                      ← Utility scripts
```

---

## 🔗 Environment Variables

Configure behavior via environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `UNITY_PROJECT_PATH` | `${workspaceFolder}` | Project root directory |
| `MCP_TIMEOUT` | `30000` | Tool call timeout (ms) |
| `MCP_AUTO_RECONNECT` | `true` | Reconnect on disconnect |
| `MCP_LOG_LEVEL` | `info` | Logging verbosity |

---

## ✅ Checklist: Getting Started

- [ ] Unity project created/opened
- [ ] MCP-FOR-UNITY package installed
- [ ] HTTP Server enabled in Unity (Window → MCP for Unity)
- [ ] VS Code workspace contains `.agents/` folder
- [ ] Copilot extension installed in VS Code
- [ ] Open Copilot Chat (`Ctrl+Shift+I`)
- [ ] Type `/unity-mcp-check` to verify connection

---

## 🎮 Example Commands

### Create Your First Controlled Scene

```
/unity-3d-setup
```

Sets up a new 3D project with proper structure.

### Test Real-Time Control

```
"Create a cube named TestCube at position (0, 1, 0) with a Rigidbody"
```

You'll immediately see the cube appear in the Unity Scene view.

### List Project Assets

```
"Show me all prefabs in the Assets/Prefabs folder"
```

Copilot will enumerate and describe them.

---

## 📚 Learning Path

1. **Beginner**: Run `/unity-mcp-check` → Create simple GameObjects
2. **Intermediate**: Use `/unity-3d-setup` → Build scenes with Copilot
3. **Advanced**: Combine `@brainstorming` + `@csharp-master` + MCP tools
4. **Expert**: Vibe Coding workflow (design→implement→test→review)

---

## 🔗 External Resources

- **MCP-FOR-UNITY GitHub**: https://github.com/peterbrittain/mcp-for-unity
- **Model Context Protocol**: https://modelcontextprotocol.io
- **Unity Documentation**: https://docs.unity.com
- **.agents Project**: See `skills/` and `workflows/` folders

---

## 💡 Tips & Tricks

**Faster Development**
- Keep both VS Code and Unity visible side-by-side
- Use Copilot to create prefabs and scenes in batch
- Combine multiple tool calls in one request

**Reliability**
- If tools timeout, check Unity Console for errors
- Always verify MCP connection before making changes
- Keep HTTP Server continuous (don't toggle it repeatedly)

**Best Practices**
- Use descriptive GameObject names for clarity
- Organize assets in consistent folder hierarchy
- Test MCP commands on non-production scenes
- Commit frequently when using automated tools

---

## ❓ FAQ

**Q: Can I control multiple Unity instances?**  
A: Currently, MCP-FOR-UNITY runs on a single port (8080) per machine. Multiple instances require custom port forwarding.

**Q: Does this work offline?**  
A: No, requires Unity Editor running with HTTP Server enabled.

**Q: Can I use this in build pipelines?**  
A: Not directly. Requires running Editor. For CI/CD, export MCP tool definitions instead.

**Q: Is there a performance hit?**  
A: Minimal. MCP calls are asynchronous and don't block the Editor.

**Q: Can I extend MCP-FOR-UNITY?**  
A: Yes. MCP-FOR-UNITY is extensible with custom tools via the official API.

---

## 🚀 Ready to Start?

1. Install MCP-FOR-UNITY in your Unity project
2. Enable HTTP Server in Connection window
3. Open VS Code Copilot
4. Type: `/unity-mcp-check`
5. Start building! 🎮✨

---

**Last Updated**: March 19, 2026  
**Status**: Production Ready  
**Support**: See MCP-FOR-UNITY GitHub Issues
