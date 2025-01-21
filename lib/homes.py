class Home:
    def __init__(self, id, title, description, location, price_per_night, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.price_per_night = price_per_night
        self.user_id = user_id

    def __repr__(self):
        return f"Home({self.id}, {self.title}, {self.description}, {self.location}, {self.price_per_night}, {self.user_id})"

    def __eq__(self, other):
        if isinstance(other, Home):
            return self.__dict__ == other.__dict__
        return False

