class Users:
    def __init__(self, id, home_id, date_available):
        self.id = id 
        self.home_id = home_id
        self.date_available = date_available
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User{self.id}, {self.home_id}, {self.date_available})"
