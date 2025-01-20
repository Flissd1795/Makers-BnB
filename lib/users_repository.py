from lib.users import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    '''
    List all users in the users database
    '''
    def all_user(self):
        rows = self._connection.execute("SELECT * FROM users;")
        return [
            User(row["id"], row["username"], row["email", row["password"]])
            for row in rows
        ]
    
    '''
    Add a new user to the users database
    '''
    def create_user(self, user):
        self._connection.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            [user.username, user.email, user.password]
        )

    '''
    Find a user on the database based on id (changeable)
    '''
    def find_user(self, user_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"], row["password"])





