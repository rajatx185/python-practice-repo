"""
The Builder Design Pattern is a creational design pattern that allows you to create complex objects step by step. It separates the construction of a complex object from its representation so that the same construction process can create different representations.

A real-world example would be a fast food restaurant where you can order a burger. The burger order can have multiple options such as the size of the patty, the type of cheese, the toppings, and sauces. Using the Builder pattern, each option would be a separate builder that you can use to construct the final product.

Here's an example of the Builder pattern in Python:
"""

class Burger:
    def __init__(self):
        self._size = None
        self._cheese = None
        self._toppings = []
        self._sauce = None

    def __str__(self):
        return f"A {self._size} burger with {self._cheese} cheese, toppings: {self._toppings}, sauce: {self._sauce}"


class BurgerBuilder:
    def __init__(self):
        self._burger = Burger()

    def add_patty(self, size):
        self._burger._size = size
        return self

    def add_cheese(self, cheese):
        self._burger._cheese = cheese
        return self

    def add_topping(self, topping):
        self._burger._toppings.append(topping)
        return self

    def add_sauce(self, sauce):
        self._burger._sauce = sauce
        return self

    def build(self):
        return self._burger


builder = BurgerBuilder()
burger = builder\
    .add_patty("large")\
    .add_cheese("cheddar")\
    .add_topping("lettuce")\
    .add_topping("tomato")\
    .add_sauce("mayo")\
    .build()

print(burger)
# Output: A large burger with cheddar cheese, toppings: ['lettuce', 'tomato'], sauce: mayo
