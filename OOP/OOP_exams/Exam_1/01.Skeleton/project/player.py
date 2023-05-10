class Player:
    ADDED_PLAYERS = []
    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina


    @property
    def need_sustenance(self):
        return self.__stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")
        if value in self.ADDED_PLAYERS:
            raise ValueError(f"Name {value} is already used!")
        Player.ADDED_PLAYERS.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.__name}, {self.__age}, {self.__stamina}, {self.need_sustenance}"
