from resume_parser.extractors.name_extractor import (
    NameExtractor,
)


def test_extract_name():

    text = """
    John Michael Doe

    Software Engineer

    john@example.com

    +91 9876543210
    """

    assert (
        NameExtractor.extract(text)
        == "John Michael Doe"
    )


def test_extract_name_none():

    assert NameExtractor.extract("") is None


def test_extract_name_skips_headers():

    text = """
    Resume

    Professional Summary

    Skills
    """

    assert NameExtractor.extract(text) is None