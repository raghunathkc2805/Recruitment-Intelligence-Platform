from resume_parser.extractors.ai_recommendation_extractor import (
    AIRecommendationExtractor,
)


def test_ai_recommendation():

    match_result = {
        "skill_match": {"score": 90},
        "experience_match": {"score": 85},
        "education_match": {"score": 80},
        "designation_match": {"score": 75},
        "location_match": {"score": 100},
        "certification_match": {"score": 70},
    }

    result = AIRecommendationExtractor.extract(
        match_result
    )

    assert "overall_score" in result

    assert "recommendation" in result

    assert "priority" in result


def test_ai_recommendation_high():

    match_result = {
        "skill_match": {"score": 100},
        "experience_match": {"score": 100},
        "education_match": {"score": 100},
        "designation_match": {"score": 100},
        "location_match": {"score": 100},
        "certification_match": {"score": 100},
    }

    result = AIRecommendationExtractor.extract(
        match_result
    )

    assert result["recommendation"] == "Highly Recommended"

    assert result["priority"] == "High"