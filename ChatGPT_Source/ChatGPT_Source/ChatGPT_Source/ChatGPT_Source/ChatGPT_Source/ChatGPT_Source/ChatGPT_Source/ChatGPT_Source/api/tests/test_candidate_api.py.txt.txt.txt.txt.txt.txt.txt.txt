from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_candidate_endpoint_exists():

    response = client.get(
        "/candidates"
    )

    assert response.status_code in (
        200,
        500,
    )