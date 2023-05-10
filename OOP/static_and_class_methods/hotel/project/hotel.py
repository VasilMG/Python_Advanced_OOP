from room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

   
    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")
    def add_room(self, room: Room):
        self.rooms.append(room)
    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)
    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()
    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if r.guests == 0])}\n"\
        f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.guests != 0])}"
