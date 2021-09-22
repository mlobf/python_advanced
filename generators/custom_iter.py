"""
    Just creating a custom iter using
    python classes

"""
# Below the old school way to create a iter
import sys


class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current


x = Iter(5)


for i in x:
    print(i)


# => End of the old school way to create a iter





