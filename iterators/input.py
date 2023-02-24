""" These iterators allow you to read elements from a collection of elements, but you cannot modify them. """
class InputIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration
        self.current += 1
        return self.current

for i in InputIterator(5):
    print(i)
