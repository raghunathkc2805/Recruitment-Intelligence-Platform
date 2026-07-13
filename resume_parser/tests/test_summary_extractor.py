from resume_parser.extractors.summary_extractor import (
    SummaryExtractor,
)


def test_extract_summary():

    text = """
    PROFESSIONAL SUMMARY

    Experienced Python Developer with 8 years of
    experience in Telecom and Cloud technologies.

    SKILLS

    Python
    Docker
    """

    result = SummaryExtractor.extract(text)

    assert result is not None

    assert "Python Developer" in result


def test_extract_career_objective():

    text = """
    Career Objective

    To work in a challenging organization.

    Experience

    ABC Company
    """

    result = SummaryExtractor.extract(text)

    assert result == "To work in a challenging organization."


def test_extract_empty():

    assert SummaryExtractor.extract("") is None


def test_extract_without_summary_section():

    text = """
    Experience

    Software Engineer
    """

    assert SummaryExtractor.extract(text) is None