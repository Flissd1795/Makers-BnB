class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email}, {self.password})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.__dict__ == other.__dict__
        return False

    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False    
        return True

    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("Username is required")
        if self.email == None or self.email == "":
            errors.append("Email is required")
        if self.password == None or self.password == "":
            errors.append("Password is required")
        return errors
    