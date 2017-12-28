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

    def test_select_product_initial_conditions(self):
        for product in [("cola", 1.0), ("chips", 0.5), ("candy", 0.65)]:
            self.assertEqual(self.vending_machine.select_product(product[0]),
                             "PRICE: ${0:.2f}".format(product[1]))

    def test_get_products_initial_consitions(self):
        for quarters in range(7):
            self.vending_machine.accept_coins({"weight": 5.670, "diameter": 24.26, "thickness": 1.75})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*quarters))
        for dimes in range(7):
            self.vending_machine.accept_coins({"weight": 2.268, "diameter": 17.91, "thickness": 1.35})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*quarters + 0.10*dimes))
        for nickles in range(7):
            self.vending_machine.accept_coins({"weight": 5.000, "diameter": 21.21, "thickness": 1.95})
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*quarters + 0.10*dimes + 0.05*nickles))
        for product in ["cola", "chips", "candy"]:
            self.vending_machine.select_product(product)
            self.assertEqual(self.vending_machine.check_display(), "SOLD OUT")
            self.assertEqual(self.vending_machine.check_display(), "AMOUNT: ${0:.2f}".format(
                0.25*quarters + 0.10*dimes + 0.05*nickles))
        self.vending_machine.return_coins()
        self.assertEqual(self.vending_machine.check_display(), "INSERT COIN")

    def test_add_product_stock(self):
        self.vending_machine.add_product_stock({"cola": 6, "chips": 5, "candy": 4})
        self.assertEqual(self.vending_machine.product_stock, {"cola": 6, "chips": 5, "candy": 4})
        self.vending_machine.add_product_stock({"cola": 2, "chips": 3, "candy": 4})
        self.assertEqual(self.vending_machine.product_stock, {"cola": 8, "chips": 8, "candy": 8})


if __name__ == '__main__':
    unittest.main()
