# /sc:test - Test Generation & Strategy

## Purpose
Generate comprehensive tests based on PRP test scenarios and implementation details.

## Usage
```
/sc:test [component/feature] [--type unit|integration|e2e] [--framework jest|mocha|playwright]
```

## What It Does
1. Reads test scenarios from PRP
2. Analyzes implementation for test points
3. Generates appropriate test suites
4. Creates test data and fixtures
5. Integrates with FloSho for visual testing

## Test Types
- **Unit Tests**: Component and function level
- **Integration Tests**: API and service interaction
- **E2E Tests**: Full user flows from PRP
- **Performance Tests**: Load and stress testing
- **Security Tests**: Vulnerability testing

## Examples
```
/sc:test user-authentication --type integration
/sc:test checkout-flow --type e2e --framework playwright
/sc:test api-endpoints --type unit --framework jest
```

## FloSho Integration
Automatically creates FloSho visual test flows for:
- UI component testing
- User journey validation
- API response documentation

## PRP Alignment
Ensures test coverage for:
- All PRP-defined user stories
- Success criteria validation
- Edge cases from PRP
- Performance requirements