from resume_parser.ranking.recommendation_engine import (
    RecommendationEngine,
)


def test_highly_recommended():

    result = RecommendationEngine.recommend(90)

    assert result["recommendation"] == "Highly Recommended"

    assert result["priority"] == "High"


def test_recommended():

    result = RecommendationEngine.recommend(75)

    assert result["recommendation"] == "Recommended"

    assert result["priority"] == "Medium"


def test_consider():

    result = RecommendationEngine.recommend(55)

    assert result["recommendation"] == "Consider"

    assert result["priority"] == "Low"


def test_not_recommended():

    result = RecommendationEngine.recommend(40)

    assert result["recommendation"] == "Not Recommended"

    assert result["priority"] == "Reject"


def test_score_rounding():

    result = RecommendationEngine.recommend(84.678)

    assert result["score"] == 84.68