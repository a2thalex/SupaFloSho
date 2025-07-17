# SupaFloSho Quick Start Example

## Building a Complete App in Minutes

This example shows how SupaFloSho's unified approach dramatically speeds up development.

### Traditional Approach (Multiple Tools)
```bash
# 1. Write requirements doc manually
# 2. Set up project structure manually  
# 3. Implement features without context
# 4. Write tests separately
# 5. Create documentation manually
# Time: Days to weeks
```

### SupaFloSho Approach (Unified Framework)
```bash
# Everything flows from one command!
/xt:init "Build a recipe sharing app with search and ratings"
```

## What Happens Next?

### 1️⃣ Context Engineering (Automatic)

SupaFloSho generates a complete PRP:

```markdown
# Recipe Sharing App - Product Requirements Prompt

## User Stories
- As a user, I want to browse recipes by category
- As a user, I want to search recipes by ingredients
- As a user, I want to rate and review recipes
- As a chef, I want to share my recipes with photos

## Technical Specifications
- Frontend: React with Material-UI
- Backend: Node.js with Express
- Database: PostgreSQL with full-text search
- Storage: AWS S3 for images

## Test Scenarios
1. Browse recipes → View details → Rate recipe
2. Search by ingredient → Filter results → Save favorites
3. Create recipe → Upload photos → Publish
```

### 2️⃣ Smart Implementation (Context-Aware)

```bash
# Backend persona reads PRP, knows we need PostgreSQL
/sc:implement "recipe API with search"
# ✓ Creates models with rating system
# ✓ Implements full-text search
# ✓ Sets up image upload endpoints

# Frontend persona reads PRP, knows we need Material-UI
/sc:design "recipe browsing interface"
# ✓ Creates category navigation
# ✓ Implements search with filters
# ✓ Adds rating components
```

### 3️⃣ Automated Testing & Documentation

```javascript
// FloSho reads PRP test scenarios and creates:
await flosho.flow('Recipe User Journey', [
  // Automatically derived from PRP!
  { action: 'navigate', url: '/', description: 'Open recipe app' },
  { action: 'click', selector: '.category-italian', description: 'Browse Italian recipes' },
  { action: 'screenshot', name: 'recipe-list', description: 'Italian recipes displayed' },
  { action: 'click', selector: '.recipe-card:first', description: 'View recipe details' },
  { action: 'screenshot', name: 'recipe-detail', description: 'Full recipe with ingredients' },
  { action: 'click', selector: '.rating-5-star', description: 'Rate recipe 5 stars' },
  { action: 'screenshot', name: 'rating-submitted', description: 'Rating confirmed' }
]);
```

### 4️⃣ Generated Output

📄 **User Manual** (with screenshots!)  
📄 **API Documentation** (with examples!)  
📄 **Architecture Guide** (with diagrams!)  
📄 **Test Coverage Report** (visual!)  

## The Magic: Everything is Connected! 🪄

```
PRP defines "search by ingredients"
         ↓
Backend persona implements search API
         ↓  
Frontend persona creates search UI
         ↓
FloSho tests the search flow
         ↓
Documentation shows how to search!
```

## Complete Example Script

```javascript
// supaflosho-recipe-app.js
import { SupaFloSho } from 'supaflosho';

// Initialize the project
const app = new SupaFloSho('recipe-app');

// 1. Define context
await app.command('/xt:init', {
  description: 'Recipe sharing platform with search, ratings, and chef profiles',
  features: ['browse', 'search', 'rate', 'share', 'profile'],
  tech: { frontend: 'React', backend: 'Node.js', db: 'PostgreSQL' }
});

// 2. Implement features (personas auto-selected!)
await app.command('/sc:implement', 'recipe CRUD with search');
await app.command('/sc:implement', 'rating and review system');
await app.command('/sc:design', 'responsive recipe cards');
await app.command('/sc:implement', 'chef profile pages');

// 3. Test everything
await app.command('/fs:flow', 'Complete recipe experience');
await app.command('/fs:api', 'Test all endpoints');

// 4. Generate documentation
await app.command('/fs:document', 'Create user guide');

console.log('✅ Recipe app complete with full documentation!');
```

## Time Comparison

| Task | Traditional | SupaFloSho |
|------|------------|------------|
| Requirements | 2-4 hours | 2 minutes |
| Implementation | 2-3 days | 2-3 hours |
| Testing | 1 day | 30 minutes |
| Documentation | 1 day | Automatic! |
| **Total** | **1 week** | **< 4 hours** |

## Why It Works

1. **Context is King** - Everything starts from a well-defined PRP
2. **Personas are Smart** - They read the PRP and implement accordingly
3. **Tests are Automatic** - FloSho knows what to test from the PRP
4. **Docs are Real** - Screenshots and guides from actual usage

## Try It Yourself!

```bash
# 1. Install SupaFloSho
git clone https://github.com/a2thalex/SupaFloSho.git
cd SupaFloSho
npm run install:complete

# 2. Start Claude Code
code .

# 3. Initialize your project
/xt:init "Your amazing app idea here"

# 4. Watch the magic happen! 🪄
```

---

*SupaFloSho: From idea to documented app in hours, not weeks! 🚀*