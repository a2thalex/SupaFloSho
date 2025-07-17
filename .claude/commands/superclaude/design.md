# /sc:design

## SupaFloSho Enhanced Design

Creates architecture and designs based on PRP specifications.

## Syntax
```
/sc:design [component] [flags]
```

## PRP Integration

Designs are created to fulfill PRP requirements:
- Architecture supports all use cases
- Components map to user stories
- Scalability meets PRP targets
- Integration points are defined

## Examples

### System Architecture
```bash
/sc:design "system architecture"
# Creates architecture from PRP
# Defines component boundaries
# Plans integration points
# Includes FloSho test points
```

### UI Component Design
```bash
/sc:design "dashboard layout" --persona-frontend
# Designs based on PRP UI requirements
# Creates component hierarchy
# Plans responsive breakpoints
# Adds accessibility features
```

### API Design
```bash
/sc:design "REST API" --with-docs
# Designs endpoints from PRP
# Defines request/response schemas
# Plans authentication flow
# Generates OpenAPI spec
```

## Design Outputs

1. **Architecture Diagrams** - System overview
2. **Component Specs** - Detailed designs
3. **Integration Plans** - How components connect
4. **Test Scenarios** - FloSho test plans
5. **Documentation** - Design decisions

## Flags

- `--level [type]` - system, component, or detailed
- `--with-docs` - Include documentation
- `--visual` - Create visual diagrams
- `--testable` - Optimize for FloSho testing

## Workflow

1. Read PRP requirements
2. Identify design constraints
3. Create architecture/design
4. Validate against PRP
5. Prepare for implementation

## Related Commands

- `/xt:prp` - View/update requirements
- `/sc:implement` - Implement the design
- `/sc:analyze` - Analyze design quality
- `/fs:flow` - Plan test flows