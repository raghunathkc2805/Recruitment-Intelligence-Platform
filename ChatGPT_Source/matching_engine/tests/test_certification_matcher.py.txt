from matching_engine.matchers.certification_matcher import (
    CertificationMatcher,
)


def test_certification_match():

    result = CertificationMatcher.match(
        [
            {
                "certification": "AWS Certified Solutions Architect",
            }
        ],
        [
            "AWS Certified Solutions Architect",
        ],
    )

    assert result["score"] == 100.0

    assert len(result["matched"]) == 1


def test_certification_no_match():

    result = CertificationMatcher.match(
        [
            {
                "certification": "CCNA",
            }
        ],
        [
            "AWS Certified Solutions Architect",
        ],
    )

    assert result["score"] == 0.0