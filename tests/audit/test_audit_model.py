import uuid

from database.models.audit_log import AuditLog


def test_audit_model_creation():

    audit = AuditLog(
        id=uuid.uuid4(),
        action="LOGIN",
        event_type="AUTH",
        status="SUCCESS",
    )

    assert audit.action == "LOGIN"
    assert audit.event_type == "AUTH"
    assert audit.status == "SUCCESS"


def test_audit_model_resource():

    audit = AuditLog(
        id=uuid.uuid4(),
        action="UPDATE",
        event_type="CRUD",
        resource_type="candidate",
        resource_id="123",
        status="SUCCESS",
    )

    assert audit.resource_type == "candidate"
    assert audit.resource_id == "123"


def test_audit_model_network():

    audit = AuditLog(
        id=uuid.uuid4(),
        action="LOGIN",
        event_type="AUTH",
        client_ip="127.0.0.1",
        status="SUCCESS",
    )

    assert audit.client_ip == "127.0.0.1"
