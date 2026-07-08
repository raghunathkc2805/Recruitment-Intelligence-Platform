import pytest

from jd_parser.extractors.certification_extractor import extract_certifications


@pytest.mark.parametrize(
    "text, expected",
    [
        ("CCNA", ["CCNA"]),
        ("CCNP", ["CCNP"]),
        ("CCIE", ["CCIE"]),
        ("RHCE", ["RHCE"]),
        ("RHCSA", ["RHCSA"]),
        ("AWS Certified Solutions Architect", ["AWS Certified Solutions Architect"]),
        ("Azure Administrator", ["Azure Administrator"]),
        ("Google Cloud Professional", ["Google Cloud Professional"]),
        ("PMP", ["PMP"]),
        ("Prince2", ["Prince2"]),
        ("ITIL", ["ITIL"]),
        ("CEH", ["CEH"]),
        ("CISSP", ["CISSP"]),
        ("CompTIA Security+", ["CompTIA Security+"]),
        ("CCNA CCNP", ["CCNA", "CCNP"]),
        ("CCNA CCNA", ["CCNA"]),
        ("No certification mentioned", []),
        ("", []),
        (None, []),
    ],
)
def test_extract_certifications(text, expected):
    assert extract_certifications(text) == expected