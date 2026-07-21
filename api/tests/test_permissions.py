from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

from api.auth.dependencies import get_current_user
from api.auth.permissions import require_permissions


app = FastAPI()


def admin_user():
    return {
        "id": 1,
        "username": "admin",
        "permissions": [
            "candidate.view",
            "candidate.create",
            "candidate.update",
            "candidate.delete",
        ],
    }


def recruiter_user():
    return {
        "id": 2,
        "username": "recruiter",
        "permissions": [
            "candidate.view",
        ],
    }


@app.get("/admin")
def admin_endpoint(
    current_user=Depends(require_permissions("candidate.delete"))
):
    return {"status": "ok"}


@app.get("/view")
def view_endpoint(
    current_user=Depends(require_permissions("candidate.view"))
):
    return {"status": "ok"}


client = TestClient(app)


def test_permission_granted():

    app.dependency_overrides = {}
    app.dependency_overrides[get_current_user] = admin_user

    response = client.get("/admin")

    assert response.status_code == 200


def test_permission_denied():

    app.dependency_overrides = {}
    app.dependency_overrides[get_current_user] = recruiter_user

    response = client.get("/admin")

    assert response.status_code == 403


def test_view_permission():

    app.dependency_overrides = {}
    app.dependency_overrides[get_current_user] = recruiter_user

    response = client.get("/view")

    assert response.status_code == 200

