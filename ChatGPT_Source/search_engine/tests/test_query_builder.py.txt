from search_engine.builders.query_builder import (
    QueryBuilder,
)


def test_query_builder():

    query = QueryBuilder.build(
        keywords=["Python"],
        skills=["FastAPI"],
        locations=["Bangalore"],
        experience=5,
    )

    assert "Python" in query

    assert "FastAPI" in query

    assert "Bangalore" in query

    assert "5 years" in query