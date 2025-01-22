# from lib.requests import Request
# from lib.requests_repository import RequestRepository

# def test_get_all_requests(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = RequestRepository(db_connection)
#     requests = repository.get_all_requests()
#     assert requests == ["Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)", "Request(2, confirmed, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)"]
#     # updated from database

# def test_create_request(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = RequestRepository(db_connection)
#     repository.create_request("Unseen3", 2000-01-01, 3, 3, 2000-02-01, 2000-03-01)
#     requests = repository.get_all_requests()
#     assert requests == ["Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)", 
#                         "Request(2, confirmed, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)", 
#                         "Request(3, unseen3, 2000-01-01, 3, 3, 2000-02-01, 2000-03-01)"]
    



# def test_find_request(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = RequestRepository(db_connection)
#     request = repository.find_request(1)
#     assert request == "Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)"
#     # check this is the same as JOINS on db

# def test_update_request_dates(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = RequestRepository(db_connection)
#     request = repository.update_request_dates(2000-02-01, 2000-02-15, 1)
#     assert request == "Request(1, Unseen, 2000-01-01, 1, 1, 2000-02-01, 2000-02-15)"
    
# def test_delete_request(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql")
#     repository = RequestRepository(db_connection)
#     repository.delete_request(3)
#     request = repository.get_all_requests()
#     assert request == 




