from matching_engine.matchers.designation_matcher import (
    DesignationMatcher,
)


def test_designation_match():

    result = DesignationMatcher.match(
        [
            "Software Engineer",
        ],
        [
            "Software Engineer",
        ],
    )

    assert result["score"] == 100.0


def test_designation_partial():

    result = DesignationMatcher.match(
        [
            "Developer",
        ],
        [
            "Software Engineer",
        ],
    )

    assert result["score"] == 0.0