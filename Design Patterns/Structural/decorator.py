"""
Examples
- Pizza - BASE PIZZA WITH TOPPINGS ARE DECORATORS
- COFFEE - TOPPINGS - CREAM, EXTRA MILK
- CAR - ADDITIONAL FEATURES - SEAT COVER, AC
WHY WE NEED A DECORATOR PATTERN?
- TO HANDLE CLASS EXPLOSION
decorator is both is-a and has-a
"""

from abc import ABC, abstractmethod

### abstract class (not an interface)
class PizzaBase(ABC):
    @abstractmethod
    def cost(self):
        pass

    def business_logic(self):
        pass

class Farmhouse(PizzaBase):
    def cost(self):
        return 100
    
class TandooriPaneer(PizzaBase):
    def cost(self):
        return 150


class Toppings(PizzaBase):
    @abstractmethod
    def cost(self):
        pass

## inherited toppings abstract class
## has a (composition) pizza object
class Cheese(Toppings):
    def __init__(self, pizza) -> None:
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 10

class Mushroom(Toppings):
    def __init__(self, pizza) -> None:
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 15

if __name__ == "__main__":
    ## farmhouse Pizza with extra cheese
    farmhouse = Farmhouse()
    ## decorated with cheese
    farmhouse_with_extra_cheese = Cheese(farmhouse)
    print(farmhouse_with_extra_cheese.cost())
    ## decorated with mushroom
    farmhouse_with_extra_cheese_and_mushroom = Mushroom(farmhouse_with_extra_cheese)
    print(farmhouse_with_extra_cheese_and_mushroom.cost())