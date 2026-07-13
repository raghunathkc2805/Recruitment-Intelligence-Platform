from ranking_engine.models.ranked_candidate import (
    RankedCandidate,
)
from ranking_engine.models.ranking_result import (
    RankingResult,
)


def test_ranked_candidate():

    model = RankedCandidate()

    assert model.to_dict()["rank"] == 0


def test_ranking_result():

    model = RankingResult()

    assert model.to_dict()["total_candidates"] == 0