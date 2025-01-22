# from lib.requests import Request
# # import hashlib

# class RequestRepository:
#     def __init__(self, connection):
#         self._connection = connection
    
#     '''
#     List all requests in the requests database
#     '''
#     def get_all_requests(self):
#         rows = self._connection.execute("SELECT * FROM requests;")
#         return [
#             Request(row["id"], row["status"], row["date_submitted"], row["home_id"], row["user_id"], row["start_date"], row["end_date"])
#             for row in rows
#         ]
    
#     '''
#     List requests sent by user
#     Executes the query to retrieve requests where the specified user is the requester (requests.user_id = %s)
#     '''
#     # user id specifies the id of the user whose sent requests we want to fetch
#     def get_requests_by_user(self, user_id):
#         # query pulls all requests of a user based on their linked user_id in requests db
#         # query also pulls info from homes tables in db to include info on homes they've requested (based on home_id in requests)
#         # requests and homes id renamed to request_id and homes_id for clarity (otherwise would show as just 'id')
#         query = """
#         SELECT 
#             requests.id AS request_id,
#             requests.status,
#             requests.date_submitted,
#             requests.start_date,
#             requests.end_date,
#             homes.title AS home_title,
#             homes.location AS home_location,
#             homes.price_per_night
#         FROM requests
#         JOIN homes ON requests.home_id = homes.id
#         WHERE requests.user_id = %s;
#         """
#         # cursors are db objects used to execute SQL queries and execute results
#         # self.connection.cursor ensures cursors closed automatically after execution
#         with self.connection.cursor() as cursor:
#             # executes query passing user_id as value for %s
#             cursor.execute(query, (user_id,))
#             # rows retrieves all the rows returned by the query
#             rows = cursor.fetchall()
#         # returns list of rows, each row represents a booking request with associated home
#         return rows


#     '''
#     List requests received to users home
#     Get all requests made to a users home
#     '''
#     # same functionality as the above method but using home id
#     def get_requests_by_home(self, home_id):
#         query = """
#         SELECT 
#             requests.id AS request_id,
#             requests.status,
#             requests.date_submitted,
#             requests.start_date,
#             requests.end_date,
#             users.username AS requester_username,
#             users.email AS requester_email
#         FROM requests
#         JOIN users ON requests.user_id = users.id
#         WHERE requests.home_id = %s;
#     """
#         with self.connection.cursor() as cursor:
#             cursor.execute(query, (home_id,))
#             rows = cursor.fetchall()
#         return rows

    
#     def create_request(self)

#     find_request

#     delete_request

#     update_request (to change dates e.g.)
    
    






    
#     '''
#     Add a new request in the requets database
#     '''
#     def create_request(self, status, date_submitted, home_id, user_id, start_date, end_date):
#         self._connection.execute(
#             'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
#             [username, email, hashed_password])
#         return None
#     # def verify_password(self, email, password):
#     def check_password(self, email, password_attempt):
#         # Hash the password attempt
#         binary_password_attempt = password_attempt.encode("utf-8")
#         hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

#         # Check whether there is a user in the database with the given email
#         # and a matching password hash, using a SELECT statement.
#         rows = self._connection.execute(
#             'SELECT * FROM users WHERE email = %s AND password = %s',
#             [email, hashed_password_attempt])

#         # If that SELECT finds any rows, the password is correct.
#         return len(rows) > 0






# CREATE TABLE requests ( 
#     id SERIAL PRIMARY KEY, 
#     status VARCHAR(255),
#     date_submitted DATE NOT NULL,
#     home_id INT NOT NULL, 
#     user_id INT NOT NULL,
#     start_date DATE NOT NULL,
#     end_date DATE NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
#     FOREIGN KEY (home_id) REFERENCES homes (id) ON DELETE CASCADE
#     -- UNIQUE (home_id, date_available) 
# );




















#     '''
#     Find a user on the database based on id (changeable)
#     '''

#     def find_request(self, email):
#         result = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
#         if result:
#             return result[0]
#         else:
#             return None

#         #Used in session creation 
#     def get_username(self, id):
#         result = self._connection.execute('SELECT username FROM users WHERE id = %s', [id])
#         if result:
#             return result[0]
#         else:
#             return None
        


