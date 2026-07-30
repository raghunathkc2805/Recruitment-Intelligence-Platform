from api.services.boolean_search_service import BooleanSearchService


def test_phrase_search():

    parsed = BooleanSearchService.parse(

        '"Project Manager" AND Cisco'

    )

    assert parsed["phrases"] == [

        "Project Manager"

    ]
