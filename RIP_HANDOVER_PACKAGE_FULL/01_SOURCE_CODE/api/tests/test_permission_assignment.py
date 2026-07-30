from api.services.rbac_service import RBACService


class MockRole:

    id = 1


class MockPermission:

    id = 101


class MockRepository:

    def __init__(self):
        self.role_calls = 0
        self.permission_calls = 0

    def get_role_by_name(self, name):
        return MockRole()

    def get_permission_by_name(self, name):
        return MockPermission()

    def assign_role_to_user(self, **kwargs):
        self.role_calls += 1

    def assign_permission_to_role(self, **kwargs):
        self.permission_calls += 1


def test_assign_single_permission():

    service = RBACService(db=None)

    repository = MockRepository()

    service.repository = repository

    service.assign_permission_to_role(
        "Recruiter",
        "candidate.view",
    )

    assert repository.permission_calls == 1


def test_assign_multiple_permissions():

    service = RBACService(db=None)

    repository = MockRepository()

    service.repository = repository

    service.assign_permissions(
        "Recruiter",
        [
            "candidate.view",
            "candidate.create",
            "candidate.update",
        ],
    )

    assert repository.permission_calls == 3


def test_assign_user_role():

    service = RBACService(db=None)

    repository = MockRepository()

    service.repository = repository

    service.assign_role_to_user(
        user_id=10,
        role_name="Recruiter",
    )

    assert repository.role_calls == 1
