from order import Order  # Make sure there is an order.py file with an Order class defined

class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def orders(self):
        # Return all orders for this customer from the global Order list
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        # Return all unique coffees this customer has ordered
        return list(set(order.coffee for order in self.orders()))

    @staticmethod
    def most_aficionado(coffee):
        from order import Order
        customer_counts = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_counts[order.customer] = customer_counts.get(order.customer, 0) + 1
        if not customer_counts:
            return None
        return max(customer_counts, key=customer_counts.get)
