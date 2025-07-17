# /fs:flow - Define Test Flows

## Purpose
Define and execute visual test flows based on PRP test scenarios.

## Usage
```
/fs:flow "[flow-name]" [--scenario prp-scenario-id] [--viewport desktop|tablet|mobile]
```

## What It Does
1. Reads test scenarios from PRP
2. Creates step-by-step visual flows
3. Captures screenshots at each step
4. Documents user interactions
5. Generates visual test reports

## Flow Actions
- `navigate` - Go to URL
- `click` - Click element
- `fill` - Enter text
- `select` - Choose option
- `screenshot` - Capture state
- `wait` - Wait for element/time
- `hover` - Hover over element
- `press` - Keyboard input

## Examples
```javascript
/fs:flow "User Registration" --scenario user-story-1
// Automatically creates flow from PRP scenario

/fs:flow "Checkout Process" 
[
  { action: 'navigate', url: '/shop' },
  { action: 'click', selector: '.product' },
  { action: 'screenshot', name: 'product-view' },
  { action: 'click', selector: '#add-to-cart' },
  { action: 'navigate', url: '/checkout' },
  { action: 'screenshot', name: 'checkout-form' }
]
```

## PRP Integration
Automatically maps PRP test scenarios to visual flows.