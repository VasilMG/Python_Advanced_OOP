import math

from project2.truck_driver import TruckDriver
from unittest import TestCase

class TestTruckDriver(TestCase):



    def setUp(self):
        self.driver = TruckDriver("Kostadin", 1.40)

    def test_init(self):
        self.assertEqual(self.driver.name, "Kostadin")
        self.assertEqual(self.driver.money_per_mile, 1.40)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)



    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")


    def test_driver_add_cargo_when_data_is_valid_expect_proper_message(self):
        driver = TruckDriver('Pesho', 1.5)
        location = 'Sofia'
        miles = 30
        output = f"Cargo for 30 to Sofia was added as an offer."
        result = driver.add_cargo_offer(location, miles)
        self.assertEqual(output, result)
        self.assertEqual(miles, driver.available_cargos[location])
        self.assertEqual({'Sofia': 30}, driver.available_cargos)



    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("California", 2000)
        self.driver.add_cargo_offer("Los Angeles", 20000)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.driver.name} is driving 20000 to Los Angeles.")
        self.assertEqual(self.driver.earned_money, 4000)
        self.assertEqual(self.driver.miles, 20000)

    def test_driver_add_cargo_when_try_to_add_existing_location_expect_exception(self):
        driver = TruckDriver('Pesho', 1.5)
        location = 'Sofia'
        miles = 30
        driver.add_cargo_offer(location, miles)
        with self.assertRaises(Exception) as e:
            driver.add_cargo_offer(location, miles)
        self.assertEqual("Cargo offer is already added.", str(e.exception)) 

    def test_driver_best_cargo_when_no_cargos_available_expect_value_error(self):
        driver = TruckDriver('Pesho', 1.5)
        result = driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_eat_when_miles_less_than_250_expect_earned_money_not_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 50
        driver.eat(249)
        self.assertEqual(50, driver.earned_money)

    def test_eat_when_miles_equal_to_250_and_500_expect_earned_money_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 50
        driver.eat(250)
        driver.eat(500)
        self.assertEqual(10, driver.earned_money)

    def test_sleep_when_miles_less_than_1000_expect_earned_money_not_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 50
        driver.eat(999)
        self.assertEqual(50, driver.earned_money)

    def test_sleep_when_miles_equal_to_1000_and_200_expect_earned_money_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 100
        driver.sleep(1000)
        driver.sleep(2000)
        self.assertEqual(10, driver.earned_money)

    def test_pump_gas_when_miles_equal_to_1500_and_3000_expect_earned_money_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 1500
        driver.pump_gas(1500)
        driver.pump_gas(3000)
        self.assertEqual(500, driver.earned_money)

    def test_pump_gas_when_miles_less_than_1500_expect_earned_money_not_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 1500
        driver.pump_gas(1499)
        self.assertEqual(1500, driver.earned_money)

    def test_repair_truck_when_miles_less_than_10000_expect_earned_money_not_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 1500
        driver.repair_truck(9999)
        self.assertEqual(1500, driver.earned_money)

    def test_repair_truck_when_miles_equalt_to_10000__and_20000_expect_earned_money_not_changed(self):
        driver = TruckDriver('Pesho', 1.5)
        driver.earned_money = 16000
        driver.repair_truck(10000)
        driver.repair_truck(20000)
        self.assertEqual(1000, driver.earned_money)

    def test_repr_when_called_expect_proper_message(self):
        driver = TruckDriver('Pesho', 1.5)
        self.assertEqual(f"{driver.name} has 0 miles behind his back.", repr(driver))







