---
allowed-tools: [Read, Glob, Task, BrowsingWeb]
description: "Deep code, architecture, and project analysis with intelligent recommendations"
---

# /sc:analyze - Deep Analysis

## Purpose
Perform comprehensive analysis of code, architecture, performance, security, and project structure with actionable insights.

## Usage
```
/sc:analyze [target] [--type code|architecture|performance|security|all] [--depth shallow|medium|deep]
```

## Arguments
- `target` - File, directory, or concept to analyze
- `--type` - Analysis type (code, architecture, performance, security, all)
- `--depth` - Analysis depth level
- `--metrics` - Include quantitative metrics
- `--recommendations` - Provide improvement suggestions
- `--compare` - Compare with best practices

## Execution
1. Scan target for analysis scope
2. Apply specialized analysis based on type
3. Generate insights and findings
4. Provide actionable recommendations
5. Create visual analysis reports if applicable

## Examples
```
/sc:analyze src/ --type architecture --depth deep
/sc:analyze api/auth.js --type security --recommendations
/sc:analyze . --type performance --metrics
```