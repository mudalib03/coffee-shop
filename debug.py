from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")
c3 = Customer("Cara")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create Orders
c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 4.5)
c2.create_order(coffee1, 2.5)
c3.create_order(coffee1, 5.0)
c3.create_order(coffee1, 4.0)

print(f"{c1.name}'s orders: {[order.price for order in c1.orders()]}")
print(f"{coffee1.name} has {coffee1.num_orders()} orders")
print(f"Average price for {coffee1.name}: {coffee1.average_price()}")
print(f"Most aficionado for {coffee1.name}: {Customer.most_aficionado(coffee1).name}")
