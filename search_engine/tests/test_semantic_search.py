from search_engine.algorithms.semantic_search import (
    SemanticSearch,
)


def test_semantic_search(sample_candidates):

    results = SemanticSearch.search(
        "Python Developer",
        sample_candidates,
    )

    assert len(results) >= 1

    assert results[0]["search_score"] > 0