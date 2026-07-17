from api.services.recommendation_engine import RecommendationEngine


def test_weighted_score():

    result = RecommendationEngine.calculate(

        matched_skills=8,

        total_required_skills=10,

        experience_match=1.0,

        designation_match=True,

        certification_match=1.0,

        location_match=True,

    )

    assert result.final_score > 80


def test_zero_skill_score():

    result = RecommendationEngine.calculate(

        matched_skills=0,

        total_required_skills=10,

        experience_match=0,

        designation_match=False,

        certification_match=0,

        location_match=False,

    )

    assert result.final_score == 0
