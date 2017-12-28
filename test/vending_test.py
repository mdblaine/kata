#!/usr/bin/python
import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.vending import VendingMachine  # noqa


class TestVending(unittest.TestCase):

    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_select_product_no_inventory(self):
        # without coins
        for product in ["cola", "chips", "candy"]:
            self.vending_machine.select_product(product)
            self.assertEqual(self.vending_machine.check_display(), "SOLD OUT")
        # with coins
        for quarters in range(1, 8):
            self.vending_machine.accept_coin({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
        for product in ["cola", "chips", "candy"]:
            self.vending_machine.select_product(product)
            self.assertEqual(self.vending_machine.check_display(), "SOLD OUT")

    def test_accept_coins(self):
        num_quarters = 7
        num_dimes = 7
        num_nickels = 7
        for quarters in range(1, num_quarters+1):
            self.vending_machine.accept_coin({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*quarters))
        for dimes in range(1, num_dimes+1):
            self.vending_machine.accept_coin({"weight": 2.268, "diameter": 17.91, "thickness": 1.35})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*num_quarters + 0.10*dimes))
        for nickles in range(1, num_nickels+1):
            self.vending_machine.accept_coin({"weight": 5.000, "diameter": 21.21, "thickness": 1.95})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*num_quarters + 0.10*num_dimes + 0.05*nickles))
        self.vending_machine.return_coins()
        self.assertEqual(self.vending_machine.check_display(), "INSERT COIN")

    def test_add_product_stock(self):
        self.vending_machine.add_product_stock({"cola": 6, "chips": 5, "candy": 4})
        self.assertEqual(self.vending_machine.product_stock, {"cola": 6, "chips": 5, "candy": 4})
        self.vending_machine.add_product_stock({"cola": 2, "chips": 3, "candy": 4})
        self.assertEqual(self.vending_machine.product_stock, {"cola": 8, "chips": 8, "candy": 8})

    def test_select_product_with_stock_no_coin(self):
        self.vending_machine.add_product_stock({"cola": 2, "chips": 3, "candy": 4})
        self.vending_machine.return_coins()
        for product in [("cola", 1.0), ("chips", 0.5), ("candy", 0.65)]:
            self.vending_machine.select_product(product[0])
            self.assertEqual(self.vending_machine.check_display(), "PRICE: ${0:.2f}".format(product[1]))

    def test_exact_change_only(self):
        self.vending_machine.accept_coin({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
        self.vending_machine.accept_coin({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
        self.vending_machine.accept_coin({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
        self.vending_machine.add_product_stock({"cola": 2, "chips": 3, "candy": 4})
        self.vending_machine.select_product("candy")
        self.assertEqual("EXACT CHANGE ONLY", self.vending_machine.check_display())

    def test_make_change(self):
        self.vending_machine.add_product_stock({"cola": 6, "chips": 5, "candy": 4})
        num_quarters = 5
        num_dimes = 1
        num_nickels = 1
        for quarters in range(1, num_quarters+1):
            self.vending_machine.accept_coin({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*quarters))
        for dimes in range(1, num_dimes+1):
            self.vending_machine.accept_coin({"weight": 2.268, "diameter": 17.91, "thickness": 1.35})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*num_quarters + 0.10*dimes))
        for nickles in range(1, num_nickels+1):
            self.vending_machine.accept_coin({"weight": 5.000, "diameter": 21.21, "thickness": 1.95})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*num_quarters + 0.10*num_dimes + 0.05*nickles))
        self.vending_machine.select_product("cola")
        self.assertEqual({"quarters": 1, "dimes": 1, "nickles": 1}, self.vending_machine.coins_to_return)


if __name__ == '__main__':
    unittest.main()
