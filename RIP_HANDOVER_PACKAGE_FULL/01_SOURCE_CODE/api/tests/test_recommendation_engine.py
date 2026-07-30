from api.services.recommendation_engine import RecommendationEngine


def test_full_match():

    result = RecommendationEngine.calculate(

        matched_skills=10,

        total_required_skills=10,

        experience_match=1.0,

        designation_match=True,

        certification_match=1.0,

        location_match=True,

    )

    assert result.final_score == 100.0


def test_partial_match():

    result = RecommendationEngine.calculate(

        matched_skills=5,

        total_required_skills=10,

        experience_match=0.5,

        designation_match=False,

        certification_match=0.5,

        location_match=False,

    )

    assert result.final_score > 0


def test_no_required_skills():

    result = RecommendationEngine.calculate(

        matched_skills=0,

        total_required_skills=0,

        experience_match=0,

        designation_match=False,

        certification_match=0,

        location_match=False,

    )

    assert result.final_score == 50.0
