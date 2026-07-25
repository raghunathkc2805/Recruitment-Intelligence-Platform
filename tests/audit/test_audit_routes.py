from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_list_audit():

    response = client.get("/audit")

    assert response.status_code in (200, 401, 403)


def test_get_invalid_audit():

    response = client.get(
        "/audit/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code in (200, 404, 401, 403)


def test_search_audit():

    response = client.post(
        "/audit/search",
        json={}
    )

    assert response.status_code in (200, 401, 403)


def test_export_csv():

    response = client.post(
        "/audit/export",
        json={
            "format": "csv"
        }
    )

    assert response.status_code in (200, 401, 403)


def test_export_json():

    response = client.post(
        "/audit/export",
        json={
            "format": "json"
        }
    )

    assert response.status_code in (200, 401, 403)


def test_delete_invalid_audit():

    response = client.delete(
        "/audit/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code in (200, 404, 401, 403)


def test_get_user_audit():

    response = client.get(
        "/audit/users/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code in (200, 401, 403)


def test_get_action_audit():

    response = client.get(
        "/audit/actions/LOGIN"
    )

    assert response.status_code in (200, 401, 403)


def test_get_resource_audit():

    response = client.get(
        "/audit/resources/candidate"
    )

    assert response.status_code in (200, 401, 403)


def test_retention_cleanup():

    response = client.delete(
        "/audit/retention/30"
    )

    assert response.status_code in (200, 401, 403)
