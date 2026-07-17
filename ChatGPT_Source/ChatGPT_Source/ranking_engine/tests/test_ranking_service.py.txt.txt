from ranking_engine.ranking_service import (
    RankingService,
)


def test_ranking_service(candidates):

    ranked = RankingService.rank(
        candidates
    )

    assert len(ranked) == 3

    assert ranked[0]["overall_score"] >= ranked[-1]["overall_score"]