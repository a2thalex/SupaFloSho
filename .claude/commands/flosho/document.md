# /fs:document - Generate Documentation

## Purpose
Generate comprehensive user documentation from test flows and implementations.

## Usage
```
/fs:document [--type user-guide|api-docs|developer-guide] [--format markdown|html|pdf]
```

## What It Does
1. Collects all FloSho test flows
2. Organizes screenshots and annotations  
3. Generates structured documentation
4. Links features to PRP requirements
5. Creates multiple output formats

## Documentation Types
- **User Guide**: Step-by-step guides with screenshots
- **API Documentation**: Endpoint references with examples
- **Developer Guide**: Technical documentation
- **Test Reports**: Coverage and results

## Examples
```
/fs:document --type user-guide --format html
/fs:document --type api-docs --include-examples
/fs:document --comprehensive  # Generates all documentation types
```

## Output Structure
```
docs/
├── user-guide/
│   ├── getting-started.md
│   ├── features/
│   └── screenshots/
├── api-docs/
│   ├── endpoints/
│   └── examples/
└── developer-guide/
```

## PRP Traceability
- Links documentation to PRP requirements
- Shows feature coverage
- Validates documentation completeness