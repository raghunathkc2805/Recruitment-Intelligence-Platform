from fastapi import HTTPException

from api.dependencies.audit_permission import (
    require_audit_admin,
    require_audit_export,
    require_audit_view,
)


class PermissionServiceStub:

    def __init__(self, allowed=True):
        self.allowed = allowed

    def has_permission(self, user, permission):
        return self.allowed


class UserStub:
    id = 1


def test_view_permission_allowed(monkeypatch):

    import api.dependencies.audit_permission as permission

    monkeypatch.setattr(
        permission,
        "PermissionService",
        lambda: PermissionServiceStub(True),
    )

    result = permission.require_audit_view(UserStub())

    assert result is not None


def test_view_permission_denied(monkeypatch):

    import api.dependencies.audit_permission as permission

    monkeypatch.setattr(
        permission,
        "PermissionService",
        lambda: PermissionServiceStub(False),
    )

    try:
        permission.require_audit_view(UserStub())
        assert False
    except HTTPException as ex:
        assert ex.status_code == 403


def test_export_permission_allowed(monkeypatch):

    import api.dependencies.audit_permission as permission

    monkeypatch.setattr(
        permission,
        "PermissionService",
        lambda: PermissionServiceStub(True),
    )

    result = permission.require_audit_export(UserStub())

    assert result is not None


def test_admin_permission_allowed(monkeypatch):

    import api.dependencies.audit_permission as permission

    monkeypatch.setattr(
        permission,
        "PermissionService",
        lambda: PermissionServiceStub(True),
    )

    result = permission.require_audit_admin(UserStub())

    assert result is not None
