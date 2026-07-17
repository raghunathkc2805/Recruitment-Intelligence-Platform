from resume_parser.extractors.boolean_search_extractor import (
    BooleanSearchExtractor,
)


def test_boolean_search():

    candidate = {
        "skills": {
            "technical_skills": [
                "Python",
                "Docker",
            ],
            "functional_skills": [
                "Project Management",
            ],
            "soft_skills": [
                "Leadership",
            ],
        },
        "education": [
            {
                "degree": "B.E",
            }
        ],
        "employers": [
            {
                "company": "Infosys",
            }
        ],
    }

    result = BooleanSearchExtractor.extract(
        candidate
    )

    assert "boolean_search" in result

    assert '"Python"' in result["boolean_search"]

    assert '"Docker"' in result["boolean_search"]

    assert result["keyword_count"] > 0


def test_boolean_search_empty():

    candidate = {
        "skills": {
            "technical_skills": [],
            "functional_skills": [],
            "soft_skills": [],
        },
        "education": [],
        "employers": [],
    }

    result = BooleanSearchExtractor.extract(
        candidate
    )

    assert result["keyword_count"] == 0

    assert result["boolean_search"] == ""