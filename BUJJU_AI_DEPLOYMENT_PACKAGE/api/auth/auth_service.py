"""
Authentication Service
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from api.auth.jwt_handler import (
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)
from api.auth.password import (
    hash_password,
    verify_password,
)
from database.models.user import User
from database.repositories.user_repository import UserRepository


class AuthenticationError(Exception):
    pass


class AuthService:

    @classmethod
    def register(
        cls,
        db: Session,
        username: str,
        email: str,
        password: str,
        role: str = "Recruiter",
    ) -> User:

        repository = UserRepository(db)

        if repository.get_by_email(email):
            raise AuthenticationError(
                "User already exists."
            )

        user = User(
            username=username,
            email=email,
            password_hash=hash_password(password),
            role=role,
            is_active=True,
        )

        return repository.create(user)

    @classmethod
    def login(
        cls,
        db: Session,
        email: str,
        password: str,
    ) -> dict:

        repository = UserRepository(db)

        user = repository.get_by_email(email)

        if user is None:
            raise AuthenticationError(
                "Invalid email or password."
            )

        if not user.is_active:
            raise AuthenticationError(
                "User account is disabled."
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise AuthenticationError(
                "Invalid email or password."
            )

        claims = {
            "sub": str(user.id),
            "username": user.username,
            "email": user.email,
            "role": user.role,
        }

        return {
            "access_token": create_access_token(claims),
            "refresh_token": create_refresh_token(claims),
            "token_type": "bearer",
            "user": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "role": user.role,
            },
        }

    @classmethod
    def refresh(
        cls,
        refresh_token: str,
    ) -> dict:

        payload = decode_refresh_token(
            refresh_token,
        )

        claims = {
            "sub": payload["sub"],
            "username": payload["username"],
            "email": payload["email"],
            "role": payload["role"],
        }

        return {
            "access_token": create_access_token(
                claims,
            ),
            "refresh_token": create_refresh_token(
                claims,
            ),
            "token_type": "bearer",
        }

    @classmethod
    def change_password(
        cls,
        db: Session,
        user: User,
        current_password: str,
        new_password: str,
    ) -> None:

        if not verify_password(
            current_password,
            user.password_hash,
        ):
            raise AuthenticationError(
                "Current password is incorrect."
            )

        user.password_hash = hash_password(
            new_password,
        )

        db.commit()
        db.refresh(user)