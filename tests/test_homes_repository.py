from lib.homes_repository import HomesRepository

def test_show_all_homes(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.show_all_homes()
    assert homes == ["Home(1, test_title, test_location, test_description, 1, test_booked_dates", "Home(2, test_title2, test_location2, test_description2, 2, test_booked_dates2)"]

def test_create_home(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    repository.create_home("test_title3", "test_location3", "test_description3", 3, "test_booked_dates3")
    homes = repository.show_all_homes()
    assert homes == ["Home(1, test_title, test_location, test_description, 1, test_booked_dates", "Home(2, test_title2, test_location2, test_description2, 2, test_booked_dates2)", "Home(3, test_title3, test_location3, test_description3, 3, test_booked_dates3)"]

def test_find_home_by_id(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.find(1)
    assert homes == "Home(1, test_title, test_location, test_description, 1, test_booked_dates"