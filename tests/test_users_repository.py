from lib.users import User
from lib.users_repository import UserRepository
import hashlib
from unittest.mock import patch

def test_all_users():
    connection = {
        "execute": lambda query, params: [
            {"id": 1, "username": "test_username", "email": "test_email", "password": "test_password"},
            {"id": 2, "username": "test_username_2", "email": "test_email_2", "password": "test_password_2"}
        ]
    }
    repository = UserRepository(connection)
    users = repository.all_user()
    assert users == [
        User(1, "test_username", "test_email", "test_password"),
        User(2, "test_username_2", "test_email_2", "test_password_2")
    ]