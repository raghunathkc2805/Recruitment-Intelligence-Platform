from resume_parser.extractors.resume_search_extractor import (
    ResumeSearchExtractor,
)


def test_resume_search_keywords():

    candidate = {
        "name": "John Doe",
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
        "locations": [
            {
                "location": "Bangalore",
            }
        ],
        "certifications": [
            {
                "certification": "AWS Certified Solutions Architect",
            }
        ],
    }

    result = ResumeSearchExtractor.extract(candidate)

    assert "keywords" in result

    assert "keyword_count" in result

    assert "John Doe" in result["keywords"]

    assert "Python" in result["keywords"]

    assert "Docker" in result["keywords"]

    assert "Infosys" in result["keywords"]

    assert "Bangalore" in result["keywords"]


def test_resume_search_empty():

    candidate = {
        "name": None,
        "skills": {
            "technical_skills": [],
            "functional_skills": [],
            "soft_skills": [],
        },
        "education": [],
        "employers": [],
        "locations": [],
        "certifications": [],
    }

    result = ResumeSearchExtractor.extract(candidate)

    assert result["keywords"] == []

    assert result["keyword_count"] == 0