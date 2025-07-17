# /fs:flow

## Define FloSho Test Flow

Creates visual test flows based on PRP scenarios with automatic documentation.

## Syntax
```
/fs:flow "flow name" [flags]
```

## PRP Integration

FloSho flows are automatically derived from:
- PRP user stories
- Test scenarios in PRP
- Acceptance criteria
- Success metrics

## Examples

### Basic User Flow
```bash
/fs:flow "User Registration"
# Creates flow from PRP registration story
# Captures each step with screenshots
# Validates against PRP criteria
# Generates user guide
```

### Complex Workflow
```bash
/fs:flow "Complete Purchase" --with-api
# Tests UI flow and API calls
# Screenshots each step
# Documents request/response
# Creates visual guide
```

### From PRP Scenario
```bash
/fs:flow --from-prp "scenario-3"
# Uses specific PRP test scenario
# Implements exact steps
# Validates acceptance criteria
# Auto-generates documentation
```

## Flow Structure

```javascript
await flosho.flow('Flow Name', [
  {
    action: 'navigate',
    url: '/page',
    description: 'Start point'
  },
  {
    action: 'fill',
    selector: '#input',
    value: 'test data',
    description: 'Enter information'
  },
  {
    action: 'click',
    selector: '#submit',
    description: 'Submit form',
    highlightSelector: '#submit'
  },
  {
    action: 'screenshot',
    name: 'result',
    description: 'Final state'
  }
]);
```

## Actions Available

- `navigate` - Go to URL
- `click` - Click element
- `fill` - Enter text
- `select` - Choose option
- `screenshot` - Capture state
- `wait` - Wait for element/time
- `hover` - Hover over element
- `press` - Press key
- `api` - Test API endpoint

## Documentation Output

1. **User Manual** - Step-by-step guide with screenshots
2. **API Docs** - Visual request/response documentation
3. **Test Report** - Coverage and results
4. **Video Guide** - Optional screen recording

## Flags

- `--from-prp [id]` - Use PRP scenario
- `--with-api` - Include API testing
- `--viewport [size]` - Test responsive design
- `--record` - Create video guide
- `--validate` - Strict PRP validation

## Integration

FloSho flows integrate with:
- PRP test scenarios
- SuperClaude implementations
- Personas for test creation
- MCP Playwright server

## Related Commands

- `/fs:capture` - Take screenshots
- `/fs:api` - Test APIs
- `/fs:document` - Generate docs
- `/xt:validate` - Validate coverage