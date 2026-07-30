"""
database/repositories/audit_repository.py
"""

from __future__ import annotations

from database.models.audit_log import AuditLog
from database.repositories.base_repository import BaseRepository


class AuditRepository(BaseRepository):

    def create(
        self,
        *,
        user_id: str,
        action: str,
        module: str,
        details: str,
    ) -> AuditLog:

        record = AuditLog(
            user_id=user_id,
            action=action,
            module=module,
            details=details,
        )

        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record
