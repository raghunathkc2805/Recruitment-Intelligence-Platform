import uuid

from api.repositories.audit_repository import AuditRepository
from database.models.audit_log import AuditLog


def test_create_audit(db_session):

    repository = AuditRepository(db_session)

    audit = AuditLog(
        id=uuid.uuid4(),
        action="LOGIN",
        event_type="AUTH",
        status="SUCCESS",
    )

    result = repository.create(audit)

    assert result.id == audit.id


def test_get_audit(db_session):

    repository = AuditRepository(db_session)

    audit = AuditLog(
        id=uuid.uuid4(),
        action="LOGIN",
        event_type="AUTH",
        status="SUCCESS",
    )

    repository.create(audit)

    entity = repository.get(audit.id)

    assert entity is not None
    assert entity.id == audit.id


def test_list_audit(db_session):

    repository = AuditRepository(db_session)

    results = repository.list()

    assert isinstance(results, list)


def test_count(db_session):

    repository = AuditRepository(db_session)

    total = repository.count()

    assert isinstance(total, int)


def test_delete_audit(db_session):

    repository = AuditRepository(db_session)

    audit = AuditLog(
        id=uuid.uuid4(),
        action="DELETE",
        event_type="CRUD",
        status="SUCCESS",
    )

    repository.create(audit)

    repository.delete(audit.id)

    assert repository.get(audit.id) is None
