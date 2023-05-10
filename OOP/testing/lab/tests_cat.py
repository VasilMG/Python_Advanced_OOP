from unittest import TestCase
import unittest
from cat import Cat


class CatTests(TestCase):

    def test_init_attributes(self):
        cat = Cat('Tom')
        self.assertEqual('Tom', cat.name)
        self.assertEqual(0, cat.size)
        self.assertEqual(False, cat.fed)
        self.assertEqual(False, cat.sleepy)

    def test_increased_attr_after_eating(self):
        cat = Cat('Tom')
        cat.eat()
        self.assertEqual(1, cat.size)
        self.assertEqual(True, cat.fed)
        self.assertEqual(True, cat.sleepy)

    def test_error_eat_after_eating(self):
        cat = Cat('Tom')
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cannot_sleep_if_not_fed(self):
        cat = Cat('Tom')
        cat.fed = False
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_when_fed(self):
        cat = Cat('Tom')
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)
