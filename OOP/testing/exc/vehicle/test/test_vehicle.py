from unittest import TestCase
import unittest

from project.vehicle import Vehicle

class TestVehicle(TestCase):
    FUEL = 100
    HORSE_POWER =120
    DEFAULT_FUEL_CONSUMPTION = 1.25
    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle_init_returns_proper(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_reaises_error_when_foel_is_less(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(exc.exception))
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_drive_reduces_fuel_when_fuel_is_enough(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        result = self.FUEL - fuel_needed
        self.assertEqual(result, self.vehicle.fuel)

    def test_drive_with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        result = self.FUEL - fuel_needed
        self.assertEqual(result, self.vehicle.fuel)

    def test_refuel_raises_error_more_than_capacity(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(self.vehicle.capacity +1)
        self.assertEqual("Too much fuel", str(exc.exception))

    def test_refuel_when_space_in_tank(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount
        self.vehicle.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_str_returns_proper_value(self):
        actual_result = str(self.vehicle)
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
