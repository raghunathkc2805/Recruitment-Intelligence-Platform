from search_engine.models.search_query import (
    SearchQuery,
)
from search_engine.models.search_result import (
    SearchResult,
)


def test_search_query():

    model = SearchQuery()

    assert model.to_dict()["limit"] == 25


def test_search_result():

    model = SearchResult()

    assert model.to_dict()["total_results"] == 0