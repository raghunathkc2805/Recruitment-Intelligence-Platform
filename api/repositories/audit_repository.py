from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from database.models.audit_log import AuditLog


class AuditRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, audit: AuditLog) -> AuditLog:
        self.db.add(audit)
        self.db.commit()
        self.db.refresh(audit)
        return audit

    def get(self, audit_id: UUID | str):
        return self.db.get(AuditLog, str(audit_id))

    def delete(self, audit_id: UUID | str):
        entity = self.get(str(audit_id))
        if entity:
            self.db.delete(entity)
            self.db.commit()
        return entity

    def list(
        self,
        page: int = 1,
        page_size: int = 50,
    ):
        stmt = (
            select(AuditLog)
            .order_by(AuditLog.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        )
        return self.db.scalars(stmt).all()

    def count(self):
        stmt = select(func.count()).select_from(AuditLog)
        return self.db.scalar(stmt)

    def by_user(
        self,
        user_id: UUID | str,
        page: int = 1,
        page_size: int = 50,
    ):
        stmt = (
            select(AuditLog)
            .where(AuditLog.user_id == str(user_id))
            .order_by(AuditLog.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        )
        return self.db.scalars(stmt).all()

    def by_action(self, action: str):
        stmt = (
            select(AuditLog)
            .where(AuditLog.action == action)
            .order_by(AuditLog.created_at.desc())
        )
        return self.db.scalars(stmt).all()

    def by_resource(
        self,
        resource_type: str,
        resource_id: Optional[str] = None,
    ):
        stmt = select(AuditLog).where(
            AuditLog.resource_type == resource_type
        )

        if resource_id:
            stmt = stmt.where(
                AuditLog.resource_id == resource_id
            )

        stmt = stmt.order_by(AuditLog.created_at.desc())

        return self.db.scalars(stmt).all()

    def search(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        action: Optional[str] = None,
        status: Optional[str] = None,
        user_id: Optional[UUID | str] = None,
    ):
        stmt = select(AuditLog)

        if start_date:
            stmt = stmt.where(
                AuditLog.created_at >= start_date
            )

        if end_date:
            stmt = stmt.where(
                AuditLog.created_at <= end_date
            )

        if action:
            stmt = stmt.where(
                AuditLog.action == action
            )

        if status:
            stmt = stmt.where(
                AuditLog.status == status
            )

        if user_id:
            stmt = stmt.where(
                AuditLog.user_id == str(user_id)
            )

        stmt = stmt.order_by(AuditLog.created_at.desc())

        return self.db.scalars(stmt).all()
