# SupaFloSho PRP Templates

Product Requirements Prompt templates for different project types.

## Available Templates

### basic-app.json
General purpose application template with:
- User stories structure
- Technical specifications
- Test scenarios for FloSho
- Implementation phases
- SupaFloSho integration settings

### web-app.json (coming soon)
Web application specific template with:
- Frontend-focused user stories
- Responsive design requirements
- SEO and performance specs
- Browser compatibility matrix

### api-service.json (coming soon)
API service template with:
- Endpoint specifications
- Authentication requirements
- Rate limiting and scaling
- API documentation structure

### mobile-app.json (coming soon)
Mobile application template with:
- Platform-specific requirements
- Offline functionality
- Push notifications
- App store requirements

## Using Templates

### With xText Command
```bash
/xt:init "My App" --template basic-app
```

### Programmatically
```javascript
import { PRPGenerator } from 'supaflosho/prp';

const prp = await PRPGenerator.fromTemplate('basic-app', {
  projectName: 'My Amazing App',
  description: 'An app that does amazing things',
  vision: 'To revolutionize how people do X'
});
```

## Custom Templates

Create your own templates by:

1. Copy an existing template
2. Modify the structure for your needs
3. Use variables with `${VARIABLE_NAME}` syntax
4. Save in `~/.claude/templates/prp/`

## Template Variables

Common variables available:
- `${PROJECT_NAME}` - Project name
- `${PROJECT_DESCRIPTION}` - Project description
- `${TIMESTAMP}` - Current timestamp
- `${USER}` - Current user
- `${VISION}` - Project vision statement

Custom variables can be defined and will be prompted during initialization.

## Integration with SupaFloSho

Templates automatically configure:
- Which personas to activate
- Test scenarios for FloSho
- MCP server requirements
- Implementation phases

This ensures smooth workflow from initialization through testing and documentation.