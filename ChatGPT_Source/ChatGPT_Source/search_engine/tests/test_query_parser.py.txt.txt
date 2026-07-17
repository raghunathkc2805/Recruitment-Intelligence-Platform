from search_engine.parsers.query_parser import (
    QueryParser,
)


def test_query_parser():

    result = QueryParser.parse(
        "Python AND Docker"
    )

    assert result["token_count"] == 3

    assert "Python" in result["tokens"]