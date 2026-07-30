import uuid

from api.repositories.audit_repository import AuditRepository
from api.schemas.audit import AuditCreate
from api.services.audit_service import AuditService


def test_create_audit(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    audit = AuditCreate(
        action="LOGIN",
        event_type="AUTH",
        status="SUCCESS"
    )

    result = service.create(audit)

    assert result.action == "LOGIN"
    assert result.event_type == "AUTH"
    assert result.status == "SUCCESS"


def test_get_audit(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    audit = service.create(
        AuditCreate(
            action="LOGIN",
            event_type="AUTH",
            status="SUCCESS"
        )
    )

    entity = service.get(audit.id)

    assert entity.id == audit.id


def test_list_audit(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    results = service.list()

    assert isinstance(results, list)


def test_count_audit(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    total = service.count()

    assert isinstance(total, int)


def test_delete_audit(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    audit = service.create(
        AuditCreate(
            action="DELETE",
            event_type="CRUD",
            status="SUCCESS"
        )
    )

    service.delete(audit.id)

    assert service.get(audit.id) is None


def test_search_audit(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    results = service.search(
        action="LOGIN"
    )

    assert isinstance(results, list)


def test_find_by_user(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    user_id = uuid.uuid4()

    results = service.by_user(user_id)

    assert isinstance(results, list)


def test_find_by_action(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    results = service.by_action("LOGIN")

    assert isinstance(results, list)


def test_find_by_resource(db_session):

    repository = AuditRepository(db_session)
    service = AuditService(repository)

    results = service.by_resource("candidate")

    assert isinstance(results, list)
