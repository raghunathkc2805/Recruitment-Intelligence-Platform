from unittest.mock import MagicMock, patch

from api.database.seed_all import main


@patch("api.database.seed_all.SessionLocal")
@patch("api.database.seed_all.seed_enterprise_rbac")
def test_seed_all_success(
    mock_seed,
    mock_session_local,
):

    session = MagicMock()
    mock_session_local.return_value = session

    main()

    mock_seed.assert_called_once_with(session)
    session.close.assert_called_once()


@patch("api.database.seed_all.SessionLocal")
@patch("api.database.seed_all.seed_enterprise_rbac")
def test_seed_all_exception(
    mock_seed,
    mock_session_local,
):

    session = MagicMock()

    mock_session_local.return_value = session

    mock_seed.side_effect = RuntimeError("Seed Failed")

    try:
        main()
    except RuntimeError:
        pass

    session.rollback.assert_called_once()
    session.close.assert_called_once()
