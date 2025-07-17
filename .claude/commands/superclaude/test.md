---
allowed-tools: [Read, Write, Edit, MultiEdit, Bash]
description: "Generate comprehensive test suites and testing strategies"
---

# /sc:test - Test Generation

## Purpose
Create comprehensive test suites including unit, integration, and e2e tests.

## Usage
```
/sc:test [target] [--type unit|integration|e2e|all] [--framework jest|mocha|playwright]
```

## Arguments
- `target` - Code or feature to test
- `--type` - Test type to generate
- `--framework` - Testing framework
- `--coverage` - Target coverage percentage
- `--mocks` - Include mock data
- `--ci` - CI/CD integration

## Execution
1. Analyze code structure
2. Identify test scenarios
3. Generate test files
4. Create mock data and fixtures
5. Setup test configuration

## Examples
```
/sc:test src/auth --type unit --framework jest
/sc:test api/ --type integration --coverage 80
/sc:test app --type e2e --framework playwright
```