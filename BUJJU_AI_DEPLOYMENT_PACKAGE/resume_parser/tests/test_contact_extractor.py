from resume_parser.extractors.contact_extractor import (
    ContactExtractor,
)


def test_contact_extractor():

    text = """
    John Michael Doe

    john.doe@example.com

    +91 9876543210
    """

    result = ContactExtractor.extract(text)

    assert result["name"] == "John Michael Doe"

    assert result["email"] == "john.doe@example.com"

    assert result["phone"] == "+919876543210"


def test_contact_extractor_empty():

    result = ContactExtractor.extract("")

    assert result["name"] is None

    assert result["email"] is None

    assert result["phone"] is None