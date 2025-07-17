# SupaFloSho Quick Reference

## 🚀 Installation (One Command!)

```bash
# Clone and set up everything
git clone https://github.com/a2thalex/SupaFloSho.git
cd SupaFloSho
chmod +x migrate-complete.sh
./migrate-complete.sh
npm install
python setup/install.py install --profile complete
```

## 📋 Command Reference

### Context Engineering (/xt:*)
| Command | Description | Example |
|---------|-------------|---------|
| `/xt:init` | Start new project with PRP | `/xt:init "e-commerce platform"` |
| `/xt:prp` | Manage PRPs | `/xt:prp show` |
| `/xt:context` | Optimize context window | `/xt:context optimize` |
| `/xt:validate` | Check against PRP | `/xt:validate frontend` |

### Implementation (/sc:*)
| Command | Description | Example |
|---------|-------------|---------|
| `/sc:implement` | Build features | `/sc:implement "user auth"` |
| `/sc:design` | Architecture design | `/sc:design "api structure"` |
| `/sc:analyze` | Analyze code/issues | `/sc:analyze performance` |
| `/sc:test` | Generate tests | `/sc:test unit` |
| `/sc:troubleshoot` | Debug issues | `/sc:troubleshoot "login bug"` |
| `/sc:document` | Technical docs | `/sc:document api` |
| `/sc:improve` | Enhance quality | `/sc:improve "user.js"` |
| `/sc:build` | Compile/package | `/sc:build production` |

### Testing & Docs (/fs:*)
| Command | Description | Example |
|---------|-------------|---------|
| `/fs:flow` | Visual test flow | `/fs:flow "checkout process"` |
| `/fs:capture` | Screenshot | `/fs:capture "dashboard"` |
| `/fs:api` | Test APIs | `/fs:api "/api/users"` |
| `/fs:document` | Generate docs | `/fs:document user-guide` |

## 🎯 Typical Workflow

```bash
# 1. Start with context
/xt:init "social media dashboard with analytics"

# 2. Design architecture
/sc:design "microservices architecture"

# 3. Implement features
/sc:implement "user authentication service"
/sc:implement "analytics dashboard frontend"

# 4. Test visually
/fs:flow "User Login Journey"
/fs:api "/api/auth/login"

# 5. Generate documentation
/fs:document complete

# Result: Full app with tests and docs!
```

## 🎭 Smart Personas

Personas automatically activate based on your commands:

- **🏗️ Architect** → `/sc:design`
- **🎨 Frontend** → UI implementation
- **⚙️ Backend** → API development
- **🧪 Tester** → Test creation
- **📊 Data** → Database work
- **🚀 DevOps** → Deployment

## 📸 FloSho Example

```javascript
// Automatic test from PRP
await flosho.flow('User Registration', [
  { action: 'navigate', url: '/register' },
  { action: 'fill', selector: '#email', value: 'test@example.com' },
  { action: 'fill', selector: '#password', value: 'secure123' },
  { action: 'click', selector: '#submit' },
  { action: 'screenshot', name: 'registration-success' }
]);
```

## 🔧 Configuration

Main config locations:
- `~/.claude/CLAUDE.md` - Global behavior
- `~/.claude/supaflosho-config.json` - Framework settings
- `~/.claude/commands/` - Command definitions

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Commands not working | Restart Claude Code |
| Missing dependencies | Run `npm install` |
| MCP not connected | Check `~/.claude/mcp-config.json` |
| Tests failing | Ensure Playwright installed: `npx playwright install` |

## 📚 Resources

- **Docs**: `/docs` directory
- **Examples**: `/examples` directory
- **Templates**: `/templates` directory
- **Support**: [GitHub Issues](https://github.com/a2thalex/SupaFloSho/issues)

---

*SupaFloSho v1.0 - Where Context meets Implementation meets Documentation* 🚀