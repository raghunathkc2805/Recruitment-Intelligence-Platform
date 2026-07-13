from search_engine.algorithms.hybrid_search import (
    HybridSearch,
)


def test_hybrid_search(sample_candidates):

    results = HybridSearch.search(
        "Python Docker",
        sample_candidates,
    )

    assert len(results) >= 1

    assert results[0]["search_score"] > 0