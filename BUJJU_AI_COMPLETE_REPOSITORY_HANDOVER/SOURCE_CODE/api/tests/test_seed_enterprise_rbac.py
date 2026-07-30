from unittest.mock import MagicMock
from unittest.mock import patch

from api.database.seed_enterprise_rbac import (
    seed_enterprise_rbac,
)


@patch("api.database.seed_enterprise_rbac.seed_role_permissions")
@patch("api.database.seed_enterprise_rbac.seed_rbac")
def test_seed_enterprise_rbac(
    mock_seed_rbac,
    mock_seed_role_permissions,
):

    db = MagicMock()

    seed_enterprise_rbac(db)

    mock_seed_rbac.assert_called_once_with(db)
    mock_seed_role_permissions.assert_called_once_with(db)

    db.commit.assert_called_once()


@patch("api.database.seed_enterprise_rbac.seed_role_permissions")
@patch("api.database.seed_enterprise_rbac.seed_rbac")
def test_seed_enterprise_rbac_seed_failure(
    mock_seed_rbac,
    mock_seed_role_permissions,
):

    db = MagicMock()

    mock_seed_rbac.side_effect = RuntimeError("Seed Failure")

    try:
        seed_enterprise_rbac(db)
    except RuntimeError:
        pass

    mock_seed_role_permissions.assert_not_called()
    db.commit.assert_not_called()
