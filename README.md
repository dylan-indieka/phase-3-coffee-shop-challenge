# Phase 3 Coffee Shop Challenge

This project models a simple coffee shop system using Python classes. It demonstrates object-oriented relationships between customers, coffees, and orders.

## Files

- `customer.py`: Defines the `Customer` class, representing a customer who can place orders for coffee.
- `coffee.py`: Defines the `Coffee` class, representing different types of coffee.
- `order.py`: Defines the `Order` class, representing an order placed by a customer for a coffee at a specific price.
- `debug.py`: Script to test and demonstrate the relationships and methods in the system.

## Features

- Customers can place orders for different coffees.
- Track all orders, and retrieve orders and coffees for each customer.
- Calculate the number of orders and average price for each coffee.
- Find the customer who ordered a specific coffee the most times.

## Usage

1. Ensure all Python files (`customer.py`, `coffee.py`, `order.py`, `debug.py`) are in the same directory.
2. Run the test script:

   ```bash
   python3 debug.py
   ```

3. The script will output information about customers, coffees, and orders, and demonstrate the bonus method to find the top customer for a coffee.

## Example Output

```
Dylan's orders: ['Mocha', 'Latte']
Dylan's coffees: ['Mocha', 'Latte']
Mocha's customers: ['Aisha', 'Dylan']
Mocha's number of orders: 2
Mocha's average price: 3.0
Biggest mocha fan: Dylan
```

## Requirements

- Python 3.x

## License

MIT License
