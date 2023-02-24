from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send(self, sender, message):
        pass

class Colleague(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

class ConcreteColleagueA(Colleague):
    def receive(self, message):
        print(f"Colleague A received message: {message}")

    def send(self, message):
        self._mediator.send(self, message)

class ConcreteColleagueB(Colleague):
    def receive(self, message):
        print(f"Colleague B received message: {message}")

    def send(self, message):
        self._mediator.send(self, message)

class ConcreteMediator(Mediator):
    def send(self, sender, message):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)

mediator = ConcreteMediator()
colleague_a = ConcreteColleagueA(mediator)
colleague_b = ConcreteColleagueB(mediator)
mediator._colleagues = [colleague_a, colleague_b]
colleague_a.send("Hello from colleague A")


### Air Traffic Control

from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send_message(self, sender, message):
        pass

class Plane(ABC):
    def __init__(self, mediator, id):
        self._mediator = mediator
        self._id = id

    @abstractmethod
    def receive_message(self, message):
        pass

    @abstractmethod
    def send_message(self, message):
        pass

class CommercialPlane(Plane):
    def receive_message(self, message):
        print(f"Commercial plane {self._id} received message: {message}")

    def send_message(self, message):
        self._mediator.send_message(self, message)

class MilitaryPlane(Plane):
    def receive_message(self, message):
        print(f"Military plane {self._id} received message: {message}")

    def send_message(self, message):
        self._mediator.send_message(self, message)

class AirTrafficControlTower(Mediator):
    def send_message(self, sender, message):
        for plane in self._planes:
            if plane != sender:
                plane.receive_message(message)

tower = AirTrafficControlTower()
commercial_plane_1 = CommercialPlane(tower, 1)
commercial_plane_2 = CommercialPlane(tower, 2)
military_plane_1 = MilitaryPlane(tower, 1)
tower._planes = [commercial_plane_1, commercial_plane_2, military_plane_1]

commercial_plane_1.send_message("Commercial plane 1 requests permission to land.")

"""
In this example, the Mediator class defines the abstract method send_message for sending messages between objects. The Plane class is an abstract base class for the CommercialPlane and MilitaryPlane concrete classes. Each concrete plane class implements the receive_message and send_message methods, allowing them to receive and send messages via the mediator. The AirTrafficControlTower class implements the send_message method to relay messages between the planes.
"""


"""
No, the mediator and command design patterns are different.

The mediator pattern is used to handle communication between objects and reduce the coupling between objects. In a mediator pattern, the objects communicate through a central object called a mediator. The mediator abstracts the communication between objects and acts as a middleman to handle their interactions.

The command pattern, on the other hand, is used to represent an action or request as an object. The command pattern decouples the object that invokes the action from the object that performs the action. In this pattern, a command object is created for each action, and the invoker calls the execute method on the command object to perform the action.

In summary, the mediator pattern is focused on communication between objects, while the command pattern is focused on representing actions as objects.
"""