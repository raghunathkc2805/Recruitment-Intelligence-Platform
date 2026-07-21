from unittest.mock import MagicMock, patch

from api.database.seed_role_permissions import (
    seed_role_permissions,
)


@patch("api.database.seed_role_permissions.RBACService")
def test_seed_role_permissions(mock_service):

    db = MagicMock()

    service = MagicMock()

    mock_service.return_value = service

    seed_role_permissions(db)

    assert service.assign_permissions.call_count > 0

    db.commit.assert_called_once()


@patch("api.database.seed_role_permissions.RBACService")
def test_seed_role_permissions_with_empty_defaults(
    mock_service,
):

    db = MagicMock()

    service = MagicMock()

    mock_service.return_value = service

    with patch(
        "api.database.seed_role_permissions.DEFAULT_ROLE_PERMISSIONS",
        {},
    ):
        seed_role_permissions(db)

    service.assign_permissions.assert_not_called()

    db.commit.assert_called_once()
