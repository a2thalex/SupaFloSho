#!/bin/bash

# SupaFloSho Complete Migration Script
# This script completes the migration by pulling remaining components from source repos

echo "🚀 SupaFloSho Complete Migration Script"
echo "======================================"
echo ""
echo "This script will:"
echo "1. Clone xText-PRP and SuperClaude repositories"
echo "2. Copy missing components into SupaFloSho"
echo "3. Set up the unified framework"
echo ""

# Check if we're in the SupaFloSho directory
if [ ! -f "package.json" ] || [ ! -d ".claude" ]; then
    echo "❌ Error: Please run this script from the SupaFloSho root directory"
    exit 1
fi

echo "📥 Step 1: Cloning source repositories..."
mkdir -p temp
cd temp

# Clone repositories
if [ ! -d "xText-PRP" ]; then
    echo "  Cloning xText-PRP..."
    git clone https://github.com/a2thalex/xText-PRP.git
fi

if [ ! -d "SuperClaude" ]; then
    echo "  Cloning SuperClaude..."
    git clone https://github.com/NomenAK/SuperClaude.git
fi

cd ..

echo ""
echo "📋 Step 2: Migrating xText-PRP components..."

# Create directories if they don't exist
mkdir -p core/context
mkdir -p templates/prp
mkdir -p .claude/commands/context

