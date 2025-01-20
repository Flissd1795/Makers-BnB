from lib.available_dates import AvailableDate

"""
Constructs with an id, home_id, date_available
"""

def test_constructs():
    available_date = AvailableDate(1, '1', '2000-01-01')
    assert available_date.id == 1
    assert available_date.home_id == '1'
    assert available_date.date_available == '2000-01-01'
    
"""
Artists with equal contents are equal
"""
def test_compares():
    available_date_1 = AvailableDate(1, '1', '2000-01-01')
    available_date_2 = AvailableDate(1, '1', '2000-01-01')
    assert available_date_1 == available_date_2

"""
Artists can be represented as strings
"""
def test_stringifying():
    available_date = AvailableDate(1, '1', '2000-01-01')
    assert str(available_date) == "AvailableDate(1, 1, 2000-01-01)"

