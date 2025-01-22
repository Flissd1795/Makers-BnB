from lib.homes import Home
import datetime

class HomesRepository:
    def __init__(self, connection):
        self.connection = connection

    def all_homes(self):
        homes = self.connection.execute("SELECT * FROM homes;")
        all_homes = []
        for home in homes:
            item = Home(home["id"], home["title"], home["description"], home["location"], home["price_per_night"], home["user_id"])
            all_homes.append(item)
        return all_homes
    
    def view_booked_dates(self, home_id):
        requests = self.connection.execute("SELECT * FROM requests WHERE home_id = %s;", [home_id])
        booked_dates = []
        for request in requests:
            iter_date = request["start_date"]
            while iter_date < request["end_date"]:
                booked_dates.append(iter_date)
                iter_date += datetime.timedelta(days=1)