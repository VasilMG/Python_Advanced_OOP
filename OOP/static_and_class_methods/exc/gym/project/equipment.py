class Equipment:
    ID = 1
    def __init__(self, name: str):
        self.name = name
        self.id = self.ID
        self.get_next_id1()

    @classmethod
    def get_next_id1(cls):
        cls.ID += 1
        return cls.ID

    @staticmethod
    def get_next_id():
        return Equipment.ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"