"""
State Design Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. The pattern involves a set of state classes that define the behavior for each possible state, and a context class that maintains the current state and delegates the behavior to the current state class.
"""

class OrderState:
    def handle(self):
        pass

class NewOrder(OrderState):
    def handle(self,order):
        pass

class InProgressOrder(OrderState):
    def handle(self,order):
        pass

class ShippedOrder(OrderState):
    def handle(self,order):
        pass

class DeliveredOrder(OrderState):
    def handle(self,order):
        pass

class Order:
    def __init__(self) -> None:
        self.__state = NewOrder()
    
    def set_state(self, state):
        self.__state = state
    
    def handle(self):
        self.__state.handle(self)

"""
In this example, the Order class has an internal state represented by the state attribute, which is initially set to NewOrder. The handle method delegates the behavior to the current state class, which is determined by the value of the state attribute. When the order state changes, the set_state method is called to update the state attribute, and the next call to handle will delegate the behavior to the new state class.

The line self.state.handle(self) in the Order class is where the delegation of behavior occurs. It calls the handle method on the current state object stored in the state attribute, passing the Order object (self) as an argument. This allows the state object to access and modify the state of the Order object if necessary. The handle method of the state class defines the behavior for that state.
"""

# create a new order
order = Order()

# handle the order, which should call the handle method of the NewOrder state
order.handle()

# change the order state to InProgress
order.set_state(InProgressOrder())

# handle the order again, which should call the handle method of the InProgressOrder state
order.handle()

# change the order state to Shipped
order.set_state(ShippedOrder())

# handle the order again, which should call the handle method of the ShippedOrder state
order.handle()

# change the order state to Delivered
order.set_state(DeliveredOrder())

# handle the order again, which should call the handle method of the DeliveredOrder state
order.handle()


"""
In this example, the Order object is created in the NewOrder state, and the handle method is called four times, each time with a different state. The set_state method is used to change the state of the Order object, and each call to handle delegates the behavior to the current state class.
"""