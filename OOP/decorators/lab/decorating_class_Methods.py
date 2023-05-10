from decorators.lab.accepting_args import measure_time




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @measure_time
    def get_age_after_years(self, years):
        return self.age + years

p = Person('gosho', 92)

print(p.get_age_after_years(20)) 