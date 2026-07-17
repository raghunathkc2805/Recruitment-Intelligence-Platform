from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_unknown_job():

    response = client.get(

        "/recommendations/invalid-job"

    )

    assert response.status_code in (

        404,

        422,

        401,

    )


def test_top_candidate():

    response = client.get(

        "/recommendations/invalid-job/top"

    )

    assert response.status_code in (

        404,

        422,

        401,

    )
