
"Forward Iterators: These iterators allow you to traverse a collection of elements in a single direction, from start to end."

class ForwardIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            result = self.data[self.index]
            self.index += 1
            return result

# Example usage:
my_iterator = ForwardIterator([1, 2, 3, 4, 5])
for x in my_iterator:
    print(x)
