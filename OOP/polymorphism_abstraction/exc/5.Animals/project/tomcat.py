from project.cat import Cat
from project.dog import Dog


class Tomcat(Cat):
    def __init__(self, name, age): # znachi tuk moje da se mahne do default stoynost se podava otdolu
        super().__init__(name, age, gender='Male')


    def make_sound(self):
        return "Hiss"


dog = Dog("Rocky", 3, "Male")

print(dog.make_sound())

print(dog)

tomcat = Tomcat("Tom", 6)

print(tomcat.make_sound())

print(tomcat)