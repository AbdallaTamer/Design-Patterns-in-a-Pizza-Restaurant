# Design Patterns in the Pizza Restaurant

## 1. Factory Method Pattern

- Intent: Encapsulates the creation of complex pizza objects (e.g., Margherita, Pepperoni).
- Motivation: Centralized creation logic simplifies pizza initialization and supports easy addition of new types.
- Structure: A `PizzaFactory` class creates specific `Pizza` subclasses (`Margherita`, `Pepperoni`) based on user input.
- Code Example:
```
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        raise ValueError("Unknown Pizza Type")
```
- Benefits: Encapsulates pizza creation, supports polymorphism, and adheres to OCP and SRP.


# 2. Decorator Pattern
- Intent: Dynamically adds behavior (toppings) to pizzas.
- Motivation: Avoids creating multiple pizza combinations as separate classes.
- Structure: The `ToppingDecorator` class wraps around a `Pizza` object to add toppings like `Cheese`, `Olives`, or `Mushrooms`.
- Code Example:
```
class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 1.0
```
- Benefits: Enhances flexibility, reduces class proliferation, and adheres to SRP and OCP.

# 3.Singleton Pattern

- Intent: Ensures only one instance of the `InventoryManager` class.
- Motivation: Centralizes inventory state for consistency and efficiency.
- Structure: The `__new__` method ensures a single instance of `InventoryManager` is created.
- Code Example:
```
class InventoryManager:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance
```
- Benefits: Prevents inventory conflicts, ensures data consistency, and adheres to SRP.


# 4.Strategy Pattern
- Intent: Allows flexible and interchangeable payment methods.
- Motivation: Decouples payment logic from the main system, making it easier to add new methods.
- Structure: The `PaymentMethod` interface is implemented by concrete classes like `PayPal` and `CreditCard`.
- Code Example:
```
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")
```
- Benefits: Improves modularity, enhances flexibility, and adheres to OCP and Encapsulation.


# Overengineering Concept
- Definition: Overengineering occurs when unnecessary complexity is added to a system, often due to overuse of design patterns or abstractions.
- Example in the Pizza Project: Implementing a topping factory would introduce unnecessary complexity since the decorator pattern already handles dynamic topping additions.
- Code Example:
```
class ToppingFactory:
    def create_topping(self, topping_type, pizza):
        if topping_type == "Cheese":
            return Cheese(pizza)
        elif topping_type == "Olives":
            return Olives(pizza)
        elif topping_type == "Mushrooms":
            return Mushrooms(pizza)
        raise ValueError("Unknown Topping Type")
```
Why Avoid Overengineering?
- Adds unnecessary layers of abstraction.
- Increases development and maintenance time.
- Reduces code readability and simplicity.
