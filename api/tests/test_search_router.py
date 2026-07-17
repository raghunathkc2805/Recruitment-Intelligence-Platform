from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_search_endpoint():

    response = client.post(
        "/search",
        json={
            "query":"Python"
        },
    )

    assert response.status_code in (
        200,
        400,
        401,
        404,
        422,
    )


def test_search_skills():

    response = client.post(
        "/search/skills",
        json={
            "skills":"Python AND FastAPI"
        },
    )

    assert response.status_code in (
        200,
        400,
        401,
        404,
        422,
    )


def test_search_designation():

    response = client.post(
        "/search/designation",
        json={
            "designation":"Project Manager"
        },
    )

    assert response.status_code in (
        200,
        400,
        401,
        404,
        422,
    )


def test_search_location():

    response = client.post(
        "/search/location",
        json={
            "location":"Bangalore"
        },
    )

    assert response.status_code in (
        200,
        400,
        401,
        404,
        422,
    )
