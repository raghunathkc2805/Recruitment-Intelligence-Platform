import csv
import json
from pathlib import Path

from api.services.audit_export_service import AuditExportService


class DummyAudit:

    def __init__(self):

        self.id = "1"
        self.action = "LOGIN"
        self.event_type = "AUTH"
        self.status = "SUCCESS"
        self.user_id = "100"
        self.resource_type = "candidate"
        self.resource_id = "500"


def test_export_json(tmp_path):

    service = AuditExportService()

    output = tmp_path / "audit.json"

    service.export_json(
        [DummyAudit()],
        output
    )

    assert output.exists()

    data = json.loads(output.read_text())

    assert len(data) == 1
    assert data[0]["action"] == "LOGIN"


def test_export_csv(tmp_path):

    service = AuditExportService()

    output = tmp_path / "audit.csv"

    service.export_csv(
        [DummyAudit()],
        output
    )

    assert output.exists()

    with open(output, newline="", encoding="utf-8") as fp:

        rows = list(csv.DictReader(fp))

    assert len(rows) == 1
    assert rows[0]["action"] == "LOGIN"


def test_empty_json_export(tmp_path):

    service = AuditExportService()

    output = tmp_path / "empty.json"

    service.export_json([], output)

    assert output.exists()

    data = json.loads(output.read_text())

    assert data == []


def test_empty_csv_export(tmp_path):

    service = AuditExportService()

    output = tmp_path / "empty.csv"

    service.export_csv([], output)

    assert output.exists()


def test_export_overwrite(tmp_path):

    service = AuditExportService()

    output = tmp_path / "audit.json"

    service.export_json([DummyAudit()], output)
    service.export_json([DummyAudit()], output)

    assert output.exists()
