# /sc:analyze - Code & System Analysis

## Purpose
Analyze code, performance, security, and system behavior with PRP-aware insights.

## Usage
```
/sc:analyze [target] [--type code|performance|security|architecture] [--depth shallow|deep]
```

## Analysis Types
- **Code Quality**: Style, complexity, maintainability
- **Performance**: Bottlenecks, optimization opportunities
- **Security**: Vulnerabilities, best practices
- **Architecture**: Design patterns, coupling, cohesion
- **PRP Compliance**: Alignment with requirements

## What It Does
1. Examines specified code or system aspect
2. Compares against PRP requirements
3. Identifies issues and improvements
4. Provides actionable recommendations
5. Generates analysis reports

## Examples
```
/sc:analyze user-service --type performance
/sc:analyze authentication --type security --depth deep
/sc:analyze frontend --type code
/sc:analyze --type prp-compliance
```

## Output
- Detailed analysis report
- Issue severity rankings
- Improvement recommendations
- PRP compliance score
- Suggested FloSho test scenarios for found issues