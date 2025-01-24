from lib.homes_repository import HomesRepository
from lib.homes import Home

def test_show_all_homes(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.all_homes()
    assert str(homes) == '[Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1), Home(2, The cave, Damp and smelly, Wales, 100.0, 2), Home(3, Garys garage, Room for more than a car, Front of Garys house, 1000.0, 2), Home(4, Steves shed, Better than Garys garage, Back of Steves house, 100.0, 2), Home(5, Barrys basement, Dark and dingy, At the bottom, 50.0, 2), Home(6, Carls climbingframe, Lots of fun to be had, Outside somewhere, 100.0, 2), Home(7, Andys attic, Large and lofty, At the top, 100.0, 2), Home(8, Grahams garden, Lots of room for activities, The back of Grahams house, 10.0, 2), Home(9, Tonys toilet, Fragrant, The bog, 3000.0, 2), Home(10, Freddies fruitbowl, Small and cosy, Kitchen counter, 200.0, 2), Home(11, Penelopes plane, Cosy stay in the cockpit, In the air, 30.0, 2), Home(12, Alanas allotment, Lovely fruit and veg, In a field, 100.0, 2), Home(13, Love island villa, Great spot for a fireside chat, Spain, 100.0, 2), Home(14, Ilonas igloo, Bit chilly, North Pole, 70.0, 2), Home(15, Torys treehouse, Dont visit if scared of heights, In a tree, 500.0, 2)]'

def test_create_home(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    repository.create_home("test_title3", "test_description3", "test_location3", 100.0, 1)
    homes = repository.all_homes()
    assert str(homes) == '[Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1), Home(2, The cave, Damp and smelly, Wales, 100.0, 2), Home(3, Garys garage, Room for more than a car, Front of Garys house, 1000.0, 2), Home(4, Steves shed, Better than Garys garage, Back of Steves house, 100.0, 2), Home(5, Barrys basement, Dark and dingy, At the bottom, 50.0, 2), Home(6, Carls climbingframe, Lots of fun to be had, Outside somewhere, 100.0, 2), Home(7, Andys attic, Large and lofty, At the top, 100.0, 2), Home(8, Grahams garden, Lots of room for activities, The back of Grahams house, 10.0, 2), Home(9, Tonys toilet, Fragrant, The bog, 3000.0, 2), Home(10, Freddies fruitbowl, Small and cosy, Kitchen counter, 200.0, 2), Home(11, Penelopes plane, Cosy stay in the cockpit, In the air, 30.0, 2), Home(12, Alanas allotment, Lovely fruit and veg, In a field, 100.0, 2), Home(13, Love island villa, Great spot for a fireside chat, Spain, 100.0, 2), Home(14, Ilonas igloo, Bit chilly, North Pole, 70.0, 2), Home(15, Torys treehouse, Dont visit if scared of heights, In a tree, 500.0, 2), Home(16, test_title3, test_description3, test_location3, 100.0, 1)]'



def test_find_home_by_id(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.find(1)
    assert str(homes) == 'Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1)'


    