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
            end_date = request["end_date"]
            while iter_date < end_date:
                booked_dates.append(iter_date)
                iter_date += datetime.timedelta(days=1)
        return booked_dates
        
    def find_all(self ,id):
        homes = self.connection.execute("SELECT * FROM homes WHERE user_id = %s;", [id])
        all_homes = []
        for home in homes:
            item = Home(home["id"], home["title"], home["description"], home["location"], home["price_per_night"], home["user_id"])
            all_homes.append(item)
        return all_homes
    
    def load_calendar_page(self, booked_dates, offset=-299):
        cal = calendar.TextCalendar()
        today = datetime.date.today()

        month_to_inspect = today.month + (offset % 12)
        year_to_inspect = today.year + (offset // 12)

        days_on_page = []
        for date in booked_dates:
            print(f'booked date: {date}')
        for day in cal.itermonthdays3(year=year_to_inspect, month=month_to_inspect):
            day_as_datetime = datetime.date(day[0], day[1], day[2])
            is_booked = False
            print(f'day as datetime: {day_as_datetime}')
            if day_as_datetime in booked_dates:
                is_booked = True
            days_on_page.append((day_as_datetime, is_booked))
        return days_on_page
