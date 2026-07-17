from matching_engine.matching_service import (
    MatchingService,
)


def test_matching_service(
    candidate,
    job,
):

    result = MatchingService.match(
        candidate,
        job,
    )

    assert "overall_score" in result

    assert (
        result["overall_score"] >= 0
    )

    assert (
        result["recommendation"]
        != ""
    )