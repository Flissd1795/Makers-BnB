from lib.requests import Request

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection
    
    '''
    List all requests in the requests database
    '''
    def list_all_requests(self):
        rows = self._connection.execute("SELECT * FROM requests;")
        return [
            str(Request(row["id"], row["status"], row["date_submitted"], row["home_id"], row["user_id"], row["start_date"], row["end_date"]))
            for row in rows
        ]
    
    '''
    Create a new booking request
    '''
    def create_request(self, status, date_submitted, home_id, user_id, start_date, end_date):
        status ='unseen'
        self._connection.execute('INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)',
        [status, date_submitted, home_id, user_id, start_date, end_date])
        return None
    
    def confirm_request(self, request_id):
        self._connection.execute("UPDATE requests SET status = 'confirmed' WHERE id = %s", [request_id])
        return None
    
    def deny_request(self, request_id):
        self._connection.execute("UPDATE requests SET status = 'denied' WHERE id = %s", [request_id])
        return None

    '''
    Find a single booking request by its id
    '''
    def find_request(self, id):
        query = "SELECT * FROM requests WHERE id = %s"
        result = self._connection.execute(query, [id])
        # Check if the result list is not empty
        if result:
        # Use the first row (result[0])
            row = result[0]
            return f"Request({row['id']}, {row['status']}, {row['date_submitted']}, {row['home_id']}, {row['user_id']}, {row['start_date']}, {row['end_date']})"
        # Return None or handle case where no row matches the ID
        return None

    '''
    Update a request by its date
    '''
    def update_request_dates(self, start_date, end_date, id):
        # had to make sure the SQL had returning id, status etc. or it was returning None
        query = """
        UPDATE requests
        SET start_date = %s, end_date = %s
        WHERE id = %s
        RETURNING id, status, date_submitted, home_id, user_id, start_date, end_date
        """
        result = self._connection.execute(query, [start_date, end_date, id])
        if result:
        # Assuming result is a list, fetch the first row
            row = result[0]
            return f"Request({row['id']}, {row['status']}, {row['date_submitted']}, {row['home_id']}, {row['user_id']}, {row['start_date']}, {row['end_date']})"
        return None
    
    '''
    Delete a request by its id
    '''
    def delete_request(self, id):
        self._connection.execute('DELETE FROM requests WHERE id = %s', [id])
        return None
        # for declined request or if request sender changes their mind

    """
    List requests sent by a specific user.
    Executes the query to retrieve requests where the specified user is the requester (requests.user_id = %s).
    """
    # def list_requests_by_user_id(self, user_id):
    #     # SQL query to fetch user requests and associated home details
    #     query = """
    #     SELECT 
    #         requests.id AS request_id,
    #         requests.status,
    #         requests.date_submitted,
    #         requests.start_date,
    #         requests.end_date,
    #         homes.title AS home_title,
    #         homes.location AS home_location,
    #         homes.price_per_night
    #     FROM requests
    #     JOIN homes ON requests.home_id = homes.id
    #     WHERE requests.user_id = %s;
    #     """
    #     # Directly execute the query using self._connection
    #     # Use fetchall() or similar methods depending on the DB driver
    #     rows = self._connection.execute(query, (user_id,))
    #     formatted_requests = [
    #         f"Request({row['request_id']}, {row['status']}, {row['date_submitted']}, {row['start_date']}, {row['end_date']}, {row['home_title']}, {row['home_location']}, {row['price_per_night']})"
    #     for row in rows
    #     ]
    #     # Return the results
    #     return formatted_requests
#    
#    def list_requests_by_user_id(self, user_id):
#        query = """
#        SELECT 
#            requests.id AS request_id,
#            requests.status,
#            requests.date_submitted,
#            requests.start_date,
#            requests.end_date,
#            homes.title AS home_title
#        FROM requests
#        JOIN homes ON requests.home_id = homes.id
#        WHERE requests.user_id = %s;
#        """
#        rows = self._connection.execute(query, [user_id])
#        return [
#            {
#                "id": row["request_id"],
#                "status": row["status"],
#                "date_submitted": row["date_submitted"],
#                "start_date": row["start_date"],
#                "end_date": row["end_date"],
#                "home_title": row["home_title"]
#            }
#        for row in rows
#        ]
#
#    '''
#    List requests received to a specific home
#    Get all requests made to a users home
#    '''
#    # same functionality as the above method but using home id
#    def list_requests_by_home_id(self, home_id):
#        query = """
#        SELECT 
#            requests.id AS request_id,
#            requests.status,
#            requests.start_date,
#            requests.end_date,
#            homes.title AS home_title
#        FROM requests
#        JOIN homes ON requests.home_id = homes.id
#        WHERE requests.user_id = %s;
#        """
#        rows = self._connection.execute(query, (home_id,))
#        return [
#            {
#                "id": row["request_id"],
#                "status": row["status"],
#                "date_submitted": row["date_submitted"],
#                "start_date": row["start_date"],
#                "end_date": row["end_date"],
#                "username": row["requester_username"],
#                "email": row["requester_email"]
#            }
#        for row in rows
#        ]
#
#    '''
    def list_requests_by_user_id(self, user_id):
        query = """
        SELECT 
            requests.id AS request_id,
            requests.status,
            requests.date_submitted,
            requests.start_date,
            requests.end_date,
            homes.title AS home_title
        FROM requests
        JOIN homes ON requests.home_id = homes.id
        WHERE requests.user_id = %s;
        """
        rows = self._connection.execute(query, [user_id])
        return rows

    def list_requests_by_home_owner(self, owner_id):
        query = """
        SELECT 
            requests.id AS request_id,
            requests.status,
            requests.date_submitted,
            requests.start_date,
            requests.end_date,
            homes.title AS home_title
        FROM requests
        JOIN homes ON requests.home_id = homes.id
        WHERE homes.user_id = %s;
        """
        rows = self._connection.execute(query, [owner_id])
        return rows
    
    def get_request_details(self, request_id):
        query = """
        SELECT 
            requests.id AS request_id,
            requests.status,
            requests.date_submitted,
            requests.start_date,
            requests.end_date,
            homes.title AS home_title,
            homes.location AS home_location,
            users.username AS requester_username,
            users.email AS requester_email
        FROM requests
        JOIN homes ON requests.home_id = homes.id
        JOIN users ON requests.user_id = users.id
        WHERE requests.id = %s;
        """
        result = self._connection.execute(query, [request_id])

        if result:
            row = result[0]
            return {
                'id': row['request_id'],
                'status': row['status'],
                'date_submitted': row['date_submitted'],
                'start_date': row['start_date'],
                'end_date': row['end_date'],
                'home_title': row['home_title'],
                'home_location': row['home_location'],
                'requester_username': row['requester_username'],
                'requester_email': row['requester_email'],
            }
        return None
