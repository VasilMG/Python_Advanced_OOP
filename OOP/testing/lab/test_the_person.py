from unittest import TestCase

from the_person import Person


class TestPerson(TestCase):

    def setUp(self):
        self.person = Person('Pesho', 'Peshev', 92)

    def test_fullname__to_be_correct(self):
        person = Person('Pesho', 'Peshev', 92)
        actual_fullname = person.get_full_name
        expected_fullname = "Pesho Peshev"
        self.assertEqual(expected_fullname, actual_fullname)

    def test_get_info(self):
        person = Person('Pesho', 'Peshev', 92)
        expected_result = "kgkvkhfyj"
        actual_result = person.get_info()
        self.assertEqual(expected_result, actual_result)


