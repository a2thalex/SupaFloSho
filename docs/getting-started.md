# Getting Started with SupaFloSho

Welcome to SupaFloSho! This guide will walk you through your first project using our unified framework.

## What is SupaFloSho?

SupaFloSho combines three powerful frameworks:
- **xText-PRP**: Define what you're building with context engineering
- **SuperClaude**: Build it with smart commands and personas
- **FloSho**: Test it and auto-generate documentation

## Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/a2thalex/SupaFloSho.git
cd SupaFloSho

# Install everything
npm run install:complete
```

### Custom Install

```bash
# Interactive installation
npm run install:interactive

# Or choose a profile
npm run install:minimal    # Just core features
npm run install:dev       # Everything for developers
```

## Your First SupaFloSho Project

Let's build a simple recipe app to see how all three frameworks work together.

### Step 1: Initialize with Context (xText-PRP)

```bash
# In Claude Code, type:
/xt:init "Recipe sharing app where users can browse, search, and rate recipes"
```

SupaFloSho will generate a comprehensive PRP (Product Requirements Prompt) with:
- User stories (browse recipes, search by ingredient, rate recipes)
- Technical specifications (React, Node.js, PostgreSQL)
- Test scenarios for FloSho
- Success criteria

### Step 2: Design the Architecture (SuperClaude)

```bash
# The architect persona activates automatically
/sc:design "recipe app architecture"
```

The architect persona reads your PRP and creates:
- System architecture diagram
- Component structure
- Database schema
- API endpoints design

### Step 3: Implement Features (SuperClaude)

```bash
# Backend implementation
/sc:implement "recipe CRUD API with search"
# Backend persona creates API endpoints based on PRP

# Frontend implementation
/sc:implement "recipe browsing interface"
# Frontend persona builds UI components per PRP specs
```

Each persona:
- Reads the PRP requirements
- Implements exactly what's specified
- Adds hooks for FloSho testing

### Step 4: Test and Document (FloSho)

```bash
# Test the user journey
/fs:flow "Complete Recipe Experience"
```

FloSho will:
1. Run through the test scenarios from your PRP
2. Take screenshots at each step
3. Test the API endpoints
4. Generate a beautiful user manual
5. Create API documentation

### Step 5: Validate Everything

```bash
# Check if we met all PRP requirements
/xt:validate
```

This confirms:
- ✅ All user stories implemented
- ✅ Technical specs followed
- ✅ Test scenarios passed
- ✅ Documentation complete

## The Magic of Integration 🪄

### Example: Adding a New Feature

Let's add recipe categories to our app:

```bash
# 1. Update the PRP
/xt:prp add-feature "recipe categories"

# 2. Design the feature
/sc:design "category system"
# Architect persona designs based on updated PRP

# 3. Implement it
/sc:implement "category management"
# Appropriate personas implement per PRP

# 4. Test it
/fs:flow "Category Management"
# FloSho tests the new PRP scenarios

# 5. Documentation is auto-updated!
```

## Understanding the Workflow

### Context is King (xText-PRP)
- Everything starts with a PRP
- The PRP is the single source of truth
- All decisions flow from the PRP

### Smart Implementation (SuperClaude)
- Personas read the PRP before acting
- Each persona is an expert in their domain
- Commands are context-aware

### Visual Validation (FloSho)
- Tests are derived from PRP scenarios
- Screenshots document actual behavior
- User guides are generated automatically

## Common Workflows

### Starting Fresh
```bash
/xt:init "your idea" → /sc:design → /sc:implement → /fs:flow
```

### Adding Features
```bash
/xt:prp update → /sc:implement "new feature" → /fs:flow "test new feature"
```

### Debugging Issues
```bash
/sc:analyze "problem area" → /sc:troubleshoot → /sc:improve → /fs:flow
```

### Creating Documentation
```bash
/fs:flow "complete user journey" → /fs:document
```

## Tips for Success

### 1. Let the PRP Guide You
- Don't skip the initialization step
- Keep your PRP updated as requirements change
- Reference the PRP when making decisions

### 2. Trust the Personas
- Let them auto-activate based on context
- Each persona is optimized for their domain
- Use manual override only when needed

### 3. Test Everything with FloSho
- Every feature should have a test flow
- Use screenshots to document behavior
- Let FloSho generate your user guides

### 4. Iterate Quickly
```bash
# The SupaFloSho loop
Define (PRP) → Build (SuperClaude) → Test (FloSho) → Refine (Repeat)
```

## Advanced Features

### Using MCP Servers

```bash
# Get library documentation
/sc:implement "auth system" --with-context7

# Complex reasoning
/sc:analyze "performance bottleneck" --with-sequential

# Generate UI components
/sc:design "dashboard" --with-magic
```

### Custom PRP Templates

```bash
# Use a template
/xt:init "SaaS app" --template saas-starter

# Create from existing PRP
/xt:init --from examples/todo-app.prp.json
```

### Batch Testing

```javascript
// Test multiple flows at once
const flosho = new FloSho('my-app');
await flosho.init();

// Run all PRP test scenarios
await flosho.runAllPRPScenarios();

// Generate complete documentation suite
await flosho.done();
```

## Troubleshooting

### PRP Not Found
```bash
# Initialize first
/xt:init "your project idea"
```

### Persona Not Activating
```bash
# Force activation
/sc:implement "feature" --persona-backend
```

### FloSho Tests Failing
```bash
# Debug mode
/fs:flow "test name" --debug --slowmo
```

## Next Steps

1. **Explore Commands**: See all available commands with `/sc:help`
2. **Learn Personas**: Read about each persona in `~/.claude/PERSONAS.md`
3. **Try Examples**: Check out `examples/` for complete projects
4. **Join Community**: Share your SupaFloSho projects!

## Quick Reference

### Essential Commands
- `/xt:init` - Start a new project
- `/sc:implement` - Build features
- `/fs:flow` - Test and document
- `/xt:validate` - Check completeness

### Key Concepts
- **PRP**: Your project's source of truth
- **Personas**: Domain expert AI personalities
- **Flows**: Visual test scenarios
- **Context**: Shared understanding across all tools

---

*Ready to build something amazing? Start with `/xt:init "your idea"` and let SupaFloSho guide you!* 🚀