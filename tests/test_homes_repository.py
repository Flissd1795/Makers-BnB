from lib.homes_repository import HomesRepository
from lib.homes import Home

def test_show_all_homes(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.all_homes()
    assert str(homes) == "[Home(1, test_title, test_description, test_location, 100, 1), Home(2, test_title2, test_description2, test_location2, 100, 2)]"

def test_create_home(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    repository.create_home("test_title3", "test_description3", "test_location3", 100, 1)
    homes = repository.all_homes()

    expected_homes = [
        Home(1, "test_title", "test_description", "test_location", 100, 1),
        Home(2, "test_title2", "test_description2", "test_location2", 100, 2),
        Home(3, "test_title3", "test_description3", "test_location3", 100, 1),
    ]
    assert homes == expected_homes

def test_find_home_by_id(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.find(1)
    assert str(homes) == "Home(1, test_title, test_description, test_location, 100, 1)"


    