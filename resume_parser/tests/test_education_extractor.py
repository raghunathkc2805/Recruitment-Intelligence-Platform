from resume_parser.extractors.education_extractor import (
    EducationExtractor,
)


def test_extract_single_education():

    text = """
    Bachelor of Engineering in Computer Science
    2022
    82%
    """

    result = EducationExtractor.extract(text)

    assert len(result) == 1

    assert result[0]["degree"] is not None


def test_extract_multiple_education():

    text = """
    SSLC 2015 85%

    PUC 2017 90%

    B.E Computer Science 2021 8.5/10
    """

    result = EducationExtractor.extract(text)

    assert len(result) >= 3


def test_extract_empty():

    assert EducationExtractor.extract("") == []


def test_extract_no_degree():

    text = """
    Worked as Software Engineer
    Python Developer
    """

    assert EducationExtractor.extract(text) == []