# SupaFloSho PRP Templates

## Overview

Product Requirements Prompts (PRPs) are the foundation of the SupaFloSho workflow. They define everything about your project in a structured format that all components can understand.

## Available Templates

### 1. Default Template (`default.json`)
A generic template with placeholders for any type of project. Use this when starting from scratch or for unique project types.

### 2. Web Application (`web-app.json`)
Pre-configured for modern web applications with:
- User authentication flows
- Real-time features
- Responsive design requirements
- API specifications
- Standard web app test scenarios

### 3. Mobile App (`mobile-app.json`) - Coming Soon
Optimized for mobile application development

### 4. API Service (`api-service.json`) - Coming Soon
Focused on backend API development

## Using Templates

### Quick Start
```bash
# Use default template
/xt:init "My awesome project"

# Use specific template
/xt:init "My web app" --template web-app
```

### Template Structure

Every PRP template includes:

1. **Project Overview**
   - Vision and goals
   - Constraints and assumptions
   - Success criteria

2. **User Stories**
   - Personas and their needs
   - Acceptance criteria
   - Priority levels

3. **Technical Specifications**
   - Technology stack
   - Architecture patterns
   - Performance requirements

4. **Features**
   - Feature descriptions
   - Components needed
   - Implementation scenarios

5. **Test Scenarios**
   - E2E test flows
   - API test cases
   - Test data requirements

## Creating Custom Templates

1. Start with `default.json`
2. Modify sections for your domain
3. Save as `templates/prp/your-template.json`
4. Use with `/xt:init --template your-template`

## Integration with SupaFloSho

### How PRPs Flow Through the System

```
PRP Definition
     ↓
SuperClaude Commands read requirements
     ↓
Personas understand context
     ↓
Implementation follows specs
     ↓
FloSho tests match scenarios
     ↓
Documentation reflects reality
```

### Example: Web App Flow

1. **PRP defines**: "User authentication with email/password"
2. **SuperClaude implements**: `/sc:implement user authentication`
   - Backend persona creates auth endpoints
   - Frontend persona builds login forms
3. **FloSho tests**: `/fs:flow "User Login"`
   - Runs test scenario from PRP
   - Captures screenshots
4. **Documentation generated**: Complete with visuals!

## Best Practices

1. **Be Specific**: The more detail in your PRP, the better the output
2. **Include Examples**: Add sample data and expected behaviors
3. **Define All Scenarios**: Both happy paths and edge cases
4. **Set Clear Metrics**: Measurable success criteria
5. **Update Regularly**: PRPs should evolve with your project

## Template Variables

Templates use `{{VARIABLE}}` placeholders that are filled during initialization:

- `{{PROJECT_NAME}}` - Your project name
- `{{PROJECT_DESCRIPTION}}` - Brief description
- `{{TIMESTAMP}}` - Creation timestamp
- `{{USER_TYPE}}` - Primary user persona
- `{{FRONTEND_TECH}}` - Frontend technology choice
- `{{BACKEND_TECH}}` - Backend technology choice

These are automatically populated through the `/xt:init` interactive process.

---

*PRPs: Where great projects begin in SupaFloSho*