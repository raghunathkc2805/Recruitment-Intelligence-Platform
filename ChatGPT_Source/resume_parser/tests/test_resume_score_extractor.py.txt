from resume_parser.extractors.resume_score_extractor import (
    ResumeScoreExtractor,
)


def test_resume_score_complete():

    candidate = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+919876543210",
        "summary": "Python Developer",
        "experience": {"years": 5},
        "education": [{"degree": "B.E"}],
        "skills": {
            "technical_skills": ["Python", "Docker"],
            "functional_skills": ["Project Management"],
            "soft_skills": ["Leadership"],
        },
        "projects": [{"project_name": "Project A"}],
        "certifications": [
            {
                "certification": "AWS Certified Solutions Architect"
            }
        ],
    }

    result = ResumeScoreExtractor.extract(candidate)

    assert result["resume_score"] == 100

    assert result["grade"] == "A"


def test_resume_score_partial():

    candidate = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": None,
        "summary": None,
        "experience": None,
        "education": [],
        "skills": {
            "technical_skills": [],
            "functional_skills": [],
            "soft_skills": [],
        },
        "projects": [],
        "certifications": [],
    }

    result = ResumeScoreExtractor.extract(candidate)

    assert result["resume_score"] == 20

    assert result["grade"] == "D"


def test_resume_score_empty():

    result = ResumeScoreExtractor.extract({})

    assert result["resume_score"] == 0

    assert result["grade"] == "D"