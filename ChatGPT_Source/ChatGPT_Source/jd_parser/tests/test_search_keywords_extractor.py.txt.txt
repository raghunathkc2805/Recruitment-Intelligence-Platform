import pytest

from jd_parser.extractors.search_keywords_extractor import extract_search_keywords


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            "Python Developer with Django and AWS",
            ["Python Developer", "Django", "AWS"],
        ),
        (
            "Cisco Network Engineer with CCNA",
            ["Cisco", "Network Engineer", "CCNA"],
        ),
        (
            "Java Full Stack Developer Spring Boot React",
            ["Java", "Full Stack Developer", "Spring Boot", "React"],
        ),
        (
            "Telecom Engineer with GPON and DWDM",
            ["Telecom Engineer", "GPON", "DWDM"],
        ),
        (
            "Project Manager PMP Agile",
            ["Project Manager", "PMP", "Agile"],
        ),
        (
            "Python Python AWS AWS",
            ["Python", "AWS"],
        ),
        (
            "",
            [],
        ),
        (
            None,
            [],
        ),
    ],
)
def test_extract_search_keywords(text, expected):
    assert extract_search_keywords(text) == expected