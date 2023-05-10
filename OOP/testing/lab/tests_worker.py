class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest
from unittest import TestCase

class TestWorker(TestCase):
    NAME = "Test Worker"
    SALARY = 1024
    ENERGY = 1
    def setUp(self):
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init_if_valid(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0 , self.worker.money)

    def test_rest_incremented_energy(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_work_when_energy_zero(self):
        worker = Worker(self.NAME, self.SALARY, 0) 
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertIsNotNone(ex)

    def test_energy_below_zero(self):
        worker = Worker(self.NAME, self.SALARY, -10)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception)) 

    def test_work_salary_increase(self): 
        self.worker.work()
        self.assertEqual(self.SALARY, self.worker.money)

    def test_work_energy_decreased(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_values_get_info(self):
        actual_info = self.worker.get_info()
        expected_info =  f'{self.NAME} has saved 0 money.' 
        self.assertEqual(expected_info, actual_info)

if __name__ == '__main__':
    unittest.main()