# SupaFloSho Implementation Guide

## Quick Migration from Existing Projects

This guide shows how to easily migrate from xText-PRP and SuperClaude to SupaFloSho.

## Step 1: Clone and Prepare

```bash
# Clone SupaFloSho
git clone https://github.com/a2thalex/SupaFloSho.git
cd SupaFloSho

# Create directory structure
mkdir -p .claude/commands/{context,superclaude,flosho}
mkdir -p core/{context,prp,personas,commands}
mkdir -p testing mcp templates/{prp,flows} docs setup
```

## Step 2: Migrate xText-PRP Components

```bash
# Copy xText context engineering
cp -r ../xText-PRP/context/* core/context/
cp -r ../xText-PRP/PRPs/* templates/prp/
cp ../xText-PRP/.claude/CLAUDE.md .claude/CLAUDE_xtext.md

# Copy FloSho testing framework (already in xText)
cp -r ../xText-PRP/testing/* testing/
```

## Step 3: Migrate SuperClaude Components

```bash
# Copy SuperClaude commands
cp -r ../SuperClaude/SuperClaude/Commands/* .claude/commands/superclaude/

# Copy personas
cp -r ../SuperClaude/SuperClaude/Core/PERSONAS.md core/personas/

# Copy MCP configurations
cp -r ../SuperClaude/config/* mcp/
```

## Step 4: Create Unified Configuration

Create `.claude/CLAUDE.md` that merges both frameworks:

```markdown
# SupaFloSho AI Assistant Configuration

## Overview
You are an AI assistant enhanced with SupaFloSho - a unified framework combining:
- xText-PRP context engineering
- SuperClaude commands and personas  
- FloSho testing and documentation

## Command Namespaces
- `/xt:*` - Context engineering commands
- `/sc:*` - SuperClaude implementation commands
- `/fs:*` - FloSho testing commands

## Workflow
1. Use `/xt:init` to establish project context with PRP
2. Use `/sc:*` commands to implement based on PRP
3. Use `/fs:*` to test and document

[Include merged rules from both CLAUDE.md files]
```

## Step 5: Create Unified Installer

Create `setup/install.py`:

```python
#!/usr/bin/env python3
import os
import shutil
import json
import argparse

class SupaFloShoInstaller:
    def __init__(self):
        self.claude_dir = os.path.expanduser('~/.claude')
        self.profiles = {
            'minimal': ['core', 'commands'],
            'complete': ['core', 'commands', 'personas', 'mcp', 'testing'],
            'developer': ['core', 'commands', 'personas', 'mcp', 'testing', 'templates']
        }
    
    def install(self, profile='complete'):
        print(f"Installing SupaFloSho with '{profile}' profile...")
        
        # Create directories
        os.makedirs(self.claude_dir, exist_ok=True)
        
        # Copy components based on profile
        components = self.profiles.get(profile, self.profiles['complete'])
        
        if 'core' in components:
            self._install_core()
        if 'commands' in components:
            self._install_commands()
        if 'personas' in components:
            self._install_personas()
        if 'mcp' in components:
            self._install_mcp()
        if 'testing' in components:
            self._install_testing()
            
        print("✅ SupaFloSho installed successfully!")
        print("Restart Claude Code to activate the framework.")
    
    def _install_core(self):
        # Copy unified CLAUDE.md
        shutil.copy('.claude/CLAUDE.md', f'{self.claude_dir}/CLAUDE.md')
        
    def _install_commands(self):
        # Copy all command sets
        shutil.copytree('.claude/commands', f'{self.claude_dir}/commands', dirs_exist_ok=True)
        
    def _install_personas(self):
        # Copy persona definitions
        shutil.copy('core/personas/PERSONAS.md', f'{self.claude_dir}/PERSONAS.md')
        
    def _install_mcp(self):
        # Install MCP servers
        print("Installing MCP servers...")
        os.system('npm install -g @context7/mcp')
        os.system('npm install -g @sequential/mcp')
        # ... other MCP installations
        
    def _install_testing(self):
        # Install FloSho dependencies
        print("Installing FloSho testing framework...")
        os.system('npm install playwright')
        os.system('npx playwright install chromium')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SupaFloSho Installer')
    parser.add_argument('--profile', choices=['minimal', 'complete', 'developer'], 
                       default='complete', help='Installation profile')
    parser.add_argument('--interactive', action='store_true', 
                       help='Interactive component selection')
    
    args = parser.parse_args()
    
    installer = SupaFloShoInstaller()
    installer.install(args.profile)
```

## Step 6: Create Example Usage

Create `examples/todo-app.md`:

```markdown
# Building a Todo App with SupaFloSho

## 1. Initialize with Context
```
/xt:init "Build a collaborative todo app with real-time sync"
```

## 2. Implement Features
```
/sc:implement "todo model with CRUD operations"
/sc:design "responsive todo list interface"
/sc:implement "real-time sync with WebSockets"
```

## 3. Test and Document
```javascript
// test-todo-flow.js
import { FloSho } from './testing/flosho';

const flosho = new FloSho('todo-app');
await flosho.init();

await flosho.flow('Complete Todo Workflow', [
  { action: 'navigate', url: 'http://localhost:3000' },
  { action: 'screenshot', name: 'home' },
  { action: 'fill', selector: '#new-todo', value: 'Test SupaFloSho' },
  { action: 'press', key: 'Enter' },
  { action: 'screenshot', name: 'todo-added' },
  // ... more steps
]);

await flosho.done();
```

This generates:
- User manual with screenshots
- API documentation
- Test coverage report
```

## Step 7: Package.json

Create unified `package.json`:

```json
{
  "name": "supaflosho",
  "version": "1.0.0",
  "description": "Unified AI-driven development framework",
  "scripts": {
    "install:complete": "python setup/install.py --profile complete",
    "install:minimal": "python setup/install.py --profile minimal",
    "install:dev": "python setup/install.py --profile developer",
    "test:flosho": "node testing/run-tests.js",
    "docs:generate": "node testing/generate-docs.js"
  },
  "dependencies": {
    "playwright": "^1.40.0",
    "marked": "^4.0.0",
    "jimp": "^0.22.0"
  },
  "keywords": [
    "ai",
    "claude",
    "development",
    "testing",
    "documentation"
  ]
}
```

## Next Steps

1. **Test the Installation**
   ```bash
   npm run install:complete
   ```

2. **Try Example Project**
   ```bash
   # In Claude Code
   /xt:init "todo app"
   ```

3. **Customize Configuration**
   - Edit `.claude/CLAUDE.md` for global behavior
   - Add custom commands in `.claude/commands/`
   - Create new PRP templates in `templates/prp/`

## Benefits of the Unified Approach

✅ **No Conflicts** - Each framework has its own namespace
✅ **Shared Context** - PRPs inform all commands and personas
✅ **Automatic Docs** - FloSho documents everything you build
✅ **Easy Migration** - Existing projects work with minor adjustments
✅ **Extensible** - Add new features without breaking existing ones

---

*Ready to experience the power of unified AI development? Let's build something amazing with SupaFloSho! 🚀*