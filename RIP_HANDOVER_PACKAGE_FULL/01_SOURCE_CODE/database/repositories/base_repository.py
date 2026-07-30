"""
Base Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session


class BaseRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def add(
        self,
        model,
    ):
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model

    def delete(
        self,
        model,
    ):
        self.db.delete(model)
        self.db.commit()

    def update(self):
        self.db.commit()