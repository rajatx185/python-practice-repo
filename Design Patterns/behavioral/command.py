"""
Command design pattern is a behavioral design pattern that converts requests or simple operations into objects. The main goal of this pattern is to decouple the object that invokes the operation from the object that performs the operation. This way, the objects that perform the operation can be chosen dynamically, and the same object can be used to perform multiple operations.

In this example, we have an abstract class OrderCommand that serves as the base class for all order commands. The BurgerOrder and FriesOrder classes are concrete implementations of the OrderCommand class, each representing a different type of food order. The Cook class is the receiver class, and the Waiter class is the invoker class. The client code uses the Waiter class to place food orders, which are then executed by the Cook class.

The code defines a system for ordering food in a restaurant. The OrderCommand class is an abstract class that serves as the base class for all types of food orders. The BurgerOrder and FriesOrder classes are concrete implementations of the OrderCommand class, representing specific food orders (burger and fries, respectively). The Cook class is responsible for preparing the food, and the Waiter class is responsible for receiving and placing the orders.

When a customer places an order, the Waiter class sets the order using the set_order method and then calls the place_order method to actually place the order. This invokes the execute method on the concrete OrderCommand object, which in turn calls the appropriate method on the Cook class to prepare the food.

This code uses the Command design pattern to decouple the food order process into separate objects, making it easier to modify and extend the system in the future. For example, we could easily add additional types of food orders by creating new concrete implementations of the OrderCommand class.


The Command design pattern decouples things by breaking down the food ordering process into separate objects, each with a clear and specific responsibility.

In the code, the Waiter class is responsible for receiving and placing orders, the OrderCommand class and its concrete implementations (e.g., BurgerOrder and FriesOrder) represent the specific food orders, and the Cook class is responsible for preparing the food. Each of these objects is separated from the others and only communicates with the other objects through well-defined interfaces (in this case, the execute method and the methods on the Cook class).

This decoupling allows us to modify or extend the system more easily and with less risk of unintended consequences. For example, if we wanted to add a new type of food order, we could simply create a new concrete implementation of the OrderCommand class, without having to make changes to the Waiter or Cook classes. Additionally, if we wanted to change the way that orders are placed, we could modify the Waiter class without affecting the way that food is prepared.

"""

"""
It's true that the Command design pattern might seem unnecessary in a simple example like the restaurant ordering system. However, in more complex systems with many different types of actions and actors, the Command pattern can provide a number of benefits, including:

Encapsulating request as an object: The Command pattern allows you to encapsulate a request as an object, which makes it easier to pass requests as method arguments, delay or queue a request’s execution, and implement undo/redo.

Loose coupling: By decoupling the objects that initiate an action from the objects that actually perform the action, the Command pattern promotes loose coupling between these objects. This makes it easier to add new commands to the system and change the way that commands are executed, without affecting the rest of the system.

Single Responsibility Principle: The Command pattern helps to adhere to the Single Responsibility Principle (SRP) by dividing the responsibilities of a system into separate, cohesive objects.

In short, while the Command design pattern may seem unnecessary in a simple example, it can provide a flexible and maintainable architecture for more complex systems, making it easier to add new features and make changes to the system over time.
"""


"""
In the restaurant ordering system example, the customer is the one who initiates the action by placing an order. The Waiter class acts as an intermediary, receiving the order from the customer and then using the OrderCommand class to represent the order. The Cook class performs the action by preparing the food.

Here's a step-by-step breakdown of the process:

The customer places an order for, say, a burger.
The Waiter class receives the order and sets it using the set_order method.
The Waiter class then calls the place_order method to actually place the order.
The place_order method invokes the execute method on the OrderCommand object, which in turn calls the appropriate method on the Cook class to prepare the food (e.g., prepare_burger).
The Cook class prepares the food and serves it to the customer.
So in this example, the customer initiates the action, the Waiter class acts as an intermediary, and the Cook class performs the action. The OrderCommand class represents the order and acts as the bridge between the Waiter and the Cook.
"""
# Abstract class for command
from abc import ABC, abstractmethod

class OrderCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete command class for handling burger orders
class BurgerOrder(OrderCommand):
    def __init__(self, cook):
        self._cook = cook

    def execute(self):
        self._cook.make_burger()

# Concrete command class for handling fries orders
class FriesOrder(OrderCommand):
    def __init__(self, cook):
        self._cook = cook

    def execute(self):
        self._cook.make_fries()

# Receiver class
class Cook:
    def make_burger(self):
        print("Making burger...")

    def make_fries(self):
        print("Making fries...")

# Invoker class
class Waiter:
    def set_order(self, order_command):
        self._order_command = order_command

    def place_order(self):
        self._order_command.execute()

# Client code
if __name__ == "__main__":
    cook = Cook()
    burger_order = BurgerOrder(cook)
    fries_order = FriesOrder(cook)

    waiter = Waiter()
    waiter.set_order(burger_order)
    waiter.place_order()

    waiter.set_order(fries_order)
    waiter.place_order()

