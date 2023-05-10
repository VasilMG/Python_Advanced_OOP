from unittest import TestCase
import unittest
from project.mammal import Mammal


class TestMammal(TestCase):
    def test_mammal_init_should_return_proper_object(self):
        name = "Susu"
        the_type = 'Lion'
        sound = "Raaahh"
        mammal = Mammal(name, the_type, sound)
        self.assertEqual(name, mammal.name)
        self.assertEqual(the_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual('animals',mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_result(self):
        name = "Susu"
        the_type = 'Lion'
        sound = "Raaahh"
        mammal = Mammal(name, the_type, sound)
        actual_result = mammal.make_sound()
        expected_result = f"{name} makes {sound}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kongdom_returns_proper_value(self):
        name = "Susu"
        the_type = 'Lion'
        sound = "Raaahh"
        mammal = Mammal(name, the_type, sound)
        actual_result = mammal.get_kingdom()
        expected_result = mammal._Mammal__kingdom
        self.assertEqual(expected_result, actual_result)

    def test_info_restuns_proper_string(self):
        name = "Susu"
        the_type = 'Lion'
        sound = "Raaahh"
        mammal = Mammal(name, the_type, sound)
        expected_result = f"{name} is of type {the_type}"
        actual_result = mammal.info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()