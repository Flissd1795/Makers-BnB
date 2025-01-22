from lib.requests import Request
from lib.requests_repository import RequestRepository

def test_get_all_requests(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    requests = repository.get_all_requests()
    assert requests == ["Request(1, Unseen, 2000-01-01, 1, 1, 2000-02-01, 2000-03-01), Request(2, Confirmed, 2000-01-01, 1, 1, 2000-02-01, 2000-03-01)"]
    # both examples added to database

def test_get_requests_by_user():



def get_requests_to_user_homes():








# def test_get_all_users(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     users = repository.all_users()
#     assert users == ["User(1, test_username, test@email.com, test_password)", "User(2, test_username2, test2@email.com, test_password2)"]

# def test_create_user(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     repository.create_user("test_username3", "test3@email.com", "test_password3")
#     users = repository.all_users()
#     assert users == ["User(1, test_username, test@email.com, test_password)", "User(2, test_username2, test2@email.com, test_password2)", "User(3, test_username3, test3@email.com, test_password3)"]

# def test_check_password(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     assert repository.check_password("test@email.com", "test_password") == True

# def test_check_incorrect_password(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     assert repository.check_password("test2@email.com", "wrong_password") == False

# def test_find_user(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     user = repository.find_user("test@email.com")
#     assert user == "User(1, test_username, test@email.com, test_password)"

# def test_find_user_invalid(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     user = repository.find_user("invalid@email.com")
#     assert user == None

# def test_get_username(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     username = repository.get_username(1)
#     assert username == "test_username"

# def test_get_username_invalid(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = UserRepository(db_connection)
#     username = repository.get_username(len(db_connection.execute("SELECT * FROM users;")) + 1)
#     assert username == None
