from matching_engine.matchers.location_matcher import (
    LocationMatcher,
)


def test_location_match():

    result = LocationMatcher.match(
        [
            {
                "location": "Bangalore",
            }
        ],
        [
            "Bangalore",
        ],
    )

    assert result["score"] == 100.0


def test_location_no_match():

    result = LocationMatcher.match(
        [
            {
                "location": "Hyderabad",
            }
        ],
        [
            "Bangalore",
        ],
    )

    assert result["score"] == 0.0