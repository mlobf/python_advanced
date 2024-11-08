import sys


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = range(1, 99999999)

y = map(lambda i: i**2, x)

print(sys.getsizeof(y))
# print(sys.getsizeof(list(y)))

x = iter(x)


print(next(x))
