from api.repositories.permission_repository import PermissionRepository


class MockRole:
    def __init__(self):
        self.id = 1
        self.name = "Recruiter"


class MockPermission:
    def __init__(self):
        self.id = 10
        self.name = "candidate.view"


class MockResult:
    def first(self):
        return None


class MockSession:

    def query(self, model):
        return self

    def filter(self, *args, **kwargs):
        return self

    def first(self):
        return MockRole()

    def execute(self, *args, **kwargs):
        return MockResult()

    def commit(self):
        pass


def test_repository_creation():

    repo = PermissionRepository(MockSession())

    assert repo is not None


def test_get_role():

    repo = PermissionRepository(MockSession())

    role = repo.get_role_by_name("Recruiter")

    assert role is not None


def test_get_permission():

    class PermissionSession(MockSession):

        def first(self):
            return MockPermission()

    repo = PermissionRepository(PermissionSession())

    permission = repo.get_permission_by_name("candidate.view")

    assert permission is not None


def test_assign_role():

    repo = PermissionRepository(MockSession())

    repo.assign_role_to_user(
        user_id=1,
        role_id=1,
    )


def test_assign_permission():

    repo = PermissionRepository(MockSession())

    repo.assign_permission_to_role(
        role_id=1,
        permission_id=1,
    )
