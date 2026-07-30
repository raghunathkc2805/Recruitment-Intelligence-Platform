from __future__ import annotations

from fastapi import Depends, HTTPException, status

from api.auth.dependencies import get_current_user
from api.services.permission_service import PermissionService


AUDIT_VIEW = "audit.view"
AUDIT_EXPORT = "audit.export"
AUDIT_ADMIN = "audit.admin"


def require_audit_view(
    current_user=Depends(get_current_user),
):
    permission_service = PermissionService()

    if not permission_service.has_permission(
        current_user,
        AUDIT_VIEW,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Audit view permission required."
        )

    return current_user


def require_audit_export(
    current_user=Depends(get_current_user),
):
    permission_service = PermissionService()

    if not permission_service.has_permission(
        current_user,
        AUDIT_EXPORT,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Audit export permission required."
        )

    return current_user


def require_audit_admin(
    current_user=Depends(get_current_user),
):
    permission_service = PermissionService()

    if not permission_service.has_permission(
        current_user,
        AUDIT_ADMIN,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Audit administrator permission required."
        )

    return current_user
