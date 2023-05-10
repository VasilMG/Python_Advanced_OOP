from project.rooms.room import Room

class AloneOld(Room):
    MEMBERS_COUNT = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, members_count=self.MEMBERS_COUNT)
        self.budget = pension
        self.room_cost = 10



