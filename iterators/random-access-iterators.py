"""
Random Access Iterators: These iterators allow you to traverse a collection of elements in any direction and to access elements at any position in constant time.
"""

class RandomAccessIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        else:
            item = self.items[self.index]
            self.index += 1
            return item

    def jump(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError
        else:
            self.index = index

items = [1, 2, 3, 4, 5]
iterator = RandomAccessIterator(items)
for item in iterator:
    print(item)

iterator.jump(2)
print(next(iterator))
