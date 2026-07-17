from matching_engine.matchers.education_matcher import (
    EducationMatcher,
)


def test_education_match():

    result = EducationMatcher.match(
        [
            {
                "degree": "B.E",
            }
        ],
        [
            "B.E",
        ],
    )

    assert result["score"] == 100.0

    assert len(result["matched"]) == 1


def test_education_partial():

    result = EducationMatcher.match(
        [
            {
                "degree": "Diploma",
            }
        ],
        [
            "B.E",
        ],
    )

    assert result["score"] == 0.0