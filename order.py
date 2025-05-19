class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        coffee.add_order(self)
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @classmethod
    def most_aficionado(cls, coffee):
        if coffee.num_orders() == 0:
            return None
        max_spender = None
        max_spent = 0
        for customer in coffee.customers():
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                max_spender = customer
        return max_spender