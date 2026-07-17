"""
Authentication Router
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from api.auth.auth_service import (
    AuthService,
    AuthenticationError,
)
from api.dependencies import DatabaseSession
from api.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
)
def register(
    request: RegisterRequest,
    db: DatabaseSession,
):

    try:

        return AuthService.register(
            db=db,
            username=request.username,
            email=request.email,
            password=request.password,
            role=request.role,
        )

    except AuthenticationError as exc:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: DatabaseSession,
):

    try:

        return AuthService.login(
            db=db,
            email=request.email,
            password=request.password,
        )

    except AuthenticationError as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc