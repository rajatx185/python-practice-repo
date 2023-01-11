"""
Single leading underscores are used as a weak “internal use” or “private” indicator for methods and data attributes
https://medium.com/analytics-vidhya/python-name-mangling-and-how-to-use-underscores-e67b529f744f
https://www.geeksforgeeks.org/name-mangling-in-python/#:~:text=With%20the%20help%20of%20dir,that%20belong%20to%20that%20object. - For private instance understanding

"""

class Base:
    def __init__(self) -> None:
        # protected member
        self._a = 2
        self.a = "geeks"
        self.__c = "geeks"

class Derived(Base):
    def __init__(self) -> None:
        super().__init__()
        # print(f"Calling protected member of base class: {self._a}")
        # self._a = 3
        # print(f"Calling modified protected member outside class:{self._a}")
        # print("calling private member of base class")
        print(self.__c)

# obj1 = Derived()
# obj2 = Base()

# obj = Base()
# obj2 = Derived()

# print(obj.a)
# print(obj.__c)
# print(obj2.__c)
# print(dir(obj))
# print(obj._Base__c)

## by convention:  _ should be used for protected members though it does not pose any restriction
# print(f"Accessing protected member of obj1: {obj1._a}")
# print(f"Accessing protected member of obj2: {obj2._a}")

# Python code to illustrate how mangling works 
# With method overriding
  
class Map: 
    def __init__(self): 
        self.__geek() 
          
    def geek(self): 
        print("In parent class")
    
    # private copy of original geek() method 
    __geek = geek    
    
class MapSubclass(Map):
    # provides new signature for geek() but 
    # does not break __init__() 
    def geek(self):         
        print("In Child class")

# Driver's code
obj = MapSubclass()
obj.geek()