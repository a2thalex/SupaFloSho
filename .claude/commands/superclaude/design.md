# /sc:design - System Design & Architecture

## Purpose
Design systems, architectures, and technical solutions based on PRP requirements.

## Usage
```
/sc:design [system/component] [--level high|detailed] [--pattern mvc|microservices|etc]
```

## What It Does
1. Reads architectural requirements from PRP
2. Activates architect persona with PRP context
3. Creates design proposals aligned with project goals
4. Generates architectural diagrams and documentation
5. Defines integration points and interfaces

## Design Outputs
- System architecture diagrams
- Component interaction maps
- Database schemas (from PRP data models)
- API contracts (from PRP endpoints)
- Security architecture
- Deployment architecture

## Examples
```
/sc:design overall system architecture
/sc:design microservices architecture --pattern event-driven
/sc:design database schema --level detailed
/sc:design authentication flow
```

## PRP Alignment
- Uses technology stack defined in PRP
- Follows scalability requirements from PRP
- Implements security patterns from PRP
- Designs for PRP-defined user load

## Integration
Designs created here become blueprints for `/sc:implement` commands and test scenarios for FloSho.