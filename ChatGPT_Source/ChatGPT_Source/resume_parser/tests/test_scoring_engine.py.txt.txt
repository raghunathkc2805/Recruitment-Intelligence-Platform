from resume_parser.ranking.scoring_engine import (
    ScoringEngine,
)


def test_scoring_engine():

    match_result = {
        "skill_match": {"score": 90},
        "experience_match": {"score": 80},
        "education_match": {"score": 100},
        "designation_match": {"score": 70},
        "location_match": {"score": 100},
        "certification_match": {"score": 60},
    }

    result = ScoringEngine.calculate(match_result)

    assert "overall_score" in result

    assert result["overall_score"] > 0

    assert result["overall_score"] <= 100


def test_scoring_engine_custom_weights():

    match_result = {
        "skill_match": {"score": 100},
        "experience_match": {"score": 100},
        "education_match": {"score": 100},
        "designation_match": {"score": 100},
        "location_match": {"score": 100},
        "certification_match": {"score": 100},
    }

    weights = {
        "skills": 0.50,
        "experience": 0.20,
        "education": 0.10,
        "designation": 0.10,
        "location": 0.05,
        "certification": 0.05,
    }

    result = ScoringEngine.calculate(
        match_result,
        weights,
    )

    assert result["overall_score"] == 100.0