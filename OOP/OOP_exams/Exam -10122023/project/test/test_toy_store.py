from project.toy_store import ToyStore
from unittest import TestCase

class TestToyStore(TestCase):

    def test_init_expect_shelf_set(self):
        ts = ToyStore()
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, ts.toy_shelf)


    def test_add_toy_when_values_are_valid_expect_shelf_filled(self):
        ts = ToyStore()
        result = ts.add_toy('D', 'Doll')
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": 'Doll',
            "E": None,
            "F": None,
            "G": None,
        }, ts.toy_shelf)
        self.assertEqual(f"Toy:Doll placed successfully!", result)



    def test_add_toy_when_shelf_not_in_keys_expect_exception(self):
        ts = ToyStore()
        with self.assertRaises(Exception) as ex:
            ts.add_toy('Z', 'Doll')
        self.assertEqual("Shelf doesn't exist!",str(ex.exception))

    def test_add_toy_when_doll_already_on_shelf_expect_exception(self):
        ts = ToyStore()
        ts.add_toy('D', 'Doll')
        with self.assertRaises(Exception) as ex:
            ts.add_toy('D', 'Doll')
        self.assertEqual("Toy is already in shelf!",str(ex.exception))


    def test_add_toy_when_shelf_not_empty_expect_exception(self):
        ts = ToyStore()
        ts.toy_shelf['D'] = 'Doll'
        with self.assertRaises(Exception) as ex:
            ts.add_toy('D', 'Bell')
        self.assertEqual("Shelf is already taken!",str(ex.exception))



    def test_remove_toy_when_data_is_valid_expect_shelf_none_and_message(self):
        ts = ToyStore()
        toy_name= 'Doll'
        ts.add_toy('D', toy_name)
        self.assertEqual(f"Remove toy:{toy_name} successfully!", ts.remove_toy('D', 'Doll'))
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, ts.toy_shelf)

    def test_remove_toy_when_shelf_not_in_keys_expect_exception(self):
        ts = ToyStore()
        with self.assertRaises(Exception) as ex:
            ts.remove_toy('Z', 'Doll')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_when_shelf_toy_not_on_shelf_expect_exception(self):
        ts = ToyStore()
        ts.add_toy('D', 'Doll')
        with self.assertRaises(Exception) as ex:
            ts.remove_toy('D', 'Puppy')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_when_shelf_empty_expect_exception(self):
        ts = ToyStore()
        with self.assertRaises(Exception) as ex:
            ts.remove_toy('D', 'Puppy')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


