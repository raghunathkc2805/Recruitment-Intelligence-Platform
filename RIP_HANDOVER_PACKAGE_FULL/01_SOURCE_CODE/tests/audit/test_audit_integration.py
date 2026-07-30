from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_audit_module_available():

    response = client.get("/audit")

    assert response.status_code in (200, 401, 403)


def test_audit_search_endpoint():

    response = client.post(
        "/audit/search",
        json={}
    )

    assert response.status_code in (200, 401, 403)


def test_audit_export_csv():

    response = client.post(
        "/audit/export",
        json={
            "format": "csv"
        }
    )

    assert response.status_code in (200, 401, 403)


def test_audit_export_json():

    response = client.post(
        "/audit/export",
        json={
            "format": "json"
        }
    )

    assert response.status_code in (200, 401, 403)


def test_audit_retention_endpoint():

    response = client.delete("/audit/retention/30")

    assert response.status_code in (200, 401, 403)


def test_audit_user_endpoint():

    response = client.get(
        "/audit/users/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code in (200, 401, 403)


def test_audit_action_endpoint():

    response = client.get("/audit/actions/LOGIN")

    assert response.status_code in (200, 401, 403)


def test_audit_resource_endpoint():

    response = client.get("/audit/resources/candidate")

    assert response.status_code in (200, 401, 403)


def test_invalid_audit_record():

    response = client.get(
        "/audit/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code in (200, 401, 403, 404)


def test_delete_invalid_record():

    response = client.delete(
        "/audit/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code in (200, 401, 403, 404)
