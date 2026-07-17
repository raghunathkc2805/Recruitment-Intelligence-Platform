from search_engine.algorithms.boolean_search import (
    BooleanSearch,
)


def test_boolean_search(
    sample_candidates,
):

    results = BooleanSearch.search(
        "Python AND Docker",
        sample_candidates,
    )

    assert len(results) == 1