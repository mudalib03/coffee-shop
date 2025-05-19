import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("AB")  # Too short
        self.assertEqual(Coffee("Americano").name, "Americano")

    def test_orders_customers_stats(self):
        coffee = Coffee("Latte")
        c1 = Customer("Tim")
        c2 = Customer("Sue")
        c1.create_order(coffee, 2.5)
        c2.create_order(coffee, 3.5)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 3.0)
        self.assertEqual(set(coffee.customers()), {c1, c2})

if __name__ == '__main__':
    unittest.main()
