# -*- coding: utf-8 -*-
"""Design Patterns in a Pizza Restaurant.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w7rDKnXxxfsy1zOsLBkhGwmWiunxoET8

#1. Creational Pattern: Factory Method

Problem:
Creating pizzas (Margherita, Pepperoni) is a complex and repetitive task.

Solution:
Use a Factory Method to encapsulate pizza creation to separates pizza creation logic from the main program and allows easy addition of new pizza types.
"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class Margherita(Pizza):
    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 5.0

class Pepperoni(Pizza):
    def get_description(self):
        return "Pepperoni"

    def get_cost(self):
        return 6.0

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        raise ValueError("Unknown Pizza Type")

"""## Benefits:

- Encapsulation: Pizza creation logic is hidden from the client.
- Polymorphism: All pizzas implement the Pizza interface.
- Open-Closed Principle (OCP): Add new pizza types without modifying the existing code.

# 2. Structural Pattern: Decorator

Problem:
Allow customers to add toppings dynamically while maintaining flexibility.

Solution:
Use the Decorator Pattern to extend pizza functionality (adding Cheese, Olives, Mushrooms) without modifying the Pizza classes.
"""

class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description()

    def get_cost(self):
        return self._pizza.get_cost()

class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 1.0

class Olives(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Olives"

    def get_cost(self):
        return self._pizza.get_cost() + 0.5

class Mushrooms(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Mushrooms"

    def get_cost(self):
        return self._pizza.get_cost() + 0.7

"""## Benefits:

- Single Responsibility Principle (SRP): Each topping class handles only its behavior.
- Open-Closed Principle (OCP): Add new toppings without modifying existing classes.

# 3. Behavioral Pattern: Singleton
Problem:
Ensure a single inventory manager to manage ingredient availability consistently.

Solution:
Use the Singleton Pattern for the InventoryManager class.
"""

class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

"""##Benefits:

- Centralized inventory management avoids inconsistencies.
- Ensures a shared state across the application.

# 4. Behavioral Pattern: Strategy
- Problem:
Allow flexible payment options (e.g., PayPal, Credit Card).

- Solution:
Use the Strategy Pattern to define multiple payment methods and switch between them dynamically.
"""

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, am  ount):
        pass

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card.")

"""Benefits:

- Open-Closed Principle (OCP): Add new payment methods without changing existing code.
- Encapsulation: Payment logic is abstracted from the main system.

#Overengineering Concept
Overengineering occurs when a system becomes unnecessarily complex due to overuse of patterns or abstractions.

For example:
"""

class AbstractToppingFactory:
    def create_topping(self, topping_type):
        if topping_type == "Cheese":
            return Cheese(None)
        elif topping_type == "Olives":
            return Olives(None)
        raise ValueError("Unknown Topping Type")

"""This is unnecessary when a simpler decorator approach suffices.

#Main
"""

def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == "0":
            break

        pizza_type = "Margherita" if pizza_choice == "1" else "Pepperoni"
        if not inventory_manager.check_and_decrement(pizza_type):
            print(f"Sorry, {pizza_type} is out of stock!")
            continue

        pizza = PizzaFactory.create_pizza(pizza_type)

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            topping_map = {"1": ("Cheese", Cheese), "2": ("Olives", Olives), "3": ("Mushrooms", Mushrooms)}

            if topping_choice in topping_map:
                topping_name, topping_class = topping_map[topping_choice]
                if inventory_manager.check_and_decrement(topping_name):
                    pizza = topping_class(pizza)
                else:
                    print(f"Sorry, {topping_name} is out of stock!")
            elif topping_choice == "4":
                break
            else:
                print("Invalid choice!")

        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        payment_method = PayPal() if payment_choice == "1" else CreditCard()
        payment_method.pay(pizza.get_cost())

        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()