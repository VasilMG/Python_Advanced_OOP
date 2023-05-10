from abc import ABC, abstractmethod
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def __repr__(self):
        return self.name + ' ' + self.surname

    @abstractmethod
    def __add__(self, other):
        return Person(self.name, other.surname)

class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people
        self.current_index = 0

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = self.name + ' ' + other.name
        people = self.people + other.people
        return Group(name, people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([repr(x) for x in self.people])}"

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_index < len(self.people):
            value_to_return = f"Person {self.current_index}: {repr(self.people[self.current_index])}"
            self.current_index += 1
            return value_to_return
        raise StopIteration


    def __getitem__(self, item):
        return f"Person {item}: {repr(self.people[item])}"

p0 = Person('Aliko', 'Dangote')

p1 = Person('Bill', 'Gates')

p2 = Person('Warren', 'Buffet')

p3 = Person('Elon', 'Musk')

p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])

second_group = Group('Special', [p3, p4])

third_group = first_group + second_group

print(len(first_group))

print(second_group)

print(third_group[0])

for person in third_group:
    print(person)