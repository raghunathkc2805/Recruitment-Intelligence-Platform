from resume_parser.extractors.recruiter_query_extractor import (
    RecruiterQueryExtractor,
)


def test_recruiter_query():

    candidate = {
        "skills": {
            "technical_skills": [
                "Python",
                "Docker",
            ],
            "functional_skills": [
                "Project Management",
            ],
            "soft_skills": [],
        },
        "locations": [
            {
                "location": "Bangalore",
            }
        ],
        "experience": {
            "years": 5,
        },
    }

    result = RecruiterQueryExtractor.extract(
        candidate
    )

    assert "recruiter_query" in result

    assert "Python" in result["recruiter_query"]

    assert "Docker" in result["recruiter_query"]

    assert "5 Years" in result["recruiter_query"]

    assert "Bangalore" in result["recruiter_query"]


def test_recruiter_query_empty():

    candidate = {
        "skills": {
            "technical_skills": [],
            "functional_skills": [],
            "soft_skills": [],
        },
        "locations": [],
        "experience": None,
    }

    result = RecruiterQueryExtractor.extract(
        candidate
    )

    assert result["recruiter_query"] == ""

    assert result["technical_skills"] == []

    assert result["functional_skills"] == []

    assert result["locations"] == []