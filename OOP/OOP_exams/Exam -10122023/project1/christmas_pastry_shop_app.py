from project1.delicacies.stolen import Stolen
from project1.delicacies.gingerbread import Gingerbread
from project1.booths.private_booth import PrivateBooth
from project1.booths.open_booth import OpenBooth

# booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy_names = [x.name for x in self.delicacies]
        if type_delicacy not in self.VALID_DELICACIES.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        elif name in delicacy_names:
            raise Exception(f"{name} already exists!")

        new_delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."



    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        numbers = [x.booth_number for x in self.booths]
        if type_booth not in self.VALID_BOOTHS.keys():
            raise Exception(f"{type_booth} is not a valid booth!")
        elif booth_number in numbers:
            raise Exception(f"Booth number {booth_number} already exists!")

        new_booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        available_booths = [x for x in self.booths if x.is_reserved is False and x.capacity >= number_of_people]
        if not available_booths:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth = available_booths[0]
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."


    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = [x for x in self.booths if x.booth_number == booth_number]
        # booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        delicacy = [x for x in self.delicacies if x.name == delicacy_name]
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        elif not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        return booth[0].add_delicacy(delicacy[0])


    def leave_booth(self, booth_number: int):
        booth = [x for x in self.booths if x.booth_number == booth_number]
        boot_total_price = booth[0].price_for_reservation + sum([x.price for x in booth[0].delicacy_orders])
        self.income += boot_total_price
        booth[0].delicacy_orders = []
        booth[0].price_for_reservation = 0
        booth[0].is_reserved = False
        return f"Booth {booth_number}:\n" + f"Bill: {boot_total_price:.2f}lv."


    def get_income(self):
        return f"Income: {self.income:.2f}lv."





