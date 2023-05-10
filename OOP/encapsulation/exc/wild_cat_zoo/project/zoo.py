from wild_zoo.project import Animal
from wild_zoo.project import Worker


class Zoo:
    def __init__(self, name, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price <= self.__budget and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if price > self.__budget and self.__animal_capacity > 0:
            return "Not enough budget"
        return "Not enough space for animal"


    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for item in self.workers:
            if worker_name == item.name:
                self.workers.remove(item)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for item in self.workers:
            salaries += item.salary

        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_animals = 0
        for item in self.animals:
            money_for_animals += item.money_for_care

        if money_for_animals <= self.__budget:
            self.__budget -= money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        all_animals = {}
        for item in self.animals:
            if item.__class__.__name__ not in all_animals:
                all_animals[item.__class__.__name__] = []
                all_animals[item.__class__.__name__].append(item)
            else:
                all_animals[item.__class__.__name__].append(item)
        return f"You have {len(self.animals)} animals" + '\n' + f"----- {len(all_animals['Lion'])} Lions:" + '\n' +\
            '\n'.join([x.__repr__() for x in all_animals['Lion']]) + '\n' + f"----- {len(all_animals['Tiger'])} Tigers:" +\
            '\n' + '\n'.join([x.__repr__() for x in all_animals['Tiger']]) + '\n' + \
            f"----- {len(all_animals['Cheetah'])} Cheetahs:" +'\n' + '\n'.join([x.__repr__() for x in all_animals['Cheetah']])


    def workers_status(self):
        all_workers = {}
        for item in self.workers:
                if item.__class__.__name__ not in all_workers:
                    all_workers[item.__class__.__name__] = []
                    all_workers[item.__class__.__name__].append(item)
                else:
                    all_workers[item.__class__.__name__].append(item)

        return f"You have {len(self.workers)} workers" + '\n' + f"----- {len(all_workers['Keeper'])} Keepers:" + '\n' + \
            '\n'.join(
                [x.__repr__() for x in all_workers['Keeper']]) + '\n' + f"----- {len(all_workers['Caretaker'])} Caretakers:" + \
            '\n' + '\n'.join([x.__repr__() for x in all_workers['Caretaker']]) + '\n' + \
            f"----- {len(all_workers['Vet'])} Vets:" +'\n'+ '\n'.join([x.__repr__() for x in all_workers['Vet']])

