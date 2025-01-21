from lib.homes import Home

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
    