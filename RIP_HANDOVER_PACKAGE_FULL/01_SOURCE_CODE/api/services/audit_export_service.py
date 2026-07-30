from __future__ import annotations

import csv
import io
import json
from typing import Iterable

from database.models.audit_log import AuditLog


class AuditExportService:

    EXPORT_FORMATS = {"csv", "json"}

    def export(self, records: Iterable[AuditLog], export_format: str) -> bytes:

        export_format = export_format.lower()

        if export_format not in self.EXPORT_FORMATS:
            raise ValueError(f"Unsupported export format: {export_format}")

        if export_format == "csv":
            return self._csv(records)

        return self._json(records)

    def _csv(self, records: Iterable[AuditLog]) -> bytes:

        buffer = io.StringIO()

        writer = csv.writer(buffer)

        writer.writerow([
            "id",
            "created_at",
            "user_id",
            "username",
            "action",
            "event_type",
            "resource_type",
            "resource_id",
            "status",
            "client_ip"
        ])

        for item in records:

            writer.writerow([
                item.id,
                getattr(item, "created_at", None),
                item.user_id,
                getattr(item, "username", None),
                item.action,
                item.event_type,
                item.resource_type,
                item.resource_id,
                item.status,
                getattr(item, "client_ip", None)
            ])

        return buffer.getvalue().encode("utf-8")

    def _json(self, records: Iterable[AuditLog]) -> bytes:

        payload = []

        for item in records:

            payload.append({

                "id": str(item.id),
                "created_at": str(getattr(item, "created_at", None)),
                "user_id": str(item.user_id) if item.user_id else None,
                "username": getattr(item, "username", None),
                "action": item.action,
                "event_type": item.event_type,
                "resource_type": item.resource_type,
                "resource_id": item.resource_id,
                "status": item.status,
                "client_ip": getattr(item, "client_ip", None)

            })

        return json.dumps(
            payload,
            indent=2,
            default=str
        ).encode("utf-8")

    def export_json(self, records, output_path):
        output_path.write_bytes(self._json(records))

    def export_csv(self, records, output_path):
        output_path.write_bytes(self._csv(records))


