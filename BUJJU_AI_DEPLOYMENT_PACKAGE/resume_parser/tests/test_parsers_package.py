from resume_parser.parsers import (
    DOCXParser,
    ParserFactory,
    PDFParser,
    TXTParser,
)


def test_parsers_package_exports():

    assert ParserFactory is not None

    assert PDFParser is not None

    assert DOCXParser is not None

    assert TXTParser is not None