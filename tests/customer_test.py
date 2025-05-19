import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("x" * 16)  # Too long
        self.assertEqual(Customer("Alex").name, "Alex")

    def test_orders_and_coffees(self):
        customer = Customer("Ben")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        order1 = customer.create_order(coffee1, 3.0)
        order2 = customer.create_order(coffee2, 4.0)
        order3 = customer.create_order(coffee1, 5.0)
        
        self.assertEqual(len(customer.orders()), 3)
        self.assertEqual(set(customer.coffees()), {coffee1, coffee2})

    def test_most_aficionado(self):
        c1 = Customer("Ann")
        c2 = Customer("Bob")
        coffee = Coffee("Mocha")
        c1.create_order(coffee, 3.0)
        c2.create_order(coffee, 4.0)
        c2.create_order(coffee, 5.0)

        self.assertEqual(Customer.most_aficionado(coffee), c2)

if __name__ == '__main__':
    unittest.main()
