from lib.users import User
from lib.users_repository import UserRepository
import hashlib
from unittest.mock import patch, Mock

def test_all_users():
    connection = Mock()
    connection.execute.return_value = [
        {"id": 1, "username": "test_username", "email": "test_email", "password": "test_password"},
        {"id": 2, "username": "test_username", "email": "test_email", "password": "test_password"},
    ]
    repository = UserRepository(connection)
    users = repository.all_users()
    assert users == [
        User(1, "test_username", "test_email", "test_password"),
        User(2, "test_username", "test_email", "test_password"),
    ]