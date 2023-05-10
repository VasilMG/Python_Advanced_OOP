from unittest import TestCase
import unittest
from unittest.mock import patch, Mock, MagicMock

from mocking import Person
from testing.lab.mocking.name_validators import ValidationException, validate_name


class TestPerson(TestCase):
    FIRST_NAME = 'Pesho'
    LAST_NAME = "Peshev"
    AGE = 92

   
    def setUp(self):
        pass
        
    @patch('testing.lab.mocking.name_validators.validate_name')
    def test_fullname__to_be_correct(self, _):
        self.person = Person(self.FIRST_NAME, self.LAST_NAME, self.AGE)
        actual_fullname = self.person.get_full_name
        expected_fullname = f'{self.FIRST_NAME} {self.LAST_NAME}'
        self.assertEqual(expected_fullname, actual_fullname)

    @patch('testing.lab.mocking.name_validators.validate_name')
    def test_get_info(self, _):
        self.person = Person(self.FIRST_NAME, self.LAST_NAME, self.AGE)
        expected_result = f'{self.FIRST_NAME} {self.LAST_NAME} is {self.AGE} years old.'
        actual_result = self.person.get_info()
        self.assertEqual(expected_result, actual_result)

    @patch('testing.lab.mocking.name_validators.validate_name')
    def test_init_when_first_is_not_valid_expect_to_raise(self, mock_validate_name):
        mock_validate_name.side_effect = Mock(side_effect=ValidationException('First name'))
        with self.assertRaises(ValidationException) as exc:
            Person('a', 'Peshev', 93)

        self.assertIsNotNone(exc.exception)

    @patch('testing.lab.mocking.name_validators.validate_name')
    def test_init_when_last_is_not_valid_expect_to_raise(self, mock_validate_name):
        mock_validate_name.side_effect = Mock(side_effect=ValidationException('Last name'))
        with self.assertRaises(ValidationException) as exc:
            Person('a', 'Peshev', 93)

        self.assertIsNotNone(exc.exception)

    @patch('testing.lab.mocking.name_validators.validate_name')
    def test_init_when_names_is_valid_expect_to_be_correct(self, mock_validate_name):
        Person('Pesho', 'Peshev', 93)