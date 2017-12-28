#!/usr/bin/python
from collections import namedtuple


class VendingMachine:
    """
    see https://github.com/guyroyse/vending-machine-kata
    """

    def __init__(self):
        self.display = "INSERT COIN"
        self.display_current = False
        self.amount_inserted = 0
        self.coins_inserted = {"quarters": 0, "dimes": 0, "nickles": 0}
        self.coin_stock = {"quarters": 0, "dimes": 0, "nickles": 0}
        self.product_price = {"cola": 100, "chips": 50, "candy": 65}
        self.product_stock = {"cola": 0, "chips": 0, "candy": 0}

        Coin = namedtuple("Coin", "name amount weight diameter thickness")
        # see https://www.usmint.gov/learn/coin-and-medal-programs/coin-specifications
        self.coin_specs = (Coin("quarters", 25, 5.670, 24.26, 1.75),
                           Coin("dimes",    10, 2.268, 17.91, 1.35),
                           Coin("nickles",   5, 5.000, 21.21, 1.95))

        self.coins_to_return = {"quarters": 0, "dimes": 0, "nickles": 0}  # only for testing make change

    def accept_coin(self, coin):
        """
        Add a coin to coins_inserted if in coin_specs
        :param coin: a dict of the form {"weight": 5.670, "diameter": 24.26, "thickness": 1.75}
        """
        # TODO validate coin dict
        for coin_spec in self.coin_specs:
            if coin_spec[2:] == (coin["weight"], coin["diameter"], coin["thickness"]):
                # TODO allow inserted coin to be close enough (e.g. within 3% ???)
                # a valid coin
                self.coins_inserted[coin_spec.name] += 1  # TODO not working???
                self.amount_inserted += coin_spec.amount
            else:
                # must not have been a valid coin...passed to coin return
                pass

    def select_product(self, product):
        """
        Respond to product select based on present state
        :param product: one of: "cola", "chips" or "candy"
        """
        # TODO validate product
        if self.product_stock[product] == 0:
            self.display = "SOLD OUT"
        elif self.amount_inserted < self.product_price[product]:
            self.display = "PRICE: ${0:.2f}".format(self.product_price[product]/100)
        else:
            have_change, coins_to_return = self.make_change(self.product_price[product])
            print("have_change: {}   //  coins_to_return: {}".format(have_change, coins_to_return))
            if have_change:
                self.product_stock[product] -= 1  # dispense product...
                self.coins_to_return = coins_to_return
                for coin in ["quarters", "dimes", "nickles"]:
                    self.coin_stock[coin] += self.coins_inserted[coin] - coins_to_return[coin]
                    # send coins_to_return[coin] to coin return...
                    self.display = "THANK YOU"
                    self.amount_inserted = 0
            elif not have_change:
                self.display = "EXACT CHANGE ONLY"
            else:
                print("SELECT PRODUCT ERROR")
                self.display = "ERROR"
        self.display_current = True

    def make_change(self, product_cost):
        remainder_to_return = self.amount_inserted - product_cost
        coins_to_return = {"quarters": 0, "dimes": 0, "nickles": 0}

        for coin, coin_amount in [("quarters", 25), ("dimes", 10), ("nickles", 5)]:
            number_of_coins = remainder_to_return // coin_amount
            if number_of_coins <= self.coin_stock[coin] + self.coins_inserted[coin]:
                # have enough of this coin; take number of coins needed; keep track of remainder
                coins_to_return[coin] = number_of_coins
                remainder_to_return %= coin_amount
            else:
                # don't have enough of this coin; take number of coins that there are; keep track of remainder
                coins_to_return[coin] = self.coin_stock[coin] + self.coins_inserted[coin]
                remainder_to_return -= coins_to_return[coin] * coin_amount

        return remainder_to_return == 0, coins_to_return

    def return_coins(self):
        """return coins customer has placed in the machine"""
        # dump all coins_inserted to coin return...
        self.coins_inserted = {"quarters": 0, "dimes": 0, "nickles": 0}
        self.amount_inserted = 0
        self.display = "INSERT COIN"
        self.display_current = False

    def add_product_stock(self, products):
        """Add products to product_stock"""
        # TODO validate products dict
        for product in products:
            self.product_stock[product] += products[product]
        self.display_current = False
        self.display = "INSERT COIN"

    def check_display(self):
        """return appropriate display_current state"""
        if self.display_current:
            self.display_current = False
            return self.display
        elif self.amount_inserted == 0:
            self.display = "INSERT COIN"
            return self.display
        elif self.amount_inserted > 0:
            self.display = "AMOUNT: ${0:.2f}".format(self.amount_inserted/100)
            return self.display
        else:
            print("CHECK DISPLAY ERROR")
            self.display = "ERROR"
            return self.display


def main():
    # TODO trivial examples of VendingMachine
    pass


if __name__ == '__main__':
    main()
