from resume_parser.extractors.certification_extractor import (
    CertificationExtractor,
)


def test_extract_certification():

    result = CertificationExtractor.extract(
        "AWS Certified Solutions Architect"
    )

    assert len(result) >= 1

    assert (
        result[0]["certification"]
        == "AWS Certified Solutions Architect"
    )


def test_extract_multiple_certifications():

    result = CertificationExtractor.extract(
        """
        CCNA
        AWS Certified Solutions Architect
        ITIL Foundation
        """
    )

    assert len(result) >= 2


def test_extract_empty():

    assert CertificationExtractor.extract("") == []


def test_extract_unknown_certification():

    result = CertificationExtractor.extract(
        "Internal Company Excellence Award"
    )

    assert result == []