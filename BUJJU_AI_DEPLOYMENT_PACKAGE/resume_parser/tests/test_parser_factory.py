import pytest

from resume_parser.parsers.parser_factory import ParserFactory
from resume_parser.parsers.pdf_parser import PDFParser
from resume_parser.parsers.docx_parser import DOCXParser
from resume_parser.parsers.txt_parser import TXTParser


def test_get_pdf_parser():

    parser = ParserFactory.get_parser("resume.pdf")

    assert parser is PDFParser


def test_get_docx_parser():

    parser = ParserFactory.get_parser("resume.docx")

    assert parser is DOCXParser


def test_get_txt_parser():

    parser = ParserFactory.get_parser("resume.txt")

    assert parser is TXTParser


def test_unsupported_parser():

    with pytest.raises(ValueError):

        ParserFactory.get_parser("resume.xlsx")