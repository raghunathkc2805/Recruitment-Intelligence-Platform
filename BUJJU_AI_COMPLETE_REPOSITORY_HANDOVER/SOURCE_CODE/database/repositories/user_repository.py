"""
User Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.user import User

from .base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def get_by_email(
        self,
        email: str,
    ) -> User | None:

        return (
            self.db.query(User)
            .filter(
                User.email == email
            )
            .first()
        )

    def create(
        self,
        user: User,
    ) -> User:

        return self.add(user)