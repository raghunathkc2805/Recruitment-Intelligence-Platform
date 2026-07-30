from pathlib import Path

from resume_parser.parsers.pdf_parser import PDFParser


def test_pdf_parser(sample_pdf):

    result = PDFParser.parse(sample_pdf)

    assert result["success"] is True

    assert "text" in result

    assert result["text"].strip() != ""

    assert result["file_type"] == ".pdf"

    assert result["file_name"] == Path(sample_pdf).name