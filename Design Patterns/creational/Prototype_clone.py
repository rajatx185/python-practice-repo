""""
In the code above, the Prototype interface defines a clone method that must be implemented by the concrete prototypes. The Dragon and Goblin classes implement the clone method by using the deepcopy function from the copy module to make a deep copy of the object and return the copied object. In the main function, prototypes for the dragon and goblin creatures are created and customized, and copies of these prototypes are created using the clone method.

"""

import copy

class Prototype:
    def clone(self):
        pass

class Dragon(Prototype):
    def __init__(self, name, fire):
        self.name = name
        self.fire = fire

    def clone(self):
        return copy.deepcopy(self)

class Goblin(Prototype):
    def __init__(self, name, claws):
        self.name = name
        self.claws = claws

    def clone(self):
        return copy.deepcopy(self)

def main():
    dragon_prototype = Dragon("Dragon", True)
    goblin_prototype = Goblin("Goblin", True)

    dragon_copy = dragon_prototype.clone()
    dragon_copy.name = "Fire Dragon"

    goblin_copy = goblin_prototype.clone()
    goblin_copy.name = "Green Goblin"

    print(dragon_copy.name, dragon_copy.fire)
    print(goblin_copy.name, goblin_copy.claws)

if __name__ == "__main__":
    main()
