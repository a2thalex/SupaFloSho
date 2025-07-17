# SupaFloSho Example: Todo App

This example demonstrates the complete SupaFloSho workflow by building a todo application from scratch.

## The Power of Integration

Watch how all three frameworks work together:

1. **xText-PRP** defines what we're building
2. **SuperClaude** implements it intelligently
3. **FloSho** tests and documents everything

## Step 1: Initialize with Context

```bash
/xt:init "Build a collaborative todo app with real-time sync, categories, and team sharing"
```

This generates a complete PRP (see `todo-app-prp.json`) with:
- User stories for all features
- Technical architecture (React + Node.js + PostgreSQL)
- API specifications
- Test scenarios
- UI/UX guidelines

## Step 2: Implementation with SuperClaude

### Backend Development
```bash
# Backend persona reads PRP, knows we need PostgreSQL + real-time
/sc:implement "todo API with CRUD operations"
# → Creates models with categories and sharing
# → Sets up WebSocket for real-time sync
# → Implements team collaboration endpoints

/sc:implement "authentication and team management"
# → JWT authentication matching PRP security specs
# → Team invitation system as defined in user stories
```

### Frontend Development
```bash
# Frontend persona reads PRP UI specifications
/sc:design "todo app interface"
# → Creates component architecture
# → Follows PRP design system (Material-UI)

/sc:implement "todo list component with categories"
# → Builds exactly what PRP specifies
# → Includes real-time updates via WebSocket

/sc:implement "team collaboration UI"
# → Share todos with team members
# → Real-time presence indicators
```

## Step 3: Testing with FloSho

```javascript
// FloSho automatically uses PRP test scenarios!
const flosho = new FloSho('todo-app');
await flosho.init();

// This reads test scenario TS-001 from PRP
await flosho.flow('Complete Todo Workflow');
// Automatically executes:
// 1. Navigate to app
// 2. Create account
// 3. Add todo with category
// 4. Share with team
// 5. Mark complete
// 6. Captures screenshots at each step!

// Test the API using PRP specifications
await flosho.api('/api/todos');
// Tests all CRUD operations defined in PRP
// Generates visual API documentation

await flosho.done();
```

## Step 4: Generated Documentation

### User Manual (Automatic!)
- Getting Started with screenshots
- Creating and Managing Todos (with visuals)
- Team Collaboration Guide
- Category Management

### API Documentation (Automatic!)
- All endpoints with examples
- Request/Response schemas from PRP
- Authentication guide
- WebSocket events

### Test Report (Automatic!)
- 100% PRP scenario coverage
- Visual test flows
- Performance metrics

## The Magic: Everything Connected!

```
PRP defines "todos must have categories"
         ↓
Backend implements category model
         ↓
Frontend creates category selector
         ↓
FloSho tests category functionality
         ↓
Docs show how to use categories!
```

## Running This Example

1. **Setup**
   ```bash
   cd examples/todo-app
   npm install
   ```

2. **Initialize**
   ```bash
   # In Claude Code
   /xt:init --template todo-app
   ```

3. **Watch the Magic**
   - See how personas collaborate
   - Watch tests run automatically
   - Get complete documentation

## Key Benefits Demonstrated

1. **No Redundancy**: Define requirements once in PRP
2. **Smart Implementation**: Personas understand context
3. **Automatic Testing**: Test scenarios from PRP
4. **Real Documentation**: Generated from actual usage
5. **Full Alignment**: Everything matches the PRP

## Files in This Example

- `todo-app-prp.json` - Complete PRP for the todo app
- `implementation-log.md` - How SuperClaude built it
- `test-results/` - FloSho test outputs
- `docs/` - Generated documentation
- `src/` - Implemented code

---

*This is the power of SupaFloSho: From idea to documented app in hours, not weeks!*