# /xt:init

## Initialize Project with PRP

Creates a comprehensive Product Requirements Prompt for your project.

## Syntax
```
/xt:init "project description" [flags]
```

## What It Does

1. **Analyzes** your project idea
2. **Generates** comprehensive PRP with:
   - User stories
   - Technical specifications
   - Success criteria
   - Test scenarios
3. **Prepares** for implementation and testing

## Examples

### Basic Initialization
```bash
/xt:init "Recipe sharing app with search and ratings"
# Creates PRP with:
# - User stories (browse, search, rate, share)
# - Tech specs (stack, architecture)
# - Test scenarios for FloSho
```

### With Technology Preferences
```bash
/xt:init "E-commerce platform" --tech "Next.js, PostgreSQL, Stripe"
# Generates PRP with specified stack
# Plans architecture accordingly
# Creates tech-specific test scenarios
```

### With Specific Requirements
```bash
/xt:init "Task management tool" --requirements "real-time sync, offline mode"
# Emphasizes specific features in PRP
# Plans architecture for requirements
# Creates targeted test scenarios
```

## PRP Structure

Generated PRP includes:

1. **Project Overview**
   - Vision and goals
   - Target audience
   - Key differentiators

2. **User Stories**
   - Structured scenarios
   - Acceptance criteria
   - Priority levels

3. **Technical Specifications**
   - Architecture overview
   - Technology stack
   - Integration points
   - Performance targets

4. **Test Scenarios**
   - User journey tests
   - API test cases
   - Edge cases
   - Performance benchmarks

5. **Success Criteria**
   - Measurable goals
   - Quality metrics
   - Performance SLAs

## Flags

- `--tech [stack]` - Specify technology preferences
- `--requirements [list]` - Specific requirements
- `--template [type]` - Use PRP template
- `--minimal` - Create minimal PRP
- `--comprehensive` - Maximum detail (default)

## Next Steps

After initialization:

1. Review generated PRP
2. `/sc:design` - Create architecture
3. `/sc:implement` - Build features
4. `/fs:flow` - Test scenarios

## Related Commands

- `/xt:prp` - View/edit PRP
- `/xt:context` - Manage context
- `/xt:validate` - Validate against PRP
- `/sc:design` - Design from PRP