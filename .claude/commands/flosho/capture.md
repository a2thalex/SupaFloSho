# /fs:capture - Screenshot Capture

## Purpose
Capture annotated screenshots for documentation and testing.

## Usage
```
/fs:capture [name] [--annotate] [--highlight selector] [--viewport size]
```

## What It Does
- Takes screenshots of current application state
- Adds annotations and highlights
- Organizes screenshots by feature/flow
- Generates captions from context

## Capture Options
- `--annotate` - Add automatic annotations
- `--highlight` - Highlight specific elements
- `--viewport` - Set viewport size
- `--wait` - Wait before capture
- `--fullpage` - Capture entire page

## Examples
```
/fs:capture login-form --annotate
/fs:capture dashboard --highlight ".metrics" --viewport desktop
/fs:capture error-state --annotate --wait 2000
```

## Integration
- Used within `/fs:flow` for automatic captures
- Screenshots become part of user documentation
- Linked to PRP requirements for traceability