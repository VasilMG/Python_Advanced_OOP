from project.rooms.room import Room

class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for r in self.rooms:
            total += (r.expenses + r.room_cost)
        return f"Monthly consumption: {total:.2f}$"

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget >= total_cost:
                room.budget -= total_cost
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        result = []
        total_people = sum([x.members_count for x in self.rooms])
        result.append(f'Total population: {total_people}')
        for room in self.rooms:
            details_room = f'{room.family_name} with {room.members_count} ' \
                           f'members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$'
            result.append(details_room)
            if room.children:
                count = 0
                for child in room.children:
                    count += 1
                    details_child = f'--- Child {count} monthly cost: {child.get_monthly_expense():.2f}$'
                    result.append(details_child)
            if room.appliances:
                cost_appl = sum([x.get_monthly_expense() for x in room.appliances])
            else:
                cost_appl = 0
            result.append(f'--- Appliances monthly cost: {cost_appl:.2f}$')

        return '\n'.join(result)



