from resume_parser.extractors.employer_extractor import (
    EmployerExtractor,
)


def test_extract_employer():

    result = EmployerExtractor.extract(
        "Worked at Infosys Technologies Ltd."
    )

    assert len(result) >= 1

    assert result[0]["company"] == "Infosys"


def test_extract_multiple_employers():

    result = EmployerExtractor.extract(
        """
        Infosys
        TCS
        Wipro
        """
    )

    assert len(result) >= 2


def test_extract_empty():

    assert EmployerExtractor.extract("") == []


def test_extract_unknown_company():

    result = EmployerExtractor.extract(
        "Worked at My Startup Pvt Ltd."
    )

    assert result == []