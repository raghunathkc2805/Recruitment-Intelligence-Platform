from search_engine.algorithms.keyword_search import (
    KeywordSearch,
)


def test_keyword_search(
    sample_candidates,
):

    results = KeywordSearch.search(
        "Python",
        sample_candidates,
    )

    assert len(results) == 2