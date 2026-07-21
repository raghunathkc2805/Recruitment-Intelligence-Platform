from api.repositories.rbac_repository import RBACRepository


class MockRole:
    def __init__(self):
        self.id = 1
        self.name = "Recruiter"


class MockPermission:
    def __init__(self):
        self.id = 1
        self.name = "candidate.view"
        self.module = "candidate"


class MockQuery:

    def __init__(self, result):
        self.result = result

    def filter(self, *args, **kwargs):
        return self

    def order_by(self, *args, **kwargs):
        return self

    def first(self):
        return self.result

    def all(self):
        return [self.result]


class MockSession:

    def query(self, model):

        if model.__name__ == "Role":
            return MockQuery(MockRole())

        return MockQuery(MockPermission())

    def add(self, obj):
        pass

    def commit(self):
        pass

    def refresh(self, obj):
        pass


def test_get_role():

    repo = RBACRepository(MockSession())

    role = repo.get_role("Recruiter")

    assert role.name == "Recruiter"


def test_list_roles():

    repo = RBACRepository(MockSession())

    roles = repo.list_roles()

    assert len(roles) == 1


def test_get_permission():

    repo = RBACRepository(MockSession())

    permission = repo.get_permission("candidate.view")

    assert permission.name == "candidate.view"


def test_list_permissions():

    repo = RBACRepository(MockSession())

    permissions = repo.list_permissions()

    assert len(permissions) == 1


def test_create_role():

    repo = RBACRepository(MockSession())

    role = repo.create_role(
        name="Hiring Manager",
        description="Hiring Manager",
    )

    assert role.name == "Hiring Manager"


def test_create_permission():

    repo = RBACRepository(MockSession())

    permission = repo.create_permission(
        name="resume.view",
        module="resume",
    )

    assert permission.name == "resume.view"
