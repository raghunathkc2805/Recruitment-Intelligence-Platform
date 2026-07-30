from resume_parser.extractors.candidate_match_extractor import (
    CandidateMatchExtractor,
)


def test_candidate_match():

    candidate = {
        "skills": ["Python", "Docker"],
        "experience": {"years": 5},
        "education": [{"degree": "B.E"}],
        "designations": ["Software Engineer"],
        "locations": [{"location": "Bangalore"}],
        "certifications": [
            {
                "certification": "AWS Certified Solutions Architect"
            }
        ],
    }

    requirements = {
        "skills": ["Python"],
        "experience": 3,
        "education": ["B.E"],
        "designations": ["Software Engineer"],
        "locations": ["Bangalore"],
        "certifications": [
            "AWS Certified Solutions Architect"
        ],
    }

    result = CandidateMatchExtractor.extract(
        candidate,
        requirements,
    )

    assert "candidate" in result

    assert "requirements" in result

    assert "match_result" in result

    assert "overall_score" in result


def test_candidate_match_score_range():

    candidate = {
        "skills": ["Python"],
        "experience": {"years": 5},
        "education": [{"degree": "B.E"}],
        "designations": ["Software Engineer"],
        "locations": [{"location": "Bangalore"}],
        "certifications": [],
    }

    requirements = {
        "skills": ["Python"],
        "experience": 5,
        "education": ["B.E"],
        "designations": ["Software Engineer"],
        "locations": ["Bangalore"],
        "certifications": [],
    }

    result = CandidateMatchExtractor.extract(
        candidate,
        requirements,
    )

    assert 0 <= result["overall_score"] <= 100