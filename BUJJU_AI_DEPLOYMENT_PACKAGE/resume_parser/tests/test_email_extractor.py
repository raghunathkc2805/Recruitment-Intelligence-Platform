from resume_parser.extractors.email_extractor import (
    EmailExtractor,
)


def test_extract_email():

    text = """
    John Doe
    john.doe@example.com
    """

    assert (
        EmailExtractor.extract(text)
        == "john.doe@example.com"
    )


def test_extract_all_emails():

    text = """
    john@example.com
    hr@example.org
    john@example.com
    """

    emails = EmailExtractor.extract_all(text)

    assert len(emails) == 2

    assert "john@example.com" in emails

    assert "hr@example.org" in emails


def test_extract_email_none():

    assert EmailExtractor.extract("") is None