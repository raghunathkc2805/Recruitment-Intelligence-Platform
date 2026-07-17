from search_engine.algorithms.search_ranker import (
    SearchRanker,
)


def test_search_ranker():

    results = [
        {"search_score": 40},
        {"search_score": 95},
        {"search_score": 70},
    ]

    ranked = SearchRanker.rank(results)

    assert ranked[0]["search_score"] == 95

    assert ranked[-1]["search_score"] == 40