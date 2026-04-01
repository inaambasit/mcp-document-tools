# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py

# Run a single test by name
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_docx
```

## Architecture

This project exposes Python functions as MCP tools via `FastMCP` from the `mcp` library.

**Entry point:** `main.py` creates the `FastMCP` server instance, imports tool functions, and registers them using `mcp.tool()(function_name)`. Tools must be explicitly imported and registered here — there is no auto-discovery.

**Tool modules** live in `tools/`. Each file contains plain Python functions. Currently:
- `tools/math.py` — arithmetic tools (registered in `main.py`)
- `tools/document.py` — document-to-markdown conversion via `markitdown` (defined and tested but **not yet registered** in `main.py`)

## Defining MCP Tools

Tools are plain Python functions. Use `pydantic.Field` for parameter descriptions and write docstrings in this structure:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="What this parameter is"),
    param2: int = Field(description="What this parameter does"),
) -> str:
    """One-line summary.

    Detailed explanation of what the tool does.

    When to use:
    - Situation A
    - Situation B

    When NOT to use:
    - Situation C

    Examples:
    >>> my_tool("foo", 42)
    "result"
    """
    ...
```

Register the tool in `main.py`:

```python
from tools.my_module import my_tool
mcp.tool()(my_tool)
```

## Code Style

Always apply type annotations to all function arguments and return values, including test methods (`-> None`).

## Testing

Tests use pytest with real binary fixtures in `tests/fixtures/`. When testing document tools, load the fixture as bytes and pass to the function directly — no mocking.
