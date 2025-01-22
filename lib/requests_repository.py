from lib.requests import Request
# import hashlib

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection
    
    '''
    List all requests in the requests database
    '''
    def get_all_requests(self):
        rows = self._connection.execute("SELECT * FROM requests;")
        return [
            Request(row["id"], row["status"], row["date_submitted"], row["home_id"], row["user_id"], row["start_date"], row["end_date"])
            for row in rows
        ]
    
    '''
    Create a new booking request
    '''
    def create_request(self):
        self._connection.execute('INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)',
        [self.status, self.date_submitted, self.home_id, self.user_id, self.start_date, self.end_date])
        return None

    '''
    Find a single booking request by its id
    '''
    def find_request(self, id):
        result = self._connection.execute('SELECT * FROM users WHERE email = %s', [self.id])
        if result:
            return result[0]
        else:
            return None

    '''
    Update a request by its date
    '''
    def update_request_dates(self, start_date, end_date):
        self._connection.execute('UPDATE requests SET start_date = %s, end_date = %s WHERE id = %s', [start_date, end_date, self.id])
        return None
    
    '''
    Delete a request by its id
    '''
    def delete_request(self, id):
        self._connection.execute('DELETE FROM requests WHERE id = %s', [id])
        return None
    # for declined request


    
    '''
    List requests sent by specific user
    Executes the query to retrieve requests where the specified user is the requester (requests.user_id = %s)
    '''
    # user id specifies the id of the user whose sent requests we want to fetch
    def get_requests_by_user(self, user_id):
        # query pulls all requests of a user based on their linked user_id in requests db
        # query also pulls info from homes tables in db to include info on homes they've requested (based on home_id in requests)
        # requests and homes id renamed to request_id and homes_id for clarity (otherwise would show as just 'id')
        query = """
        SELECT 
            requests.id AS request_id,
            requests.status,
            requests.date_submitted,
            requests.start_date,
            requests.end_date,
            homes.title AS home_title,
            homes.location AS home_location,
            homes.price_per_night
        FROM requests
        JOIN homes ON requests.home_id = homes.id
        WHERE requests.user_id = %s;
        """
        # cursors are db objects used to execute SQL queries and execute results
        # self.connection.cursor ensures cursors closed automatically after execution
        with self.connection.cursor() as cursor:
            # executes query passing user_id as value for %s
            cursor.execute(query, (user_id,))
            # rows retrieves all the rows returned by the query
            rows = cursor.fetchall()
        # returns list of rows, each row represents a booking request with associated home
        return rows


    '''
    List requests received to a specific home
    Get all requests made to a users home
    '''
    # same functionality as the above method but using home id
    def get_requests_by_home(self, home_id):
        query = """
        SELECT 
            requests.id AS request_id,
            requests.status,
            requests.date_submitted,
            requests.start_date,
            requests.end_date,
            users.username AS requester_username,
            users.email AS requester_email
        FROM requests
        JOIN users ON requests.user_id = users.id
        WHERE requests.home_id = %s;
    """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (home_id,))
            rows = cursor.fetchall()
        return rows

