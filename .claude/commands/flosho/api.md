# /fs:api - API Testing & Documentation

## Purpose
Test APIs and generate visual documentation with request/response examples.

## Usage
```
/fs:api [endpoint] [--method GET|POST|PUT|DELETE] [--document]
```

## What It Does
1. Tests API endpoints from PRP specifications
2. Captures request/response pairs
3. Generates visual API documentation
4. Validates against PRP API contracts
5. Creates example code snippets

## API Test Features
- Request builder with PRP schemas
- Response validation
- Error case testing
- Performance metrics
- Visual documentation

## Examples
```
/fs:api /api/users --method GET --document
/fs:api /api/auth/login --method POST --data '{"email": "test@example.com"}'
/fs:api /api/products --test-all-methods
```

## Documentation Output
- Interactive API documentation
- Request/response examples
- Error scenarios
- Integration code samples
- Postman/Insomnia collections