# /xt:validate

## Purpose
Validate implementation against Product Requirements Prompt specifications.

## Usage
```
/xt:validate [component]
```

## What It Does
- Compares current implementation with PRP requirements
- Identifies missing features or deviations
- Checks test coverage against PRP scenarios
- Validates documentation completeness

## Validation Areas
- Feature completeness
- API compliance
- UI/UX adherence
- Test scenario coverage
- Performance criteria
- Security requirements

## Examples
```
/xt:validate all
/xt:validate features
/xt:validate api
/xt:validate tests
/xt:validate --fix-issues
```

## Output
- Validation report with pass/fail status
- List of deviations from PRP
- Recommendations for alignment
- Coverage metrics

## Integration
Works with FloSho to validate test coverage and with SuperClaude commands to ensure implementation compliance.