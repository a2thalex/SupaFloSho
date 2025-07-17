# /sc:implement - Feature Implementation

## Purpose
Implement features, components, and code functionality with PRP-aware intelligent expert activation.

## Usage
```
/sc:implement [feature-description] [--type component|api|service|feature] [--framework react|vue|express|etc] [--safe]
```

## Arguments
- `feature-description` - Description of what to implement
- `--type` - Implementation type (component, api, service, feature, module)
- `--framework` - Target framework or technology stack
- `--safe` - Use conservative implementation approach
- `--iterative` - Enable iterative development with validation steps
- `--with-tests` - Include test implementation
- `--documentation` - Generate documentation alongside implementation

## PRP Integration
This command automatically:
1. References the current PRP for requirements
2. Ensures implementation aligns with defined specifications
3. Uses PRP-defined technology stack
4. Follows PRP architectural patterns

## Execution Flow
1. Read relevant PRP sections for the feature
2. Analyze implementation requirements
3. Auto-activate relevant personas (frontend, backend, security, etc.)
4. Coordinate with MCP servers when needed
5. Generate implementation code following PRP guidelines
6. Apply security and quality validation
7. Create FloSho test scenarios from PRP

## Auto-Activation Patterns
- **Frontend**: UI components matching PRP UI/UX specs
- **Backend**: APIs following PRP endpoint definitions
- **Security**: Authentication per PRP security requirements
- **Architecture**: System design from PRP architecture
- **Performance**: Optimization for PRP performance criteria

## Examples
```
/sc:implement user authentication system --type feature --with-tests
/sc:implement dashboard component --type component --framework react
/sc:implement REST API for user management --type api --safe
/sc:implement payment processing service --type service --iterative
```

## Integration with FloSho
After implementation, automatically generates FloSho test flows based on PRP test scenarios for the implemented feature.