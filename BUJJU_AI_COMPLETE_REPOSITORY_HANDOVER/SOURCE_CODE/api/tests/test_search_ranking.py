from api.services.boolean_search_service import BooleanSearchService


def test_boolean_parser():

    parsed = BooleanSearchService.parse(

        'Python AND FastAPI OR Django NOT PHP'

    )

    assert "Python" in parsed["and"]

    assert "FastAPI" in parsed["and"]

    assert "Django" in parsed["or"]

    assert "PHP" in parsed["not"]
