# /sc:implement

## SupaFloSho Enhanced Implementation

Implements features based on PRP (Product Requirements Prompt) specifications.

## Syntax
```
/sc:implement [feature] [flags]
```

## PRP Integration

This command:
1. Reads the current project PRP
2. Identifies relevant requirements for the feature
3. Auto-activates appropriate personas
4. Implements according to PRP specifications
5. Prepares for FloSho testing

## Examples

### Basic Implementation
```bash
/sc:implement "user authentication"
# Reads PRP auth requirements
# Backend persona implements API
# Frontend persona implements UI
# Adds test hooks for FloSho
```

### With Specific Focus
```bash
/sc:implement "payment processing" --focus backend
# Implements only backend components
# Follows PRP payment specifications
# Creates API endpoints per PRP
```

### With Testing Preparation
```bash
/sc:implement "search feature" --with-tests
# Implements search per PRP
# Adds data-testid attributes
# Creates FloSho test templates
```

## Flags

- `--persona-[name]` - Force specific persona
- `--focus [area]` - frontend, backend, or fullstack
- `--with-tests` - Include FloSho test preparation
- `--validate` - Validate against PRP after implementation

## Workflow Integration

1. **Pre-Implementation**:
   - Validates PRP exists
   - Checks implementation status
   - Identifies dependencies

2. **Implementation**:
   - Follows PRP specifications
   - Uses appropriate patterns
   - Adds testing hooks

3. **Post-Implementation**:
   - Updates implementation status
   - Prepares FloSho test scenarios
   - Documents changes

## Related Commands

- `/xt:init` - Create initial PRP
- `/sc:design` - Design before implementing
- `/fs:flow` - Test after implementing
- `/xt:validate` - Validate implementation