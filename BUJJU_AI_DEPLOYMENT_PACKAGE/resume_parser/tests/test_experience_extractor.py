from resume_parser.extractors.experience_extractor import (
    ExperienceExtractor,
)


def test_extract_experience():

    result = ExperienceExtractor.extract(
        "Overall experience: 5 years and 6 months."
    )

    assert result is not None

    assert result["years"] == 5

    assert result["months"] == 6

    assert result["total_months"] == 66


def test_extract_decimal_experience():

    result = ExperienceExtractor.extract(
        "Experience: 3.5 years"
    )

    assert result["years"] == 3.5

    assert result["total_months"] == 42


def test_extract_no_experience():

    assert ExperienceExtractor.extract("") is None


def test_extract_multiple_experience_values():

    result = ExperienceExtractor.extract(
        """
        Experience: 2 years

        Total Experience: 8 years 4 months
        """
    )

    assert result["years"] == 8

    assert result["months"] == 4

    assert result["total_months"] == 100