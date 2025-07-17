# SupaFloSho Examples

## Overview

These examples demonstrate the power of the unified SupaFloSho framework, showing how xText-PRP, SuperClaude, and FloSho work together seamlessly.

## Available Examples

### 1. Todo App (`todo-app/`)
A complete collaborative todo application showcasing:
- PRP-driven development
- Smart implementation with personas
- Automated visual testing
- Generated documentation

### 2. E-commerce Platform (Coming Soon)
Building a full e-commerce site with:
- Product catalog
- Shopping cart
- Payment processing
- Order management

### 3. Real-time Chat App (Coming Soon)
Creating a chat application with:
- WebSocket communication
- Room management
- File sharing
- User presence

## Running Examples

### Prerequisites
1. Install SupaFloSho:
   ```bash
   npm install
   python setup/install.py --profile complete
   ```

2. Install example dependencies:
   ```bash
   cd examples/todo-app
   npm install
   ```

### Running the Todo App Example

1. **In Claude Code:**
   ```bash
   # Initialize the project
   /xt:init --template todo-app
   
   # Implement features
   /sc:implement "todo backend API"
   /sc:implement "todo frontend UI"
   ```

2. **Run FloSho tests:**
   ```bash
   node run-example.js
   ```

## What Makes These Examples Special

### 1. **PRP-Driven**
Every example starts with a comprehensive PRP that defines:
- User stories
- Technical requirements
- Test scenarios
- API specifications

### 2. **Intelligent Implementation**
SuperClaude personas read the PRP and implement accordingly:
- Backend persona builds APIs matching PRP specs
- Frontend persona creates UI following PRP designs
- Security persona ensures PRP security requirements

### 3. **Automated Testing**
FloSho reads test scenarios from the PRP:
- Executes visual test flows
- Captures screenshots
- Tests API endpoints
- Validates coverage

### 4. **Real Documentation**
Generated documentation includes:
- User guides with screenshots
- API documentation with examples
- Architecture diagrams
- Test reports

## Learning Path

1. **Start Simple**: Run the todo app example
2. **Examine the PRP**: See how requirements drive everything
3. **Watch Implementation**: Observe how personas work
4. **Review Tests**: See FloSho in action
5. **Check Documentation**: Marvel at the automatic docs

## Creating Your Own Example

1. **Define PRP**:
   ```bash
   /xt:init "Your app idea"
   ```

2. **Implement**:
   ```bash
   /sc:implement "core features"
   ```

3. **Test**:
   ```javascript
   const flosho = new FloSho('your-app');
   await flosho.flow('User Journey');
   ```

4. **Document**:
   ```bash
   /fs:document --comprehensive
   ```

## Key Takeaways

- **Context is King**: Everything starts with a well-defined PRP
- **Integration is Seamless**: Components work together naturally
- **Documentation is Automatic**: No manual work needed
- **Quality is Built-in**: Tests come from requirements

---

*Explore these examples to see the future of AI-driven development with SupaFloSho!*