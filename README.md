# Document Tools

This small Python project connects local PDF and DOCX conversion to an AI assistant through MCP. Microsoft MarkItDown performs the underlying conversion; this repository provides the tool interface, path-based integration and basic fixture tests.

**Scope:** trusted local prototype. It has not been validated as a hosted, multi-user or confidential-document processing service. The fixture tests check basic conversion output; they do not establish extraction fidelity, table accuracy or comprehensive edge-case handling.

**Development:** AI-assisted integration work. The underlying document parser is Microsoft MarkItDown, not a new parsing engine developed in this repository.

## Setup

```bash
# Create a virtual env and activate it
uv venv
source .venv/bin/activate

# Install the package in development mode
uv pip install -e .
```

## Running

```bash
# Start the MCP server
uv run main.py
```

## Testing

```bash
# Run all tests
uv run pytest
```

## Development

### Tool Definitions

Tools are defined as Python functions and registered with the MCP server:

```python
mcp.tool()(my_function)
```

Tool descriptions should:

- Begin with a one-line summary
- Provide detailed explanation of functionality
- Explain when to use (and not use) the tool
- Include usage examples with expected input/output

Use `Field` from pydantic for parameter descriptions:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """Comprehensive docstring here"""
    # Implementation
```
