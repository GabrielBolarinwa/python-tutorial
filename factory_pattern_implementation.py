# Factory Pattern
from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        raise NotImplementedError("This method should be implemented by the subclass")


class VeggiePizza(Pizza):
    def prepare(self):
        return "Preparing Veggie Pizza"


class CheesePizza(Pizza):
    def prepare(self):
        return "Preparing cheese pizza"


class PepperoniPizza(Pizza):
    def prepare(self):
        return "Preparing peperoni pizza"

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        elif pizza_type == "veggie":
            return VeggiePizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")

def main():
    try:
        user_input = input("Enter the type of pizza: ")
        pizza = PizzaFactory.create_pizza(user_input)
        print(pizza.prepare())
    except ValueError:
        print("Please enter a valid pizza type")
