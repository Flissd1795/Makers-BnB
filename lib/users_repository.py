from lib.users import User
import hashlib

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    '''
    List all users in the users database
    '''
    def all_users(self):
        rows = self._connection.execute('SELECT * FROM users')
        return [
            User(row["id"], row["username"], row["email"], row["password"])
            for row in rows
        ]
    
    '''
    Add a new user to the users database
    '''
    def create_user(self, username, email, password):
        
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()
        self._connection.execute(
            'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
            [username, email, hashed_password])
        return None
    
    
    # def verify_password(self, email, password):
    def check_password(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])

        # If that SELECT finds any rows, the password is correct.
        print(hashed_password_attempt)
        print(len(rows))
        print(rows)
        return len(rows) > 0
        # return len(rows[0]) > 0

    '''
    Find a user on the database based on id (changeable)
    '''

    def find_user(self, email):
        result = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        if result:
            return result[0]
        else:
            return None

        #Used in session creation 
    def get_username(self, id):
        result = self._connection.execute('SELECT username FROM users WHERE id = %s', [id])
        if result:
            return result[0]
        else:
            return None
        


