from lib.users_repository import UserRepository


def test_get_all_users(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    users = repository.all_users()
    assert str(users) == "[User(1, test_username, test@email.com, test_password), User(2, test_username2, test2@email.com, test_password2)]"

def test_create_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    repository.create_user("test_username3", "test3@email.com", "test_password3")
    users = repository.all_users()
    assert str(users) == "[User(1, test_username, test@email.com, test_password), User(2, test_username2, test2@email.com, test_password2), User(3, test_username3, test3@email.com, 26ce23907653f55c5e7b537f93467180eda26864fcd58e1bc95ea2d356048ea1)]"

def test_check_password(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    repository.create_user("test_username3", "test3@email.com", "test_password3")
    assert repository.check_password("test3@email.com", "test_password3") == True

def test_check_incorrect_password(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    assert repository.check_password("test2@email.com", "wrong_password") == False

def test_find_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user("test@email.com")
    assert user == {'email': 'test@email.com', 'id': 1, 'password': 'test_password', 'username': 'test_username'}

def test_find_user_invalid(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user("invalid@email.com")
    assert user == None

def test_get_username(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    username = repository.get_username(1)
    assert username == {'username': 'test_username'}

def test_get_username_invalid(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    username = repository.get_username(len(db_connection.execute("SELECT * FROM users;")) + 1)
    assert username == None
