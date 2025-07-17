# /xt:init

## Purpose
Initialize a new project with comprehensive Product Requirements Prompt (PRP) generation.

## Usage
```
/xt:init "[project description]"
```

## What It Does
1. Analyzes your project idea
2. Generates a complete PRP including:
   - User stories and personas
   - Technical specifications
   - Success criteria
   - Test scenarios
   - Implementation roadmap
3. Sets up project context for all subsequent commands
4. Configures personas to understand project requirements

## Examples
```
/xt:init "E-commerce platform with AI recommendations"
/xt:init "Real-time collaborative document editor"
/xt:init "Mobile fitness app with social features"
```

## Flags
- `--template [name]` - Use a specific PRP template
- `--tech [stack]` - Specify technology preferences
- `--scope [mvp|full]` - Define project scope

## Output
- Generated PRP document
- Project structure recommendations
- Configured context for all SupaFloSho components