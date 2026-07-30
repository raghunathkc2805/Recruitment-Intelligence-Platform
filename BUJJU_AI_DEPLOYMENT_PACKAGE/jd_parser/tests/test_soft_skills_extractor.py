import pytest

from jd_parser.extractors.skills_extractor import extract_skills


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Communication", ["Communication"]),
        ("Leadership", ["Leadership"]),
        ("Teamwork", ["Teamwork"]),
        ("Problem Solving", ["Problem Solving"]),
        ("Analytical Skills", ["Analytical Skills"]),
        ("Decision Making", ["Decision Making"]),
        ("Critical Thinking", ["Critical Thinking"]),
        ("Presentation Skills", ["Presentation Skills"]),
        ("Negotiation", ["Negotiation"]),
        ("Time Management", ["Time Management"]),
        ("Adaptability", ["Adaptability"]),
        ("Creativity", ["Creativity"]),
        ("Interpersonal Skills", ["Interpersonal Skills"]),
        ("Attention to Detail", ["Attention to Detail"]),
        ("Communication Leadership Teamwork", ["Communication", "Leadership", "Teamwork"]),
        ("Leadership Leadership", ["Leadership"]),
        ("No soft skills here", []),
        ("", []),
        (None, []),
    ],
)
def test_soft_skills(text, expected):
    result = extract_skills(text)
    assert result["soft_skills"] == expected