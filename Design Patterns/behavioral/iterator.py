"""
Iterator Design Pattern is a behavioral design pattern that provides a way to access elements of a collection object sequentially without exposing the underlying representation. It separates the collection of elements from the ways those elements are accessed and processed.

It is memory efficient. We don't need to store all data in memory.
We can use iterator to access the data sequentially.
"""

"""
__iter__ and __next__ are "dunder" methods (short for "double underscore") in Python.

The __iter__ method is used to define an object as an iterator. It returns the iterator object itself. The __next__ method is used to return the next value from the iterator. The __next__ method should raise a StopIteration exception when there are no more values to be returned.

In the examples I provided earlier, the ChannelIterator and FileReader classes implement the __iter__ and __next__ methods to provide iteration functionality. The __iter__ method returns the iterator object itself, and the __next__ method returns the next channel or line from the file.
"""

class Channel:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

class ChannelIterator:
    def __init__(self, channels):
        self.index = 0
        self.channels = channels

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.channels):
            result = self.channels[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

class TV:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)

    def get_iterator(self):
        return ChannelIterator(self.channels)

if __name__ == "__main__":
    tv = TV()
    tv.add_channel(Channel("HBO", 301))
    tv.add_channel(Channel("ESPN", 302))
    tv.add_channel(Channel("CNN", 303))

    for channel in tv.get_iterator():
        print(channel.name, channel.frequency)



class FileReader:
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line
        else:
            raise StopIteration

if __name__ == "__main__":
    file_reader = FileReader("sample.txt")

    for line in file_reader:
        print(line)
