from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field


def binary_document_to_markdown(
    binary_data: bytes = Field(description="Raw binary content of the document to convert"),
    file_type: str = Field(description="File extension indicating the document format (e.g. 'docx', 'pdf')"),
) -> str:
    """Convert binary document data to markdown-formatted text.

    Accepts the raw bytes of a document and its file type, and returns the
    document content as a markdown string using the MarkItDown library.

    When to use:
    - When you have binary document content (e.g. read from disk or received over a network)
      and need to extract it as readable markdown text

    When NOT to use:
    - When you already have a file path — open and read the file to bytes first

    Examples:
    >>> with open("report.docx", "rb") as f:
    ...     md = binary_document_to_markdown(f.read(), "docx")
    >>> with open("report.pdf", "rb") as f:
    ...     md = binary_document_to_markdown(f.read(), "pdf")
    """
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    file_path: str = Field(description="Absolute or relative path to a PDF or DOCX file to convert"),
) -> str:
    """Convert a PDF or DOCX file at a given path to markdown-formatted text.

    Reads the file at the provided path, detects the format from the file
    extension, and returns the document content as a markdown string.

    When to use:
    - When you have a file path to a PDF or DOCX document and want its contents as markdown

    When NOT to use:
    - When you already have the file's binary content — use binary_document_to_markdown instead

    Examples:
    >>> md = document_path_to_markdown("report.docx")
    >>> md = document_path_to_markdown("/tmp/report.pdf")
    """
    path = Path(file_path)
    file_type = path.suffix.lstrip(".")
    binary_data = path.read_bytes()
    return binary_document_to_markdown(binary_data, file_type)
