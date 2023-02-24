"""
Behavioral design patterns are concerned with the communication between objects, and the delegation design pattern specifically focuses on allowing objects to delegate responsibilities to other objects. This can help to reduce coupling and increase flexibility in the design of a system, as the objects involved can change their behavior at runtime based on the delegation relationship.

The Delegation design pattern can be explained with an example of a manager delegating tasks to their subordinates.

Imagine a manager who wants to complete several tasks, but they are too busy to handle all of them on their own. Instead of doing everything themselves, the manager delegates some of the tasks to their subordinates. This way, the manager can still ensure that the tasks are being completed, but they don't have to do all the work themselves.

In software design, this can be implemented by having a main object delegate responsibilities to other objects, which are better suited to handle the tasks. For example, a graphical user interface (GUI) component might delegate the task of drawing itself to a separate graphical rendering object. This way, the GUI component can change the way it is drawn at runtime by delegating to different rendering objects, without having to change its own code.

In this example, the manager is the main object that delegates tasks, and the subordinates are the objects that are being delegated to. The delegation relationship allows for a separation of responsibilities and a more flexible design.
"""

from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def execute(self):
        pass

class Manager:
    def __init__(self):
        self.task = None

    def set_task(self, task):
        self.task = task

    def do_task(self):
        if self.task is not None:
            self.task.execute()

class SubordinateA(Task):
    def execute(self):
        print("Task executed by Subordinate A")

class SubordinateB(Task):
    def execute(self):
        print("Task executed by Subordinate B")

# Client code
manager = Manager()

subordinateA = SubordinateA()
manager.set_task(subordinateA)
manager.do_task()

subordinateB = SubordinateB()
manager.set_task(subordinateB)
manager.do_task()

"""
In this example, the Task class is defined as an abstract base class (ABC) using the abc module in Python. This enforces the requirement for any concrete implementations of the Task class to provide an implementation for the execute method.

The Manager class delegates the task execution to the Task objects that are assigned to it. The SubordinateA and SubordinateB classes inherit from the Task class and provide the specific implementation of the execute method.

The rest of the example remains the same as in the previous example. The client code creates an instance of Manager and sets the task to be executed using the set_task method. The manager can then execute the task by calling the do_task method. In this example, two different subordinates are assigned to the manager, and each time the task is executed, it is handled by the assigned subordinate. This demonstrates how the delegation pattern allows for a separation of responsibilities and a more flexible design.
"""