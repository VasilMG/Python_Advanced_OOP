from project.shopping_cart import ShoppingCart
from unittest import TestCase

class TestShoppingCart(TestCase):

    def test_init_when_data_is_valid(self):
        sc = ShoppingCart('Market', 505.5)
        self.assertEqual('Market', sc.shop_name)
        self.assertEqual(505.5, sc.budget)
        self.assertEqual({}, sc.products)

    def test_init_when_shop_name_not_capital_letter(self):
        with self.assertRaises(Exception) as ex:
            sc = ShoppingCart('market', 505.5)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_init_when_shop_name_not_isalpha(self):
        with self.assertRaises(Exception) as ex:
            sc = ShoppingCart('M1arket', 505.5)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart_when_data_is_valid(self):
        sc = ShoppingCart('Market', 505.5)
        sc.add_to_cart('Bread', 99)
        self.assertEqual(f"Bread product was successfully added to the cart!",sc.add_to_cart('Bread', 99))
        self.assertEqual({'Bread': 99}, sc.products)

    def test_add_cart_when_price_over_100(self):
        sc = ShoppingCart('Market', 505.5)
        with self.assertRaises(Exception) as ex:
            sc.add_to_cart('Bread', 100)
        self.assertEqual(f"Product Bread cost too much!", str(ex.exception))


    def test_remove_when_data_is_valid(self):
        sc = ShoppingCart('Market', 505.5)
        sc.add_to_cart('Bread', 50)
        sc.add_to_cart('Cheese', 50)
        self.assertEqual(f"Product Cheese was successfully removed from the cart!", sc.remove_from_cart('Cheese'))
        self.assertEqual({'Bread': 50}, sc.products)

    def test_remove_when_products_empty(self):
        sc = ShoppingCart('Market', 505.5)
        with self.assertRaises(ValueError) as ex:
            sc.remove_from_cart('Cheese')
        self.assertEqual(f"No product with name Cheese in the cart!", str(ex.exception))

    def test_remove_when_product_not_in_cart(self):
        sc = ShoppingCart('Market', 505.5)
        sc.add_to_cart('Bread', 50)
        sc.add_to_cart('Cheese', 50)
        with self.assertRaises(ValueError) as ex: # ValueError - NOT Exception!!! BE careful!!!
            sc.remove_from_cart('Honey')
        self.assertEqual(f"No product with name Honey in the cart!", str(ex.exception))

    def test_add_method(self):
        sc1 = ShoppingCart('Shopping', 100)
        sc1.add_to_cart('Bread', 50)
        sc2 = ShoppingCart('Market', 100)
        sc2.add_to_cart('Cheese', 50)
        new_sc = sc1.__add__(sc2)
        self.assertEqual("ShoppingMarket", new_sc.shop_name)
        self.assertEqual({'Bread': 50, 'Cheese': 50}, new_sc.products)
        self.assertEqual(200, new_sc.budget)

    # def test_add_method(self):
    #     first = ShoppingCart('Test', 200)
    #     first.add_to_cart('from_first', 1)
    #     second = ShoppingCart('SecondTest', 100)
    #     second.add_to_cart('from_second', 2)
    #     merged = first.__add__(second)
    #     self.assertEqual('TestSecondTest', merged.shop_name)
    #     self.assertEqual(300, merged.budget)
    #     self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_products_enough_budget(self):
        sc1 = ShoppingCart('Shopping', 100)
        sc1.add_to_cart('Bread', 50)
        sc1.add_to_cart('Cheese', 50)
        self.assertEqual(f'Products were successfully bought! Total cost: {100:.2f}lv.', sc1.buy_products())

    def test_buy_when_not_enough_budget(self):
        sc1 = ShoppingCart('Shopping', 100)
        sc1.add_to_cart('Bread', 51)
        sc1.add_to_cart('Cheese', 50)
        with self.assertRaises(Exception) as ex:
            sc1.buy_products()
        self.assertEqual(f"Not enough money to buy the products! Over budget with {1:.2f}lv!", str(ex.exception))

