from lib.homes import Home
import datetime
import calendar

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
    
    def create_home(self, title, description, location, price_per_night, user_id):
        self.connection.execute('INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s)', [title, description, location, price_per_night, user_id])
        return None
    
    def find(self, id):
        home = self.connection.execute("SELECT * FROM homes WHERE id = %s;", [id])
        return Home(home[0]["id"], home[0]["title"], home[0]["description"], home[0]["location"], home[0]["price_per_night"], home[0]["user_id"])

    def fetch_booked_dates(self, id):
        requests = self.connection.execute("SELECT * FROM requests WHERE home_id = %s AND status = 'confirmed';", [id])
        booked_dates = []
        for request in requests:
            iter_date = request["start_date"]
            while iter_date < request["end_date"]:
                booked_dates.append(iter_date.day)
                iter_date += datetime.timedelta(days=1)
        return booked_dates
      
          def find_all(self ,id):
        # home = self.connection.execute("SELECT * FROM homes WHERE id = %s;", [id])
        homes = self.connection.execute("SELECT * FROM homes WHERE user_id = %s;", [id])
        all_homes = []
        for home in homes:
            item = Home(home["id"], home["title"], home["description"], home["location"], home["price_per_night"], home["user_id"])
            all_homes.append(item)
        return all_homes
      

    def filter_by_location(self, location):
        query = """
        SELECT 
            id, 
            title, 
            description, 
            location, 
            price_per_night 
        FROM homes
        WHERE location = %s;
        """
        rows = self._connection.execute(query, (location,))
        formatted_location_filter = [
            f"Home({row['id']}, {row['title']}, {row['description']}, {row['location']}, {row['price_per_night']})"
        for row in rows
        ]
        return formatted_location_filter
    



    def filter_by_price(self, min_price, max_price):
        """
        Filters homes by a price range (min_price to max_price).

        Args:
            min_price (float): The minimum price per night.
            max_price (float): The maximum price per night.

        Returns:
            list: A list of formatted strings representing the homes within the price range.
        """
        query = """
        SELECT 
            id, 
            title, 
            description, 
            location, 
            price_per_night 
        FROM homes
        WHERE price_per_night BETWEEN %s AND %s;
        """
        # Execute the query with the price range as parameters
        rows = self._connection.execute(query, (min_price, max_price))

        # Format the result rows
        formatted_homes = [
            f"Home({row['id']}, {row['title']}, {row['description']}, {row['location']}, {row['price_per_night']})"
            for row in rows
        ]
        
        return formatted_homes
