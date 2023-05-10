from wild_zoo.project import Customer
from wild_zoo.project import DVD
class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []
    @staticmethod
    def dvd_capacity():
        return 15
    @staticmethod
    def customer_capacity():
        return  10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = ''
        current_dvd = ''
        for item in self.customers:
            if item.id == customer_id:
                current_customer = item
                break
        for d in self.dvds:
            if dvd_id == d.id:
                current_dvd = d
                break
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd.is_rented and current_dvd not in current_customer.rented_dvds:
            return "DVD is already rented"
        if current_dvd.age_restriction > current_customer.age:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = ''
        current_dvd = ''
        for item in self.customers:
            if item.id == customer_id:
                current_customer = item
                break
        for d in self.dvds:
            if dvd_id == d.id:
                current_dvd = d
                break
        if current_dvd in current_customer.rented_dvds:
            current_dvd.is_rented = False
            current_customer.rented_dvds.remove(current_dvd)
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        else:
            return f"{current_customer.name} does not have that DVD"

    def __repr__(self):

        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(y) for y in self.dvds])