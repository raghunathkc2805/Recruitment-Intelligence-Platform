from ranking_engine.algorithms.tie_breaker import (
    TieBreaker,
)


def test_tie_breaker(candidates):

    ranked = TieBreaker.resolve(
        candidates
    )

    assert ranked[0]["experience"]["years"] == 10