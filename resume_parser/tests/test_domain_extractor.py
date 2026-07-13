from resume_parser.extractors.domain_extractor import (
    DomainExtractor,
)


def test_extract_domain():

    result = DomainExtractor.extract(
        """
        Worked in Telecom and Cloud Computing domains.
        """
    )

    assert len(result) >= 1

    assert "domain" in result[0]


def test_extract_multiple_domains():

    result = DomainExtractor.extract(
        """
        Telecom
        Datacenter
        Networking
        Cloud
        """
    )

    assert len(result) >= 2


def test_extract_empty():

    assert DomainExtractor.extract("") == []


def test_extract_unknown_domain():

    result = DomainExtractor.extract(
        "Interested in outdoor sports."
    )

    assert result == []