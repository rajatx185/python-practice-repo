class Test:
    def __init__(self) -> None:
        self._foo = 5
        self.foo = 4
        self.foo = 7

obj = Test()
print(obj._foo)
print(obj.foo)


"""
How _ works with property in python ???
"""