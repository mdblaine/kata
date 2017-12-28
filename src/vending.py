#!/usr/bin/python
from collections import namedtuple


class VendingMachine:
    """
    see https://github.com/guyroyse/vending-machine-kata
    """

    def __init__(self):
        self.display = "INSERT COIN"
        self.display_update_next_check = True
        self.amount_inserted = 0
        self.coins_inserted = {"quarter": 0, "dime": 0, "nickle": 0}
        self.coin_stock = {"quarter": 0, "dime": 0, "nickle": 0}
        self.product_price = {"cola": 1.00, "chips": 0.50, "candy": 0.65}
        self.product_stock = {"cola": 0, "chips": 0, "candy": 0}

        Coin = namedtuple("Coin", "name amount weight diameter thickness")
        # see https://www.usmint.gov/learn/coin-and-medal-programs/coin-specifications
        self.coin_specs = (Coin("quarter", 0.25, 5.670, 24.26, 1.75),
                           Coin("dime",    0.10, 2.268, 17.91, 1.35),
                           Coin("nickle",  0.05, 5.000, 21.21, 1.95))

    def accept_coins(self):
        # TODO identify coin by weight and size...then assign value for insert
        pass

    def select_product(self):
        # TODO self.display = "THANK YOU" and dispensed
        # TODO self.display = "SOLD OUT" if no stock; display_update_next_check=False
        # TODO self.display = "PRICE: ${0:.2f}" if amount not enough; display_update_next_check=False
        # TODO display = "EXACT CHANGE ONLY"  # not able to make change
        pass

    def make_change(self):
        pass

    def return_coins(self):
        pass

    def add_product_stock(self):
        pass

    def check_display(self):
        # TODO display = "INSERT COIN"  # able to make change
        # TODO display = "EXACT CHANGE ONLY"  # not able to make change
        # TODO display = "AMOUNT: ${0:.2f}"
        pass


def main():
    pass


if __name__ == '__main__':
    main()
