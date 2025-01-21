from lib.requests import Request

"""
Constructs with an id, status, date_submitted, home_id, user_id, start_date, end_date
"""

def test_constructs():
    request = Request('1', 'Unseen', '2000-01-01', '1', '1', '2000-02-01', '2000-03-01')
    assert request.id == '1'
    assert request.status == 'Unseen'
    assert request.date_submitted == '2000-01-01'
    assert request.home_id == '1'
    assert request.user_id == '1'
    assert request.start_date == '2000-02-01'
    assert request.end_date == '2000-03-01'
    
"""
Requests with equal contents are equal
"""
def test_compares():
    request_1 = Request('1', 'Unseen', '2000-01-01', '1', '1', '2000-02-01', '2000-03-01')
    request_2 = Request('1', 'Unseen', '2000-01-01', '1', '1', '2000-02-01', '2000-03-01')
    assert request_1 == request_2

"""
Requests can be represented as strings
"""
def test_stringifying():
    available_date = Request('1', 'Unseen', '2000-01-01', '1', '1', '2000-02-01', '2000-03-01')
    assert str(available_date) == "Request(1, Unseen, 2000-01-01, 1, 1, 2000-02-01, 2000-03-01)"
