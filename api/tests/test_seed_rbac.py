from api.database.rbac_defaults import DEFAULT_ROLE_PERMISSIONS
from api.database.seed_rbac import DEFAULT_PERMISSIONS, DEFAULT_ROLES


def test_default_roles_exist():

    assert len(DEFAULT_ROLES) >= 7

    role_names = [role[0] for role in DEFAULT_ROLES]

    assert "Super Admin" in role_names
    assert "Admin" in role_names
    assert "Recruitment Manager" in role_names
    assert "Recruiter" in role_names
    assert "Hiring Manager" in role_names
    assert "Interviewer" in role_names
    assert "Read Only" in role_names


def test_default_permissions_exist():

    permission_names = [permission[0] for permission in DEFAULT_PERMISSIONS]

    assert "candidate.create" in permission_names
    assert "candidate.view" in permission_names
    assert "candidate.update" in permission_names
    assert "candidate.delete" in permission_names
    assert "resume.upload" in permission_names
    assert "resume.view" in permission_names
    assert "jd.create" in permission_names
    assert "jd.view" in permission_names
    assert "matching.run" in permission_names
    assert "ranking.run" in permission_names
    assert "search.execute" in permission_names


def test_every_role_has_permissions():

    assert len(DEFAULT_ROLE_PERMISSIONS) > 0

    for role_name, permissions in DEFAULT_ROLE_PERMISSIONS.items():

        assert isinstance(role_name, str)
        assert isinstance(permissions, list)
        assert len(permissions) > 0


def test_super_admin_exists():

    assert "Super Admin" in DEFAULT_ROLE_PERMISSIONS


def test_admin_exists():

    assert "Admin" in DEFAULT_ROLE_PERMISSIONS
