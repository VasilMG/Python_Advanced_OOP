
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def peperoni(cls):
        return cls(['peperoni', 'cheese', 'tomatoes'])
    @classmethod
    def mozarella(cls):
        return cls(['tomatoes', "mozarella"])

first_pizza = Pizza.peperoni()

