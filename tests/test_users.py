from lib.users import User

"""
Constructs with an id, username, email and password
"""

def test_constructs():
    user = User(1, 'test_username', 'test_email', 'test_password')
    assert user.id == 1
    assert user.username == 'test_username'
    assert user.email == 'test_email'
    assert user.password == 'test_password'
    

"""
Artists with equal contents are equal
"""
def test_compares():
    user_1 = User(1, 'test_username', 'test_email', 'test_password')
    user_2 = User(1, 'test_username', 'test_email', 'test_password')
    assert user_1 == user_2

"""
Artists can be represented as strings
"""
def test_stringifying():
    user = User(1, 'test_username', 'test_email', 'test_password')
    assert str(user) == "User(1, test_username, test_email, test_password)"

def test_is_valid():
    user = User(1, 'test_username', 'test_email', 'test_password')
    assert user.is_valid() == True

def test_is_not_valid():
    user = User(1, '', 'test_email', 'test_password')
    assert user.is_valid() == False

def test_generate_errors():
    user = User(1, '', 'test_email', 'test_password')
    assert user.generate_errors() == ['Username is required']

    user = User(1, 'test_username', '', 'test_password')
    assert user.generate_errors() == ['Email is required']

    user = User(1, 'test_username', 'test_email', '')
    assert user.generate_errors() == ['Password is required']

    user = User(1, '', '', '')
    assert user.generate_errors() == ['Username is required', 'Email is required', 'Password is required']