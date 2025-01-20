from lib.homes import Home

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



class Homes:
    def __init__(self, id, title, description, location, price_per_night, user_id):
        self.id = id 
        self.title = title
        self.description = description
        self.location = location
        self.price_per_night = price_per_night
        self.user_id = user_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User{self.id}, {self.title}, {self.description}, {self.location}, {self.price_per_night}, {self.user_id})"
    


