from datetime import UTC, datetime, timedelta, UTC

from api.services.audit_retention_service import AuditRetentionService


class RepositoryStub:

    def __init__(self):
        self.cleaned = False

    def delete_older_than(self, cutoff_date):
        self.cleaned = True
        self.cutoff_date = cutoff_date
        return 12


def test_cleanup_old_records():

    repository = RepositoryStub()
    service = AuditRetentionService(repository)

    deleted = service.cleanup(days=90)

    assert deleted == 12
    assert repository.cleaned is True


def test_cutoff_date_is_datetime():

    repository = RepositoryStub()
    service = AuditRetentionService(repository)

    service.cleanup(days=30)

    assert isinstance(repository.cutoff_date, datetime)


def test_cutoff_date_is_in_past():

    repository = RepositoryStub()
    service = AuditRetentionService(repository)

    before = datetime.now(UTC) - timedelta(days=29)

    service.cleanup(days=30)

    assert repository.cutoff_date < before


def test_zero_day_retention():

    repository = RepositoryStub()
    service = AuditRetentionService(repository)

    deleted = service.cleanup(days=0)

    assert deleted == 12


def test_large_retention():

    repository = RepositoryStub()
    service = AuditRetentionService(repository)

    deleted = service.cleanup(days=3650)

    assert deleted == 12



