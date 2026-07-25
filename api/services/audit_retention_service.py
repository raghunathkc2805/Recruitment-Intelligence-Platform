from __future__ import annotations

from datetime import datetime, timedelta

from sqlalchemy import delete

from database.models.audit_log import AuditLog


class AuditRetentionService:

    def __init__(self, db):
        self.db = db

    def purge(self, retention_days: int) -> int:

        cutoff = datetime.utcnow() - timedelta(days=retention_days)

        stmt = (
            delete(AuditLog)
            .where(AuditLog.created_at < cutoff)
        )

        result = self.db.execute(stmt)

        self.db.commit()

        return result.rowcount or 0

    def count_expired(self, retention_days: int) -> int:

        cutoff = datetime.utcnow() - timedelta(days=retention_days)

        return (
            self.db.query(AuditLog)
            .filter(AuditLog.created_at < cutoff)
            .count()
        )

    def oldest_record(self):

        return (
            self.db.query(AuditLog)
            .order_by(AuditLog.created_at.asc())
            .first()
        )

    def newest_record(self):

        return (
            self.db.query(AuditLog)
            .order_by(AuditLog.created_at.desc())
            .first()
        )
