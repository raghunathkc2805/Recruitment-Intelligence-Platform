from unittest.mock import MagicMock
from unittest.mock import patch

from api.database.rbac_seed_runner import main


@patch("api.database.rbac_seed_runner.seed_rbac")
@patch("api.database.rbac_seed_runner.SessionLocal")
def test_seed_runner(
    mock_session_local,
    mock_seed,
):

    db = MagicMock()

    mock_session_local.return_value = db

    main()

    mock_seed.assert_called_once_with(db)
    db.close.assert_called_once()


@patch("api.database.rbac_seed_runner.seed_rbac")
@patch("api.database.rbac_seed_runner.SessionLocal")
def test_seed_runner_failure(
    mock_session_local,
    mock_seed,
):

    db = MagicMock()

    mock_session_local.return_value = db

    mock_seed.side_effect = RuntimeError("Seeder Failed")

    try:
        main()
    except RuntimeError:
        pass

    db.close.assert_called_once()
