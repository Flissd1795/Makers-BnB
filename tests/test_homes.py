from lib.homes import Home

"""
Constructs with an id, title, description, location, price_per_night, user_id
"""

def test_constructs():
    home = Home(1, 'test_title', 'test_description', 'test_location',100, 'test_user_id')
    assert home.id == 1
    assert home.title == 'test_title'
    assert home.description == 'test_description'
    assert home.location == 'test_location'
    assert home.price_per_night == 100
    assert home.user_id == 'test_user_id'

    
"""
with equal contents are equal
"""
def test_compares():
    home_1 = Home(1, 'test_title', 'test_description', 'test_location', 100, 'test_user_id')
    home_2 = Home(1, 'test_title', 'test_description', 'test_location', 100, 'test_user_id')
    assert home_1 == home_2

"""
can be represented as strings
"""
def test_stringifying():
    home = Home(1, 'test_title', 'test_description', 'test_location', 100, 'test_user_id')
    assert str(home) == "Home(1, test_title, test_description, test_location, 100, test_user_id)"

def test_is_valid():
    home = Home(1, 'test_title', 'test_description', 'test_location', 100, 'test_user_id')
    assert home.is_valid() == True

def test_generate_errors():
    home = Home(1, 'test_title', 'test_description', 'test_location', 100, 'test_user_id')
    assert home.generate_errors() == []

def test_is_invalid_title():
    home = Home(1, None, 'test_description', 'test_location', 100, 'test_user_id')
    assert home.is_valid() == False

def test_generate_errors_title():
    home = Home(1, None, 'test_description', 'test_location', 100, 'test_user_id')
    assert home.generate_errors() == ['Title is required']

def test_is_invalid_description():
    home = Home(1, 'test_title', None, 'test_location', 100, 'test_user_id')
    assert home.is_valid() == False

def test_generate_errors_description():
    home = Home(1, 'test_title', None, 'test_location', 100, 'test_user_id')
    assert home.generate_errors() == ['Description is required']

def test_is_invalid_location(): 
    home = Home(1, 'test_title', 'test_description', None, 100, 'test_user_id')
    assert home.is_valid() == False

def test_generate_errors_location():
    home = Home(1, 'test_title', 'test_description', None, 100, 'test_user_id')
    assert home.generate_errors() == ['Location is required']

def test_is_invalid_price_per_night_empty():
    home = Home(1, 'test_title', 'test_description', 'test_location', None, 'test_user_id')
    assert home.is_valid() == False

def test_generate_errors_price_per_night_empty():
    home = Home(1, 'test_title', 'test_description', 'test_location', None, 'test_user_id')
    assert home.generate_errors() == ['Price per night must be a number, got NoneType']

def test_is_invalid_price_per_night_not_digit():
    home = Home(1, 'test_title', 'test_description', 'test_location', 'not_digit', 'test_user_id')
    assert home.is_valid() == False

def test_generate_errors_price_per_night_not_digit():
    home = Home(1, 'test_title', 'test_description', 'test_location', 'not_digit', 'test_user_id')
    assert home.generate_errors() == ['Price per night must be a number, got str']

def test_is_invalid_price_per_night_negative():
    home = Home(1, 'test_title', 'test_description', 'test_location', -1, 'test_user_id')
    assert home.is_valid() == False

def test_generate_errors_price_per_night_negative():
    home = Home(1, 'test_title', 'test_description', 'test_location', -1, 'test_user_id')
    assert home.generate_errors() == ['Price per night must be a positive number']


