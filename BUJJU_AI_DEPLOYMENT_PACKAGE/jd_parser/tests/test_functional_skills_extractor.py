import pytest

from jd_parser.extractors.skills_extractor import extract_skills


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Project Management", ["Project Management"]),
        ("Stakeholder Management", ["Stakeholder Management"]),
        ("Vendor Management", ["Vendor Management"]),
        ("Risk Management", ["Risk Management"]),
        ("Change Management", ["Change Management"]),
        ("Incident Management", ["Incident Management"]),
        ("Problem Management", ["Problem Management"]),
        ("Release Management", ["Release Management"]),
        ("Configuration Management", ["Configuration Management"]),
        ("Asset Management", ["Asset Management"]),
        ("ITIL", ["ITIL"]),
        ("Agile", ["Agile"]),
        ("Scrum", ["Scrum"]),
        ("Kanban", ["Kanban"]),
        ("Waterfall", ["Waterfall"]),
        ("Business Analysis", ["Business Analysis"]),
        ("Requirement Gathering", ["Requirement Gathering"]),
        ("Documentation", ["Documentation"]),
        ("Customer Support", ["Customer Support"]),
        ("Operations Management", ["Operations Management"]),
        ("Project Management Agile Scrum", ["Project Management", "Agile", "Scrum"]),
        ("Vendor Management Vendor Management", ["Vendor Management"]),
        ("No functional skills here", []),
        ("", []),
        (None, []),
    ],
)
def test_functional_skills(text, expected):
    result = extract_skills(text)
    assert result["functional_skills"] == expected