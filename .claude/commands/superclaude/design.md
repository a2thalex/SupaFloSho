---
allowed-tools: [Write, Task, MagicUI]
description: "Architecture and system design with visual diagrams and specifications"
---

# /sc:design - System Design

## Purpose
Create comprehensive system designs, architecture diagrams, and technical specifications.

## Usage
```
/sc:design [system-name] [--type architecture|database|api|ui] [--visual]
```

## Arguments
- `system-name` - Name or description of system to design
- `--type` - Design focus area
- `--visual` - Generate visual diagrams
- `--patterns` - Include design patterns
- `--scalable` - Focus on scalability
- `--microservices` - Microservices architecture

## Execution
1. Gather requirements and constraints
2. Create architecture blueprint
3. Design component interactions
4. Generate visual diagrams
5. Document design decisions

## Examples
```
/sc:design e-commerce platform --type architecture --visual
/sc:design user management --type api --patterns
/sc:design notification system --microservices
```