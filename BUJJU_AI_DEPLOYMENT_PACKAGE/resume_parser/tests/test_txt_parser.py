from pathlib import Path

from resume_parser.parsers.txt_parser import TXTParser


def test_txt_parser(sample_txt):

    result = TXTParser.parse(sample_txt)

    assert result["success"] is True

    assert "text" in result

    assert result["text"].strip() != ""

    assert result["file_type"] == ".txt"

    assert result["file_name"] == Path(sample_txt).name