from __future__ import annotations

from datetime import UTC, datetime, timedelta, UTC

from sqlalchemy import delete

from database.models.audit_log import AuditLog


class AuditRetentionService:

    def __init__(self, db):
        self.db = db

    def cleanup(self, days: int) -> int:
        """
        Backward-compatible cleanup API expected by unit tests.
        """
        cutoff = datetime.now(UTC) - timedelta(days=days)
        return self.db.delete_older_than(cutoff)



    def purge(self, retention_days: int) -> int:

        cutoff = datetime.now(UTC) - timedelta(days=retention_days)

        stmt = (
            delete(AuditLog)
            .where(AuditLog.created_at < cutoff)
        )

        result = self.db.execute(stmt)

        self.db.commit()

        return result.rowcount or 0

    def count_expired(self, retention_days: int) -> int:

        cutoff = datetime.now(UTC) - timedelta(days=retention_days)

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





