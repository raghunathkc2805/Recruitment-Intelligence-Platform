from ranking_engine.algorithms.scoring_engine import (
    ScoringEngine,
)


def test_scoring_engine():

    result = ScoringEngine.calculate(
        {
            "skill_match": {"score": 100},
            "experience_match": {"score": 100},
            "education_match": {"score": 100},
            "designation_match": {"score": 100},
            "location_match": {"score": 100},
            "certification_match": {"score": 100},
        }
    )

    assert result["overall_score"] == 100.0