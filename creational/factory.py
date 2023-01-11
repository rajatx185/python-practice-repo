# aka virtual constructor
from abc import ABC, abstractmethod
"""
We want to create an object based on a condition
"""

### Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

### Concrete Shape Classes
### these are product concrete classes
class Rectangle(Shape):
    def draw(self):
        print("Draw a Rectangle")

class Square(Shape):
    def draw(self):
        print("Draw a Square")

### Shape Factory
### has-a relationship with concrete shape classes
class ShapeFactory:
    def get_shape(self, input):
        if input == "Rectangle":
            return Rectangle()
        elif input == "Square":
            return Square()
        else:
            return None

### client code
if __name__ == "__main__":
    shape_factory = ShapeFactory()
    shape = shape_factory.get_shape(input="s")
    shape.draw() if shape else print("Shape does not exist")