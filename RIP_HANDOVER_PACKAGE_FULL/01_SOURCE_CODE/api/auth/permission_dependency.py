from functools import lru_cache
from typing import Iterable

from fastapi import Depends, HTTPException, status

from api.auth.dependencies import get_current_user


class PermissionDenied(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )


def _normalize_permissions(values: Iterable[str]) -> set[str]:
    return {
        value.strip().lower()
        for value in values
        if value and value.strip()
    }


@lru_cache(maxsize=None)
def require_permission(permission: str):

    async def dependency(
        current_user=Depends(get_current_user),
    ):
        permissions = _normalize_permissions(
            current_user.get("permissions", [])
        )

        if permission.strip().lower() not in permissions:
            raise PermissionDenied()

        return current_user

    return dependency


@lru_cache(maxsize=None)
def require_any_permission(*permissions: str):

    required = _normalize_permissions(permissions)

    async def dependency(
        current_user=Depends(get_current_user),
    ):
        user_permissions = _normalize_permissions(
            current_user.get("permissions", [])
        )

        if user_permissions.intersection(required):
            return current_user

        raise PermissionDenied()

    return dependency


@lru_cache(maxsize=None)
def require_all_permissions(*permissions: str):

    required = _normalize_permissions(permissions)

    async def dependency(
        current_user=Depends(get_current_user),
    ):
        user_permissions = _normalize_permissions(
            current_user.get("permissions", [])
        )

        if required.issubset(user_permissions):
            return current_user

        raise PermissionDenied()

    return dependency
