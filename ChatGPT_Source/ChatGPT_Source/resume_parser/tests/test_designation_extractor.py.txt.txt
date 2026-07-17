from resume_parser.extractors.designation_extractor import (
    DesignationExtractor,
)


def test_extract_designation():

    result = DesignationExtractor.extract(
        """
        Worked as Senior Software Engineer.
        Previously Software Engineer.
        """
    )

    assert len(result) >= 1

    assert "designation" in result[0]


def test_extract_multiple_designations():

    result = DesignationExtractor.extract(
        """
        Project Manager
        Technical Lead
        Software Engineer
        """
    )

    assert len(result) >= 2


def test_extract_empty():

    assert DesignationExtractor.extract("") == []


def test_extract_unknown_designation():

    result = DesignationExtractor.extract(
        "Founder of My Startup"
    )

    assert isinstance(result, list)