
class Concert:
    def __init__(self, genre, audience, ticket_price, expenses, place):
        self.place = place
        self.expenses = expenses
        self.ticket_price = ticket_price
        self.audience = audience
        self.genre = genre

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in ["Metal", "Rock", "Jazz"]:
            raise ValueError(f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        if value < 1:
            raise ValueError("At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value: float):
        if value < 1:
            raise ValueError("Ticket price must be at least 1.00$!")
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be a negative number!")
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def get_needed_skills(self):
        if self.genre == 'Rock':
            return ['play the drums with drumsticks', 'sing high pitch notes', 'play rock']
        elif self.genre == 'Metal':
            return ['play the drums with drumsticks', 'sing low pitch notes', 'play metal']
        elif self.genre == 'Jazz':
            return ['play the drums with drum brushes', 'sing high pitch notes', 'sing low pitch notes', 'play jazz']

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
