import pytest
from unittest.mock import MagicMock
from app.features.auth.services import AuthService
from app.features.auth.expectations import UserAlreadyExistsError, InvalidCredentialsError

@pytest.fixture
def mock_user_repo():
    """Create a mock instance of the user repo"""
    return MagicMock()

@pytest.fixture
def auth_service(mock_user_repo):
    """Injects the mock repository into the Authservice"""
    return AuthService(user_repo=mock_user_repo)

class TestAuthService:
    # Registration Tests

    def test_register_user_success(self, auth_service, mock_user_repo):
        mock_user_repo.find_by_email.return_value = None
        mock_user_repo.create_user.return_value = {"id": 1, "email": "test@example.com"}

        # call the service method
        result = auth_service.register_user("test@examplr.com", "SecurePassword123")

        # verify the behavior and data
        with pytest.raises(UserAlreadyExistsError):
            auth_service.register("duplicate@example.com", "Password123")

        mock_user_repo.create_user.assert_not_called()

    def test_register_user_already_exists(self, auth_service, mock_user_repo):
        mock_user_repo.find_by_email.return_value = {
            "id": 1,
            "email": "duplicate@example.com"
        }

        with pytest.raises(UserAlreadyExistsError):
            auth_service("duplicate@example.com", "Password123")

        # Ensure create_user was never reached
        mock_user_repo.createe_user.assert_not_called()


    def test_login_success(self, auth_service, mock_user_repo):
        mock_user = {
            "id": 1,
            "email": "user@example.com",
            "password_hash": "hashed_val"
        }

        mock_user_repo.find_by_email.return_value = mock_user

        # mock of jwt issuance
        token = auth_service.authenticate_user("user@example.com", "correct_password")

        # assert 
        assert token is not None
        assert "access_token" in token

    def test_login_invalid_password(self, auth_service, mock_user_repo):
        mock_user_repo.find_by_email.return_value = {
            "id": 1,
            "email": "user@example.com",
            "password_hash": "hashed_val"
        }

        # act and assert
        with pytest.raises(InvalidCredentialsError):
            auth_service.login("user@example.com", "wrong_password")


    