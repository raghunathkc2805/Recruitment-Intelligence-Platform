from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from api.auth.permission_dependency import (
    require_permission,
    require_any_permission,
    require_all_permissions,
)

app = FastAPI()


def override_current_user():
    return {
        "id": 1,
        "username": "admin",
        "permissions": [
            "candidate.view",
            "candidate.create",
            "candidate.update",
            "resume.view",
            "resume.upload",
        ],
    }


app.dependency_overrides = {}


@app.get("/permission")
def permission_route(
    user=Depends(require_permission("candidate.view")),
):
    return {"success": True}


@app.get("/any")
def any_route(
    user=Depends(
        require_any_permission(
            "candidate.delete",
            "candidate.view",
        )
    ),
):
    return {"success": True}


@app.get("/all")
def all_route(
    user=Depends(
        require_all_permissions(
            "candidate.view",
            "candidate.create",
        )
    ),
):
    return {"success": True}


client = TestClient(app)


def test_require_permission():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        require_permission("candidate.view")
    ] = override_current_user

    response = client.get("/permission")

    assert response.status_code == 200


def test_require_any_permission():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        require_any_permission(
            "candidate.delete",
            "candidate.view",
        )
    ] = override_current_user

    response = client.get("/any")

    assert response.status_code == 200


def test_require_all_permissions():

    app.dependency_overrides.clear()

    app.dependency_overrides[
        require_all_permissions(
            "candidate.view",
            "candidate.create",
        )
    ] = override_current_user

    response = client.get("/all")

    assert response.status_code == 200
