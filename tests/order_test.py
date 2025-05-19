import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from coffee_shop.customer import Customer
from coffee_shop .coffee import Coffee
from coffee_shop.order import Order

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        c = Customer("Eva")
        coffee = Coffee("Cappuccino")
        order = Order(c, coffee, 4.5)

        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Order("NotCustomer", Coffee("Latte"), 3.0)
        with self.assertRaises(TypeError):
            Order(Customer("Tom"), "NotCoffee", 3.0)
        with self.assertRaises(ValueError):
            Order(Customer("Tom"), Coffee("Latte"), 0.5)  # Too cheap

if __name__ == '__main__':
    unittest.main()
