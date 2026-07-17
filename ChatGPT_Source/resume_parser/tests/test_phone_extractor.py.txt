from resume_parser.extractors.phone_extractor import (
    PhoneExtractor,
)


def test_extract_phone():

    text = """
    John Doe
    +91 9876543210
    """

    assert (
        PhoneExtractor.extract(text)
        == "+919876543210"
    )


def test_extract_multiple_phones():

    text = """
    +91 9876543210
    9123456789
    """

    phones = PhoneExtractor.extract_all(text)

    assert len(phones) == 2

    assert "+919876543210" in phones

    assert "9123456789" in phones


def test_extract_phone_none():

    assert PhoneExtractor.extract("") is None