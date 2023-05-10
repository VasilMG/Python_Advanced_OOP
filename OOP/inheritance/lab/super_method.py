

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age}'

    def get_info(self):
        info = {
            'name': self.name,
            'age': self.age
        }
        return info
class Teacher(Person):
    def __init__(self,name, age, profession):
        super().__init__(name, age)             # super()
        self.profession = profession

    def __str__(self):
        return f'{super().__str__()} and he is a teacher!'   # super()

    def get_info(self):
        full_info = super().get_info()  # super()
        full_info['Profession'] = self.profession

        return full_info

t = Teacher('Gosho', 92, 'Teacher')
print(t.get_info())