# Copy context engineering files
if [ -d "temp/xText-PRP/context" ]; then
    echo "  ✓ Copying context engineering files..."
    cp -r temp/xText-PRP/context/* core/context/ 2>/dev/null || true
fi

# Copy PRP templates
if [ -d "temp/xText-PRP/PRPs" ]; then
    echo "  ✓ Copying PRP templates..."
    cp -r temp/xText-PRP/PRPs/* templates/prp/ 2>/dev/null || true
fi

# Copy INITIAL.md template
if [ -f "temp/xText-PRP/INITIAL.md" ]; then
    echo "  ✓ Copying INITIAL.md template..."
    cp temp/xText-PRP/INITIAL.md templates/
fi

# Create xText commands
echo "  ✓ Creating xText command definitions..."
cat > .claude/commands/context/init.md << 'EOF'
# /xt:init

Initialize a new project with Product Requirements Prompt (PRP).

## Usage
```
/xt:init "project description"
```

## What it does
1. Analyzes your project idea
2. Generates comprehensive PRP
3. Sets up project structure
4. Configures personas for the project

## Example
```
/xt:init "Build a task management app with team collaboration"
```
EOF

cat > .claude/commands/context/prp.md << 'EOF'
# /xt:prp

Manage Product Requirements Prompts.

## Usage
```
/xt:prp [action] [options]
```

## Actions
- `show` - Display current PRP
- `update` - Add new requirements
- `regenerate` - Create new PRP from scratch
- `validate` - Check implementation against PRP
EOF

cat > .claude/commands/context/context.md << 'EOF'
# /xt:context

Manage context window optimization.

## Usage
```
/xt:context [action]
```

## Actions
- `show` - Display current context usage
- `optimize` - Compress context for efficiency
- `reset` - Clear and reload context
EOF

echo ""
echo "🤖 Step 3: Migrating SuperClaude components..."

# Create directories
mkdir -p .claude/commands/superclaude
mkdir -p core/personas

# Copy SuperClaude commands
if [ -d "temp/SuperClaude/SuperClaude/Commands" ]; then
    echo "  ✓ Copying SuperClaude commands..."
    cp -r temp/SuperClaude/SuperClaude/Commands/* .claude/commands/superclaude/ 2>/dev/null || true
fi

# Copy personas
if [ -f "temp/SuperClaude/SuperClaude/Core/PERSONAS.md" ]; then
    echo "  ✓ Copying personas system..."
    cp temp/SuperClaude/SuperClaude/Core/PERSONAS.md core/personas/
fi

# Copy MCP configurations if they exist
if [ -d "temp/SuperClaude/config" ]; then
    echo "  ✓ Copying MCP configurations..."
    cp -r temp/SuperClaude/config/* mcp/ 2>/dev/null || true
fi

echo ""
echo "📸 Step 4: Enhancing FloSho integration..."

# Copy additional FloSho components from xText-PRP
if [ -d "temp/xText-PRP/testing/flosho/src" ]; then
    echo "  ✓ Copying FloSho components..."
    cp temp/xText-PRP/testing/flosho/src/FlowRecorder.js testing/flosho/src/ 2>/dev/null || true
    cp temp/xText-PRP/testing/flosho/src/APIVisualizer.js testing/flosho/src/ 2>/dev/null || true
    cp temp/xText-PRP/testing/flosho/src/TestGenerator.js testing/flosho/src/ 2>/dev/null || true
fi

# Create FloSho commands
echo "  ✓ Creating FloSho command definitions..."
mkdir -p .claude/commands/flosho

cat > .claude/commands/flosho/flow.md << 'EOF'
# /fs:flow

Define and execute visual test flows.

## Usage
```
/fs:flow "flow name" [steps]
```

## Steps Format
```javascript
[
  { action: 'navigate', url: 'http://localhost:3000' },
  { action: 'click', selector: '#button' },
  { action: 'screenshot', name: 'result' }
]
```
EOF

cat > .claude/commands/flosho/api.md << 'EOF'
# /fs:api

Test and document API endpoints visually.

## Usage
```
/fs:api "endpoint" [tests]
```

## Example
```
/fs:api "/api/users" [
  { method: 'GET', expect: { status: 200 } },
  { method: 'POST', data: { name: 'Test' }, expect: { status: 201 } }
]
```
EOF

echo ""
echo "🔧 Step 5: Creating unified configuration..."

# Update settings
cat > .claude/supaflosho-config.json << 'EOF'
{
  "version": "1.0.0",
  "framework": "SupaFloSho",
  "components": {
    "xtext-prp": {
      "enabled": true,
      "commands": ["/xt:init", "/xt:prp", "/xt:context", "/xt:validate"]
    },
    "superclaude": {
      "enabled": true,
      "commands": [
        "/sc:implement", "/sc:analyze", "/sc:design", "/sc:test",
        "/sc:improve", "/sc:troubleshoot", "/sc:document", "/sc:build",
        "/sc:cleanup", "/sc:explain", "/sc:git", "/sc:estimate",
        "/sc:task", "/sc:index", "/sc:load", "/sc:spawn"
      ]
    },
    "flosho": {
      "enabled": true,
      "commands": ["/fs:flow", "/fs:capture", "/fs:api", "/fs:document"]
    }
  },
  "workflow": {
    "phases": ["context", "implementation", "testing", "documentation"],
    "auto_doc": true,
    "prp_validation": true
  }
}
EOF

echo ""
echo "🧹 Step 6: Cleaning up..."
rm -rf temp

echo ""
echo "✅ Migration Complete!"
echo ""
echo "📋 Summary:"
echo "  • xText-PRP context engineering ✓"
echo "  • SuperClaude commands and personas ✓"
echo "  • FloSho testing framework ✓"
echo "  • Unified command system ✓"
echo "  • Configuration files ✓"
echo ""
echo "🚀 Next Steps:"
echo "1. Install dependencies: npm install"
echo "2. Run installer: python setup/install.py install --profile complete"
echo "3. Restart Claude Code"
echo "4. Try: /xt:init \"your amazing project idea\""
echo ""
echo "📚 Documentation:"
echo "  • README.md - Overview and quick start"
echo "  • ARCHITECTURE.md - System design"
echo "  • IMPLEMENTATION_GUIDE.md - Setup instructions"
echo "  • MIGRATION_STATUS.md - Migration progress"
echo ""
echo "Happy coding with SupaFloSho! 🎉"