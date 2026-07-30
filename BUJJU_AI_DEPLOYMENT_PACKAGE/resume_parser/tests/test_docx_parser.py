from pathlib import Path

from resume_parser.parsers.docx_parser import DOCXParser


def test_docx_parser(sample_docx):

    result = DOCXParser.parse(sample_docx)

    assert result["success"] is True

    assert "text" in result

    assert result["text"].strip() != ""

    assert result["file_type"] == ".docx"

    assert result["file_name"] == Path(sample_docx).name