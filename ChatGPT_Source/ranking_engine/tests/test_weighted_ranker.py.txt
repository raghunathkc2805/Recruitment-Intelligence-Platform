from ranking_engine.algorithms.weighted_ranker import (
    WeightedRanker,
)


def test_weighted_ranker(candidates):

    ranked = WeightedRanker.rank(
        candidates
    )

    assert len(ranked) == 3

    assert ranked[0]["overall_score"] >= ranked[1]["overall_score"]