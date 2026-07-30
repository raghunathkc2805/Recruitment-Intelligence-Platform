from api.auth.permission_constants import Permission


def test_candidate_permissions():

    assert Permission.CANDIDATE_CREATE == "candidate.create"
    assert Permission.CANDIDATE_VIEW == "candidate.view"
    assert Permission.CANDIDATE_UPDATE == "candidate.update"
    assert Permission.CANDIDATE_DELETE == "candidate.delete"


def test_resume_permissions():

    assert Permission.RESUME_UPLOAD == "resume.upload"
    assert Permission.RESUME_VIEW == "resume.view"


def test_jd_permissions():

    assert Permission.JD_CREATE == "jd.create"
    assert Permission.JD_VIEW == "jd.view"


def test_matching_permissions():

    assert Permission.MATCHING_RUN == "matching.run"


def test_ranking_permissions():

    assert Permission.RANKING_RUN == "ranking.run"


def test_search_permissions():

    assert Permission.SEARCH_EXECUTE == "search.execute"


def test_user_permissions():

    assert Permission.USER_CREATE == "user.create"
    assert Permission.USER_VIEW == "user.view"
    assert Permission.USER_UPDATE == "user.update"
    assert Permission.USER_DELETE == "user.delete"


def test_role_permissions():

    assert Permission.ROLE_CREATE == "role.create"
    assert Permission.ROLE_VIEW == "role.view"
    assert Permission.ROLE_UPDATE == "role.update"
    assert Permission.ROLE_DELETE == "role.delete"


def test_permission_permissions():

    assert Permission.PERMISSION_CREATE == "permission.create"
    assert Permission.PERMISSION_VIEW == "permission.view"
    assert Permission.PERMISSION_UPDATE == "permission.update"
    assert Permission.PERMISSION_DELETE == "permission.delete"


def test_system_permission():

    assert Permission.SYSTEM_ADMIN == "system.admin"
