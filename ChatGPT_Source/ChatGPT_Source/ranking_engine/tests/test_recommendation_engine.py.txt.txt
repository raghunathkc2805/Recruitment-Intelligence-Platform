from ranking_engine.algorithms.recommendation_engine import (
    RecommendationEngine,
)


def test_high():

    result = RecommendationEngine.recommend(95)

    assert result["priority"] == "High"


def test_medium():

    result = RecommendationEngine.recommend(80)

    assert result["priority"] == "Medium"


def test_low():

    result = RecommendationEngine.recommend(65)

    assert result["priority"] == "Low"


def test_reject():

    result = RecommendationEngine.recommend(40)

    assert result["priority"] == "Reject"