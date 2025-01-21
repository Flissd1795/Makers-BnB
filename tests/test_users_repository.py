from lib.users_repository import UserRepository


def test_get_all_users(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    users = repository.all_users()
    assert users == ["User(1, test_username, test@email.com, test_password)", "User(2, test_username2, test2@email.com, test_password2)"]

def test_create_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    repository.create_user("test_username3", "test3@email.com", "test_password3")
    users = repository.all_users()
    assert users == ["User(1, test_username, test@email.com, test_password)", "User(2, test_username2, test2@email.com, test_password2)", "User(3, test_username3, test3@email.com, test_password3)"]

def test_check_password(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    assert repository.check_password("test@email.com", "test_password") == True

def test_check_incorrect_password(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    assert repository.check_password("test2@email.com", "wrong_password") == False

def test_find_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user("test@email.com")
    assert user == "User(1, test_username, test@email.com, test_password)"

def test_find_user_invalid(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user("invalid@email.com")
    assert user == None

def test_get_username(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    username = repository.get_username(1)
    assert username == "test_username"

def test_get_username_invalid(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    username = repository.get_username(len(db_connection.execute("SELECT * FROM users;")) + 1)
    assert username == None


# def test_all_users():
#     connection = Mock()
#     connection.execute.return_value = [
#         {"id": 1, "username": "test_username", "email": "test_email", "password": "test_password"},
#         {"id": 2, "username": "test_username", "email": "test_email", "password": "test_password"},
#     ]
#     repository = UserRepository(connection)
#     users = repository.all_users()
#     assert users == [
#         User(1, "test_username", "test_email", "test_password"),
#         User(2, "test_username", "test_email", "test_password"),
#     ]

# def test_create_user():
#     connection = Mock()
#     connection.execute.return_value = [
#     {"id": 1, "username": "test_username", "email": "test_email", "password": hashlib.sha256(b"test_password").hexdigest()}
# ]
#     repository = UserRepository(connection)
#     repository.create_user("test_username", "test_email", "test_password")
#     connection.execute.assert_called_with(
#         'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
#         ["test_username", "test_email", hashlib.sha256(b"test_password").hexdigest()]
#     )
#     users = repository.all_users()
#     assert users == [User(1, "test_username", "test_email", "10a6e6cc8311a3e2bcc09bf6c199adecd5dd59408c343e926b129c4914f3cb01")]

# def test_check_password():
#     connection = Mock()
#     # Mock the return value for a correct password check
#     connection.execute.side_effect = lambda query, params: [
#         {"id": 1, "username": "test_username", "email": "test_email", "password": hashlib.sha256(b"test_password").hexdigest()}
#     ] if params[1] == hashlib.sha256(b"test_password").hexdigest() else []
    
#     repository = UserRepository(connection)

#     # Test for correct password
#     assert repository.check_password("test_email", "test_password") == True

#     # Test for incorrect password
#     assert repository.check_password("test_email", "wrong_password") == False

# def test_find_user():
#     connection = Mock()
#     connection.execute.return_value = [
#         {"id": 1, "username": "test_username", "email": "test_email", "password": "test_password"}
#     ]
#     repository = UserRepository(connection)
#     user = repository.find_user("test_email")
#     assert user == {"id": 1, "username": "test_username", "email": "test_email", "password": "test_password"}
    
# def test_find_user_not_found():
#     connection = Mock()
#     connection.execute.return_value = []
#     repository = UserRepository(connection)
#     user = repository.find_user("test_email")
#     assert user == None

# def test_get_username():
#     connection = Mock()
#     connection.execute.return_value = [
#         {"username": "test_username"}
#     ]
#     repository = UserRepository(connection)
#     username = repository.get_username(1)
#     assert username == {"username": "test_username"}

# def test_get_username_not_found():
#     connection = Mock()
#     connection.execute.return_value = []
#     repository = UserRepository(connection)
#     username = repository.get_username(1)
#     assert username == None