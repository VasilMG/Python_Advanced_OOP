import unittest
from wild_zoo.project import Owl, Hen
from wild_zoo.project import Mouse, Dog, Cat, Tiger
from wild_zoo.project import Vegetable, Fruit, Meat, Seed

class WildFarmTests(unittest.TestCase):
    def test_first_zero(self):
        owl = Owl("Pip", 10, 10)
        self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")
        meat = Meat(4)
        self.assertEqual(owl.make_sound(), "Hoot Hoot")
        owl.feed(meat)
        veg = Vegetable(1)
        owl.feed(veg)
        self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
        self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")

if __name__ == "__main__":
    unittest.main()


# hen = Hen("Harry", 10, 10)
#
# print(hen.food_eaten)
#
# veg = Vegetable(3)
#
# fruit = Fruit(5)
#
# meat = Meat(1)
#
# print(hen)
#
# print(hen.make_sound())
#
# hen.feed(veg)
#
# hen.feed(fruit)
#
# hen.feed(meat)
# #
# print(hen)