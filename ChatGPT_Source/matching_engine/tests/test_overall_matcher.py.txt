from matching_engine.matchers.overall_matcher import (
    OverallMatcher,
)


def test_overall_match(
    candidate,
    job,
):

    result = OverallMatcher.match(
        candidate,
        job,
    )

    assert "overall_score" in result

    assert result["overall_score"] >= 0

    assert "skill_match" in result

    assert "experience_match" in result

    assert "education_match" in result

    assert "designation_match" in result

    assert "location_match" in result

    assert "certification_match" in result