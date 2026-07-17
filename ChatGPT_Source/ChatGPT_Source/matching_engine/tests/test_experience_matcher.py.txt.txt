from matching_engine.matchers.experience_matcher import (
    ExperienceMatcher,
)


def test_experience_match():

    result = ExperienceMatcher.match(
        {"years": 8},
        5,
    )

    assert result["qualified"] is True

    assert result["score"] == 100.0


def test_experience_partial():

    result = ExperienceMatcher.match(
        {"years": 2},
        5,
    )

    assert result["qualified"] is False

    assert result["score"] == 40.0


def test_experience_empty():

    result = ExperienceMatcher.match(
        None,
        5,
    )

    assert result["candidate_years"] == 0

    assert result["qualified"] is False