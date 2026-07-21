from functools import lru_cache

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from api.auth.dependencies import get_current_user


@lru_cache(maxsize=None)
def require_permissions(*permissions):

    required = {
        permission.strip()
        for permission in permissions
        if permission and permission.strip()
    }

    async def permission_checker(
        current_user=Depends(get_current_user),
    ):

        user_permissions = {
            permission.strip()
            for permission in current_user.get("permissions", [])
            if permission and permission.strip()
        }

        if not required.issubset(user_permissions):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions.",
            )

        return current_user

    return permission_checker
