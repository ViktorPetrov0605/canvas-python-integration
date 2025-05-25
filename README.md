# Canvas Research & Integration Project

## Project Structure

```
src/
├── canvas/
│   ├── api/         # Core Canvas API implementation
│   ├── models/      # Canvas API data models
│   └── utils/       # Shared utilities
├── interfaces/      # User interface implementations
└── tools/          # Development and integration tools
    ├── openapi/    # OpenAPI schema tools
    ├── proxy/      # API proxy server
    └── generated_tools/ # Auto-generated API clients
```

## Components

### 1. Canvas API Integration
- API client with OpenAPI specification support
- Auto-generated data models
- Authentication handling
- Response validation

### 2. User Interfaces
- Terminal User Interface (TUI) for course navigation
- OpenWebUI tool interface
- Assignment management interface

### 3. Development Tools
- OpenAPI schema parser and generator
- API proxy server for testing
- Document parsing tools
- AI integration utilities

### 4. Document Parsing
- DOCX file content extraction
- Paragraph and table parsing
- Content structure analysis
- Metadata extraction capabilities

## Getting Started

1. Set up environment variables:
   ```bash
   CANVAS_API_TOKEN="your_token_here"
   CANVAS_DOMAIN="your_canvas_domain"
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Choose an interface:
   - TUI: `python src/interfaces/course_tui.py`
   - OpenWebUI: Configure tool in your OpenWebUI installation

## Features

### Implemented
- Course navigation and management
- Assignment listing and details
- Document content extraction
- OpenAPI integration
- Multiple interface options

### Planned
- Submission management
- Content categorization
- Machine learning integration
- Enhanced metadata extraction
- Implement content categorization
- Integrate with machine learning model for content correlation

## End Goal Architecture
