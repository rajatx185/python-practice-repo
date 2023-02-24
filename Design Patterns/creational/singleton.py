"""
The Singleton design pattern is a creational pattern that ensures that a class has only one instance while providing a global access point to this instance. The main idea is to have a class that is responsible for creating its own instance in case it doesn't exist yet and returning the same instance every time it's requested.
"""

"""
About @staticmethod decorator
Static methods are used in a few specific cases:

Utility functions: When a method doesn't need to access instance-specific data, it can be defined as a static method to make it clear that it does not depend on instance-specific data.

Factory methods: When a class needs to provide a way to create objects, but the exact type of object to be created is not known, a static method can be used as a factory.

Constants: If a class has a constant value that needs to be shared across all instances, it can be defined as a static field.

Static methods are a way to encapsulate a piece of functionality within a class, but not tie it to a specific instance. They are typically used when the method only needs to operate on its arguments and doesn't need access to any instance-specific data or state.
"""

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance
    
    def __init__(self) -> None:
        if Singleton.__instance is not None:
            return Exception("Singleton can only be accessed through get instance")
        else:
            Singleton.__instance = self

# Client code
singleton_object1 = Singleton.get_instance()
print(singleton_object1)
singleton_object2 = Singleton.get_instance()
print(singleton_object2)

class __ElevatorSystem(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__ElevatorSystem, cls).__new__(cls)
    return cls.__instances

class ElevatorSystem(metaclass=__ElevatorSystem):
    def __init__(self, building):
      self.__building = building

    def monitoring():
        None

    def dispatcher():
        None
