# SupaFloSho Architecture

## System Overview

```
┌──────────────────────────────────────────────────┐
│                  SupaFloSho Framework                │
├────────────────┬────────────────┬─────────────────┤
│   xText-PRP    │  SuperClaude   │     FloSho      │
│                │                │                 │
│ Context Eng.   │ Commands/AI    │ Test & Docs     │
└────────────────┴────────────────┴─────────────────┘
```

## Component Integration

### 1. Context Layer (xText-PRP)
```
/xt:init "project idea"
         ↓
┌────────────────────────┐
│  Product Requirements  │
│       Prompt (PRP)     │
├────────────────────────┤
│ • User Stories         │
│ • Tech Specs           │
│ • Success Criteria     │
│ • Test Scenarios       │
└────────────────────────┘
```

### 2. Implementation Layer (SuperClaude)
```
PRP Context
    ↓
┌───────────────────────────────────────────────┐
│                   Personas                           │
├──────────────┬───────────────┬─────────────────┤
│  Architect   │   Frontend    │     Backend      │
│              │               │                  │
│ /sc:design   │ /sc:implement │  /sc:implement   │
└──────────────┴───────────────┴─────────────────┘
         ↓              ↓               ↓
    Architecture    UI/UX Code     API/Backend
```

### 3. Testing & Documentation Layer (FloSho)
```
Implemented Features
         ↓
┌───────────────────────────────────────────────┐
│                    FloSho                            │
├──────────────┬───────────────┬─────────────────┤
│  Test Flows  │  Screenshots  │  Documentation   │
│              │               │                  │
│  /fs:flow    │  /fs:capture  │  /fs:document    │
└──────────────┴───────────────┴─────────────────┘
         ↓              ↓               ↓
    E2E Tests    Visual Guide    User Manual
```

## Data Flow

```
1. Context Definition (xText)
   │
   │  PRP with requirements, specs, test scenarios
   ↓
2. Smart Implementation (SuperClaude)  
   │
   │  Personas read PRP → Execute commands
   ↓
3. Automated Testing (FloSho)
   │
   │  Test scenarios from PRP → Visual flows
   ↓
4. Documentation Generation
   │
   │  Screenshots + Steps = User Guide
   ↓
5. Iteration Loop
```

## Command Integration Map

```yaml
Context Commands (xText):
  /xt:init: "Initialize project with PRP"
  /xt:context: "Manage context window"
  /xt:prp: "Generate/update PRP"
  /xt:validate: "Validate against PRP"

Implementation Commands (SuperClaude):
  /sc:implement: "Build features from PRP"
  /sc:design: "Design architecture"
  /sc:analyze: "Analyze code/issues"
  /sc:test: "Generate unit tests"
  # ... 12 more commands

Testing Commands (FloSho):
  /fs:flow: "Define test flow from PRP"
  /fs:capture: "Screenshot UI states"
  /fs:api: "Test API endpoints"
  /fs:document: "Generate documentation"
```

## MCP Server Integration

```
┌───────────────────────────────────────────────┐
│              SupaFloSho Core                         │
└───────────────────┬───────────────────────────┘
                    │
        ┌──────────┴──────────┐
        │    MCP Servers      │
        ├────────────────────┤
        │ Context7 - Docs     │
        │ Sequential - Think  │
        │ Magic - UI Gen      │
        │ Playwright - Test   │
        └────────────────────┘
```

## Example Workflow

### Building a Chat Application

```bash
# 1. Context Phase (xText)
/xt:init "Real-time chat app with rooms and file sharing"
# Generates PRP with:
# - User stories (join rooms, send messages, share files)
# - Tech specs (WebSocket, React, Node.js)
# - Test scenarios (message flow, file upload, room creation)

# 2. Implementation Phase (SuperClaude)
/sc:design "chat architecture"
# Architect persona designs WebSocket server, room management

/sc:implement "chat backend with rooms"
# Backend persona builds API endpoints, WebSocket handlers

/sc:implement "chat UI with message list"
# Frontend persona creates React components

# 3. Testing Phase (FloSho)
/fs:flow "Complete chat experience"
# FloSho runs through:
# - Join room → Screenshot
# - Send message → Screenshot  
# - Upload file → Screenshot
# - Leave room → Screenshot

# 4. Documentation Generated
# - User guide with screenshots
# - API documentation
# - Architecture diagrams
```

## Benefits of Integration

### 1. **Contextual Awareness**
- Personas understand PRP requirements
- Commands execute with project context
- Tests align with defined scenarios

### 2. **Automated Documentation**
- FloSho captures implementation visually
- Documentation matches actual features
- No manual screenshot taking

### 3. **Quality Assurance**
- PRP defines success criteria
- SuperClaude implements to spec
- FloSho validates visually

### 4. **Reduced Redundancy**
- One context definition (PRP)
- Shared by all components
- No repeated specifications

### 5. **Seamless Workflow**
- Natural progression: Define → Build → Test
- Each phase builds on previous
- Complete development cycle

---

*SupaFloSho: Where AI development becomes a coordinated symphony 🎼*