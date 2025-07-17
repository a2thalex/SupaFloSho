# /sc:analyze

## SupaFloSho Enhanced Analysis

Systematic analysis with PRP validation and evidence-based investigation.

## Syntax
```
/sc:analyze [target] [flags]
```

## PRP Integration

Analyzes implementations against PRP requirements:
- Compliance with specifications
- Coverage of user stories
- Performance vs. targets
- Security requirement adherence

## Examples

### PRP Compliance Analysis
```bash
/sc:analyze --prp-compliance
# Checks all PRP requirements
# Identifies gaps in implementation
# Suggests missing features
```

### Codebase Analysis
```bash
/sc:analyze "src/"
# Analyzes code structure
# Validates against PRP architecture
# Identifies improvement areas
```

### Performance Analysis
```bash
/sc:analyze --focus performance
# Measures against PRP targets
# Identifies bottlenecks
# Suggests optimizations
```

## Analysis Types

- **quality** - Code quality metrics
- **security** - Security vulnerabilities
- **performance** - Performance bottlenecks
- **architecture** - System design issues
- **prp-compliance** - PRP requirement coverage

## Flags

- `--focus [type]` - Specific analysis focus
- `--depth [level]` - Analysis depth (quick/standard/deep)
- `--compare-prp` - Compare against PRP specs
- `--suggest-tests` - Suggest FloSho test scenarios

## Output

Analysis reports include:
1. Executive summary
2. PRP compliance status
3. Detailed findings
4. Recommendations
5. FloSho test suggestions

## Related Commands

- `/sc:troubleshoot` - Debug specific issues
- `/sc:improve` - Act on analysis findings
- `/xt:validate` - Validate PRP compliance
- `/fs:flow` - Test identified scenarios